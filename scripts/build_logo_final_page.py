"""Compose la version finale : logo actuel recolore 1a + tagline dore 2C.

Variantes :
- V1a : logo 1a complet (monogramme + wordmark bold condense) + tagline dore inline
- V1b : idem sur fond navy
- V2a : monogramme 1a crop + wordmark Fraunces SVG + tagline dore (alignement V4)
- V2b : idem sur fond navy

Produit egalement des PNG cropes du monogramme seul pour reutilisation.
"""
import base64
from io import BytesIO
from pathlib import Path
from PIL import Image

ASSETS = Path("/Users/fabienberger/berger-site/assets")
RECOLOR_DIR = ASSETS / "logo-recolor"
CONTENT_DIR = Path("/Users/fabienberger/berger-site/.superpowers/brainstorm/66468-1776693627/content")
OUT_HTML = CONTENT_DIR / "logo-final-v3.html"


def crop_monogram(src_png: Path, dst_png: Path, bottom_ratio: float = 0.74):
    """Crop la partie wordmark (bas) pour isoler le monogramme (haut).
    bottom_ratio = 0.74 signifie qu'on garde les 74% du haut.
    """
    img = Image.open(src_png).convert("RGBA")
    w, h = img.size
    cropped = img.crop((0, 0, w, int(h * bottom_ratio)))
    # Trim transparency margins
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
    cropped.save(dst_png, "PNG", optimize=True)
    return cropped


def to_b64(p: Path, max_w: int = 700) -> str:
    img = Image.open(p).convert("RGBA")
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


# Crop du monogramme (sans le wordmark)
mono_strict = RECOLOR_DIR / "monogram-strict-only.png"
crop_monogram(RECOLOR_DIR / "recolor-strict.png", mono_strict)

# Versions base64
logo_full_1a = to_b64(RECOLOR_DIR / "recolor-strict.png", max_w=600)
monogram_only = to_b64(mono_strict, max_w=240)

html = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

.f-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px; margin-bottom: 32px; }}
.f-card {{ border-radius: 10px; overflow: hidden; cursor: pointer; transition: transform .18s, box-shadow .18s; display: flex; flex-direction: column; background: #fff; }}
.f-card:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0,0,0,.10); }}
.f-stage {{ padding: 52px 32px 42px; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 260px; }}
.f-stage.ivoire {{ background: #FAF6EC; }}
.f-stage.navy {{ background: #14233A; }}
.f-stage img.logo-full {{ max-width: 360px; max-height: 180px; object-fit: contain; }}
.f-stage img.mono {{ max-width: 140px; max-height: 140px; object-fit: contain; margin-bottom: 16px; }}
.f-tagline {{
  font-family: 'Inter', system-ui, sans-serif;
  font-size: 11.5px;
  font-weight: 400;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #B69153;
  margin-top: 14px;
  text-align: center;
}}
.f-tagline.navy-bg {{ color: #B69153; }}
.f-tagline.divider {{
  display: flex; align-items: center; gap: 14px;
  margin-top: 16px;
}}
.f-tagline.divider::before,
.f-tagline.divider::after {{
  content: ''; height: 1px; width: 28px; background: #B69153; opacity: 0.6;
}}
.f-wordmark-svg {{ display: block; margin: 0 auto; }}
.f-meta {{ padding: 18px 22px 22px; background: #fff; border-top: 1px solid rgba(0,0,0,.06); }}
.f-meta .lbl {{ font-family: 'Inter', system-ui; font-size: 11px; letter-spacing: .13em; text-transform: uppercase; color: #888; margin-bottom: 6px; }}
.f-meta .ttl {{ font-family: 'Inter', system-ui; font-size: 16px; font-weight: 600; color: #14233A; margin: 0 0 6px; }}
.f-meta .desc {{ font-family: 'Inter', system-ui; font-size: 12.5px; line-height: 1.5; color: #555; margin: 0; }}
.f-section-head {{ font-family: 'Inter', system-ui; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; color: #888; margin: 36px 0 14px; display: flex; align-items: center; gap: 14px; }}
.f-section-head::after {{ content: ''; height: 1px; background: rgba(0,0,0,.12); flex: 1; }}
</style>

<h2>Itération finale — logo actuel recoloré + tagline doré</h2>
<p class="subtitle">Le logo existant recoloré 1a (or + navy) avec le tagline doré de 2C ajouté dessous. Deux scénarios : <strong>V1</strong> = garder le wordmark actuel tel quel (bold condensed) ; <strong>V2</strong> = remplacer le wordmark par Fraunces 600 pour aligner avec le site V4. Clique ta préférée.</p>

<div class="f-section-head">V1 — Garder le wordmark bold condensed actuel</div>
<div class="f-grid">

  <div class="f-card" data-choice="V1a-ivoire" onclick="toggleSelect(this)">
    <div class="f-stage ivoire">
      <img class="logo-full" src="{logo_full_1a}" alt="Logo 1a + tagline or sur ivoire">
      <div class="f-tagline divider">Conseil en gestion de patrimoine · Paris</div>
    </div>
    <div class="f-meta">
      <div class="lbl">V1a · Le brief exact</div>
      <h3 class="ttl">Logo recolor 1a + tagline doré · fond ivoire</h3>
      <p class="desc">Monogramme et wordmark actuels recolorés or+navy, tagline en Inter 11.5 doré #B69153 avec filets or. Garde l'intégralité de ton logo existant.</p>
    </div>
  </div>

  <div class="f-card" style="background:#14233A;" data-choice="V1b-navy" onclick="toggleSelect(this)">
    <div class="f-stage navy">
      <img class="logo-full" src="{logo_full_1a}" alt="Logo 1a sur fond navy">
      <div class="f-tagline divider navy-bg">Conseil en gestion de patrimoine · Paris</div>
    </div>
    <div class="f-meta">
      <div class="lbl">V1b · Test fond sombre</div>
      <h3 class="ttl">V1a sur fond navy</h3>
      <p class="desc">Même composition sur fond navy — usage footer / carte de visite / papier à en-tête. L'or du tagline pop fort.</p>
    </div>
  </div>

</div>

<div class="f-section-head">V2 — Wordmark remplacé par Fraunces 600 (aligné V4)</div>
<div class="f-grid">

  <div class="f-card" data-choice="V2a-ivoire" onclick="toggleSelect(this)">
    <div class="f-stage ivoire">
      <img class="mono" src="{monogram_only}" alt="Monogramme recoloré seul">
      <svg class="f-wordmark-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 70" style="width:280px;">
        <text x="200" y="52" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#14233A" letter-spacing="-1.2" font-size="48">Berger &amp; Associés</text>
      </svg>
      <div class="f-tagline divider">Conseil en gestion de patrimoine · Paris</div>
    </div>
    <div class="f-meta">
      <div class="lbl">V2a · Alignement V4</div>
      <h3 class="ttl">Monogramme recoloré + Fraunces + tagline doré · ivoire</h3>
      <p class="desc">Le monogramme existant est conservé (recolor 1a), mais le wordmark bold condensed daté est remplacé par Fraunces 600 — même typo que les titres du site. Cohérence totale.</p>
    </div>
  </div>

  <div class="f-card" style="background:#14233A;" data-choice="V2b-navy" onclick="toggleSelect(this)">
    <div class="f-stage navy">
      <img class="mono" src="{monogram_only}" alt="Monogramme recoloré seul">
      <svg class="f-wordmark-svg" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 70" style="width:280px;">
        <text x="200" y="52" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#FAF6EC" letter-spacing="-1.2" font-size="48">Berger &amp; Associés</text>
      </svg>
      <div class="f-tagline divider navy-bg">Conseil en gestion de patrimoine · Paris</div>
    </div>
    <div class="f-meta">
      <div class="lbl">V2b · Test fond sombre</div>
      <h3 class="ttl">V2a sur fond navy</h3>
      <p class="desc">Monogramme or+navy qui ressort sur le navy profond, wordmark Fraunces ivoire, tagline doré. Le plus "maison de confiance" des 4 versions.</p>
    </div>
  </div>

</div>

<div class="section" style="padding:22px 26px; background:rgba(0,0,0,.04); border-radius:10px;">
  <div style="text-transform:uppercase; letter-spacing:.13em; font-size:10.5px; color:#888; margin-bottom:10px;">Mon arbitrage honnête</div>
  <p style="margin:0; font-size:13.5px; line-height:1.7;">
    <strong>V1 (garder le wordmark bold condensed)</strong> : respecte littéralement ton brief — mémoire de marque préservée à 100%. <u>Mais</u> le bold condensed original n'est pas aligné avec la typo du site V4 (Fraunces serif). Tu auras, sur le site, un <em>décalage de voix</em> entre le logo en entête et les titres Fraunces juste en dessous.<br><br>
    <strong>V2 (wordmark en Fraunces)</strong> : garde ton monogramme recoloré (l'ADN visuel), modernise juste le wordmark. L'ensemble devient cohérent avec le site V4. C'est l'équivalent d'un <em>ravalement de façade</em> sans toucher à la structure.<br><br>
    <strong>Ma reco</strong> : <strong>V2a (fond ivoire)</strong> comme composition principale du site, <strong>V2b (fond navy)</strong> pour le footer. V1 à garder en archive seulement.<br><br>
    <u>Note technique</u> : V2 implique 2 "fichiers logo" différents — l'un est ton monogramme actuel en PNG (que tu as déjà), l'autre est un wordmark SVG que je peux te livrer dès validation. Sabine et Marine doivent être d'accord sur ce détachement wordmark.
  </p>
</div>

<div class="section" style="margin-top:20px;">
  <p class="subtitle">→ Clique ta préférée. Après validation, je te livre les fichiers .svg + .png en taille réelle utilisables immédiatement.</p>
</div>
"""

OUT_HTML.write_text(html)
print(f"OK: {OUT_HTML.name} ({len(html.encode())//1024} Ko)")
print(f"Crops: {mono_strict}")
