# Berger & Associés

Site du cabinet de conseil en gestion de patrimoine à Paris. Astro 6, CSS, hébergement existant Cloudflare Pages.

La proposition de septembre 2026 réintroduit le logo original et les portraits du cabinet, avec une navigation adaptée au mobile. [Direction, sources et vérifications](docs/reprise-design-2026-09-26.md).

## Développement

- `npm ci` : installation.
- `npm run dev` : aperçu local.
- `npm run build` : compilation statique dans `dist/`.
- `npx playwright test` : neuf contrôles sur le résultat compilé, servi sur le port 4392.

La variable `PLAYWRIGHT_CHROMIUM_EXECUTABLE` permet d'utiliser un navigateur Chromium déjà installé.

## Publication

La branche `main` alimente la production. Les autres branches créent des prévisualisations Cloudflare, exclues de l'indexation par une balise robots. Elles sont publiques.

Le domaine commercial n'est pas encore raccordé au projet. La proposition doit être revue avec le cabinet, son portrait de Marine complété et les pièces réglementaires actuelles rapprochées des textes avant cette bascule.

## Ressources

Les portraits, images et polices sont hébergés avec le site. Aucun outil publicitaire ni de mesure d'audience n'est chargé par les pages. Les liens email ouvrent la messagerie du visiteur ; le plan est un lien externe.

Les documents de reconstitution et les sauvegardes des comptes restent dans l'espace de travail principal. Les archives privées ne doivent jamais être publiées.
