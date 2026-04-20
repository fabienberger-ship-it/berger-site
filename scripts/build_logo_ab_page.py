"""Genere la page HTML logo-ab-v2.html avec les PNG en base64 inline.
Downscale les images a 700px de large pour rester raisonnable en taille.
"""
import base64
from io import BytesIO
from pathlib import Path
from PIL import Image

IMG_SRC = Path("/Users/fabienberger/berger-site/.superpowers/brainstorm/66468-1776693627/content/img")
OUT_HTML = Path("/Users/fabienberger/berger-site/.superpowers/brainstorm/66468-1776693627/content/logo-ab-v2.html")


def png_to_b64(p: Path, max_w: int = 700) -> str:
    img = Image.open(p).convert("RGBA")
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


imgs = {
    "actuel": png_to_b64(IMG_SRC / "logo-actuel.png"),
    "strict": png_to_b64(IMG_SRC / "recolor-strict.png"),
    "mono_navy": png_to_b64(IMG_SRC / "recolor-mono-navy.png"),
    "mono_ink": png_to_b64(IMG_SRC / "recolor-mono-ink.png"),
}

for name, data in imgs.items():
    kb = len(data) // 1024
    print(f"  {name}: {kb} Ko")

html = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

.logo-grid {{ display: grid; grid-template-columns: repeat(2, 1fr); gap: 22px; margin-bottom: 32px; }}
.logo-card {{ background: #FAF6EC; border-radius: 10px; overflow: hidden; cursor: pointer; transition: transform .18s, box-shadow .18s; display: flex; flex-direction: column; }}
.logo-card:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(0,0,0,.10); }}
.logo-stage {{ padding: 40px 32px; background: #FAF6EC; display: flex; align-items: center; justify-content: center; min-height: 180px; }}
.logo-stage.dark {{ background: #14233A; }}
.logo-stage img {{ max-width: 80%; max-height: 140px; object-fit: contain; }}
.logo-stage svg {{ max-width: 100%; height: auto; }}
.logo-meta {{ padding: 18px 22px 22px; background: #fff; border-top: 1px solid rgba(0,0,0,.06); }}
.logo-meta .lbl {{ font-family: 'Inter', system-ui; font-size: 11px; letter-spacing: .13em; text-transform: uppercase; color: #888; margin-bottom: 6px; }}
.logo-meta .ttl {{ font-family: 'Inter', system-ui; font-size: 16px; font-weight: 600; color: #14233A; margin: 0 0 6px; }}
.logo-meta .desc {{ font-family: 'Inter', system-ui; font-size: 12.5px; line-height: 1.5; color: #555; margin: 0; }}
.section-head {{ font-family: 'Inter', system-ui; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; color: #888; margin: 36px 0 14px; display: flex; align-items: center; gap: 14px; }}
.section-head::after {{ content: ''; height: 1px; background: rgba(0,0,0,.12); flex: 1; }}
</style>

<h2>Traitement logo — A/B visuel (v2, images inline)</h2>
<p class="subtitle">7 variantes, toutes sur fond P2 Ivoire. <strong>Option 1</strong> = PIL recolor (garde le monogramme). <strong>Option 2</strong> = reconstruction SVG vectorielle. Clique celle qui te parle.</p>

<div class="section-head">Référence — logo actuel</div>
<div class="logo-grid" style="grid-template-columns: 1fr;">
  <div class="logo-card" data-choice="00-actuel" onclick="toggleSelect(this)">
    <div class="logo-stage"><img src="{imgs['actuel']}" alt="Logo actuel"></div>
    <div class="logo-meta">
      <div class="lbl">Référence</div>
      <h3 class="ttl">Logo actuel sur palette P2</h3>
      <p class="desc">Bleu ciel + bleu nuit + gradient lustré + ombre portée. Sur fond ivoire, la dissonance chromatique se voit nettement.</p>
    </div>
  </div>
</div>

<div class="section-head">Option 1 — Recolor PIL du PNG (garde le monogramme)</div>
<div class="logo-grid">

  <div class="logo-card" data-choice="O1a-strict" onclick="toggleSelect(this)">
    <div class="logo-stage"><img src="{imgs['strict']}" alt="Recolor strict"></div>
    <div class="logo-meta">
      <div class="lbl">Option 1a · Recolor strict</div>
      <h3 class="ttl">Or + Navy — duotone P2</h3>
      <p class="desc">Bleu clair → or #B69153, bleu nuit → navy #14233A, gris → ardoise. Effet "maison notariale". L'ombre portée subsiste (résolvable par graphiste).</p>
    </div>
  </div>

  <div class="logo-card" data-choice="O1b-mono-navy" onclick="toggleSelect(this)">
    <div class="logo-stage"><img src="{imgs['mono_navy']}" alt="Recolor mono navy"></div>
    <div class="logo-meta">
      <div class="lbl">Option 1b · Mono navy</div>
      <h3 class="ttl">Tout en bleu nuit</h3>
      <p class="desc">Monochrome navy #14233A, silhouette plus sobre. Perd le duotone mais gagne en cohérence pure P2.</p>
    </div>
  </div>

  <div class="logo-card" data-choice="O1c-mono-ink" onclick="toggleSelect(this)">
    <div class="logo-stage"><img src="{imgs['mono_ink']}" alt="Recolor mono encre"></div>
    <div class="logo-meta">
      <div class="lbl">Option 1c · Mono encre</div>
      <h3 class="ttl">Tout en encre neutre</h3>
      <p class="desc">Monochrome #121212. Transférable partout (print, n&amp;b, favicon). Perd la mémoire bleue.</p>
    </div>
  </div>

  <div class="logo-card" style="background:#14233A;" data-choice="O1d-invert-strict" onclick="toggleSelect(this)">
    <div class="logo-stage dark"><img src="{imgs['strict']}" alt="Strict sur fond navy"></div>
    <div class="logo-meta">
      <div class="lbl">Option 1 · Test inverse</div>
      <h3 class="ttl">Recolor strict sur fond navy</h3>
      <p class="desc">Comportement sur fond sombre (footer, mobile dark, print). L'or pop plus, lecture claire.</p>
    </div>
  </div>

</div>

<div class="section-head">Option 2 — Reconstruction SVG vectorielle</div>
<div class="logo-grid">

  <div class="logo-card" data-choice="O2a-wordmark-fraunces" onclick="toggleSelect(this)">
    <div class="logo-stage">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 140" style="width:100%; max-width:520px;">
        <text x="0" y="86" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#14233A" letter-spacing="-1.5" font-size="80">Berger &amp; Associés</text>
        <text x="2" y="122" font-family="Inter, sans-serif" font-weight="400" fill="#5F6574" font-size="12" letter-spacing="2.6">CONSEIL EN GESTION DE PATRIMOINE · PARIS</text>
      </svg>
    </div>
    <div class="logo-meta">
      <div class="lbl">Option 2a · Wordmark éditorial</div>
      <h3 class="ttl">Fraunces 600 — aucun monogramme</h3>
      <p class="desc">Logo texte pur, serif contemporaine alignée avec V4. Abandonne le monogramme `ba`. Le plus chic, le plus radical.</p>
    </div>
  </div>

  <div class="logo-card" data-choice="O2b-wordmark-inter" onclick="toggleSelect(this)">
    <div class="logo-stage">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 700 140" style="width:100%; max-width:520px;">
        <text x="0" y="82" font-family="Inter, sans-serif" font-weight="600" fill="#14233A" letter-spacing="-2.6" font-size="76">Berger &amp; Associés</text>
        <text x="2" y="118" font-family="Inter, sans-serif" font-weight="400" fill="#5F6574" font-size="12" letter-spacing="2.6">CONSEIL EN GESTION DE PATRIMOINE · PARIS</text>
      </svg>
    </div>
    <div class="logo-meta">
      <div class="lbl">Option 2b · Wordmark sobre</div>
      <h3 class="ttl">Inter 600 — aucun monogramme</h3>
      <p class="desc">Version sans-serif, plus sobre encore. Moderne sans clinquant. 100% V4 Minéral parisien.</p>
    </div>
  </div>

  <div class="logo-card" data-choice="O2c-mark" onclick="toggleSelect(this)">
    <div class="logo-stage">
      <div style="display:flex; align-items:center; gap:28px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" style="width:110px; height:110px;">
          <circle cx="100" cy="100" r="96" fill="#14233A"/>
          <circle cx="100" cy="100" r="94" fill="none" stroke="#B69153" stroke-width="0.75"/>
          <text x="100" y="128" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#FAF6EC" font-size="88" letter-spacing="-3">b&amp;a</text>
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 140" style="width:280px;">
          <text x="0" y="86" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#14233A" letter-spacing="-1.5" font-size="66">Berger &amp; Associés</text>
          <text x="2" y="118" font-family="Inter, sans-serif" font-weight="400" fill="#5F6574" font-size="10.5" letter-spacing="2.4">CONSEIL EN GESTION DE PATRIMOINE · PARIS</text>
        </svg>
      </div>
    </div>
    <div class="logo-meta">
      <div class="lbl">Option 2c · Mark + wordmark</div>
      <h3 class="ttl">Nouveau mark minimal "b&amp;a"</h3>
      <p class="desc">Petit monogramme sobre (cercle navy + filet or + b&amp;a en Fraunces) + wordmark. Garde l'esprit "marque" pour favicon/avatar. Compromis.</p>
    </div>
  </div>

  <div class="logo-card" style="background:#14233A;" data-choice="O2d-mark-inverse" onclick="toggleSelect(this)">
    <div class="logo-stage dark">
      <div style="display:flex; align-items:center; gap:28px;">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 200" style="width:110px; height:110px;">
          <circle cx="100" cy="100" r="96" fill="#FAF6EC"/>
          <circle cx="100" cy="100" r="94" fill="none" stroke="#14233A" stroke-width="1"/>
          <text x="100" y="128" text-anchor="middle" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#14233A" font-size="88" letter-spacing="-3">b&amp;a</text>
        </svg>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 140" style="width:280px;">
          <text x="0" y="86" font-family="Fraunces, Georgia, serif" font-weight="600" fill="#FAF6EC" letter-spacing="-1.5" font-size="66">Berger &amp; Associés</text>
          <text x="2" y="118" font-family="Inter, sans-serif" font-weight="400" fill="#B69153" font-size="10.5" letter-spacing="2.4">CONSEIL EN GESTION DE PATRIMOINE · PARIS</text>
        </svg>
      </div>
    </div>
    <div class="logo-meta">
      <div class="lbl">Option 2c · Test inverse</div>
      <h3 class="ttl">Mark + wordmark sur fond navy</h3>
      <p class="desc">Test sur fond sombre (footer, carte de visite, papier à en-tête). Touche or sur le tagline.</p>
    </div>
  </div>

</div>

<div class="section" style="padding:22px 26px; background:rgba(0,0,0,.04); border-radius:10px;">
  <div style="text-transform:uppercase; letter-spacing:.13em; font-size:10.5px; color:#888; margin-bottom:10px;">Mon arbitrage honnête</div>
  <p style="margin:0; font-size:13.5px; line-height:1.7;">
    <strong>1a (Strict or + navy)</strong> : meilleur rapport bénéfice/coût pour garder l'existant. Signal maison notariale. <u>Mais</u> l'ombre et le gradient lustré restent — PIL ne peut pas les supprimer sans dégrader.<br><br>
    <strong>2a (Wordmark Fraunces seul)</strong> : le plus aligné V4. <u>Mais</u> abandonne le monogramme — décision de marque lourde.<br><br>
    <strong>2c (Mark minimal + wordmark)</strong> : meilleur compromis. Garde un mark reconnaissable pour carrés (favicon, LinkedIn), et wordmark propre pour le site.<br><br>
    <strong>Ma reco pour décision collégiale Sabine &amp; Marine :</strong> présentez <strong>1a</strong> vs <strong>2c</strong>. 1a = rénovation légère mémoire préservée. 2c = modernisation vraie, alignement total.
  </p>
</div>

<div class="section" style="margin-top:20px;">
  <p class="subtitle">→ Clique ta préférée, ou décris une variante manquante.</p>
</div>
"""

OUT_HTML.write_text(html)
size_kb = len(html.encode()) // 1024
print(f"\nHTML genere: {OUT_HTML.name} ({size_kb} Ko total)")
