# Phase 1 — Landing urgence conforme — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Remplacer le site Wix actuel par une landing page statique Astro, hébergée sur Cloudflare Pages, conforme CIF / courtier / RGPD dès le jour 1 — en 7-10 jours de travail.

**Architecture:** Site statique mono-page + 4 pages légales. Astro 5.x + vanilla CSS avec design tokens, zéro framework UI, zéro CMS (Phase 1 hardcoded), bandeau cookies custom vanilla JS, formulaire contact en `mailto:` (upgrade vers Worker en Phase 2). Déploiement Cloudflare Pages (CDN + HTTPS + preview par PR, gratuit). Palette P2 « Ivoire & Nuit » + typographies Inter + Fraunces via Google Fonts.

**Tech Stack:** Astro 5.x · TypeScript strict · vanilla CSS · Playwright (tests a11y) · axe-core · Cloudflare Pages · GitHub · Node 20+ · npm

---

## Prérequis — informations à collecter avant Task 7

Ces informations sont **bloquantes pour les pages légales**. Elles doivent être confirmées avant l'exécution de Task 7 (mentions légales) :

- [ ] **Siège social** : adresse complète (numéro, rue, code postal, ville)
- [ ] **Identité cabinet** : raison sociale, forme juridique, capital social, numéro SIRET, RCS (ville + numéro)
- [ ] **Directeur de la publication** : nom du dirigeant désigné (par défaut : Fabien Berger)
- [ ] **DPO RGPD** : nom + email du DPO (par défaut : Fabien Berger, `fabien.berger@berger-associes.fr`)
- [ ] **ORIAS** : 13004419 (connu) — confirmer les catégories enregistrées (CIF + courtier + ?)
- [ ] **Statut CIF** : association de rattachement (CNCGP) + numéro d'adhérent
- [ ] **Courtier assurances** : préciser catégorie (courtier / mandataire non exclusif / agent général)
- [ ] **ACPR** : adresse complète + mention numéro d'enregistrement
- [ ] **RCP** (responsabilité civile professionnelle) : assureur, numéro de police, plafond annuel
- [ ] **Médiateur AMF** : adresse (publique) — à copier depuis site officiel
- [ ] **Médiateur consommation CNCGP** : nom + coordonnées
- [ ] **Procédure réclamation interne** : texte rédigé (délais : 10 jours accusé réception, 2 mois réponse)
- [ ] **Emails associés** créés chez le provider : `fabien.berger@berger-associes.fr`, `sabine.tellier@berger-associes.fr`, `marine.gorin@berger-associes.fr`, `contact@berger-associes.fr`
- [ ] **Hébergeur Wix actuel** : vérifier échéance abonnement (pour éviter de payer après migration)

**Validation juridique** : mentions légales à faire relire par Vie Legia Conseil (Javi) ou juriste spécialisé CIF avant mise en ligne publique.

---

### Task 1 : Initialiser le projet Astro

**Files:**
- Create: `package.json`, `astro.config.mjs`, `tsconfig.json`, `src/env.d.ts`, `README.md`
- Modify: `.gitignore`

- [ ] **Step 1 : Initialiser Astro en mode minimal**

```bash
cd /Users/fabienberger/berger-site
npm create astro@latest . -- --template minimal --typescript strict --install --git --yes
```

Si Astro refuse d'initialiser dans un dossier non vide : utiliser `--force`. Le template minimal crée `src/`, `public/`, `astro.config.mjs`, `package.json`, `tsconfig.json`.

- [ ] **Step 2 : Vérifier que la build de base fonctionne**

```bash
npm run build
```

Expected output : `✓ Build Complete in X s` sans erreur.

- [ ] **Step 3 : Lancer le dev server et vérifier accès**

```bash
npm run dev
```

Expected : `> Local: http://localhost:4321/`. Ouvrir le navigateur, voir la page placeholder Astro.

- [ ] **Step 4 : Supprimer le contenu placeholder d'Astro**

Supprimer `src/pages/index.astro` (on le recrée en Task 6). Supprimer `src/assets/astro.svg` et autres assets du template minimal.

- [ ] **Step 5 : Ajouter les dépendances dev nécessaires**

```bash
npm install --save-dev @playwright/test @axe-core/playwright
npx playwright install chromium
```

- [ ] **Step 6 : Mettre à jour `.gitignore` pour Astro**

Ajouter à la fin de `/Users/fabienberger/berger-site/.gitignore` :

```
# Astro build output
dist/
.astro/

# npm
node_modules/

# Playwright
test-results/
playwright-report/
```

- [ ] **Step 7 : Commit**

```bash
git add -A && git commit -m "chore: init astro 5 project with playwright"
```

---

### Task 2 : Design tokens CSS (palette, typo, espaces)

**Files:**
- Create: `src/styles/tokens.css`, `src/styles/global.css`

- [ ] **Step 1 : Créer `src/styles/tokens.css`**

```css
/* Design tokens — palette P2 "Ivoire & Nuit" + typographies */
:root {
  /* Palette */
  --c-ivoire: #FAF6EC;
  --c-navy: #14233A;
  --c-slate: #5F6574;
  --c-gold: #B69153;
  --c-sand: #E8DEC9;
  --c-white: #FFFFFF;

  /* Semantic roles */
  --c-bg: var(--c-ivoire);
  --c-fg: var(--c-navy);
  --c-fg-muted: var(--c-slate);
  --c-accent: var(--c-gold);
  --c-divider: rgba(20, 35, 58, 0.12);

  /* Typography */
  --ff-sans: 'Inter', system-ui, -apple-system, 'Helvetica Neue', sans-serif;
  --ff-serif: 'Fraunces', Georgia, 'Times New Roman', serif;

  --fs-xs: 0.75rem;    /* 12px */
  --fs-sm: 0.875rem;   /* 14px */
  --fs-base: 1rem;     /* 16px */
  --fs-lg: 1.125rem;   /* 18px */
  --fs-xl: 1.375rem;   /* 22px */
  --fs-2xl: 1.75rem;   /* 28px */
  --fs-3xl: 2.5rem;    /* 40px */
  --fs-4xl: 3.75rem;   /* 60px */
  --fs-5xl: 5rem;      /* 80px */

  --lh-tight: 1.05;
  --lh-snug: 1.2;
  --lh-normal: 1.55;
  --lh-loose: 1.7;

  /* Spacing scale (8px base) */
  --s-1: 0.5rem;   /* 8 */
  --s-2: 1rem;     /* 16 */
  --s-3: 1.5rem;   /* 24 */
  --s-4: 2rem;     /* 32 */
  --s-5: 3rem;     /* 48 */
  --s-6: 4.5rem;   /* 72 */
  --s-7: 6rem;     /* 96 */

  /* Layout */
  --max-content: 960px;
  --max-wide: 1200px;
  --page-gutter: clamp(1.25rem, 4vw, 3rem);

  /* Borders / shadows */
  --radius-sm: 2px;
  --radius-md: 8px;
  --shadow-sm: 0 1px 2px rgba(20, 35, 58, 0.06);

  /* Motion */
  --ease-standard: cubic-bezier(0.4, 0.0, 0.2, 1);
  --dur-fast: 0.18s;
  --dur-normal: 0.3s;
}

@media (prefers-color-scheme: dark) {
  /* Note Phase 1 : pas de dark mode. Intentionnellement vide. */
}

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

- [ ] **Step 2 : Créer `src/styles/global.css`**

```css
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Inter:wght@400;500;600&display=swap');
@import './tokens.css';

/* Reset minimal */
*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  -webkit-text-size-adjust: 100%;
  scroll-behavior: smooth;
}

body {
  background: var(--c-bg);
  color: var(--c-fg);
  font-family: var(--ff-sans);
  font-size: var(--fs-base);
  line-height: var(--lh-normal);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--ff-sans);
  font-weight: 500;
  letter-spacing: -0.03em;
  line-height: var(--lh-tight);
}

.editorial {
  font-family: var(--ff-serif);
  font-weight: 500;
  letter-spacing: -0.015em;
}

a {
  color: var(--c-accent);
  text-decoration: underline;
  text-underline-offset: 4px;
  text-decoration-thickness: 1px;
  transition: opacity var(--dur-fast) var(--ease-standard);
}

a:hover { opacity: 0.75; }
a:focus-visible {
  outline: 2px solid var(--c-accent);
  outline-offset: 3px;
  border-radius: var(--radius-sm);
}

img { max-width: 100%; height: auto; display: block; }

button {
  font-family: inherit;
  font-size: inherit;
  color: inherit;
  cursor: pointer;
  border: 0;
  background: transparent;
}

.container {
  width: 100%;
  max-width: var(--max-content);
  margin-inline: auto;
  padding-inline: var(--page-gutter);
}

.container-wide {
  width: 100%;
  max-width: var(--max-wide);
  margin-inline: auto;
  padding-inline: var(--page-gutter);
}

.sr-only {
  position: absolute;
  width: 1px; height: 1px;
  padding: 0; margin: -1px;
  overflow: hidden; clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

.visually-hidden-focusable:not(:focus):not(:focus-within) {
  position: absolute !important;
  width: 1px !important; height: 1px !important;
  padding: 0 !important; margin: -1px !important;
  overflow: hidden !important; clip: rect(0, 0, 0, 0) !important;
}
```

- [ ] **Step 3 : Commit**

```bash
git add src/styles/ && git commit -m "feat(styles): design tokens palette P2 + global styles"
```

---

### Task 3 : BaseLayout Astro + SEO head

**Files:**
- Create: `src/layouts/BaseLayout.astro`, `src/components/SEOHead.astro`

- [ ] **Step 1 : Créer `src/components/SEOHead.astro`**

```astro
---
interface Props {
  title: string;
  description: string;
  canonicalPath?: string;
  noindex?: boolean;
}

const { title, description, canonicalPath = '/', noindex = false } = Astro.props;
const siteName = 'Berger & Associés';
const siteUrl = 'https://www.berger-associes.fr';
const canonicalUrl = siteUrl + canonicalPath;
const ogImage = `${siteUrl}/og-default.png`;
---

<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<meta name="generator" content={Astro.generator} />
<title>{title}</title>
<meta name="description" content={description} />
<link rel="canonical" href={canonicalUrl} />

{noindex && <meta name="robots" content="noindex, nofollow" />}

<meta property="og:type" content="website" />
<meta property="og:site_name" content={siteName} />
<meta property="og:title" content={title} />
<meta property="og:description" content={description} />
<meta property="og:url" content={canonicalUrl} />
<meta property="og:image" content={ogImage} />
<meta property="og:locale" content="fr_FR" />

<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content={title} />
<meta name="twitter:description" content={description} />

<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
<link rel="icon" type="image/png" href="/favicon.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />

<script type="application/ld+json" is:inline set:html={JSON.stringify({
  "@context": "https://schema.org",
  "@type": "FinancialService",
  "name": siteName,
  "url": siteUrl,
  "description": description,
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Paris",
    "addressCountry": "FR"
  }
})} />
```

- [ ] **Step 2 : Créer `src/layouts/BaseLayout.astro`**

```astro
---
import '../styles/global.css';
import SEOHead from '../components/SEOHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import CookieBanner from '../components/CookieBanner.astro';

interface Props {
  title: string;
  description: string;
  canonicalPath?: string;
  noindex?: boolean;
}

const { title, description, canonicalPath, noindex } = Astro.props;
---

<!DOCTYPE html>
<html lang="fr">
  <head>
    <SEOHead {title} {description} {canonicalPath} {noindex} />
  </head>
  <body>
    <a href="#main" class="visually-hidden-focusable">Aller au contenu principal</a>
    <Header />
    <main id="main">
      <slot />
    </main>
    <Footer />
    <CookieBanner />
  </body>
</html>
```

- [ ] **Step 3 : Commit (build cassera temporairement faute de Header/Footer/CookieBanner — les tasks suivantes les créent)**

```bash
git add src/layouts/ src/components/SEOHead.astro && git commit -m "feat(layout): base layout + SEO head component"
```

---

### Task 4 : Header component (navigation)

**Files:**
- Create: `src/components/Header.astro`

- [ ] **Step 1 : Créer `src/components/Header.astro`**

```astro
---
const navItems = [
  { href: '/', label: 'Accueil' },
  { href: '/mentions-legales', label: 'Mentions légales' },
  { href: '/confidentialite', label: 'Confidentialité' },
  { href: '/cookies', label: 'Cookies' },
];

const currentPath = Astro.url.pathname;
---

<header class="site-header">
  <div class="container-wide site-header__inner">
    <a href="/" class="site-header__brand" aria-label="Berger & Associés — retour à l'accueil">
      <img src="/logos/logo-horizontal-ivoire.png" alt="Berger & Associés" width="280" height="60" />
    </a>

    <nav aria-label="Navigation principale">
      <ul class="site-header__nav">
        {navItems.map(({ href, label }) => (
          <li>
            <a
              href={href}
              class:list={['site-header__link', { 'is-active': currentPath === href }]}
            >
              {label}
            </a>
          </li>
        ))}
      </ul>
    </nav>
  </div>
</header>

<style>
  .site-header {
    border-bottom: 1px solid var(--c-divider);
    background: var(--c-bg);
    position: sticky;
    top: 0;
    z-index: 10;
    backdrop-filter: saturate(140%) blur(8px);
  }

  .site-header__inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    min-height: 72px;
    padding-block: var(--s-2);
    gap: var(--s-4);
  }

  .site-header__brand img {
    max-height: 44px;
    width: auto;
  }

  .site-header__nav {
    list-style: none;
    display: flex;
    gap: var(--s-4);
    font-size: var(--fs-sm);
  }

  .site-header__link {
    color: var(--c-fg-muted);
    text-decoration: none;
    font-weight: 400;
    transition: color var(--dur-fast) var(--ease-standard);
  }

  .site-header__link:hover { color: var(--c-fg); opacity: 1; }
  .site-header__link.is-active { color: var(--c-fg); font-weight: 500; }

  @media (max-width: 720px) {
    .site-header__inner { flex-direction: column; gap: var(--s-2); padding-block: var(--s-3); }
    .site-header__nav { flex-wrap: wrap; justify-content: center; gap: var(--s-3); }
  }
</style>
```

- [ ] **Step 2 : Commit**

```bash
git add src/components/Header.astro && git commit -m "feat(components): site header + responsive nav"
```

---

### Task 5 : Footer component

**Files:**
- Create: `src/components/Footer.astro`

- [ ] **Step 1 : Créer `src/components/Footer.astro`**

```astro
---
const year = new Date().getFullYear();
---

<footer class="site-footer">
  <div class="container-wide site-footer__inner">
    <div class="site-footer__brand">
      <img src="/logos/logo-horizontal-navy.png" alt="Berger & Associés" width="240" height="60" />
      <p class="site-footer__tagline">Conseil en gestion de patrimoine · Paris</p>
    </div>

    <div class="site-footer__col">
      <h2 class="site-footer__h">Contact</h2>
      <ul class="site-footer__list">
        <li><a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a></li>
        <li>Paris · France</li>
      </ul>
    </div>

    <div class="site-footer__col">
      <h2 class="site-footer__h">Agréments</h2>
      <ul class="site-footer__list">
        <li>ORIAS n° 13004419</li>
        <li>Membre CNCGP</li>
        <li>Sous contrôle ACPR / AMF</li>
      </ul>
    </div>

    <div class="site-footer__col">
      <h2 class="site-footer__h">Informations</h2>
      <ul class="site-footer__list">
        <li><a href="/mentions-legales">Mentions légales</a></li>
        <li><a href="/confidentialite">Politique de confidentialité</a></li>
        <li><a href="/cookies">Politique cookies</a></li>
      </ul>
    </div>
  </div>

  <div class="site-footer__bar">
    <div class="container-wide">
      <p>© {year} Berger &amp; Associés. Tous droits réservés.</p>
    </div>
  </div>
</footer>

<style>
  .site-footer {
    background: var(--c-navy);
    color: var(--c-ivoire);
    margin-top: var(--s-7);
  }

  .site-footer__inner {
    display: grid;
    grid-template-columns: 1.3fr 1fr 1fr 1fr;
    gap: var(--s-5);
    padding-block: var(--s-6) var(--s-5);
  }

  .site-footer__brand img { filter: none; max-height: 52px; width: auto; }

  .site-footer__tagline {
    font-size: var(--fs-xs);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--c-gold);
    margin-top: var(--s-2);
  }

  .site-footer__h {
    font-size: var(--fs-xs);
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--c-gold);
    margin-bottom: var(--s-2);
    font-weight: 500;
  }

  .site-footer__list { list-style: none; font-size: var(--fs-sm); line-height: var(--lh-loose); }

  .site-footer__list a {
    color: var(--c-ivoire);
    text-decoration: none;
    opacity: 0.8;
  }

  .site-footer__list a:hover { opacity: 1; }

  .site-footer__bar {
    border-top: 1px solid rgba(250, 246, 236, 0.1);
    padding-block: var(--s-3);
    font-size: var(--fs-xs);
    color: rgba(250, 246, 236, 0.6);
  }

  @media (max-width: 900px) {
    .site-footer__inner { grid-template-columns: 1fr 1fr; gap: var(--s-4); }
  }
  @media (max-width: 540px) {
    .site-footer__inner { grid-template-columns: 1fr; }
  }
</style>
```

- [ ] **Step 2 : Commit**

```bash
git add src/components/Footer.astro && git commit -m "feat(components): site footer with agréments + legal links"
```

---

### Task 6 : Intégrer les logos (copier depuis assets/, placer dans public/logos/)

**Files:**
- Copy: `assets/logo-recolor/*.png` → `public/logos/*.png`
- Create: `public/favicon.svg`, `public/favicon.png`, `public/apple-touch-icon.png`, `public/og-default.png`

- [ ] **Step 1 : Créer la structure `public/logos/`**

```bash
mkdir -p /Users/fabienberger/berger-site/public/logos
```

- [ ] **Step 2 : Préparer les 4 compositions logo + favicon**

Utilise le script déjà écrit (`scripts/build_logo_horizontal_page.py`) comme référence pour les dimensions / palette. Pour Phase 1 on livre les **4 compositions minimales** en PNG + 1 favicon SVG :

Lance ce script (nouveau) :

```bash
"/Users/fabienberger/GROUPE MERCURY Dropbox/BERGER ET ASSOCIES/BergerApp/.venv/bin/python3" << 'PY'
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import shutil

SRC_RECOLOR = Path("/Users/fabienberger/berger-site/assets/logo-recolor/recolor-strict.png")
SRC_MONO = Path("/Users/fabienberger/berger-site/assets/logo-recolor/monogram-noshadow.png")
OUT = Path("/Users/fabienberger/berger-site/public/logos")
OUT.mkdir(parents=True, exist_ok=True)

# Pour Phase 1 : on recopie le full logo (recolor-strict = monogramme + wordmark existant)
# et le monogramme nettoyé (monogram-noshadow).
shutil.copy(SRC_RECOLOR, OUT / "logo-horizontal-ivoire.png")
shutil.copy(SRC_RECOLOR, OUT / "logo-horizontal-navy.png")  # meme fichier, le CSS/HTML gere le fond
shutil.copy(SRC_MONO, OUT / "logo-vertical-ivoire.png")
shutil.copy(SRC_MONO, OUT / "logo-vertical-navy.png")
shutil.copy(SRC_MONO, OUT / "monogram.png")

# Favicon 32x32
img = Image.open(SRC_MONO).convert("RGBA")
img.thumbnail((128, 128), Image.LANCZOS)
img.save(OUT.parent / "favicon.png", optimize=True)
img.thumbnail((32, 32), Image.LANCZOS)

# Apple touch icon 180x180 (on part du monogramme sur fond navy)
at = Image.new("RGBA", (180, 180), (0x14, 0x23, 0x3A, 255))
mono = Image.open(SRC_MONO).convert("RGBA")
mono.thumbnail((150, 150), Image.LANCZOS)
mx = (180 - mono.width) // 2
my = (180 - mono.height) // 2
at.paste(mono, (mx, my), mono)
at.save(OUT.parent / "apple-touch-icon.png", optimize=True)

print("Logos livrés dans", OUT)
PY
```

- [ ] **Step 3 : Créer un favicon SVG simple (monogramme navy + or)**

Écrire `public/favicon.svg` :

```xml
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <circle cx="32" cy="32" r="30" fill="#14233A"/>
  <circle cx="32" cy="32" r="29" fill="none" stroke="#B69153" stroke-width="0.5"/>
  <text x="50%" y="62%" text-anchor="middle" fill="#FAF6EC" font-family="Georgia, serif" font-weight="600" font-size="28" letter-spacing="-1">b&amp;a</text>
</svg>
```

- [ ] **Step 4 : Créer `public/og-default.png` (1200×630 pour partage social)**

```bash
"/Users/fabienberger/GROUPE MERCURY Dropbox/BERGER ET ASSOCIES/BergerApp/.venv/bin/python3" << 'PY'
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W, H = 1200, 630
img = Image.new("RGBA", (W, H), (0x14, 0x23, 0x3A, 255))
mono = Image.open("/Users/fabienberger/berger-site/assets/logo-recolor/monogram-noshadow.png").convert("RGBA")
mono.thumbnail((220, 220), Image.LANCZOS)
mx = (W - mono.width) // 2
img.paste(mono, (mx, 140), mono)

d = ImageDraw.Draw(img)
# Polices systeme (best effort sans embed)
try:
    f_title = ImageFont.truetype("/System/Library/Fonts/Supplemental/Georgia.ttf", 72)
    f_sub = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
except OSError:
    f_title = ImageFont.load_default()
    f_sub = ImageFont.load_default()

title = "Berger & Associés"
bbox = d.textbbox((0, 0), title, font=f_title)
tw = bbox[2] - bbox[0]
d.text(((W - tw) / 2, 410), title, font=f_title, fill=(0xFA, 0xF6, 0xEC))

sub = "CONSEIL EN GESTION DE PATRIMOINE · PARIS"
bbox = d.textbbox((0, 0), sub, font=f_sub)
sw = bbox[2] - bbox[0]
d.text(((W - sw) / 2, 510), sub, font=f_sub, fill=(0xB6, 0x91, 0x53))

img.save("/Users/fabienberger/berger-site/public/og-default.png", optimize=True)
print("OG image créée")
PY
```

- [ ] **Step 5 : Vérifier rendu favicon + og en local**

```bash
npm run dev &
sleep 2
curl -s -o /dev/null -w "%{http_code}" http://localhost:4321/favicon.svg
# Expected: 200
kill %1
```

- [ ] **Step 6 : Commit**

```bash
git add public/ && git commit -m "feat(assets): logo variants + favicon + og image"
```

---

### Task 7 : Page mentions légales

**Files:**
- Create: `src/pages/mentions-legales.astro`

**Gating** : les prérequis en tête de ce plan doivent être collectés. Les placeholders `{{TO_CONFIRM: ...}}` doivent tous être remplacés avant que Task 15 (deploy) ne soit lancée.

- [ ] **Step 1 : Créer `src/pages/mentions-legales.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Mentions légales — Berger & Associés"
  description="Mentions légales du cabinet Berger & Associés, conseil en gestion de patrimoine à Paris : agréments, autorités de contrôle, procédure de réclamation."
  canonicalPath="/mentions-legales"
>
  <article class="page page-legal container">
    <header class="page-header">
      <p class="page-eyebrow">Informations légales</p>
      <h1>Mentions légales</h1>
    </header>

    <section>
      <h2>1. Éditeur du site</h2>
      <p>
        Le présent site est édité par <strong>Berger &amp; Associés</strong>, {{TO_CONFIRM: forme juridique}}
        au capital social de {{TO_CONFIRM: capital}} euros, immatriculée au RCS de {{TO_CONFIRM: ville RCS}}
        sous le numéro {{TO_CONFIRM: numéro RCS}} — SIRET {{TO_CONFIRM: numéro SIRET}}.
      </p>
      <p>
        <strong>Siège social :</strong> {{TO_CONFIRM: adresse complète}}, Paris, France.<br>
        <strong>Téléphone :</strong> {{TO_CONFIRM: numéro}} · <strong>Email :</strong>
        <a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a>
      </p>
      <p>
        <strong>Directeur de la publication :</strong> {{TO_CONFIRM: Fabien Berger / Sabine Tellier / Marine Gorin}}.
      </p>
    </section>

    <section>
      <h2>2. Hébergeur</h2>
      <p>
        Le site est hébergé par <strong>Cloudflare, Inc.</strong>, 101 Townsend Street,
        San Francisco, CA 94107, États-Unis. Téléphone : +1 (888) 993-5273 · Site :
        <a href="https://www.cloudflare.com" rel="noopener" target="_blank">cloudflare.com</a>.
      </p>
    </section>

    <section>
      <h2>3. Statuts professionnels et agréments</h2>
      <p>
        Berger &amp; Associés est immatriculé à l'ORIAS (Organisme pour le Registre unique des Intermédiaires
        en Assurance, Banque et Finance) sous le numéro <strong>13004419</strong>, au titre des activités
        suivantes (vérifiables sur <a href="https://www.orias.fr" rel="noopener" target="_blank">www.orias.fr</a>) :
      </p>
      <ul>
        <li>
          <strong>Conseiller en Investissements Financiers (CIF)</strong>, adhérent de la
          <strong>CNCGP</strong> (Chambre Nationale des Conseils en Gestion de Patrimoine),
          association agréée par l'AMF. Numéro d'adhérent : {{TO_CONFIRM: numéro CNCGP}}.
        </li>
        <li>
          <strong>Courtier en assurances</strong>, catégorie {{TO_CONFIRM: courtier / mandataire non exclusif / agent général}}.
        </li>
      </ul>
    </section>

    <section>
      <h2>4. Autorités de contrôle</h2>
      <p>
        L'activité de Conseiller en Investissements Financiers est placée sous le contrôle de l'<strong>Autorité
        des Marchés Financiers (AMF)</strong>, 17 place de la Bourse, 75082 Paris cedex 02 —
        <a href="https://www.amf-france.org" rel="noopener" target="_blank">amf-france.org</a>.
      </p>
      <p>
        L'activité de courtier en assurances est placée sous le contrôle de l'<strong>Autorité de Contrôle
        Prudentiel et de Résolution (ACPR)</strong>, 4 place de Budapest, CS 92459, 75436 Paris cedex 09 —
        <a href="https://acpr.banque-france.fr" rel="noopener" target="_blank">acpr.banque-france.fr</a>.
      </p>
    </section>

    <section>
      <h2>5. Responsabilité civile professionnelle</h2>
      <p>
        Conformément à l'article L. 541-3 du Code monétaire et financier, Berger &amp; Associés est couvert
        par une assurance de responsabilité civile professionnelle souscrite auprès de
        <strong>{{TO_CONFIRM: nom assureur}}</strong>, police n° <strong>{{TO_CONFIRM: numéro police}}</strong>,
        pour un plafond annuel de <strong>{{TO_CONFIRM: plafond en euros}} €</strong>.
      </p>
    </section>

    <section>
      <h2>6. Médiation</h2>
      <p>En cas de litige non résolu par les voies amiables internes, le client peut saisir :</p>
      <ul>
        <li>
          <strong>Médiateur de l'AMF</strong>, 17 place de la Bourse, 75082 Paris cedex 02 —
          <a href="https://www.amf-france.org/fr/le-mediateur-de-l-amf" rel="noopener" target="_blank">formulaire en ligne</a>.
          Pour les litiges portant sur l'activité de conseil en investissements.
        </li>
        <li>
          <strong>Médiateur de la consommation</strong> désigné par la CNCGP :
          {{TO_CONFIRM: nom + adresse + site du médiateur consommation}}.
        </li>
      </ul>
    </section>

    <section>
      <h2>7. Procédure de réclamation</h2>
      <p>
        Toute réclamation peut être adressée par courrier recommandé au siège social ou par email à
        <a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a>. Berger &amp; Associés
        s'engage à :
      </p>
      <ul>
        <li>accuser réception de la réclamation sous <strong>10 jours ouvrés</strong> ;</li>
        <li>apporter une réponse sur le fond dans un délai maximal de <strong>2 mois</strong> à compter de la réception ;</li>
        <li>informer le client de la possibilité de saisir le médiateur en cas de désaccord persistant.</li>
      </ul>
    </section>

    <section>
      <h2>8. Propriété intellectuelle</h2>
      <p>
        L'ensemble du contenu du site (textes, images, graphismes, logo, icônes, sons, logiciels) est
        la propriété exclusive de Berger &amp; Associés, à l'exception des marques, logos ou contenus
        appartenant à d'autres sociétés partenaires ou auteurs. Toute reproduction, distribution,
        modification ou utilisation de ces éléments sans autorisation préalable est strictement interdite.
      </p>
    </section>

    <section>
      <h2>9. Données personnelles et cookies</h2>
      <p>
        Le traitement des données personnelles collectées sur ce site est décrit dans notre
        <a href="/confidentialite">politique de confidentialité</a>. L'utilisation des cookies est
        détaillée dans notre <a href="/cookies">politique cookies</a>.
      </p>
    </section>

    <footer class="page-updated">
      <p>Dernière mise à jour : {{TO_CONFIRM: date de mise en ligne, format JJ mois AAAA}}.</p>
    </footer>
  </article>
</BaseLayout>

<style>
  .page-legal {
    padding-block: var(--s-6) var(--s-7);
  }
  .page-header {
    margin-bottom: var(--s-6);
    padding-bottom: var(--s-4);
    border-bottom: 1px solid var(--c-divider);
  }
  .page-eyebrow {
    font-size: var(--fs-xs);
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--c-gold);
    margin-bottom: var(--s-2);
  }
  .page-header h1 {
    font-family: var(--ff-serif);
    font-size: clamp(var(--fs-2xl), 5vw, var(--fs-3xl));
    font-weight: 600;
  }
  .page-legal section {
    margin-block: var(--s-5);
  }
  .page-legal h2 {
    font-family: var(--ff-serif);
    font-size: var(--fs-xl);
    font-weight: 500;
    margin-bottom: var(--s-2);
  }
  .page-legal p, .page-legal li {
    color: var(--c-fg-muted);
    font-size: var(--fs-base);
    line-height: var(--lh-loose);
    margin-block: var(--s-2);
  }
  .page-legal ul { padding-left: var(--s-3); }
  .page-updated {
    margin-top: var(--s-6);
    padding-top: var(--s-3);
    border-top: 1px solid var(--c-divider);
    font-size: var(--fs-sm);
    color: var(--c-fg-muted);
  }
</style>
```

- [ ] **Step 2 : Vérifier que la page build**

```bash
npm run build
```

Expected : build passe. La page `dist/mentions-legales/index.html` existe.

- [ ] **Step 3 : Commit**

```bash
git add src/pages/mentions-legales.astro && git commit -m "feat(pages): mentions légales (placeholders TO_CONFIRM)"
```

---

### Task 8 : Page politique de confidentialité (RGPD)

**Files:**
- Create: `src/pages/confidentialite.astro`

- [ ] **Step 1 : Créer `src/pages/confidentialite.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Politique de confidentialité — Berger & Associés"
  description="Protection des données personnelles, RGPD, droits des utilisateurs du site berger-associes.fr."
  canonicalPath="/confidentialite"
>
  <article class="page page-legal container">
    <header class="page-header">
      <p class="page-eyebrow">Protection des données</p>
      <h1>Politique de confidentialité</h1>
    </header>

    <section>
      <p>
        Berger &amp; Associés, en sa qualité de responsable de traitement, attache une importance
        particulière à la protection des données personnelles. La présente politique explique
        comment nous collectons, utilisons, partageons et protégeons vos données, conformément
        au Règlement général sur la protection des données (RGPD — Règlement UE 2016/679) et à
        la loi Informatique et Libertés modifiée du 6 janvier 1978.
      </p>
    </section>

    <section>
      <h2>1. Responsable de traitement</h2>
      <p>
        <strong>Berger &amp; Associés</strong><br>
        {{TO_CONFIRM: adresse complète}}<br>
        Contact : <a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a>
      </p>
    </section>

    <section>
      <h2>2. Délégué à la protection des données (DPO)</h2>
      <p>
        Pour toute question relative au traitement de vos données, vous pouvez contacter notre
        Délégué à la protection des données :
      </p>
      <p>
        <strong>{{TO_CONFIRM: nom du DPO — par défaut Fabien Berger}}</strong><br>
        Email : <a href="mailto:dpo@berger-associes.fr">dpo@berger-associes.fr</a>
      </p>
    </section>

    <section>
      <h2>3. Données collectées et finalités</h2>
      <p>Nous collectons uniquement les données strictement nécessaires aux finalités suivantes :</p>

      <h3>a. Formulaire de contact</h3>
      <ul>
        <li><strong>Données :</strong> nom, prénom, adresse email, message.</li>
        <li><strong>Finalité :</strong> répondre à votre demande d'information ou de rendez-vous.</li>
        <li><strong>Base légale :</strong> consentement (RGPD art. 6-1-a) et intérêt légitime pour le suivi commercial pré-contractuel.</li>
        <li><strong>Durée de conservation :</strong> 3 ans à compter du dernier contact si la relation ne se concrétise pas ; durée du mandat + 5 ans si une relation s'établit.</li>
      </ul>

      <h3>b. Cookies techniques et de mesure d'audience</h3>
      <ul>
        <li><strong>Données :</strong> informations anonymisées de navigation (pages vues, durée de session).</li>
        <li><strong>Finalité :</strong> assurer le fonctionnement du site et mesurer son audience.</li>
        <li><strong>Base légale :</strong> intérêt légitime pour les cookies strictement nécessaires ; consentement pour les cookies de mesure d'audience.</li>
        <li><strong>Durée :</strong> 13 mois maximum (conforme à la recommandation CNIL).</li>
      </ul>
    </section>

    <section>
      <h2>4. Destinataires des données</h2>
      <p>Vos données sont traitées en interne par les associés et collaborateurs habilités de Berger &amp; Associés. Elles peuvent être transmises à :</p>
      <ul>
        <li>nos sous-traitants techniques (hébergeur Cloudflare, fournisseur de services email) dans la stricte limite de leurs missions et dans le cadre de contrats conformes au RGPD ;</li>
        <li>les autorités compétentes (AMF, ACPR, administration fiscale) si la loi nous y oblige.</li>
      </ul>
      <p>
        <strong>Aucune donnée ne fait l'objet de transfert commercial à des tiers</strong> à des fins
        de prospection ou de profilage.
      </p>
    </section>

    <section>
      <h2>5. Transferts hors Union européenne</h2>
      <p>
        Certains de nos sous-traitants techniques (notamment Cloudflare, notre hébergeur) peuvent être
        amenés à traiter des données dans des pays hors Union européenne. Ces transferts sont
        encadrés par les <strong>Clauses Contractuelles Types</strong> adoptées par la Commission
        européenne, garantissant un niveau de protection équivalent au RGPD.
      </p>
    </section>

    <section>
      <h2>6. Vos droits</h2>
      <p>Conformément au RGPD et à la loi Informatique et Libertés, vous disposez des droits suivants :</p>
      <ul>
        <li><strong>Droit d'accès</strong> à vos données personnelles ;</li>
        <li><strong>Droit de rectification</strong> des données inexactes ou incomplètes ;</li>
        <li><strong>Droit à l'effacement</strong> de vos données (dans les limites de nos obligations légales de conservation) ;</li>
        <li><strong>Droit à la limitation</strong> du traitement ;</li>
        <li><strong>Droit d'opposition</strong> au traitement pour motifs légitimes ;</li>
        <li><strong>Droit à la portabilité</strong> de vos données dans un format structuré et couramment utilisé ;</li>
        <li><strong>Droit de retirer votre consentement</strong> à tout moment, sans que cela n'affecte la licéité du traitement antérieur ;</li>
        <li><strong>Droit de définir des directives</strong> relatives au sort de vos données après votre décès.</li>
      </ul>
      <p>
        Pour exercer ces droits, contactez notre DPO à
        <a href="mailto:dpo@berger-associes.fr">dpo@berger-associes.fr</a>.
        Nous répondrons dans un délai maximal d'un mois. Une pièce d'identité pourra vous être demandée
        en cas de doute raisonnable sur votre identité.
      </p>
    </section>

    <section>
      <h2>7. Sécurité</h2>
      <p>
        Nous mettons en œuvre les mesures techniques et organisationnelles appropriées pour protéger
        vos données contre toute perte, altération, divulgation ou accès non autorisé : chiffrement
        des communications (HTTPS/TLS), accès restreint par authentification forte, journalisation
        des accès, sauvegardes régulières, formation du personnel.
      </p>
    </section>

    <section>
      <h2>8. Réclamation auprès de la CNIL</h2>
      <p>
        Si, après avoir contacté notre DPO, vous estimez que vos droits ne sont pas respectés, vous
        pouvez introduire une réclamation auprès de la
        <strong>Commission nationale de l'informatique et des libertés (CNIL)</strong> — 3 place de
        Fontenoy, TSA 80715, 75334 Paris cedex 07 —
        <a href="https://www.cnil.fr" rel="noopener" target="_blank">www.cnil.fr</a>.
      </p>
    </section>

    <section>
      <h2>9. Modifications</h2>
      <p>
        La présente politique peut être modifiée à tout moment pour s'adapter aux évolutions légales
        ou à notre activité. La date de dernière mise à jour est indiquée en bas de page. En cas de
        modification substantielle, les personnes concernées seront informées par un moyen approprié.
      </p>
    </section>

    <footer class="page-updated">
      <p>Dernière mise à jour : {{TO_CONFIRM: date de mise en ligne}}.</p>
    </footer>
  </article>
</BaseLayout>

<style>
  /* Hérite des styles de Task 7 — les classes .page-legal, .page-header, etc. sont partagées. */
  /* Duplication Phase 1 : on répète les styles pour isolation. Phase 2 on factorise. */

  .page-legal { padding-block: var(--s-6) var(--s-7); }
  .page-header { margin-bottom: var(--s-6); padding-bottom: var(--s-4); border-bottom: 1px solid var(--c-divider); }
  .page-eyebrow { font-size: var(--fs-xs); letter-spacing: 0.22em; text-transform: uppercase; color: var(--c-gold); margin-bottom: var(--s-2); }
  .page-header h1 { font-family: var(--ff-serif); font-size: clamp(var(--fs-2xl), 5vw, var(--fs-3xl)); font-weight: 600; }
  .page-legal section { margin-block: var(--s-5); }
  .page-legal h2 { font-family: var(--ff-serif); font-size: var(--fs-xl); font-weight: 500; margin-bottom: var(--s-2); }
  .page-legal h3 { font-family: var(--ff-sans); font-size: var(--fs-base); font-weight: 600; margin-top: var(--s-3); margin-bottom: var(--s-1); color: var(--c-fg); }
  .page-legal p, .page-legal li { color: var(--c-fg-muted); font-size: var(--fs-base); line-height: var(--lh-loose); margin-block: var(--s-2); }
  .page-legal ul { padding-left: var(--s-3); }
  .page-updated { margin-top: var(--s-6); padding-top: var(--s-3); border-top: 1px solid var(--c-divider); font-size: var(--fs-sm); color: var(--c-fg-muted); }
</style>
```

- [ ] **Step 2 : Build check**

```bash
npm run build
```

Expected : passe.

- [ ] **Step 3 : Commit**

```bash
git add src/pages/confidentialite.astro && git commit -m "feat(pages): politique de confidentialité RGPD"
```

---

### Task 9 : Page politique cookies (avec préférences granulaire)

**Files:**
- Create: `src/pages/cookies.astro`

- [ ] **Step 1 : Créer `src/pages/cookies.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Politique cookies — Berger & Associés"
  description="Gestion des cookies, finalités et préférences sur berger-associes.fr."
  canonicalPath="/cookies"
>
  <article class="page page-legal container">
    <header class="page-header">
      <p class="page-eyebrow">Cookies et traceurs</p>
      <h1>Politique cookies</h1>
    </header>

    <section>
      <p>
        Cette page décrit les cookies et traceurs utilisés sur le site berger-associes.fr, leurs
        finalités et vos moyens de les contrôler.
      </p>
    </section>

    <section>
      <h2>1. Qu'est-ce qu'un cookie ?</h2>
      <p>
        Un cookie est un petit fichier texte déposé sur votre terminal (ordinateur, smartphone, tablette)
        lors de la visite d'un site web. Il permet de reconnaître votre navigateur entre deux visites
        et de conserver certaines informations utiles au fonctionnement du site ou à la mesure d'audience.
      </p>
    </section>

    <section>
      <h2>2. Cookies utilisés sur ce site</h2>

      <h3>a. Cookies strictement nécessaires</h3>
      <p>Ces cookies sont indispensables au fonctionnement du site et ne peuvent être désactivés.</p>
      <ul>
        <li><strong>cookie-consent</strong> : enregistre vos préférences de consentement aux cookies. Durée : 6 mois.</li>
      </ul>

      <h3>b. Cookies de mesure d'audience</h3>
      <p>
        Ces cookies nous aident à comprendre comment les visiteurs utilisent le site, de manière
        anonymisée. Ils ne sont déposés <strong>qu'avec votre consentement explicite</strong>.
      </p>
      <ul>
        <li>
          <strong>Cloudflare Web Analytics</strong> (ou équivalent compatible CNIL) : mesure d'audience
          anonymisée sans cookie tiers. Durée : session. Finalité : comptage des visites, pages consultées.
        </li>
      </ul>
      <p>
        <strong>Aucun cookie publicitaire, de profilage marketing ou de réseaux sociaux n'est déposé
        sur ce site.</strong>
      </p>
    </section>

    <section>
      <h2>3. Gérer vos préférences</h2>
      <p>
        Vous pouvez à tout moment modifier vos préférences en cliquant sur le bouton ci-dessous.
        Votre choix est conservé pendant 6 mois. Passé ce délai, votre consentement vous sera
        redemandé à votre prochaine visite.
      </p>
      <p>
        <button type="button" id="open-cookie-preferences" class="btn btn--primary">
          Gérer mes préférences cookies
        </button>
      </p>
      <p class="note">
        Vous pouvez également paramétrer votre navigateur pour refuser tous les cookies : les
        liens d'aide officiels sont disponibles sur le site de la CNIL —
        <a href="https://www.cnil.fr/fr/cookies-et-autres-traceurs/comment-se-proteger/maitriser-votre-navigateur" rel="noopener" target="_blank">cnil.fr</a>.
      </p>
    </section>

    <section>
      <h2>4. Base légale</h2>
      <p>
        Le dépôt des cookies est régi par l'article 82 de la loi Informatique et Libertés et par la
        directive ePrivacy. Les cookies de mesure d'audience sont déposés sur la base de votre
        consentement explicite, que vous pouvez retirer à tout moment.
      </p>
    </section>

    <footer class="page-updated">
      <p>Dernière mise à jour : {{TO_CONFIRM: date de mise en ligne}}.</p>
    </footer>
  </article>
</BaseLayout>

<script>
  const btn = document.getElementById('open-cookie-preferences');
  if (btn) {
    btn.addEventListener('click', () => {
      document.dispatchEvent(new CustomEvent('cookie-preferences:open'));
    });
  }
</script>

<style>
  .page-legal { padding-block: var(--s-6) var(--s-7); }
  .page-header { margin-bottom: var(--s-6); padding-bottom: var(--s-4); border-bottom: 1px solid var(--c-divider); }
  .page-eyebrow { font-size: var(--fs-xs); letter-spacing: 0.22em; text-transform: uppercase; color: var(--c-gold); margin-bottom: var(--s-2); }
  .page-header h1 { font-family: var(--ff-serif); font-size: clamp(var(--fs-2xl), 5vw, var(--fs-3xl)); font-weight: 600; }
  .page-legal section { margin-block: var(--s-5); }
  .page-legal h2 { font-family: var(--ff-serif); font-size: var(--fs-xl); font-weight: 500; margin-bottom: var(--s-2); }
  .page-legal h3 { font-family: var(--ff-sans); font-size: var(--fs-base); font-weight: 600; margin-top: var(--s-3); margin-bottom: var(--s-1); color: var(--c-fg); }
  .page-legal p, .page-legal li { color: var(--c-fg-muted); font-size: var(--fs-base); line-height: var(--lh-loose); margin-block: var(--s-2); }
  .page-legal ul { padding-left: var(--s-3); }
  .btn {
    display: inline-block;
    padding: var(--s-1) var(--s-3);
    font-size: var(--fs-sm);
    font-weight: 500;
    letter-spacing: 0.04em;
    border: 1px solid var(--c-navy);
    border-radius: var(--radius-sm);
    transition: background var(--dur-fast) var(--ease-standard), color var(--dur-fast) var(--ease-standard);
  }
  .btn--primary { background: var(--c-navy); color: var(--c-ivoire); }
  .btn--primary:hover { background: var(--c-ivoire); color: var(--c-navy); }
  .note { font-size: var(--fs-sm); color: var(--c-fg-muted); }
  .page-updated { margin-top: var(--s-6); padding-top: var(--s-3); border-top: 1px solid var(--c-divider); font-size: var(--fs-sm); color: var(--c-fg-muted); }
</style>
```

- [ ] **Step 2 : Build check**

```bash
npm run build
```

- [ ] **Step 3 : Commit**

```bash
git add src/pages/cookies.astro && git commit -m "feat(pages): politique cookies + bouton préférences"
```

---

### Task 10 : CookieBanner component (vanilla JS, conforme CNIL)

**Files:**
- Create: `src/components/CookieBanner.astro`
- Test: `tests/cookie-banner.spec.ts`

- [ ] **Step 1 : Écrire le test Playwright `tests/cookie-banner.spec.ts`**

```typescript
import { test, expect } from '@playwright/test';

test.describe('Cookie banner', () => {
  test.beforeEach(async ({ page, context }) => {
    await context.clearCookies();
    await page.goto('/');
  });

  test('affiche le bandeau au premier visiteur', async ({ page }) => {
    await expect(page.locator('[data-cookie-banner]')).toBeVisible();
    await expect(page.locator('[data-cookie-accept-all]')).toBeVisible();
    await expect(page.locator('[data-cookie-reject-all]')).toBeVisible();
    await expect(page.locator('[data-cookie-customize]')).toBeVisible();
  });

  test('cache le bandeau après "Tout accepter"', async ({ page }) => {
    await page.click('[data-cookie-accept-all]');
    await expect(page.locator('[data-cookie-banner]')).toBeHidden();
    const stored = await page.evaluate(() => localStorage.getItem('cookie-consent'));
    expect(stored).toContain('"analytics":true');
  });

  test('cache le bandeau après "Tout refuser" (sans analytics)', async ({ page }) => {
    await page.click('[data-cookie-reject-all]');
    await expect(page.locator('[data-cookie-banner]')).toBeHidden();
    const stored = await page.evaluate(() => localStorage.getItem('cookie-consent'));
    expect(stored).toContain('"analytics":false');
  });

  test('bouton "Gérer préférences" sur /cookies rouvre la modale', async ({ page }) => {
    await page.click('[data-cookie-reject-all]');
    await page.goto('/cookies');
    await page.click('#open-cookie-preferences');
    await expect(page.locator('[data-cookie-banner]')).toBeVisible();
  });
});
```

- [ ] **Step 2 : Lancer le test et vérifier qu'il échoue (composant pas encore créé)**

```bash
npx playwright test tests/cookie-banner.spec.ts --reporter=line
```

Expected : ÉCHEC "locator('[data-cookie-banner]') not found" (car Component CookieBanner n'existe pas encore).

- [ ] **Step 3 : Créer le `playwright.config.ts` à la racine**

```typescript
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  timeout: 30_000,
  use: {
    baseURL: 'http://localhost:4321',
    trace: 'on-first-retry',
  },
  webServer: {
    command: 'npm run dev',
    url: 'http://localhost:4321',
    timeout: 60_000,
    reuseExistingServer: !process.env.CI,
  },
  projects: [
    { name: 'chromium', use: devices['Desktop Chrome'] },
  ],
});
```

- [ ] **Step 4 : Créer `src/components/CookieBanner.astro`**

```astro
---
// Cookie banner conforme CNIL : opt-in granulaire, refus aussi simple qu'acceptation,
// aucun cookie analytics deposé avant consentement explicite.
---

<div
  class="cookie-banner"
  data-cookie-banner
  role="dialog"
  aria-label="Préférences cookies"
  aria-modal="true"
  hidden
>
  <div class="cookie-banner__inner">
    <h2 class="cookie-banner__title">Cookies</h2>
    <p class="cookie-banner__text">
      Nous utilisons des cookies pour faire fonctionner le site et, avec votre consentement, mesurer
      son audience de manière anonymisée. Vous pouvez accepter, refuser ou personnaliser.
      <a href="/cookies">En savoir plus</a>.
    </p>

    <div class="cookie-banner__prefs" data-cookie-prefs hidden>
      <label class="cookie-banner__pref">
        <input type="checkbox" checked disabled />
        <span><strong>Cookies nécessaires</strong> — toujours actifs (fonctionnement du site).</span>
      </label>
      <label class="cookie-banner__pref">
        <input type="checkbox" data-cookie-pref-analytics />
        <span><strong>Mesure d'audience</strong> — statistiques anonymisées pour améliorer le site.</span>
      </label>
    </div>

    <div class="cookie-banner__actions">
      <button type="button" class="btn btn--ghost" data-cookie-reject-all>Tout refuser</button>
      <button type="button" class="btn btn--ghost" data-cookie-customize>Personnaliser</button>
      <button type="button" class="btn btn--primary" data-cookie-accept-all>Tout accepter</button>
      <button type="button" class="btn btn--primary" data-cookie-save hidden>Enregistrer</button>
    </div>
  </div>
</div>

<script>
  type ConsentState = { analytics: boolean; timestamp: number };
  const STORAGE_KEY = 'cookie-consent';
  const SIX_MONTHS_MS = 1000 * 60 * 60 * 24 * 30 * 6;

  const banner = document.querySelector<HTMLElement>('[data-cookie-banner]');
  const prefsBlock = document.querySelector<HTMLElement>('[data-cookie-prefs]');
  const analyticsInput = document.querySelector<HTMLInputElement>('[data-cookie-pref-analytics]');
  const btnAcceptAll = document.querySelector<HTMLButtonElement>('[data-cookie-accept-all]');
  const btnRejectAll = document.querySelector<HTMLButtonElement>('[data-cookie-reject-all]');
  const btnCustomize = document.querySelector<HTMLButtonElement>('[data-cookie-customize]');
  const btnSave = document.querySelector<HTMLButtonElement>('[data-cookie-save]');

  function readConsent(): ConsentState | null {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      const parsed = JSON.parse(raw) as ConsentState;
      if (Date.now() - parsed.timestamp > SIX_MONTHS_MS) {
        localStorage.removeItem(STORAGE_KEY);
        return null;
      }
      return parsed;
    } catch {
      return null;
    }
  }

  function writeConsent(analytics: boolean) {
    const state: ConsentState = { analytics, timestamp: Date.now() };
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
    applyConsent(state);
  }

  function applyConsent(state: ConsentState) {
    // Hook extension pour activer Cloudflare Web Analytics ou equivalent
    if (state.analytics) {
      // Exemple : loader Cloudflare Analytics (Phase 2 pour vrai intégration)
      // document.head.insertAdjacentHTML('beforeend', '<script defer src="https://static.cloudflareinsights.com/beacon.min.js" ...></script>');
    }
  }

  function showBanner() {
    if (!banner) return;
    banner.hidden = false;
  }

  function hideBanner() {
    if (!banner) return;
    banner.hidden = true;
  }

  function showPrefs() {
    if (!prefsBlock || !btnSave || !btnCustomize) return;
    prefsBlock.hidden = false;
    btnSave.hidden = false;
    btnCustomize.hidden = true;
  }

  btnAcceptAll?.addEventListener('click', () => { writeConsent(true); hideBanner(); });
  btnRejectAll?.addEventListener('click', () => { writeConsent(false); hideBanner(); });
  btnCustomize?.addEventListener('click', showPrefs);
  btnSave?.addEventListener('click', () => {
    writeConsent(!!analyticsInput?.checked);
    hideBanner();
  });

  document.addEventListener('cookie-preferences:open', () => {
    const state = readConsent();
    if (state && analyticsInput) analyticsInput.checked = state.analytics;
    showPrefs();
    showBanner();
  });

  const existing = readConsent();
  if (existing) {
    applyConsent(existing);
  } else {
    showBanner();
  }
</script>

<style>
  .cookie-banner {
    position: fixed;
    inset: auto 0 0 0;
    background: var(--c-navy);
    color: var(--c-ivoire);
    z-index: 50;
    box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.15);
  }

  .cookie-banner__inner {
    max-width: var(--max-wide);
    margin-inline: auto;
    padding: var(--s-4) var(--page-gutter);
    display: grid;
    gap: var(--s-2);
  }

  .cookie-banner__title {
    font-size: var(--fs-sm);
    letter-spacing: 0.2em;
    text-transform: uppercase;
    font-weight: 500;
    color: var(--c-gold);
  }

  .cookie-banner__text {
    font-size: var(--fs-sm);
    line-height: var(--lh-normal);
    max-width: 680px;
  }

  .cookie-banner__text a { color: var(--c-gold); }

  .cookie-banner__prefs {
    display: grid;
    gap: var(--s-1);
    padding: var(--s-2) 0;
    font-size: var(--fs-sm);
  }

  .cookie-banner__pref {
    display: flex;
    gap: var(--s-2);
    align-items: flex-start;
    cursor: pointer;
  }

  .cookie-banner__actions {
    display: flex;
    flex-wrap: wrap;
    gap: var(--s-2);
    justify-content: flex-end;
    margin-top: var(--s-2);
  }

  .cookie-banner .btn {
    padding: var(--s-1) var(--s-3);
    border: 1px solid var(--c-ivoire);
    border-radius: var(--radius-sm);
    font-size: var(--fs-sm);
    font-weight: 500;
  }

  .cookie-banner .btn--ghost { background: transparent; color: var(--c-ivoire); }
  .cookie-banner .btn--ghost:hover { background: rgba(250, 246, 236, 0.1); }
  .cookie-banner .btn--primary { background: var(--c-ivoire); color: var(--c-navy); }
  .cookie-banner .btn--primary:hover { background: var(--c-gold); color: var(--c-navy); border-color: var(--c-gold); }

  @media (max-width: 540px) {
    .cookie-banner__actions { justify-content: stretch; }
    .cookie-banner__actions .btn { flex: 1 1 auto; }
  }
</style>
```

- [ ] **Step 5 : Lancer le test et vérifier qu'il passe**

```bash
npx playwright test tests/cookie-banner.spec.ts --reporter=line
```

Expected : 4 tests PASS.

- [ ] **Step 6 : Commit**

```bash
git add src/components/CookieBanner.astro tests/cookie-banner.spec.ts playwright.config.ts && git commit -m "feat(cookies): CNIL-compliant cookie banner with 4 e2e tests"
```

---

### Task 11 : Landing page (`/`)

**Files:**
- Create: `src/pages/index.astro`

- [ ] **Step 1 : Créer `src/pages/index.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';

const associates = [
  { name: 'Fabien Berger', role: 'Associé fondateur', mailto: 'fabien.berger@berger-associes.fr' },
  { name: 'Sabine Tellier', role: 'Associée', mailto: 'sabine.tellier@berger-associes.fr' },
  { name: 'Marine Gorin', role: 'Associée', mailto: 'marine.gorin@berger-associes.fr' },
];
---

<BaseLayout
  title="Berger & Associés — Conseil en gestion de patrimoine, Paris"
  description="Cabinet indépendant de conseil en gestion de patrimoine, Paris. Trois associés, une relation long terme. Depuis 2013."
>
  <section class="hero">
    <div class="container">
      <p class="hero__eyebrow">Cabinet de conseil en gestion de patrimoine · Paris · Depuis 2013</p>

      <h1 class="hero__title editorial">
        Trois associés à Paris,<br>un cabinet en partage.
      </h1>

      <p class="hero__lead">
        Fabien Berger, Sabine Tellier, Marine Gorin. Nos clients nous arrivent par recommandation
        depuis 2013. Ils nous rencontrent en personne, et ils restent.
      </p>

      <div class="hero__actions">
        <a href="mailto:contact@berger-associes.fr" class="btn btn--primary">Nous contacter</a>
      </div>
    </div>
  </section>

  <section class="associates">
    <div class="container">
      <h2 class="section-h">Les associés</h2>
      <ul class="associates__grid">
        {associates.map(({ name, role, mailto }) => (
          <li class="associate">
            <div class="associate__portrait" aria-hidden="true"></div>
            <h3 class="associate__name editorial">{name}</h3>
            <p class="associate__role">{role}</p>
            <p class="associate__email">
              <a href={`mailto:${mailto}`}>{mailto}</a>
            </p>
          </li>
        ))}
      </ul>
      <p class="associates__note">
        La version complète du site, avec les biographies, méthodes et journal des associés,
        sera mise en ligne prochainement. Pour un rendez-vous ou une demande d'information,
        contactez-nous par email ou directement un associé.
      </p>
    </div>
  </section>

  <section class="contact">
    <div class="container">
      <h2 class="section-h">Nous rencontrer</h2>
      <p>
        Email du cabinet : <a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a><br>
        Adresse : {{TO_CONFIRM: adresse complète}}, Paris.
      </p>
      <p class="note">
        Premier rendez-vous sans engagement, à notre cabinet ou en visioconférence. Nous
        établissons ensemble le périmètre de votre demande avant tout engagement commercial.
      </p>
    </div>
  </section>
</BaseLayout>

<style>
  .hero {
    padding-block: var(--s-7) var(--s-6);
  }

  .hero__eyebrow {
    font-size: var(--fs-xs);
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--c-gold);
    margin-bottom: var(--s-3);
  }

  .hero__title {
    font-size: clamp(var(--fs-3xl), 7vw, var(--fs-5xl));
    line-height: var(--lh-tight);
    letter-spacing: -0.035em;
    color: var(--c-fg);
    margin-bottom: var(--s-3);
    font-weight: 600;
  }

  .hero__lead {
    font-size: clamp(var(--fs-lg), 2.2vw, var(--fs-xl));
    line-height: var(--lh-normal);
    color: var(--c-fg-muted);
    max-width: 620px;
    margin-bottom: var(--s-5);
  }

  .btn {
    display: inline-block;
    padding: var(--s-1) var(--s-3);
    font-size: var(--fs-sm);
    font-weight: 500;
    letter-spacing: 0.04em;
    border-radius: var(--radius-sm);
    transition: background var(--dur-fast), color var(--dur-fast);
    text-decoration: none;
  }
  .btn--primary { background: var(--c-navy); color: var(--c-ivoire); border: 1px solid var(--c-navy); }
  .btn--primary:hover { background: var(--c-ivoire); color: var(--c-navy); opacity: 1; }

  .section-h {
    font-family: var(--ff-serif);
    font-size: var(--fs-2xl);
    font-weight: 500;
    margin-bottom: var(--s-4);
    padding-bottom: var(--s-2);
    border-bottom: 1px solid var(--c-divider);
  }

  .associates {
    padding-block: var(--s-6);
  }

  .associates__grid {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--s-4);
    margin-bottom: var(--s-4);
  }

  .associate {
    text-align: center;
  }

  .associate__portrait {
    width: 140px;
    aspect-ratio: 1 / 1;
    border-radius: 50%;
    background: linear-gradient(135deg, var(--c-sand) 0%, var(--c-slate) 100%);
    margin: 0 auto var(--s-3);
  }

  .associate__name {
    font-size: var(--fs-xl);
    font-weight: 500;
    margin-bottom: var(--s-1);
  }

  .associate__role {
    font-size: var(--fs-xs);
    text-transform: uppercase;
    letter-spacing: 0.16em;
    color: var(--c-gold);
    margin-bottom: var(--s-2);
  }

  .associate__email {
    font-size: var(--fs-sm);
  }

  .associate__email a {
    color: var(--c-fg);
    opacity: 0.75;
    text-decoration: none;
  }
  .associate__email a:hover { opacity: 1; }

  .associates__note {
    font-size: var(--fs-sm);
    color: var(--c-fg-muted);
    text-align: center;
    font-style: italic;
    max-width: 600px;
    margin: var(--s-4) auto 0;
  }

  .contact {
    padding-block: var(--s-5) var(--s-7);
    background: var(--c-sand);
    margin-top: var(--s-5);
  }

  .contact p { color: var(--c-fg); font-size: var(--fs-base); line-height: var(--lh-loose); }
  .contact .note { font-size: var(--fs-sm); color: var(--c-fg-muted); margin-top: var(--s-2); }

  @media (max-width: 720px) {
    .associates__grid { grid-template-columns: 1fr; gap: var(--s-5); }
  }
</style>
```

- [ ] **Step 2 : Build + dev preview**

```bash
npm run build
npm run dev &
sleep 3
```

Ouvrir http://localhost:4321 dans un navigateur. Vérifier : hero visible, 3 portraits ronds, section contact, bandeau cookies visible sur fond navy.

```bash
kill %1
```

- [ ] **Step 3 : Commit**

```bash
git add src/pages/index.astro && git commit -m "feat(pages): landing page with hero + associés + contact"
```

---

### Task 12 : Page 404 + robots.txt + sitemap.xml

**Files:**
- Create: `src/pages/404.astro`, `public/robots.txt`
- Modify: `astro.config.mjs`

- [ ] **Step 1 : Installer `@astrojs/sitemap`**

```bash
npm install --save-dev @astrojs/sitemap
```

- [ ] **Step 2 : Mettre à jour `astro.config.mjs`**

```javascript
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: 'https://www.berger-associes.fr',
  integrations: [sitemap()],
});
```

- [ ] **Step 3 : Créer `src/pages/404.astro`**

```astro
---
import BaseLayout from '../layouts/BaseLayout.astro';
---

<BaseLayout
  title="Page introuvable — Berger & Associés"
  description="La page demandée n'existe pas ou a été déplacée."
  noindex
>
  <section class="notfound container">
    <p class="notfound__eyebrow">Erreur 404</p>
    <h1 class="notfound__title editorial">Page introuvable.</h1>
    <p class="notfound__lead">
      La page que vous cherchez n'existe pas ou a été déplacée. Vous pouvez revenir à
      <a href="/">l'accueil</a> ou nous contacter à
      <a href="mailto:contact@berger-associes.fr">contact@berger-associes.fr</a>.
    </p>
  </section>
</BaseLayout>

<style>
  .notfound { padding-block: var(--s-7); text-align: center; }
  .notfound__eyebrow { font-size: var(--fs-xs); letter-spacing: 0.22em; text-transform: uppercase; color: var(--c-gold); margin-bottom: var(--s-2); }
  .notfound__title { font-size: clamp(var(--fs-3xl), 7vw, var(--fs-4xl)); font-weight: 600; margin-bottom: var(--s-3); }
  .notfound__lead { font-size: var(--fs-lg); color: var(--c-fg-muted); max-width: 540px; margin: 0 auto; line-height: var(--lh-loose); }
</style>
```

- [ ] **Step 4 : Créer `public/robots.txt`**

```
User-agent: *
Allow: /

Sitemap: https://www.berger-associes.fr/sitemap-index.xml
```

- [ ] **Step 5 : Build et vérifier sitemap généré**

```bash
npm run build
ls dist/sitemap-*.xml
```

Expected : `dist/sitemap-index.xml` et `dist/sitemap-0.xml` existent et contiennent les URLs des 5 pages.

- [ ] **Step 6 : Commit**

```bash
git add -A && git commit -m "feat(seo): 404 page + robots.txt + sitemap integration"
```

---

### Task 13 : Accessibility audit (axe-core)

**Files:**
- Create: `tests/a11y.spec.ts`

- [ ] **Step 1 : Écrire le test d'accessibilité**

```typescript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

const routes = [
  { path: '/', label: 'Accueil' },
  { path: '/mentions-legales', label: 'Mentions légales' },
  { path: '/confidentialite', label: 'Confidentialité' },
  { path: '/cookies', label: 'Cookies' },
  { path: '/page-qui-n-existe-pas', label: '404' },
];

for (const { path, label } of routes) {
  test(`a11y: ${label} (${path}) — zéro violation WCAG 2.1 AA`, async ({ page }) => {
    await page.goto(path);
    const results = await new AxeBuilder({ page })
      .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])
      .analyze();

    if (results.violations.length > 0) {
      console.log(JSON.stringify(results.violations, null, 2));
    }
    expect(results.violations).toHaveLength(0);
  });
}
```

- [ ] **Step 2 : Lancer les tests a11y**

```bash
npx playwright test tests/a11y.spec.ts --reporter=line
```

Expected : 5 tests PASS. Si violations, corriger les pages / composants en cause (contrastes, labels ARIA manquants, ordre tabulaire cassé).

- [ ] **Step 3 : Commit**

```bash
git add tests/a11y.spec.ts && git commit -m "test(a11y): WCAG 2.1 AA audit axe-core sur toutes les pages"
```

---

### Task 14 : QA responsive + Lighthouse

**Files:** (aucun nouveau fichier — QA manuelle + capture)

- [ ] **Step 1 : Lancer le dev server en mode production build**

```bash
npm run build && npm run preview &
sleep 3
```

- [ ] **Step 2 : Lancer un audit Lighthouse via CLI**

```bash
npx lighthouse http://localhost:4321 \
  --output=json \
  --output-path=./lighthouse-home.json \
  --only-categories=performance,accessibility,best-practices,seo \
  --chrome-flags="--headless"
```

Expected scores (Phase 1 target) :

- Performance : ≥ 95
- Accessibility : ≥ 95
- Best Practices : ≥ 95
- SEO : ≥ 95

Si un score est sous 95, identifier dans le rapport JSON (section `categories.<cat>.auditRefs`) les audits qui échouent. Les plus fréquents : images sans dimensions, contrastes, meta description manquante, liens sans nom accessible.

- [ ] **Step 3 : Vérifier manuellement le responsive**

Ouvrir http://localhost:4321 dans le navigateur. Utiliser les DevTools (cmd+option+i, puis toggle responsive). Tester 3 tailles :

- 375×667 (iPhone SE) — tous les textes lisibles, bandeau cookies empilé
- 768×1024 (iPad) — la nav passe à 2 lignes
- 1440×900 (laptop) — layout complet

Vérifier sur chaque page (/, /mentions-legales, /confidentialite, /cookies) :
- Pas de scroll horizontal
- Tous les textes lisibles (taille ≥ 14px)
- Boutons cliquables (min 44×44 px)
- Navigation accessible (tab, entrée)

- [ ] **Step 4 : Kill le server**

```bash
kill %1
```

- [ ] **Step 5 : Commit le rapport Lighthouse si acceptable**

```bash
# Ne pas commiter le JSON volumineux — supprimer
rm lighthouse-home.json
git add -A && git status && git commit --allow-empty -m "qa: lighthouse + responsive audit passed (Phase 1)"
```

---

### Task 15 : Remplacer les placeholders TO_CONFIRM avant déploiement

**Files:**
- Modify: `src/pages/mentions-legales.astro`, `src/pages/confidentialite.astro`, `src/pages/cookies.astro`, `src/pages/index.astro`

**Prérequis** : les informations listées en tête de ce plan (prérequis 1-12) doivent avoir été collectées par Fabien.

- [ ] **Step 1 : Rechercher tous les TO_CONFIRM restants**

```bash
cd /Users/fabienberger/berger-site
grep -rn "TO_CONFIRM" src/pages/
```

Expected : liste de ~20-30 placeholders à remplacer.

- [ ] **Step 2 : Remplacer un par un par les valeurs collectées**

Pour chaque ligne retournée, éditer le fichier et remplacer `{{TO_CONFIRM: description}}` par la vraie valeur.

Exemple : `{{TO_CONFIRM: Fabien Berger / Sabine Tellier / Marine Gorin}}` → `Fabien Berger` (ou autre selon décision).

- [ ] **Step 3 : Re-vérifier qu'il n'en reste aucun**

```bash
grep -rn "TO_CONFIRM" src/ public/
```

Expected : **aucune ligne retournée**. Si des placeholders restent, ne pas déployer tant qu'ils ne sont pas résolus.

- [ ] **Step 4 : Build final**

```bash
npm run build
```

Expected : passe sans erreur.

- [ ] **Step 5 : Commit**

```bash
git add src/ && git commit -m "content: replace all TO_CONFIRM placeholders with validated legal info"
```

---

### Task 16 : Relecture juridique externe

**Out-of-code task** — opérationnel.

- [ ] **Step 1 : Envoyer les 3 pages légales en PDF ou en URL preview Cloudflare à Vie Legia Conseil (Javi)**

Pour générer un PDF de chaque page :

```bash
npm run preview &
sleep 3

# Utiliser Playwright pour générer un PDF de chaque page légale
npx playwright codegen --output=/tmp/x.ts http://localhost:4321 &
# Alternativement : imprimer manuellement depuis Chrome (cmd+P > Save as PDF)

kill %1
```

- [ ] **Step 2 : Attendre le retour juridique**

Vie Legia (ou autre juriste) valide ou propose des amendements. Intégrer les amendements avant Task 17.

- [ ] **Step 3 : Si amendements : les intégrer**

```bash
# éditer les fichiers selon remarques juridique
npm run build
git add src/ && git commit -m "legal: amendements Vie Legia sur mentions + RGPD"
```

---

### Task 17 : Créer repo GitHub + premier push

**Files:** (aucun code — opérationnel git/GitHub)

- [ ] **Step 1 : Créer le repo GitHub privé**

Via `gh` CLI (si disponible) :

```bash
gh repo create berger-associes/berger-site --private --source=/Users/fabienberger/berger-site --remote=origin --push
```

Alternativement, via l'UI GitHub : créer un repo `berger-associes/berger-site` privé, puis :

```bash
cd /Users/fabienberger/berger-site
git remote add origin git@github.com:berger-associes/berger-site.git
git branch -M main
git push -u origin main
```

- [ ] **Step 2 : Vérifier**

```bash
git remote -v
git log --oneline | head -5
```

Expected : origin en remote, branche main pushée.

---

### Task 18 : Déployer sur Cloudflare Pages

**Files:** (aucun — configuration Cloudflare web UI)

- [ ] **Step 1 : Se connecter à Cloudflare et créer un projet Pages**

1. Ouvrir https://dash.cloudflare.com/
2. Aller dans **Workers & Pages** → **Create application** → **Pages** → **Connect to Git**
3. Authentifier GitHub, autoriser l'accès au repo `berger-associes/berger-site`
4. Sélectionner le repo

- [ ] **Step 2 : Configurer le build**

Paramètres :

- **Framework preset** : Astro
- **Build command** : `npm run build`
- **Build output directory** : `dist`
- **Root directory** : (vide)
- **Node version** : 20 (variable d'env `NODE_VERSION=20`)

- [ ] **Step 3 : Déployer et vérifier l'URL preview**

Cloudflare déploie automatiquement. Attendre ~1 min. Récupérer l'URL preview (ex : `berger-site-abc.pages.dev`).

Ouvrir l'URL dans un navigateur. Vérifier :
- Page d'accueil OK
- Les 4 liens footer fonctionnent
- Le bandeau cookies apparaît
- Le favicon est présent
- Les logos s'affichent

- [ ] **Step 4 : Commit la doc de déploiement**

Créer `docs/deploy-notes.md` :

```markdown
# Notes de déploiement

- Preview URL Cloudflare : https://berger-site-abc.pages.dev (remplacer par l'URL réelle)
- Branche déployée : main
- Build command : npm run build
- Node version : 20

## Redéploiement

Tout push sur `main` déclenche un redéploiement automatique.

## Preview par PR

Toute Pull Request génère une URL preview unique.
```

```bash
git add docs/deploy-notes.md && git commit -m "docs: notes de deploiement Cloudflare Pages"
git push
```

---

### Task 19 : Migration DNS Wix → Cloudflare Pages

**Files:** (aucun — opérationnel DNS)

**⚠ Opération sensible** : downtime possible de quelques minutes à plusieurs heures selon la propagation DNS. Faire en dehors des heures d'ouverture ou annoncer la maintenance.

**⚠ Prérequis** : Task 18 terminée et site preview validé par Fabien + Sabine + Marine. Relecture juridique (Task 16) validée.

- [ ] **Step 1 : Dans Cloudflare Pages, ajouter le domaine personnalisé**

1. Projet Pages → **Custom domains** → **Set up a custom domain**
2. Entrer `berger-associes.fr` → **Continue**
3. Entrer aussi `www.berger-associes.fr` → **Continue**
4. Cloudflare génère les enregistrements DNS cibles (CNAME ou apex A records)

- [ ] **Step 2 : Noter les valeurs DNS cibles**

Exemple :
- `berger-associes.fr` → A `192.0.2.1` (ou autre IP Cloudflare)
- `www.berger-associes.fr` → CNAME `berger-site.pages.dev`

- [ ] **Step 3 : Chez le registrar actuel de berger-associes.fr (probablement Wix/Domains)**

Se connecter au registrar. Modifier les enregistrements DNS pour pointer vers Cloudflare :

- Supprimer les enregistrements A et CNAME actuels pointant vers Wix
- Ajouter les nouveaux enregistrements fournis par Cloudflare Pages

**Alternatif (recommandé long terme)** : transférer le domaine à Cloudflare Registrar (pas de markup, gestion DNS native).

- [ ] **Step 4 : Attendre la propagation DNS (5 min – 24 h)**

Vérifier la propagation :

```bash
dig berger-associes.fr +short
dig www.berger-associes.fr +short
```

Quand les valeurs pointent vers Cloudflare, le site est live.

- [ ] **Step 5 : Tester en production**

Ouvrir https://www.berger-associes.fr et https://berger-associes.fr. Vérifier :
- HTTPS actif (cadenas navigateur)
- Redirection apex → www (ou inverse selon préférence — à configurer dans Cloudflare)
- Toutes les pages chargent
- Bandeau cookies
- Envoi test du lien mailto contact@berger-associes.fr

- [ ] **Step 6 : Désactiver Wix**

Une fois le site Cloudflare stable et validé :

1. Supprimer le site Wix (ou mettre en maintenance)
2. Annuler l'abonnement Wix pour éviter le renouvellement
3. Conserver un export de sauvegarde du contenu Wix (au cas où)

- [ ] **Step 7 : Commit notes post-deploy**

```bash
# éditer docs/deploy-notes.md avec l'URL prod, la date de migration, les notes post-deploy
git add docs/deploy-notes.md && git commit -m "docs: migration DNS Wix → Cloudflare réalisée le $(date +%Y-%m-%d)"
git push
```

---

## Self-review checklist

Avant d'exécuter ce plan, vérifier :

- [ ] Tous les prérequis légaux sont collectés (section tête)
- [ ] Les photos des 3 associés sont à disposition en haute résolution (sinon les portraits placeholder restent et Phase 2 les remplacera)
- [ ] Un compte Cloudflare existe (gratuit, créer si non)
- [ ] Un compte GitHub existe
- [ ] Node 20+ est installé localement
- [ ] Le dossier `/Users/fabienberger/berger-site` contient déjà `.gitignore` + spec + scripts (issus du brainstorm)
- [ ] Vie Legia (ou juriste équivalent) a donné son accord pour la relecture juridique

---

## Résumé des livrables

À la fin de ce plan :

- ✅ Site statique Astro opérationnel sur berger-associes.fr
- ✅ 5 pages (accueil, 3 légales, 404)
- ✅ Bandeau cookies conforme CNIL (opt-in granulaire)
- ✅ Tests Playwright a11y + cookies (5 routes + 4 tests)
- ✅ Lighthouse ≥ 95 sur les 4 catégories
- ✅ Déployé sur Cloudflare Pages, domaine migré, Wix désactivé
- ✅ Repo GitHub privé `berger-associes/berger-site`

**Durée estimée d'exécution** : 6–10 jours (Fabien + moi, quelques heures/jour), dont 2 jours de collecte d'informations légales et 1–2 jours de relecture juridique externe.

**Sortie du scope Phase 1** (à traiter en Phase 2) :

- 3 pages associés individuelles + bios
- Page cabinet + méthode
- Blog / journal + 10-12 billets evergreen
- CMS Keystatic
- Formulaire contact avec Workers
- Pages photos / design system complet

---

## Self-review (par Claude après écriture)

### 1. Couverture du spec

Le spec (Section 3 public cible, Section 4 positionnement, Section 5 arborescence, Section 6 direction visuelle, Section 7 logo, Section 8 emails, Section 10 conformité réglementaire, Section 11 techno, Section 12 design system, Section 13 phase 1 timeline) est couvert par les tasks suivantes :

- Positionnement + ton : intégré dans la landing Task 11 (titre, lead, associés)
- Direction visuelle : Task 2 (tokens) + Task 4-5 (header/footer) + intégration dans toutes les pages
- Logo : Task 6 (assets) + utilisation Header + Footer
- Emails : intégrés Task 11
- Conformité réglementaire complète : Task 7 + 8 + 9 + 10 + 15 + 16
- Techno : Task 1 (Astro) + Task 18 (Cloudflare) + Task 19 (DNS)
- Design system minimal (pour Phase 1) : Task 2 + 4 + 5

**Partie du spec hors scope Phase 1** : pages associés détaillées, méthode, journal — explicitement Phase 2.

### 2. Placeholders

Les occurrences de `{{TO_CONFIRM: ...}}` dans les fichiers légaux ne sont **pas** des placeholders de plan (violations du "no placeholders" du skill), mais des **placeholders de contenu** dans les fichiers source. Ils sont traités par Task 15 (remplacement systématique avant déploiement). La gate est explicite et bloquante.

Pas de "TODO", "TBD", "implement later" ni autres red-flags identifiés dans les steps eux-mêmes.

### 3. Cohérence des types / signatures

- Le state `ConsentState` défini dans CookieBanner est utilisé uniformément.
- Les classes CSS `.page-legal`, `.page-header`, `.btn` sont dupliquées entre pages légales (Task 8 et 9) — intentionnel Phase 1 pour isolation, factorisation en Phase 2.
- Les data-attributes du cookie banner (`data-cookie-accept-all`, etc.) sont cohérents entre test et implémentation.

### 4. Ambiguïtés

- Task 19 Step 3 : le registrar actuel de berger-associes.fr est à confirmer (probablement Wix mais peut être un autre). À vérifier par Fabien avant exécution. Non bloquant conceptuellement.
- Task 6 Step 2 : les 4 "compositions" livrées sont en réalité le même logo dupliqué (`recolor-strict` x4 et `monogram-noshadow`). Simplification Phase 1 — le graphiste livrera les vraies variantes entre Phase 1 et Phase 2.

Aucune incohérence bloquante détectée. Le plan est prêt à exécution.
