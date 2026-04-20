# Refonte berger-associes.fr — Design

**Date** : 2026-04-20
**Auteur** : Fabien Berger + Claude (brainstorm collaboratif)
**Statut** : à valider avant passage au plan d'implémentation

---

## 1. Contexte

Le site actuel (Wix, non mis à jour depuis juin 2023) présente plusieurs problèmes documentés par un audit récent :

- **Conformité légale urgente** : Joël Girod (décédé) encore listé comme Directeur de la publication avec email actif. Mentions légales lacunaires (pas d'ACPR visible, pas de RCP détaillée, pas de médiateurs, pas de catégorie courtier précise, pas de procédure de réclamation).
- **RGPD** : pas de politique de confidentialité distincte, pas de DPO identifié, pas de bandeau cookies granulaire, formulaire de contact sans consentement explicite.
- **UX/SEO** : tous les liens du menu pointent vers la même URL (one-pager déguisé), logo "OAK Horizont" incohérent, SEO quasi nul, pas de blog, pas de schéma éditorial.
- **Positionnement** : discours générique ("humain, architecture ouverte, relation long terme") partagé par 90 % des cabinets de CGP, aucune preuve sociale incarnée, aucun angle distinctif.

Décision : repartir de zéro — piste C de l'audit (migration vers une stack contrôlée).

## 2. Objectifs

- Site **rassurant** pour prospects arrivant par recommandation (100 % des acquisitions actuelles)
- **Conformité réglementaire** CIF / courtier / ORIAS / ACPR / AMF / RGPD dès le jour 1
- **Signature éditoriale** différenciante des 90 % de sites CGP concurrents
- **Éditable sans dev** pour le contenu courant (blog, actus, équipe)
- **Réversibilité** (pas de lock-in comme Wix)
- **SEO** correct (arborescence multi-pages, blog indexable, schémas Article et Organization)

## 3. Public cible

- **Segment** : particuliers à patrimoine financier 500 k€ – 3 M€
- **Profil** : ouvert (dirigeants cession, professions libérales, cadres supérieurs, familles intergénérationnelles)
- **Origine** : 100 % recommandation (clients existants, notaires, experts-comptables, réseau personnel)
- **Motivation** : relation humaine (1), confiance (2), expertise naturelle (3)

Le site est une **carte de visite augmentée**, pas un funnel d'acquisition froide. Le prospect arrive après avoir entendu « appelle Fabien chez Berger & Associés, tu verras » et doit trouver sur le site la confirmation de ce qu'on lui a promis.

## 4. Positionnement éditorial — Approche 3 « Les Trois Voix »

### Principe

Le cabinet, c'est **trois personnes** qu'on choisit de rencontrer : Fabien Berger, Sabine Tellier, Marine Gorin. Chacune avec son territoire, sa voix, son portrait. Le site n'est pas une plaque professionnelle, c'est la preuve que la recommandation est incarnée.

### Signal dominant

Humanité incarnée + collégialité. Le cabinet porte le nom de Fabien pour des raisons d'historique, mais le signal visuel et éditorial est collégial.

### Ton

- **Humanité** : chaleureux, authentique, jamais corporate froid
- **Confiance** : sérieux, précis, jamais survendu
- **Anti-brief absolu** : zéro racolage, zéro CTA vente forcée (pas de *"Audit patrimonial GRATUIT !"*, pas de bandeaux clignotants, pas d'urgence artificielle, pas de langage commercial)

### Références culturelles

- Équipes éditoriales (mastheads type *The New Yorker*)
- Cabinets d'architectes (Lacaton & Vassal dans leur auto-présentation)
- Études notariales de prestige
- Maisons d'avocats à taille humaine

## 5. Arborescence

```
/                         Accueil
├── /le-cabinet           Le cabinet (histoire, chiffres, partenaires, agréments)
├── /les-associes         Les associés (landing trio, liens vers les 3 pages)
│   ├── /fabien-berger    Page Fabien (bio, territoire, convictions, signatures blog)
│   ├── /sabine-tellier   Page Sabine
│   └── /marine-gorin     Page Marine
├── /methode              Notre méthode (process, indépendance, rémunération)
├── /journal              Journal (index blog)
│   └── /journal/[slug]   Article
├── /contact              Contact (formulaire + choix d'interlocuteur)
│
├── /mentions-legales     Mentions légales
├── /confidentialite      Politique de confidentialité (RGPD)
├── /cookies              Politique cookies + préférences
└── /plan-du-site         Plan du site
```

**Principes**

- **Les associés en landing trio** puis 3 pages individuelles — l'ADN de l'Approche 3.
- **Méthode en page dédiée** : le *comment* qui prouve la confiance (process de sélection, fréquence de revue, indépendance, rémunération).
- **Journal** (nom éditorial volontaire, pas "blog" ni "actualités").
- **3 pages légales distinctes** : conformité CIF/courtier + RGPD dès le jour 1.
- **Pas d'espace client** dans ce scope : l'accès à Harvest/O2S reste via leur URL dédiée, pas intégré au site marketing.

## 6. Direction visuelle — V4 Minéral parisien + palette P2 « Ivoire & Nuit »

### Typographie

| Usage | Police | Poids | Fournisseur |
|---|---|---|---|
| Titres site + navigation + hero | **Inter** | 500 / 600 | Google Fonts |
| Titres éditoriaux (articles, citations, signatures) | **Fraunces** | 500 / 600 | Google Fonts |
| Corps de texte | Inter | 400 | Google Fonts |

**Philosophie** : sans-serif dominante (signal moderne, minéral), serif réservée aux touches éditoriales (signal parisien discret). Cabinet d'archi qui accepte un trait parisien.

### Palette P2 « Ivoire & Nuit »

| Rôle | Code | Usage |
|---|---|---|
| Fond principal | `#FAF6EC` Ivoire | Background site, sections claires |
| Encre dominante | `#14233A` Bleu nuit | Textes, titres, fond footer, CTA |
| Ardoise (texte secondaire) | `#5F6574` | Sous-titres, métadonnées, taglines sur fond clair |
| Or (accent) | `#B69153` | Liens importants, tagline doré, filets d'accent |
| Sable (divider) | `#E8DEC9` | Fonds secondaires, séparateurs discrets |

**Règle** : l'or est réservé aux accents (tagline, liens importants, filets). Jamais en aplat large.

### Compatibilité logo

Le code bleu nuit `#14233A` est proche du navy du logo actuel — compatibilité forte, la mémoire bleue du cabinet est préservée.

## 7. Logo

### État actuel

Logo existant (monogramme `b&a` entrelacé + wordmark "BERGER & ASSOCIÉS") fourni par un graphiste en 2013. Palette : bleu ciel brillant + bleu nuit + gris argenté + gradient lustré + ombre portée. Esthétique datée (~2014-2015).

### Décision

- **Monogramme actuel conservé** (l'ADN du cabinet) — **recoloré** vers la palette P2 (or + navy, recolor PIL validé)
- **Wordmark bold condensed daté** remplacé par un **wordmark en Fraunces 600** aligné avec la typo du site
- **Tagline doré** ajouté sous le wordmark : *"Conseil en gestion de patrimoine · Paris"* (Inter 11.5px, letter-spacing 0.22em, encadré de filets or)
- **Composition cible validée** : V1B vertical sur fond navy `#14233A`, pour hero, couvertures PDF, papier à en-tête

### Finition à déléguer

Un graphiste doit passer 1–2 h sur le fichier `.ai` d'origine pour :

1. Supprimer proprement l'ombre portée et le halo gris résiduel
2. Aplatir le gradient lustré (garder juste les aplats or + navy)
3. Livrer un fichier vectoriel `.svg` propre utilisable à toute résolution

Budget estimé : **100–200 €**. Non bloquant pour le lancement — la version PIL recoloré peut être utilisée en attendant, le halo résiduel se fond sur les fonds ivoire/navy.

### Livrables logo

Tous les logos seront stockés dans `/public/logos/` du repo Astro :

- `logo-horizontal-ivoire.png` (en-tête site, signature mail)
- `logo-horizontal-navy.png` (footer, back carte de visite)
- `logo-vertical-ivoire.png` (formats carrés — avatars social, hero)
- `logo-vertical-navy.png` (couvertures PDF, papier à en-tête)
- `monogram.png` + `monogram.svg` (favicon, icônes d'app)
- `wordmark.svg` (utilisable en SVG texte pur, zoom illimité)

## 8. Emails associés

| Associé | Email public |
|---|---|
| Fabien Berger | `fabien.berger@berger-associes.fr` |
| Sabine Tellier | `sabine.tellier@berger-associes.fr` |
| Marine Gorin | `marine.gorin@berger-associes.fr` |

Contact générique : `contact@berger-associes.fr` (formulaire + adresse fallback).

## 9. Plan blog launch

### Vague 1 — evergreen (10-12 billets au lancement)

| Signature | Volume | Source / thèmes |
|---|---|---|
| **Sabine Tellier** | 6–8 billets | Retranscriptions / réécritures de ses chroniques *Sud Radio* (budget, immobilier, transmission, fiscalité grand public) |
| **Fabien Berger** | 3–4 billets | Analyses de fond : produits structurés, architecture ouverte, méthode de sélection, transmission stratégique |
| **Marine Gorin** | 0–1 billet | Optionnel au lancement, rejoindra quand la voix sera posée |

### Mention Sud Radio

Pour chaque billet Sabine issu de ses chroniques radio, ajouter en pied d'article :

> *Cette chronique a été initialement diffusée sur Sud Radio.*

Avec un lien vers le podcast Sud Radio si l'épisode est disponible en ligne.

### Point d'attention réglementaire

Vérifier avec Sud Radio que Sabine peut réutiliser son propre texte (et potentiellement l'audio). Contrat à lire avant mise en ligne des billets concernés. Non bloquant pour la conception du site.

### Cadence post-launch

Pas d'engagement public. Au choix de l'équipe selon la matière disponible. Le blog est un outil de **réassurance + SEO passif**, pas d'acquisition — pas besoin de cadence forcée. Bascule en cadence mensuelle possible si l'envie et la matière viennent (option C validée en brainstorm).

## 10. Conformité réglementaire (blocage J1)

### Mentions légales (`/mentions-legales`)

Éléments obligatoires à afficher :

- Raison sociale, forme juridique, capital social, RCS, siège social
- **Directeur de la publication** : ⚠ **Joël Girod doit être retiré immédiatement** (décédé). Remplacé par Fabien Berger (ou un des 3 associés selon arbitrage interne).
- **ORIAS** 13004419 (commun aux 3 associés)
- **Statut CIF** adhérent à la CNCGP (à confirmer)
- **Courtier en assurances** (à préciser catégorie : courtier / mandataire / agent)
- **ACPR** : mention autorité de contrôle + adresse + numéro d'enregistrement
- **AMF** : pour la partie CIF
- **Responsabilité civile professionnelle (RCP)** : nom assureur, police, plafond garantie
- **Médiateurs** :
  - Médiateur de l'AMF
  - Médiateur de la consommation désigné par la CNCGP
- **Procédure de réclamation** détaillée : voie interne, délais de réponse, escalade médiateur
- **Crédits du site** : hébergeur (Cloudflare), propriétaire des contenus

### Politique de confidentialité (`/confidentialite`)

- Nature des données collectées (formulaire contact, cookies)
- **DPO** identifié (un des associés ou délégué externe — à confirmer)
- Base légale des traitements (consentement, intérêt légitime)
- Durée de conservation
- Droits RGPD (accès, rectification, effacement, opposition, portabilité, retrait consentement)
- Adresse de contact DPO
- Transferts hors UE (si Cloudflare — dispositif de protection)
- Mention CNIL + droit de réclamation

### Politique cookies (`/cookies`)

- Liste granulaire des cookies (strictement nécessaires, analytics, préférences, marketing)
- Finalités précises pour chacun
- **Préférences interactives** : bouton de gestion permettant d'activer/désactiver par catégorie
- Bandeau cookies conforme CNIL (consentement opt-in explicite, pas de pré-cochage, possibilité de refuser aussi simplement qu'accepter)
- Pas de dépôt de cookies non essentiels avant consentement

### Formulaire de contact

- Case à cocher de consentement explicite pour le traitement des données
- Mention "Conformément à la loi Informatique et Libertés..."
- Lien direct vers la politique de confidentialité
- Pas d'envoi automatique de newsletter sans opt-in distinct

## 11. Stack technique

| Couche | Choix | Justification |
|---|---|---|
| **Framework** | **Astro** | Site à contenu, rendu statique par défaut, SEO excellent, simple à coder avec Claude |
| **CMS** | **Keystatic** | Interface admin pour l'équipe, contenu stocké en Markdown dans le repo Git (zéro vendor lock-in) |
| **Hébergement** | **Cloudflare Pages** | Gratuit, CDN mondial, HTTPS auto, déploiement par push GitHub |
| **Domaine** | **berger-associes.fr** (existant) | Migration DNS de Wix vers Cloudflare Pages. Pas de nouveau domaine. |
| **Repo** | **GitHub privé** | `berger-associes/berger-site` (à créer) |
| **CI/CD** | Cloudflare Pages auto | Push main → preview / deploy production |
| **Analytics** | **Plausible** ou **Cloudflare Web Analytics** | Pas Google Analytics (RGPD friendly), éviter consentement cookies analytics |
| **Formulaire contact** | Cloudflare Workers + SMTP | Traitement côté serveur statique, email vers `contact@berger-associes.fr` |

### Pourquoi pas Next.js

Next.js est un framework pour **apps dynamiques** (backend, auth, dashboards). Un site marketing de 15 pages + blog statique n'en a pas besoin — c'est overkill, plus verbeux à coder avec Claude, et plus lent en SEO par défaut. Astro est taillé pour ce use case.

### Pourquoi pas WordPress

Maintenance continue (plugins qui cassent, mises à jour sécurité mensuelles), écosystème daté, thèmes sur-mesure coûteux. Fabien a déjà BergerApp en production Flask, il n'a pas besoin d'un deuxième système à maintenir.

## 12. Design system (résumé)

### Composants clés

1. **Navigation** : logo + 4 entrées (Le cabinet · Les associés · Méthode · Journal · Contact) + indicateur de section active
2. **Hero accueil** : titre en Inter 500 (~68px desktop), sous-titre Inter 400 (~18px), 3 portraits ronds alignés, CTA principal navy + lien méthode doré
3. **Cards article Journal** : métadonnée or + titre Fraunces + excerpt + signature associée
4. **Page associé** : grand portrait, bio Fraunces pour les paragraphes narratifs, Inter pour les métadonnées (territoire, années, signatures récentes)
5. **Footer** : logo navy + coordonnées + agréments discrets + liens légaux + filet or
6. **Bandeau cookies** : discret en bas, 3 boutons (tout accepter / refuser / personnaliser)

### Règles générales

- **Largeur de contenu max** : ~960px pour les sections éditoriales, ~1200px pour les sections avec cards
- **Espaces** : très généreux (72–92px entre sections)
- **Animations** : très discrètes (fade up au scroll, jamais d'animation bling)
- **Images** : portraits pros des 3 associés, lumière naturelle, tenue cohérente (déjà réalisées)
- **Icônes** : SVG en ligne, couleur héritée, jamais d'emojis dans l'interface

### Accessibilité

- Contraste WCAG AA minimum (encre `#14233A` sur `#FAF6EC` : ratio 11:1 ✅)
- Navigation clavier complète
- `prefers-reduced-motion` respecté
- Balises ARIA sur les zones interactives
- Alt text sur toutes les images

## 13. Timeline proposée

**Proposition phasée**, à valider par Fabien :

### Phase 1 — Urgence conformité (7–10 jours)

Remplacer l'actuel par une **landing minimale conforme** :

- Une seule page d'atterrissage : coordonnées, équipe (sans détails), email de contact
- Mentions légales **complètes** (ACPR, ORIAS, RCP, médiateurs, Joël Girod retiré)
- Politique confidentialité + cookies
- Hébergement déjà sur Cloudflare Pages
- Design déjà dans la palette P2 pour préparer la phase 2

**Objectif** : lever le risque juridique lié au directeur de publication décédé + mentions incomplètes, le plus vite possible.

### Phase 2 — Site complet (4–6 semaines après Phase 1)

Construire les 15 pages + blog v1 (10–12 billets evergreen) :

- Semaine 1 : setup repo, stack Astro + Keystatic, design system codé
- Semaine 2 : pages cabinet + associés (3) + méthode
- Semaine 3 : journal + template article + **rédaction en parallèle des 10-12 billets** par le trio (fond = associés, je peux aider à la structuration / réécriture depuis les transcriptions Sud Radio)
- Semaine 4 : contact + polish + tests responsive + SEO + accessibilité
- Semaine 5-6 : relecture juridique des mentions, relecture éditoriale trio, déploiement production, redirection DNS, QA

### Alternative Big Bang

Skip phase 1, construire directement tout en 6–8 semaines. Problème : le risque juridique (Joël Girod) reste pendant 2 mois supplémentaires. À trancher avec Fabien selon son appétit pour le risque.

## 14. Ressources humaines

**Hypothèse par défaut** (à valider) : **Fabien code avec Claude**, sur le modèle BergerApp (Flask). Aucun dev externe dans le scope initial. Un graphiste ponctuel (100–200 €) pour la finition du logo.

**Rôles éditoriaux** :

- Fabien : rédaction de ses billets de fond, validation technique
- Sabine : retranscriptions / réécritures de ses chroniques Sud Radio pour le blog, validation éditoriale
- Marine : relecture, prise de vue si besoin de portraits complémentaires
- Tous les 3 : validation collégiale du design final avant mise en ligne

**Validation juridique** : mentions légales à faire relire par **Vie Legia Conseil** (Javi — partenaire validé) ou un juriste spécialisé CIF avant publication.

## 15. Hors scope de cette refonte

- Refonte complète du logo (gardons le V1B + finition graphiste ponctuelle)
- Espace client intégré (accès Harvest/O2S reste séparé)
- E-commerce / vente directe de produits
- Espaces de rendez-vous en ligne (Calendly ou similaire)
- Newsletter email sortante (peut venir en phase 3)
- Application mobile dédiée
- Traduction en langues étrangères (site en français uniquement v1)

## 16. Questions ouvertes — à trancher avant passage au plan d'implémentation

1. **Timeline** : phasée (landing urgence 7–10 jours + site complet 4–6 semaines) ou Big Bang 6–8 semaines ?
2. **Directeur de la publication** : qui des 3 associés prend ce rôle ?
3. **DPO** : un associé ou externalisation (ex : Vie Legia) ?
4. **Catégorie courtier** : à préciser pour les mentions légales (courtier simple, mandataire d'assurance, agent général ?)
5. **Relecture juridique** : Vie Legia accepte la mission ou on consulte un autre juriste ?
6. **Budget finition logo** : feu vert 100–200 € pour un graphiste externe ponctuel ?
7. **Droits Sud Radio** : Sabine doit vérifier son contrat avant publication des billets retranscrits.
8. **Photos équipe** : les séances photo déjà faites sont-elles **stylistiquement cohérentes entre les 3 associés** (même lumière, même cadrage, même traitement colorimétrique) ? Si les séances ont été faites séparément, prévoir un post-traitement uniforme (retouche photo commune) pour éviter une collection de portraits dissonants.

## 17. Annexes (artefacts du brainstorm)

Tous les visuels itératifs produits pendant le brainstorm sont archivés dans :

- `/.superpowers/brainstorm/66468-1776693627/content/` — moodboards, synthèses B+C, palettes, compositions logo
- `/assets/Nouveau Logo/` — kit original du graphiste (AI, EPS, PNG, PDF)
- `/assets/logo-recolor/` — PNG recolorés PIL (strict, mono navy, mono encre, no-shadow)
- `/assets/logo-svg/` — SVG produits pendant brainstorm (wordmarks, monogrammes minimaux)
- `/scripts/` — scripts Python de recolorisation (`recolor_logo.py`, `clean_monogram.py`, `build_*_page.py`)

---

**Prochaine étape** : validation de ce spec par Fabien, puis passage à l'écriture du plan d'implémentation via `superpowers:writing-plans`.
