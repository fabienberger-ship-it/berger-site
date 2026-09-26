# Reprise du design — 26 septembre 2026

La demande de reprise du design remplace l'option de remise en ligne immédiate de la version de juillet. La branche de travail est `fabienberger-ship-it/refonte-design-septembre`. La production et les DNS ne sont pas modifiés par cette proposition.

## Direction et réalisation

Le point de départ est l'identité existante : logo original bleu du site Wix, portraits réels de Fabien Berger et Sabine Tellier et signature « L'humain, avant tout. » reprise de ce site. La page combine un fond clair, du bleu nuit, un accent bronze, les caractères Libre Caslon Display / DM Sans et une composition décalée des deux portraits.

L'accueil présente le cabinet, quatre sujets patrimoniaux, les étapes de l'accompagnement, les trois associés et les coordonnées. Le menu mobile fonctionne au clavier, se referme après navigation et permet de joindre chaque associé par email. Le lien d'itinéraire ouvre un service externe à l'initiative du visiteur.

Marine Gorin est présentée dans la liste des associés, avec son email. Son portrait n'a pas été retrouvé. Une demande de dossier ou de lien a été adressée à Fabien ; aucune autre personne ni aucun portrait généré n'a été utilisé pour la représenter.

Les photographies de l'ancienne équipe n'ont pas été réutilisées comme photo de groupe actuelle.

## Sources des visuels

Les légendes dans le HTML archivé du site Wix permettent d'associer explicitement les images à Fabien et Sabine :

- Fabien : [original Wix](https://static.wixstatic.com/media/4c4fdf_39191331d3e44f8e9153b6ad53e9c333~mv2.png), légende « Fabien Berger — Associé, depuis 2013 ».
- Sabine : [original Wix](https://static.wixstatic.com/media/4c4fdf_3a810823ddf94e00a894ebd2e031966b~mv2.png), légende « Sabine Tellier — Associée, depuis 2016 ».
- Logo : [ressource du Wix](https://static.wixstatic.com/media/4c4fdf_231efc21886441d59c4c80f44d148837~mv2.png). Le fichier hérité est nommé « OAK » sur le CDN, mais l'image contient bien le logo Berger & Associés.
- Crédit photographique conservé : Lucas Marrella, selon les mentions du site d'origine.

Les portraits sont convertis en WebP, sans retouche de leur contenu, puis servis en tailles adaptées par Astro. Les originaux haute définition sont conservés dans l'archive locale de la reconstitution, hors Git.

Les deux familles de polices sont servies localement ; leurs licences SIL Open Font License sont conservées dans `public/fonts/`.

## Vignette de partage

Fichier livré : `public/og.png`. Outil intégré Imagegen, une seule génération. Le texte de la vignette a été relu : nom du cabinet, titre, activité, Paris et date de création corrects. Aucun portrait ou monogramme inventé.

Prompt exact : [imagegen-social-2026-09-26.txt](imagegen-social-2026-09-26.txt).

## Informations et confidentialité

Les éléments renseignés dans le DER de janvier 2026 ont remplacé les champs provisoires : MMA / police 112.786.342 / adhérent 229584, non-détention de fonds, Sabine Tellier pour les réclamations et les droits sur les données, AMF pour le CIF et CMAP pour les autres activités. Le caractère non indépendant du conseil CIF est précisé. La mention MIOBSP non établie par les deux inscriptions actives ORIAS et absente du DER est retirée du brouillon.

Les pièces attestant la couverture d'assurance actuelle, le renouvellement de la carte professionnelle et le contrat de médiation restent à rapprocher du texte avant la bascule commerciale. Le remplacement des champs provisoires n'est pas une certification juridique.

La confidentialité décrit les liens email réellement présents. L'adresse DPO non justifiée est remplacée par le contact indiqué dans le DER. Le bandeau de consentement sans mesure d'audience effective est retiré. Aucun outil d'analyse ou de publicité n'est ajouté ; les anciennes préférences sont nettoyées de façon ciblée.

Références consultées le 26 septembre :

- [ORIAS](https://www.orias.fr/home/showIntermediaire/791895469) : deux inscriptions actives COA et CIF.
- [CMAP, saisine consommation](https://www.cmap.fr/saisir-cmap-mediation-consommation/).
- [CNIL, cookies et traceurs](https://www.cnil.fr/fr/cookies-et-autres-traceurs/que-dit-la-loi).
- [CNIL, mesures précontractuelles](https://www.cnil.fr/fr/les-bases-legales/contrat).
- DER du cabinet daté de janvier 2026, document local non signé étudié pendant la reconstitution.

## Vérification

Compilation des cinq pages réussie. Neuf contrôles automatisés réussis : accessibilité axe sur cinq pages, absence de requêtes tierces et de cookies applicatifs, nettoyage ciblé de l'ancienne préférence, navigation mobile et fermeture du menu au clavier. Les contrôles mobiles couvrent 390 et 320 pixels de large.

Les prévisualisations Cloudflare sont marquées `noindex, nofollow` lorsque la branche de construction diffère de `main`. Les liens sociaux utilisent alors l'adresse du déploiement. Ces réglages ne protègent pas l'aperçu par mot de passe : il reste consultable par toute personne connaissant son adresse.

L'aperçu est destiné à recueillir le retour du cabinet avant la mise en ligne sur son domaine. Aucun abonnement, DNS ou état de publication Wix n'a été modifié.
