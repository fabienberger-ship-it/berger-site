"""Page compositions horizontales pro avec le monogramme nettoye.

4 compositions :
- H1 ivoire : horizontal classique [monogramme] [wordmark Fraunces + tagline dore]
- H1 navy : meme sur fond sombre
- V1 ivoire : vertical centre avec monogramme plus grand
- V1 navy : meme sur fond sombre
"""
import base64
from io import BytesIO
from pathlib import Path
from PIL import Image

SRC_MONO = Path("/Users/fabienberger/berger-site/assets/logo-recolor/monogram-noshadow.png")
OUT_HTML = Path("/Users/fabienberger/berger-site/.superpowers/brainstorm/66468-1776693627/content/logo-horizontal.html")


def to_b64(p: Path, max_w: int = 500) -> str:
    img = Image.open(p).convert("RGBA")
    if img.width > max_w:
        ratio = max_w / img.width
        img = img.resize((max_w, int(img.height * ratio)), Image.LANCZOS)
    buf = BytesIO()
    img.save(buf, "PNG", optimize=True)
    return "data:image/png;base64," + base64.b64encode(buf.getvalue()).decode()


mono = to_b64(SRC_MONO, max_w=420)

html = f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');

.comp-card {{
  border-radius: 10px;
  overflow: hidden;
  cursor: pointer;
  transition: transform .18s, box-shadow .18s;
  margin-bottom: 26px;
}}
.comp-card:hover {{ transform: translateY(-2px); box-shadow: 0 14px 36px rgba(0,0,0,.10); }}
.comp-stage {{ padding: 70px 56px; display: flex; align-items: center; justify-content: center; min-height: 280px; }}
.comp-stage.ivoire {{ background: #FAF6EC; }}
.comp-stage.navy {{ background: #14233A; }}

/* Layout horizontal : monogramme a gauche, wordmark a droite */
.comp-horiz {{ display: flex; align-items: center; gap: 36px; }}
.comp-horiz img.mono {{ width: 135px; height: auto; flex-shrink: 0; }}
.comp-horiz .text-block {{ display: flex; flex-direction: column; gap: 10px; }}
.comp-horiz .wordmark {{ font-family: 'Fraunces', Georgia, serif; font-weight: 600; font-size: 46px; line-height: 1; letter-spacing: -.03em; color: #14233A; margin: 0; }}
.comp-horiz.navy-fg .wordmark {{ color: #FAF6EC; }}
.comp-horiz .tagline {{
  font-family: 'Inter', sans-serif;
  font-size: 11.5px;
  font-weight: 400;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #B69153;
  display: flex; align-items: center; gap: 10px;
}}
.comp-horiz .tagline::before,
.comp-horiz .tagline::after {{
  content: ''; height: 1px; width: 18px; background: #B69153; opacity: .55;
}}
.comp-horiz .divider {{
  width: 1px; height: 90px; background: rgba(20,35,58,.2);
  margin: 0 8px;
}}
.comp-horiz.navy-fg .divider {{ background: rgba(255,255,255,.18); }}

/* Layout vertical : tout centre */
.comp-vert {{ display: flex; flex-direction: column; align-items: center; gap: 22px; text-align: center; }}
.comp-vert img.mono {{ width: 180px; height: auto; }}
.comp-vert .wordmark {{ font-family: 'Fraunces', Georgia, serif; font-weight: 600; font-size: 52px; line-height: 1; letter-spacing: -.03em; color: #14233A; margin: 0; }}
.comp-vert.navy-fg .wordmark {{ color: #FAF6EC; }}
.comp-vert .tagline {{
  font-family: 'Inter', sans-serif;
  font-size: 11.5px;
  font-weight: 400;
  letter-spacing: .22em;
  text-transform: uppercase;
  color: #B69153;
  display: flex; align-items: center; gap: 14px;
}}
.comp-vert .tagline::before,
.comp-vert .tagline::after {{
  content: ''; height: 1px; width: 26px; background: #B69153; opacity: .55;
}}

.comp-meta {{ padding: 18px 22px 22px; background: #fff; border-top: 1px solid rgba(0,0,0,.06); }}
.comp-meta .lbl {{ font-family: 'Inter', system-ui; font-size: 11px; letter-spacing: .13em; text-transform: uppercase; color: #888; margin-bottom: 6px; }}
.comp-meta .ttl {{ font-family: 'Inter', system-ui; font-size: 15.5px; font-weight: 600; color: #14233A; margin: 0 0 4px; }}
.comp-meta .desc {{ font-family: 'Inter', system-ui; font-size: 12.5px; line-height: 1.5; color: #555; margin: 0; }}

.sec-hd {{ font-family: 'Inter', system-ui; font-size: 13px; letter-spacing: .14em; text-transform: uppercase; color: #888; margin: 34px 0 14px; display: flex; align-items: center; gap: 14px; }}
.sec-hd::after {{ content: ''; height: 1px; background: rgba(0,0,0,.12); flex: 1; }}

.comp-grid-2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }}
</style>

<h2>Logo — compositions pro avec monogramme nettoyé</h2>
<p class="subtitle">Monogramme recoloré or+navy, ombre portée quasi-totalement retirée (léger résiduel qui se fondra sur ivoire/navy). Wordmark en Fraunces 600 aligné V4. Tagline doré à la 2C. Deux layouts : <strong>horizontal</strong> (carte de visite, signature mail) et <strong>vertical</strong> (page d'accueil, formats carrés).</p>

<div class="sec-hd">Horizontal — pour en-tête site, signature mail, papier à en-tête</div>
<div class="comp-grid-2">

  <div class="comp-card" data-choice="H1a-ivoire" onclick="toggleSelect(this)">
    <div class="comp-stage ivoire">
      <div class="comp-horiz">
        <img class="mono" src="{mono}" alt="Monogramme nettoyé">
        <div class="divider"></div>
        <div class="text-block">
          <h1 class="wordmark">Berger &amp; Associés</h1>
          <div class="tagline">Conseil en gestion de patrimoine · Paris</div>
        </div>
      </div>
    </div>
    <div class="comp-meta">
      <div class="lbl">H1a · Horizontal ivoire</div>
      <h3 class="ttl">Monogramme + wordmark Fraunces + tagline doré</h3>
      <p class="desc">Layout carte de visite. Monogramme à gauche, wordmark Fraunces 600 + tagline doré avec filets or à droite, séparés par un fin filet vertical.</p>
    </div>
  </div>

  <div class="comp-card" data-choice="H1b-navy" onclick="toggleSelect(this)">
    <div class="comp-stage navy">
      <div class="comp-horiz navy-fg">
        <img class="mono" src="{mono}" alt="Monogramme sur fond navy">
        <div class="divider"></div>
        <div class="text-block">
          <h1 class="wordmark">Berger &amp; Associés</h1>
          <div class="tagline">Conseil en gestion de patrimoine · Paris</div>
        </div>
      </div>
    </div>
    <div class="comp-meta">
      <div class="lbl">H1b · Horizontal navy</div>
      <h3 class="ttl">Version fond sombre</h3>
      <p class="desc">Pour footer site, signature mail en mode sombre, back de carte de visite, papier à en-tête coloré. L'or du monogramme et du tagline ressort fort.</p>
    </div>
  </div>

</div>

<div class="sec-hd">Vertical — pour hero page d'accueil, formats carrés, couvertures</div>
<div class="comp-grid-2">

  <div class="comp-card" data-choice="V1a-ivoire" onclick="toggleSelect(this)">
    <div class="comp-stage ivoire">
      <div class="comp-vert">
        <img class="mono" src="{mono}" alt="Monogramme vertical">
        <h1 class="wordmark">Berger &amp; Associés</h1>
        <div class="tagline">Conseil en gestion de patrimoine · Paris</div>
      </div>
    </div>
    <div class="comp-meta">
      <div class="lbl">V1a · Vertical ivoire</div>
      <h3 class="ttl">Empilé centré — monogramme 180px</h3>
      <p class="desc">Layout page de couverture / hero section / formats carrés (Instagram, LinkedIn cover). Monogramme plus grand (180px), wordmark Fraunces 600, tagline doré dessous.</p>
    </div>
  </div>

  <div class="comp-card" data-choice="V1b-navy" onclick="toggleSelect(this)">
    <div class="comp-stage navy">
      <div class="comp-vert navy-fg">
        <img class="mono" src="{mono}" alt="Monogramme vertical sur navy">
        <h1 class="wordmark">Berger &amp; Associés</h1>
        <div class="tagline">Conseil en gestion de patrimoine · Paris</div>
      </div>
    </div>
    <div class="comp-meta">
      <div class="lbl">V1b · Vertical navy</div>
      <h3 class="ttl">Version fond sombre</h3>
      <p class="desc">Pour rapport PDF de couverture, papier à en-tête premium, carte de vœux. Le plus "maison privée" des 4 compositions.</p>
    </div>
  </div>

</div>

<div class="section" style="padding:22px 26px; background:rgba(0,0,0,.04); border-radius:10px;">
  <div style="text-transform:uppercase; letter-spacing:.13em; font-size:10.5px; color:#888; margin-bottom:10px;">Comment choisir</div>
  <p style="margin:0; font-size:13.5px; line-height:1.7;">
    <strong>H1a</strong> = le logo principal du site (en-tête), signature mail, cartes de visite recto. <br>
    <strong>H1b</strong> = footer du site, back de carte de visite. <br>
    <strong>V1a</strong> = hero de la page d'accueil (centré, grand), avatar social LinkedIn. <br>
    <strong>V1b</strong> = couverture de rapports PDF, papier à en-tête premium. <br><br>
    <strong>Les 4 se complètent</strong> — on va avoir besoin des 4 dans différents contextes du site. La question à valider n'est pas "lequel choisir" mais <em>"est-ce que l'ensemble colle à ce que tu as en tête"</em>. Si oui, je te les livre en PNG haute résolution + SVG texte.<br><br>
    <u>Note sur le halo</u> : il reste un halo gris très léger autour du monogramme, inhérent à la fusion ombre+contour du PNG d'origine. Sur ivoire et navy il est quasi invisible. Pour un résultat pixel-perfect sans halo, il faut passer par un graphiste qui ouvre l'AI dans Illustrator (travail de 1-2h, ~100-200€ — à prévoir si tu veux des fichiers 100% propres pour le print).
  </p>
</div>

<div class="section" style="margin-top:20px;">
  <p class="subtitle">→ Clique une composition pour valider, ou dis-moi ce qui cloche encore (proportions, espacements, taille du tagline, etc.).</p>
</div>
"""

OUT_HTML.write_text(html)
print(f"OK: {OUT_HTML.name} ({len(html.encode())//1024} Ko)")
