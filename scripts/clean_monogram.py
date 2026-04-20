"""Nettoie le monogramme recolore (strict) en virant UNIQUEMENT l'ombre portee.
Preserve la structure entrelacee (arcs argentes, subtilites duotone).

Strategie :
1. Partir de recolor-strict.png (qui a deja les couleurs or+navy)
2. Identifier le cercle principal (connected component des pixels fortement colores)
3. Masquer tout ce qui est HORS du cercle ET qui a une faible saturation (= ombre portee grise)
4. Preserver tous les pixels DANS le cercle, meme gris, car ce sont les reflets structurels
5. Crop sur le monogramme seul (vire le wordmark qui est apres la zone cercle)
"""
from pathlib import Path
from PIL import Image
import numpy as np

SRC = Path("/Users/fabienberger/berger-site/assets/logo-recolor/recolor-strict.png")
OUT = Path("/Users/fabienberger/berger-site/assets/logo-recolor/monogram-noshadow.png")

img = Image.open(SRC).convert("RGBA")
arr = np.array(img, dtype=np.float32)
h, w = arr.shape[:2]
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

max_rgb = np.maximum(np.maximum(r, g), b)
min_rgb = np.minimum(np.minimum(r, g), b)
sat = max_rgb - min_rgb

# Restriction : on ne cherche le cercle que dans la moitie superieure de l'image
# (pour que le wordmark en bas ne biaise pas le centre/rayon)
upper_half = np.zeros((h, w), dtype=bool)
upper_half[:int(h * 0.6), :] = True

# Pixels fortement colores du monogramme seulement
strong_colored = (sat > 40) & (a > 100) & upper_half
ys, xs = np.where(strong_colored)
if len(xs) == 0:
    raise ValueError("Pas de pixels colores detectes")

# Centre/rayon du cercle principal (p95 pour ignorer les bavures)
cx, cy = int(np.mean(xs)), int(np.mean(ys))
dists = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
radius = int(np.percentile(dists, 95))

# Carte des distances pour tous les pixels
yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
dist_from_center = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)

# Strategie radicale : on garde UNIQUEMENT ce qui est a la fois
#   (a) dans le cercle (distance <= rayon + marge fine)
#   (b) ET au-dessus du bas du cercle (pas de wordmark sous)
# Tout le reste devient transparent.

# On retrecit le rayon effectif pour virer le halo/ombre qui est juste au-dela du cercle visible
effective_radius = int(radius * 0.92)
keep = (dist_from_center <= effective_radius) & (yy <= cy + effective_radius + 2)
out = arr.copy()
out[~keep, 3] = 0

# Crop sur le bbox des pixels restants
alpha_out = out[:, :, 3] > 10
ys_o, xs_o = np.where(alpha_out)
if len(xs_o) > 0:
    x0, x1 = xs_o.min() - 4, xs_o.max() + 4
    y0, y1 = ys_o.min() - 4, ys_o.max() + 4
    x0, y0 = max(0, x0), max(0, y0)
    x1, y1 = min(w, x1), min(h, y1)
    out = out[y0:y1, x0:x1]

Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA").save(OUT, optimize=True)
print(f"OK: {OUT.name} ({OUT.stat().st_size//1024} Ko) — dimensions: {out.shape[1]}x{out.shape[0]}")
print(f"Cercle detecte: centre=({cx},{cy})  rayon={radius}")
