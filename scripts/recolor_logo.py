"""Recolor le logo Berger & Associés vers la palette P2 (Ivoire & Nuit).

Approche : detection HSV des pixels bleus, split par luminosite,
remap vers navy P2 (#14233A) pour bleu fonce et or P2 (#B69153) pour bleu clair,
en preservant l'information de shading (Value HSV source).

Produit 3 variantes pour l'A/B visuel :
- recolor-strict.png : bleu clair -> or, bleu nuit -> navy (2 accents, garde lisibilite duotone)
- recolor-mono-navy.png : tout en navy (monochrome, le plus sobre)
- recolor-mono-ink.png : tout en encre (#121212, version grayscale re-teintee)
"""
from pathlib import Path
from PIL import Image
import numpy as np
import colorsys

SRC = Path("/Users/fabienberger/berger-site/assets/Nouveau Logo/PNG Transparent.png")
OUT_DIR = Path("/Users/fabienberger/berger-site/assets/logo-recolor")
OUT_DIR.mkdir(parents=True, exist_ok=True)

P2_NAVY = (0x14, 0x23, 0x3A)   # encre bleue P2
P2_GOLD = (0xB6, 0x91, 0x53)   # or P2
P2_SLATE = (0x5F, 0x65, 0x74)  # ardoise P2
P2_INK = (0x12, 0x12, 0x12)    # encre neutre

img = Image.open(SRC).convert("RGBA")
arr = np.array(img, dtype=np.float32)
h, w = arr.shape[:2]
r, g, b, a = arr[:, :, 0], arr[:, :, 1], arr[:, :, 2], arr[:, :, 3]

# Masque "pixel visible" (alpha > 0)
visible = a > 5

# Detection "bleuatre" : B dominant (pas rouge-rose, pas vert)
blue_dominant = (b > r + 10) & (b > g - 5) & visible

# Luminosite normalisee (max RGB)
max_rgb = np.maximum(np.maximum(r, g), b)

# Split bleu clair (brillant) vs bleu nuit (fonce)
# Seuil empirique : le bleu ciel vif a max_rgb > 180, le navy logo a max_rgb < 120
light_blue = blue_dominant & (max_rgb > 150)
dark_blue = blue_dominant & (max_rgb <= 150)

# Pixels gris (metalliques, reflets argentes) : faible saturation
diff_max = max_rgb - np.minimum(np.minimum(r, g), b)
gray_ish = (diff_max < 25) & visible & ~blue_dominant


def tint(target_rgb, lightness_map):
    """Applique la couleur target en modulant par la luminosite source."""
    tr, tg, tb = target_rgb
    # lightness_map est dans [0..255], on l'utilise comme facteur multiplicatif
    # pour preserver le dégradé d'origine (255 = couleur pleine, 0 = noir)
    f = lightness_map / 255.0
    return (
        np.clip(tr * f, 0, 255),
        np.clip(tg * f, 0, 255),
        np.clip(tb * f, 0, 255),
    )


# === V1 STRICT : bleu clair -> or P2, bleu nuit -> navy P2, gris -> ardoise P2 ===
v1 = arr.copy()
# Bleu clair -> or (garde la luminosite)
lum_light = max_rgb  # plus le pixel etait clair, plus il devient or clair
tr, tg, tb = tint(P2_GOLD, lum_light)
# Mais on ne veut pas de l'or trop sombre, donc boost la luminosite
lum_boosted = np.clip(max_rgb * 1.1 + 30, 60, 255)
tr, tg, tb = tint(P2_GOLD, lum_boosted)
v1[light_blue, 0] = tr[light_blue]
v1[light_blue, 1] = tg[light_blue]
v1[light_blue, 2] = tb[light_blue]
# Bleu nuit -> navy P2
lum_dark = np.clip(max_rgb * 1.3 + 20, 40, 220)
tr, tg, tb = tint(P2_NAVY, lum_dark)
v1[dark_blue, 0] = tr[dark_blue]
v1[dark_blue, 1] = tg[dark_blue]
v1[dark_blue, 2] = tb[dark_blue]
# Gris metallique -> ardoise
tr, tg, tb = tint(P2_SLATE, max_rgb)
v1[gray_ish, 0] = tr[gray_ish]
v1[gray_ish, 1] = tg[gray_ish]
v1[gray_ish, 2] = tb[gray_ish]

Image.fromarray(np.clip(v1, 0, 255).astype(np.uint8), "RGBA").save(
    OUT_DIR / "recolor-strict.png"
)

# === V2 MONO NAVY : tout en navy shades ===
v2 = arr.copy()
lum_all = max_rgb
tr, tg, tb = tint(P2_NAVY, np.clip(lum_all * 1.4, 40, 255))
all_colored = visible & ~gray_ish
v2[all_colored, 0] = tr[all_colored]
v2[all_colored, 1] = tg[all_colored]
v2[all_colored, 2] = tb[all_colored]
# Les gris restent gris clair (neutres)
tr, tg, tb = tint(P2_SLATE, lum_all)
v2[gray_ish, 0] = tr[gray_ish]
v2[gray_ish, 1] = tg[gray_ish]
v2[gray_ish, 2] = tb[gray_ish]

Image.fromarray(np.clip(v2, 0, 255).astype(np.uint8), "RGBA").save(
    OUT_DIR / "recolor-mono-navy.png"
)

# === V3 MONO INK : tout en encre neutre ===
v3 = arr.copy()
lum_all = max_rgb
tr, tg, tb = tint(P2_INK, np.clip(lum_all * 1.3, 40, 255))
all_visible = visible
v3[all_visible, 0] = tr[all_visible]
v3[all_visible, 1] = tg[all_visible]
v3[all_visible, 2] = tb[all_visible]

Image.fromarray(np.clip(v3, 0, 255).astype(np.uint8), "RGBA").save(
    OUT_DIR / "recolor-mono-ink.png"
)

print("OK, genere :")
for p in sorted(OUT_DIR.glob("*.png")):
    print(f"  {p.name} ({p.stat().st_size // 1024} Ko)")
