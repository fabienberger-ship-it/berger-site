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

## Retours de Marine intégrés le 30 septembre

Les couleurs et la sobriété sont conservées. L'accueil porte désormais « Une relation de confiance, un patrimoine qui dure » ; la section cabinet utilise « Construire ensemble, sur le long terme ». Les autres accroches proposées sont des alternatives, pas des slogans à cumuler.

La section associés devient « Faisons connaissance » et précise que ceux qui dirigent le cabinet sont ceux qui conseillent les clients. La présentation de Marine Gorin (Guillo) reprend le parcours, le diplôme, les certifications et les expertises qu'elle a elle-même fournis, avec une légère mise en forme en trois paragraphes. Ces éléments sont déclaratifs et n'ont pas été vérifiés auprès des organismes cités.

Pour Fabien, le texte court repose sur la création du cabinet en 2013 et la constitution d'une équipe aux profils complémentaires, attestées par l'accueil Wix sauvegardé. Pour Sabine, l'association depuis 2016 est attestée par la légende du portrait Wix ; la direction et l'accompagnement personnel reprennent le DER et le positionnement communiqué par Marine. Leurs diplômes, parcours antérieurs et expertises individuelles ne sont pas inventés. Leurs compléments biographiques ont été demandés à Fabien et restent attendus.

La méthode précise le rôle de généralistes et le travail en interprofessionnalité avec des notaires, avocats et experts-comptables, qu'il s'agisse des conseils habituels du client ou d'autres experts. Le texte sur la transmission est aligné sur cette ouverture.

La section contact est intitulée « Tout commence par un premier échange ». Les trois emails personnels remplacent l'adresse générique. Le pied de page, la page 404 et les données structurées utilisent également les contacts des associés ; aucune boîte mail n'est supprimée chez le fournisseur de messagerie.

La vignette de partage `public/og.png` a été actualisée par une seule édition Imagegen intégrée : [prompt exact](imagegen-social-2026-09-30.txt). La nouvelle accroche et les autres mentions de l'image ont été relues. Les photos existantes sont conservées dans l'attente du choix des trois associés et du portrait de Marine.

Les coordonnées et présentations sont réunies dans `src/data/associates.ts` pour éviter des écarts entre les différentes sections. L'aperçu de branche reste le lien à utiliser pour suivre les modifications ; les anciens liens de déploiement conservent leur version historique.

Vérification du 30 septembre : compilation réussie, neuf tests existants réussis, aucune adresse générique ni ancienne accroche restante dans les sources. La relecture sémantique a également permis d'inclure l'adresse email visible dans le nom accessible de chaque lien des biographies.
