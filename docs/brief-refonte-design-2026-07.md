# Brief de refonte — berger-associes.fr

**Destinataires** : direction artistique / studio / graphiste indépendant
**Contact** : Fabien Berger — fabien.berger@berger-associes.fr
**Date** : juillet 2026

Ce document fait l'état des lieux du projet de refonte du site, de ce qui a été tenté, de ce qui a été rejeté et pourquoi, et de ce que le cabinet attend. Il doit permettre à un spécialiste de démarrer une mission de direction artistique sans repartir de zéro.

---

## 1. Le cabinet en bref

- **Berger & Associés** — cabinet indépendant de conseil en gestion de patrimoine, fondé en **2013**.
- **Trois associés** : Fabien Berger (associé fondateur), Sabine Tellier, Marine Gorin. Sabine Tellier tient des chroniques patrimoniales sur **Sud Radio** (notoriété média réutilisable).
- **Bureaux** : 96 boulevard Sébastopol, 75003 Paris.
- **Clientèle** : particuliers et familles, patrimoine financier 500 k€ – 3 M€ (dirigeants en cession, professions libérales, cadres supérieurs, familles intergénérationnelles).
- **Acquisition : 100 % par recommandation** (clients, notaires, experts-comptables). Le site n'est pas un outil d'acquisition : c'est une **carte de visite augmentée**. Le prospect arrive après avoir entendu « appelle Fabien chez Berger & Associés, tu verras » — le site doit confirmer cette promesse.
- **Agréments** : ORIAS n° 13004419 (CIF + courtier en assurances), membre CNCGP, sous contrôle ACPR / AMF, carte professionnelle Transaction CCI Paris.

## 2. L'intention éditoriale validée (toujours d'actualité)

- **Signal dominant** : humanité incarnée + collégialité. Le cabinet, ce sont trois personnes qu'on choisit de rencontrer.
- **Ton** : chaleureux, sérieux, précis. Jamais corporate froid, jamais survendu.
- **Anti-brief absolu** : zéro racolage, zéro CTA agressif (« audit GRATUIT ! »), pas d'urgence artificielle, pas de langage commercial.
- **Références culturelles du spec initial** : mastheads éditoriaux (The New Yorker), cabinets d'architectes (Lacaton & Vassal), études notariales de prestige, maisons d'avocats à taille humaine.

## 3. État technique — solide, à conserver

- **Stack** : site statique Astro, vanilla CSS, hébergé sur Cloudflare Pages. Repo GitHub : `fabienberger-ship-it/berger-site`. Preview : https://berger-site.pages.dev
- **Conformité juridique faite et validée** : mentions légales complètes (ORIAS, ACPR, AMF, RCP, médiateurs, procédure de réclamation), politique de confidentialité RGPD, politique cookies + bandeau conforme CNIL.
- **Qualité** : 0 violation WCAG 2.1 AA (tests automatisés axe-core), site rapide, sans dépendances.
- **Important** : le domaine public www.berger-associes.fr pointe encore vers l'**ancien site Wix**, qui pose des problèmes de conformité — la bascule DNS attendra une version dont le cabinet est fier.

**La mission du spécialiste porte sur le design, pas sur la technique ni la conformité.** L'intégration peut être assurée en interne sur la stack existante : le livrable attendu est une direction artistique + maquettes, pas du code.

## 4. Ce qui a été tenté et rejeté — à lire attentivement

Deux itérations de design ont été produites (par IA) en juillet 2026 et **rejetées par le fondateur**. Elles calibrent ce qu'il ne veut pas :

### Itération 1 — « éditorial navy » → rejetée : « enfantin »

Hero sur fond bleu nuit avec filigrane monogramme géant, médaillons circulaires avec initiales des associés (FB / ST / MG), monogramme « b&a » redessiné en CSS, cartes blanches à effet de survol, micro-animations au scroll.

**Verbatim du rejet : « enfantin, dégueulasse, les textes sont ridicules, j'ai honte. »**
Lecture : les initiales en pastilles font avatar d'application, le logo bricolé dévalorise la marque, les textes façon slogan (« un cabinet en partage », « ils nous rencontrent en personne, et ils restent ») sonnent creux.

### Itération 2 — « institutionnel épuré » → rejetée : « pas à notre image »

Fond ivoire, mise en page purement typographique à filets fins (esprit étude notariale), associés en liste type masthead, textes réécrits en factuel sobre.

**Verbatim du rejet : « toujours nul et pas à notre image. »**
Lecture : propre mais générique et désincarné. Sans matière visuelle propre au cabinet, l'exercice de style typographique retombe dans l'anonyme.

### Enseignement pour le prestataire

Le problème n'est pas la mise en page : c'est l'**absence d'identité incarnée**. Le site actuel ne contient rien du cabinet — ni visages, ni vrai logo, ni lieu, ni matière. Et les goûts positifs du fondateur n'ont **jamais été collectés** : il a réagi à des propositions, mais on ne sait pas encore ce qu'il admire.

## 5. Première étape recommandée pour la mission

1. **Séance de références avec Fabien** (30–60 min) : lui faire montrer 3 à 5 sites qu'il trouve « à leur image » (banques privées, family offices, maisons de prestige, hôtels particuliers, peu importe le secteur). C'est l'information manquante n° 1.
2. **Récupérer la matière existante** :
   - Kit logo d'origine (fichiers .ai / .eps du graphiste de 2013 — monogramme b&a entrelacé). Il nécessite 1–2 h de nettoyage (suppression ombre portée et gradient lustré, livraison SVG propre) — budget 100–200 € déjà validé par le cabinet.
   - Portraits professionnels des trois associés : des séances photo ont été réalisées (à vérifier : cohérence de lumière/cadrage entre les trois ; prévoir un post-traitement uniforme, voire une reprise de séance commune).
3. **Trancher si la charte actuelle est conservée ou révisée** : palette « Ivoire & Nuit » (ivoire #FAF6EC, bleu nuit #14233A, or #B69153, ardoise, sable) + typos Inter / Fraunces. Elle avait été validée sur moodboard, mais **elle est révisable** — les deux rejets peuvent aussi signifier que cette charte ne porte pas assez l'identité.

## 6. Périmètre suggéré du livrable design

- **Maquettes desktop + mobile** pour : accueil, page « le cabinet », page associé individuel (×3 déclinables), « notre méthode », index du journal (blog), gabarit article, contact.
- **Mini design system** : couleurs, typographies, composants récurrents (navigation, pied de page, cartes d'article, blocs contact), traitement des portraits.
- **Traitement du logo** : finition du monogramme d'origine + wordmark, déclinaisons fond clair/fond sombre, favicon.
- **Contraintes non négociables** : les contenus réglementaires (agréments, mentions) doivent rester présents et lisibles ; accessibilité WCAG AA (contrastes) ; pas de photographie de banque d'images générique.

## 7. Arborescence cible (spec validée, phase 2)

```
/                       Accueil
├── /le-cabinet         Histoire, chiffres, partenaires, agréments
├── /les-associes       Landing trio → 3 pages individuelles
├── /methode            Process, indépendance, rémunération
├── /journal            Blog éditorial (10-12 billets au lancement,
│                       dont réécritures des chroniques Sud Radio de Sabine)
├── /contact            Formulaire + choix d'interlocuteur
└── pages légales       Mentions, confidentialité, cookies (déjà faites)
```

## 8. Questions ouvertes côté cabinet

- Références visuelles de Fabien (à collecter en séance — priorité 1).
- Cohérence stylistique des portraits existants des trois associés.
- Conservation ou révision de la palette / typo actuelles.
- Directeur de la publication et DPO définitifs (juridique, sans impact design).
- Droits de réutilisation des chroniques Sud Radio (impact sur le contenu du journal).

## 9. Historique documentaire

Dans le repo GitHub (`docs/`) : spec design complète d'avril 2026 (`superpowers/specs/`), plan d'implémentation Phase 1 (`superpowers/plans/`), audit du rendu et journal des itérations rejetées (`audit/2026-07-02-audit-upgrade-rendu.md`).
