"""Recolor ULTRA-FLAT du monogramme : vire l'ombre portee + les reflets argentes.

Strategie :
- Bleu clair brillant -> OR pur (#B69153), sans gradient
- Bleu nuit fonce -> NAVY pur (#14233A), sans gradient
- Gris metallique (reflets argentes dans le cercle) -> OR lui aussi (plus d'argent)
- Pixels "ombre portee" (faible saturation + distance au centre > rayon) -> transparents

Resultat : monogramme or + navy vraiment flat, sans artefact 2010.
"""
from pathlib import Path
from PIL import Image
import numpy as np

SRC = Path("/Users/fabienberger/berger-site/assets/Nouveau Logo/PNG Transparent.png")
OUT = Path("/Users/fabienberger/berger-site/assets/logo-recolor/monogram-flat-clean.png")

P2_NAVY = np.array([0x14, 0x23, 0x3A], dtype=np.uint8)
P2_GOLD = np.array([0xB6, 0x91, 0x53], dtype=np.uint8)

img = Image.open(SRC).convert("RGBA")
arr = np.array(img, dtype=np.float32)
h, w = arr.shape[:2]
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

visible = a > 5
# Saturation = range(R,G,B)
max_rgb = np.maximum(np.maximum(r, g), b)
min_rgb = np.minimum(np.minimum(r, g), b)
sat = max_rgb - min_rgb  # 0..255

# Pixel bleuate : B dominant
blue_dominant = (b > r + 8) & (b > g - 3)

# Classification tres tranchee (flat) :
# - Bright blue (b > 150) -> OR
# - Dark blue (b <= 150) -> NAVY
# - Gray (low sat) dans le cercle -> melange OR
# - Shadow : quasi-gris (sat < 15) + B > 130 (c'est gris clair autour du cercle) -> transparent

# Masque ombre portee : gris leger autour du cercle
# Detecte par : faible saturation + luminosite moyenne a claire + hors zone couleur pleine
# On part du principe que l'ombre est "gris clair flou" autour
shadow_like = (sat < 30) & (max_rgb > 130) & (max_rgb < 240) & visible

# Masque zones colorees fortes (monogramme principal)
strong_color = (sat > 30) & visible

# On veut: le cercle reste, l'ombre disparait.
# Pour cela : calculer la bounding box des strong_color, en deduire centre+rayon
ys, xs = np.where(strong_color)
if len(xs) > 0:
    cx, cy = int(np.mean(xs)), int(np.mean(ys))
    # rayon = max distance du centre aux pixels fortement colores
    dists = np.sqrt((xs - cx) ** 2 + (ys - cy) ** 2)
    radius = int(np.percentile(dists, 98))  # p98 pour eviter outliers
else:
    cx, cy = w // 2, h // 2
    radius = min(w, h) // 3

# Grille des distances
yy, xx = np.meshgrid(np.arange(h), np.arange(w), indexing="ij")
dist_from_center = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)

# Zone "cercle" = tout ce qui est dans ou tres proche du rayon max
inside_circle = dist_from_center <= radius + 8
outside_circle = ~inside_circle

# Les pixels "ombre portee" = shadow_like ET outside_circle
shadow_mask = shadow_like & outside_circle

# Les pixels a garder (dans le monogramme) = strong_color OU (inside_circle ET visible)
keep_mask = strong_color | (inside_circle & visible & ~shadow_mask)

# Construire l'image de sortie
out = np.zeros_like(arr)

# Pour les pixels a garder : recolorer
bright_blue = blue_dominant & (max_rgb > 150) & keep_mask
dark_blue = blue_dominant & (max_rgb <= 150) & keep_mask
gray_in = (~blue_dominant) & keep_mask & visible

out[bright_blue, 0] = P2_GOLD[0]
out[bright_blue, 1] = P2_GOLD[1]
out[bright_blue, 2] = P2_GOLD[2]
out[bright_blue, 3] = 255

out[dark_blue, 0] = P2_NAVY[0]
out[dark_blue, 1] = P2_NAVY[1]
out[dark_blue, 2] = P2_NAVY[2]
out[dark_blue, 3] = 255

# Gris (anciens reflets argentes) : on les bascule en OR aussi pour unifier
out[gray_in, 0] = P2_GOLD[0]
out[gray_in, 1] = P2_GOLD[1]
out[gray_in, 2] = P2_GOLD[2]
out[gray_in, 3] = 255

# Les pixels hors keep_mask (ombre portee, exterieur) : totalement transparents
# (deja 0 par defaut)

# Crop sur le monogramme (bbox des pixels non transparents)
alpha_out = out[:, :, 3] > 0
ys_o, xs_o = np.where(alpha_out)
if len(xs_o) > 0:
    x0, x1 = xs_o.min(), xs_o.max()
    y0, y1 = ys_o.min(), ys_o.max()
    out = out[y0:y1 + 1, x0:x1 + 1]

# Pas de wordmark : le wordmark actuel est en dessous et est bleu clair donc il a ete
# marque en shadow_like ET hors cercle -> transparent. Parfait pour isoler le monogramme.

Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA").save(OUT)
print(f"OK: {OUT.name} ({OUT.stat().st_size//1024} Ko)")
print(f"Centre: ({cx},{cy})  Rayon: {radius}")
