# berger-associes.fr

Site vitrine du cabinet **Berger & Associés** — conseil en gestion de patrimoine, Paris.

- **Stack** : Astro 6 · vanilla CSS (design tokens) · Playwright + axe-core
- **Design** : direction « Minéral parisien », palette P2 « Ivoire & Nuit » (`src/styles/tokens.css`)
- **Spec design** : `docs/superpowers/specs/2026-04-20-refonte-site-berger-associes-design.md`
- **Phase actuelle** : Phase 1 — landing conforme (accueil + 3 pages légales + 404)

## Structure

```
src/
├── components/     Brand (lockup marque), Header, Footer, SEOHead, CookieBanner
├── layouts/        BaseLayout (SEO + skip-link + reveal au scroll)
├── pages/          index, mentions-legales, confidentialite, cookies, 404
└── styles/         tokens.css (design tokens) + global.css (reset, utilitaires, boutons)
```

## Commandes

| Commande | Action |
| :-- | :-- |
| `npm install` | Installe les dépendances |
| `npm run dev` | Serveur de dev sur `localhost:4321` |
| `npm run build` | Build de production vers `./dist/` |
| `npm run preview` | Prévisualise le build |
| `npx playwright test` | Tests : a11y WCAG 2.1 AA (axe-core) + bandeau cookies CNIL |

Dans un environnement avec Chromium préinstallé, pointer Playwright dessus :
`PLAYWRIGHT_CHROMIUM_EXECUTABLE=/chemin/vers/chromium npx playwright test`

## Conventions

- L'or (`--c-gold`) est réservé aux accents (filets, eyebrows, liens) — jamais en aplat large.
- Contenu et mentions réglementaires : ne rien modifier sans validation (ORIAS, ACPR, AMF, CNCGP).
- Animations discrètes uniquement, `prefers-reduced-motion` respecté, contenu visible sans JavaScript.
