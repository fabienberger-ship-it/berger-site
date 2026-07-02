# Audit du site & upgrade du rendu — 2026-07-02

**Contexte** : reprise du développement après livraison de la Phase 1 (landing conforme).
**Livré dans ce commit** : audit complet + upgrade visuel de l'existant.
**Reste à faire** : Phase 2 (voir plan en fin de document).

---

## 1. Audit — état des lieux avant upgrade

### Ce qui était solide (à conserver)

- **Conformité** : mentions légales complètes (ORIAS, ACPR, AMF, RCP, médiateurs), RGPD, bandeau cookies CNIL opt-in — l'objectif Phase 1 est atteint.
- **Qualité technique** : 0 violation WCAG 2.1 AA (axe-core, 5 pages), Lighthouse 100/100, build Astro statique propre, tests Playwright en place.
- **Fondations design** : tokens CSS bien structurés, palette P2 respectée, échelle typographique cohérente.

### Problèmes de rendu identifiés (corrigés dans ce commit)

| # | Problème | Gravité | Correction |
|---|---|---|---|
| 1 | Logo header : PNG 600×414 (composition **verticale** + halo gris de l'ancien logo) écrasé à 44 px → wordmark illisible | Haute | Lockup vectoriel `Brand.astro` (monogramme + Fraunces), net à toute taille |
| 2 | Logo footer : PNG **navy sur fond navy** → moitié du texte invisible | Haute | `Brand tone="dark"` en ivoire |
| 3 | Portraits associés : sphères en dégradé gris → aspect « image cassée » | Haute | Médaillons navy à filet or avec initiales Fraunces |
| 4 | Hero plat : tout à gauche, 40 % de vide, aucun ancrage visuel — alors que le spec validait une composition hero **sur fond navy** (V1B) | Haute | Hero navy plein écran : eyebrow à filet or, titre Fraunces ivoire, monogramme en filigrane, strip de réassurance (ORIAS · CNCGP · ACPR/AMF) |
| 5 | Nav principale = liens légaux (Mentions/Confidentialité/Cookies) — nav de footer, pas de header ; 3 lignes sur mobile | Moyenne | Nav utile (Les associés · Nous rencontrer · CTA « Nous écrire ») ; le légal reste au footer |
| 6 | Section contact : texte brut sur aplat sable, sans hiérarchie | Moyenne | Grille 2 colonnes : intro + carte contact (email, adresse, CTA) |
| 7 | Aucun rythme visuel : pas de filets or, pas de micro-animations, transitions de sections brutales | Moyenne | Filets or signature (hero, contact, footer), révélation douce au scroll (IntersectionObserver, dégradation sans JS, `prefers-reduced-motion` respecté) |
| 8 | SEO : `twitter:image` absent, schema.org sans adresse complète, pas de `theme-color` | Basse | Complétés dans `SEOHead.astro` |
| 9 | README = template Astro par défaut | Basse | Réécrit |

### Points de vigilance non bloquants (inchangés)

- `og-default.png` utilise encore le monogramme PIL avec halo résiduel — à régénérer quand le SVG définitif du graphiste sera livré (budget 100–200 € déjà validé au spec).
- Les PNG `public/logos/` ne sont plus référencés par le site mais restent utiles (signature mail, PDF) — conservés.
- Formulaire de contact : toujours en `mailto:` (prévu Phase 2 via Worker).

## 2. Ce que l'upgrade ne change PAS

- Zéro modification du contenu éditorial ni des mentions réglementaires.
- Zéro dépendance ajoutée. Toujours 100 % statique, vanilla CSS/JS.
- Le bandeau cookies et ses tests sont intacts (9/9 tests verts après upgrade).

## 3. Plan proposé — prochaines étapes

### Court terme (finitions Phase 1++)

1. **SVG définitif du logo** (graphiste, 1–2 h) → régénérer og-image, favicons et remplacer le monogramme typographique du lockup par le vrai monogramme entrelacé.
2. **Portraits photo des 3 associés** : remplacer les médaillons d'initiales dès que les photos (post-traitement uniforme) sont prêtes — l'emplacement est dimensionné pour.
3. **Formulaire de contact** avec consentement RGPD explicite (Cloudflare Worker + SMTP) à la place du `mailto:`.
4. **Analytics** : brancher Cloudflare Web Analytics dans le hook `applyConsent` du bandeau cookies.

### Phase 2 — site complet (spec §5, 4–6 semaines)

- Semaine 1 : Keystatic (CMS Git) + design system étendu (cards Journal, page associé).
- Semaine 2 : pages `/le-cabinet`, `/les-associes` + 3 pages individuelles, `/methode`.
- Semaine 3 : `/journal` + template article + rédaction des 10–12 billets evergreen (Sud Radio : vérifier les droits avant publication).
- Semaine 4 : `/contact` avec choix d'interlocuteur, plan du site, polish + QA.
- Semaines 5–6 : relecture juridique + éditoriale, DNS, mise en production.

### Décisions ouvertes (rappel spec §16)

Directeur de publication définitif, DPO, catégorie courtier précise, relecture Vie Legia, droits Sud Radio, cohérence des séances photo.

---

## 4. Révision post-validation — direction « Institutionnel épuré » (même jour)

Retour de Fabien sur la V1 de l'upgrade : rendu jugé enfantin (médaillons à initiales,
monogramme CSS, filigrane, cartes à survol) et textes trop slogan. Décision actée :

- **Visuel** : fond ivoire dominant, mise en page typographique à filets fins, esprit
  étude notariale. Suppression des médaillons, du monogramme maison, du filigrane,
  des cartes et de toutes les animations décoratives. Wordmark seul en attendant
  le SVG définitif du graphiste.
- **Associés** : liste typographique (nom / fonction / email), type masthead.
- **Textes** : ton factuel et institutionnel. Suppression de « un cabinet en partage »,
  « ils nous rencontrent en personne, et ils restent » et de la note « version complète
  prochainement ».
