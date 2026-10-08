# Pages Aloi, ajoutees a build.py du site IE DIGITAL (08/10/2026).
# Les URL aloi-conditions.html, aloi-confidentialite.html, aloi-assistance.html
# et aloi-methode.html sont inscrites dans l'app et dans App Store Connect :
# ne jamais les renommer.

ALOI_PAGES = [
    ("aloi.html", "Aloi"),
    ("aloi-confidentialite.html", "Aloi — Confidentialité"),
    ("aloi-conditions.html", "Aloi — Conditions d'utilisation"),
    ("aloi-assistance.html", "Aloi — Assistance"),
    ("aloi-methode.html", "Aloi — Méthode du classement"),
]

ALOI_TITRES = {
    "aloi.html": "Aloi — IE DIGITAL",
    "aloi-confidentialite.html": "Confidentialité — Aloi",
    "aloi-conditions.html": "Conditions d'utilisation — Aloi",
    "aloi-assistance.html": "Assistance — Aloi",
    "aloi-methode.html": "Méthode du classement — Aloi",
}

ALOI_EDITEUR = """
<h2>Mentions légales</h2>
<ul>
<li><b>Éditeur</b> : IE DIGITAL, SARL à associé unique, RCS Lille Métropole 822 744 116, TVA intracommunautaire FR42 822 744 116. Siège : 31 rue du Président Kennedy, 59237 Verlinghem, France. E-mail : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Voir aussi les <a href="https://iedigital.fr/mentions-legales.html">mentions légales</a>.</li>
<li><b>Directeur de la publication</b> : Alexandre Elard, gérant.</li>
<li><b>Hébergeur de cette page</b> : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</li>
<li><b>Distribution de l'app</b> : App Store, exploité par Apple Distribution International Ltd., Hollyhill Industrial Estate, Hollyhill, Cork, Irlande.</li>
</ul>
"""

ALOI_NATURE = """<p>Aloi est un outil de calcul, de diagnostic et de comparaison de frais. Il ne fournit ni conseil en investissement, ni conseil en assurance, ni recommandation personnalisée. Il ne vend aucun produit, ne perçoit aucune commission et ne propose aucun lien de souscription. IE DIGITAL n'est ni conseiller en investissements financiers, ni intermédiaire en assurance, ni intermédiaire en opérations de banque. Avant toute décision, informez-vous auprès d'un professionnel habilité.</p>"""

ALOI_BODIES = {}

ALOI_BODIES["aloi.html"] = ("""
<p class="eyebrow">Application iOS</p>
<h1>Aloi</h1>
<p class="lede">Votre patrimoine travaille-t-il bien ? Une note sur 100 pour chaque contrat,
et ce que vos frais vous coûtent jusqu'à la retraite. Sans compte, sans connexion bancaire.</p>

<section>
  <h2>En bref</h2>
  <dl class="facts">
    <div><dt>Plateforme</dt><dd>iPhone, iOS 17 et plus.</dd></div>
    <div><dt>Compte</dt><dd>Aucun. Pas de serveur Aloi, pas de connexion bancaire, pas de publicité, pas de traceur.</dd></div>
    <div><dt>Données</dt><dd>Saisies par vous et enregistrées sur l'iPhone. Synchronisation iCloud facultative, export chiffré.</dd></div>
    <div><dt>Formules</dt><dd>Diagnostic, notes, frais, catalogue et comparaisons gratuits pour tous. Aloi Plus, achat unique : historique, univers société, immobilier complet, import illimité, export.</dd></div>
    <div><dt>Nature</dt><dd>Outil de calcul et de comparaison. Pas de conseil en investissement ni en assurance.</dd></div>
    <div><dt>Éditeur</dt><dd>IE DIGITAL</dd></div>
  </dl>
</section>

<section>
  <h2>Aide et informations</h2>
  <ul>
    <li><a href="aloi-assistance.html">Assistance, questions fréquentes et signalement d'une donnée erronée</a></li>
    <li><a href="aloi-methode.html">Méthode de la note et du classement des contrats</a></li>
    <li><a href="aloi-confidentialite.html">Politique de confidentialité</a></li>
    <li><a href="aloi-conditions.html">Conditions d'utilisation</a></li>
    <li><a href="mailto:contact@iedigital.fr?subject=Aloi%20%E2%80%94%20assistance">Nous écrire : contact@iedigital.fr</a></li>
  </ul>
</section>
""", "Aloi, application iOS de diagnostic patrimonial éditée par IE DIGITAL : note des contrats, frais en euros, comparaison neutre. Assistance, méthode, confidentialité, conditions.")

ALOI_BODIES["aloi-confidentialite.html"] = ("""
<p class="eyebrow"><a href="aloi.html">Aloi</a></p>
<h1>Politique de confidentialité</h1>
<p class="lede">Aloi, application iOS · version du 8 octobre 2026</p>

<div class="note" style="margin-bottom:32px">
<p style="margin:0"><b>En bref.</b> Aloi n'a ni compte, ni serveur, ni connexion bancaire, ni outil de mesure d'audience, ni publicité. Rien ne part sur le réseau sans un geste de votre part. Les informations que vous saisissez (contrats, frais, biens, crédits, profil) sont enregistrées sur votre iPhone. IE DIGITAL, l'éditeur, ne reçoit aucune de ces données et ne peut pas y accéder. Si vous activez la synchronisation iCloud, elles sont copiées dans votre propre espace iCloud, géré par Apple. Vous pouvez exporter ou effacer vos données à tout moment.</p>
</div>

<h2>1. Qui est responsable</h2>
<p>Le responsable du traitement est <b>IE DIGITAL</b>, SARL à associé unique immatriculée au RCS de Lille Métropole sous le numéro 822 744 116, dont le siège est au 31 rue du Président Kennedy, 59237 Verlinghem, France. Directeur de la publication : Alexandre Elard, gérant. Contact : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. IE DIGITAL n'a pas désigné de délégué à la protection des données ; pour toute question sur vos données, écrivez à cette adresse.</p>

<h2>2. Les données utilisées par Aloi</h2>
<ul>
<li><b>Vos contrats et comptes</b> (nom, établissement, enveloppe, mode de gestion, encours, frais, date d'ouverture, documents que vous importez) : calculer les frais, la note et les comparaisons. Sur l'iPhone.</li>
<li><b>Vos biens immobiliers et crédits</b> (valeur, surface, nature du bien, commune choisie dans une liste, loyers, charges, capital restant dû, taux) : calculer la valeur nette, le cash-flow, les simulations et la valeur de marché indicative. Sur l'iPhone. Aloi ne demande jamais d'adresse.</li>
<li><b>Votre profil facultatif</b> (prénom, année de naissance, horizon, dépenses, revenus, tolérance au risque, nom de votre société) : adapter les projections et la réserve de sécurité. Sur l'iPhone. Il n'intervient jamais dans le classement des contrats du marché.</li>
<li><b>Relevés datés</b> (instantanés de votre patrimoine) : tracer l'historique. Sur l'iPhone.</li>
<li><b>Réglages</b> (univers personnel ou société, mode discret, options d'affichage) : sur l'iPhone.</li>
</ul>
<p>Aloi ne vous demande ni nom de famille, ni adresse électronique, ni numéro de téléphone, ni identifiant bancaire, et ne se connecte à aucune banque.</p>

<h2>3. Bases légales</h2>
<ul>
<li><b>Fonctionnement de l'app</b> (calculs, historique, synchronisation que vous activez) : l'exécution du service que vous utilisez (article 6.1.b du RGPD).</li>
<li><b>Échanges par courriel avec IE DIGITAL</b> (assistance, signalement d'une donnée erronée) : l'intérêt légitime à vous répondre (article 6.1.f du RGPD).</li>
</ul>

<h2>4. Ce qui peut sortir de l'app</h2>
<p>IE DIGITAL ne reçoit rien. Les flux ci-dessous n'existent que si vous utilisez la fonction concernée.</p>
<ul>
<li><b>Synchronisation iCloud (facultative).</b> Si vous la choisissez, vos données sont copiées dans la base privée de votre compte iCloud, chiffrée et gérée par Apple selon sa propre politique. IE DIGITAL n'y a pas accès.</li>
<li><b>Achats.</b> L'achat d'Aloi Plus est traité par Apple. IE DIGITAL ne reçoit ni votre identité ni vos moyens de paiement, seulement des statistiques de ventes non nominatives.</li>
<li><b>Explications en langage simple.</b> Elles sont rédigées sur l'iPhone par le modèle d'Apple intégré à iOS, sans envoi de vos données à un service extérieur.</li>
<li><b>Lecture de documents.</b> Les PDF et photos de relevés que vous importez sont lus sur l'iPhone ; ils ne sont envoyés nulle part.</li>
<li><b>Partages et exports.</b> L'image de partage (note, rang, verdict, sans montant) et l'export de vos données ne sortent que si vous les partagez vous-même avec la feuille de partage d'iOS. Une fois partagés, ils relèvent du service que vous avez choisi.</li>
<li><b>Ventes comparables (facultatif).</b> Les prix médians par commune et les loyers de marché sont intégrés à l'app : les consulter n'envoie rien. Si vous demandez les ventes comparables d'un bien, Aloi vous montre d'abord ce qui sera téléchargé. Un premier geste de votre part lit la taille du fichier public des ventes de votre département sur data.gouv.fr ; un second lance le téléchargement. Le serveur de data.gouv.fr reçoit alors, comme pour tout téléchargement, votre adresse IP et le département demandé, jamais l'adresse ni la commune du bien. La recherche se fait ensuite sur l'iPhone. Le fichier se supprime dans <i>Réglages › Vos données</i>. Aucune requête n'est envoyée avant votre premier geste.</li>
<li><b>Liens vers des sources.</b> Quand vous ouvrez un lien (source d'un tarif, site d'un établissement), le site consulté reçoit votre adresse IP selon sa propre politique.</li>
</ul>

<h2>5. Mesure d'audience, publicité, traceurs</h2>
<p>Aloi ne contient aucun outil de mesure d'audience, aucune publicité, aucun traceur et aucun kit tiers de collecte. Si vous avez accepté dans iOS de partager vos analyses avec les développeurs, Apple peut transmettre à IE DIGITAL des rapports de plantage et des statistiques non nominatives ; vous pouvez modifier ce choix dans <i>Réglages › Confidentialité et sécurité › Analyse et améliorations</i>.</p>

<h2>6. Sécurité et sauvegarde</h2>
<p>Les données d'Aloi bénéficient de la protection des données d'iOS : elles sont chiffrées sur l'iPhone. Sans synchronisation iCloud ni export, si vous perdez ou changez d'iPhone, vos données sont perdues.</p>

<h2>7. Export, import, effacement</h2>
<ul>
<li><b>Export</b> : vos données dans un fichier lisible (.json) ou chiffré (.aloi) avec un mot de passe que vous choisissez. IE DIGITAL ne connaît pas ce mot de passe et ne peut pas le récupérer.</li>
<li><b>Import</b> : le fichier se réimporte dans Aloi.</li>
<li><b>Effacement</b> : supprimer un élément dans l'app l'efface ; <i>Réglages › Effacer toutes mes données</i> remet Aloi dans l'état d'une première installation (profil, contrats, biens, objectifs, relevés, documents joints, préférences et ventes téléchargées) ; désinstaller l'app efface aussi toutes ses données sur l'iPhone. Les données synchronisées se suppriment aussi de votre iCloud depuis <i>Réglages › [votre nom] › iCloud › Gérer le stockage</i>.</li>
</ul>

<h2>8. Durée de conservation</h2>
<ul>
<li>Les données d'Aloi sont conservées sur votre iPhone, et dans votre iCloud si vous l'avez choisi, jusqu'à ce que vous les effaciez.</li>
<li>Les courriels échangés avec IE DIGITAL sont conservés au plus 3 ans après le dernier échange.</li>
</ul>

<h2>9. Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, de portabilité et d'opposition. Vous pouvez aussi définir des directives sur le sort de vos données après votre décès. Comme IE DIGITAL ne détient aucune de vos données d'Aloi, vous exercez ces droits directement dans l'app (modification, export, suppression). Pour toute autre demande, écrivez à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a> ; une réponse vous sera apportée sous un mois.</p>
<p>Vous pouvez introduire une réclamation auprès de la CNIL, 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 (<a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

<h2>10. Décision automatisée</h2>
<p>Les notes, rangs et classements d'Aloi sont des calculs faits sur votre iPhone (voir la <a href="aloi-methode.html">méthode</a>). Ils n'entraînent aucune décision produisant des effets juridiques à votre égard ou vous affectant de manière significative, au sens de l'article 22 du RGPD.</p>

<h2>11. Transferts hors de l'Union européenne</h2>
<p>IE DIGITAL ne transfère aucune de vos données d'Aloi. Le téléchargement facultatif des ventes comparables s'adresse à data.gouv.fr (État français), dont les fichiers sont servis depuis un hébergeur situé dans l'Union européenne. Les services d'Apple (iCloud, achats) relèvent de la politique de confidentialité d'Apple.</p>

<h2>12. Ce qu'est Aloi</h2>
""" + ALOI_NATURE + """

<h2>13. Évolution de cette politique</h2>
<p>Toute modification importante vous sera signalée dans l'app avant de s'appliquer, en particulier avant l'ajout de toute nouvelle fonction qui se connecterait à Internet. La seule fonction qui se connecte aujourd'hui, à votre demande, est le téléchargement des ventes comparables décrit au point 4. La date de version figure en tête de cette page.</p>
""" + ALOI_EDITEUR, "Politique de confidentialité de l'app iOS Aloi : aucune donnée envoyée à l'éditeur, aucun compte, aucune connexion bancaire.")

ALOI_BODIES["aloi-conditions.html"] = ("""
<p class="eyebrow"><a href="aloi.html">Aloi</a></p>
<h1>Conditions d'utilisation</h1>
<p class="lede">Aloi, application iOS · version du 8 octobre 2026</p>

<h2>1. Objet</h2>
<p>Les présentes conditions régissent l'utilisation de l'application iOS Aloi, éditée par IE DIGITAL (voir les mentions en bas de page). Elles complètent le contrat de licence standard d'Apple pour les applications (« Licensed Application End User License Agreement »), qui s'applique à Aloi.</p>

<h2>2. Ce qu'est Aloi, et ce qu'il n'est pas</h2>
""" + ALOI_NATURE + """
<p>Les classements de contrats du marché sont publics, identiques pour tous et ne tiennent pas compte de votre situation, de vos objectifs ni de votre profil. Les marques citées le sont à titre d'identification, sans partenariat ni rémunération.</p>

<h2>3. Vos données et vos saisies</h2>
<p>Les calculs reposent sur les informations que vous saisissez. Vous êtes responsable de leur exactitude. Vos données restent sur votre iPhone (voir la <a href="aloi-confidentialite.html">politique de confidentialité</a>).</p>

<h2>4. Données de référence</h2>
<p>Le catalogue de contrats, les frais, la solidité des assureurs et les autres données de référence proviennent de sources publiques (documents d'information des établissements, annexes tarifaires, rapports réglementaires). Chaque donnée est datée et sourcée dans l'app. Le catalogue n'est pas exhaustif. Malgré le soin apporté, une donnée peut être erronée ou dépassée : vérifiez-la auprès de l'établissement avant toute décision, et <a href="aloi-assistance.html#signaler">signalez-nous toute erreur</a>.</p>

<h2>5. Simulations et projections</h2>
<p>Les projections de frais, de capital, de valeur immobilière ou de trésorerie reposent sur des hypothèses affichées à l'écran. Elles ne constituent ni une prévision ni une promesse. Les performances passées ne préjugent pas des performances futures.</p>

<h2>6. Aloi Plus</h2>
<p>Aloi Plus est un achat intégré unique, sans abonnement, vendu et facturé par Apple. Il débloque des fonctions de suivi (historique, univers société, immobilier complet, import illimité, export, mode discret). Le diagnostic, les notes, les frais, le catalogue et les comparaisons restent gratuits pour tous. Le prix est affiché dans l'app avant l'achat. L'achat se restaure depuis <i>Réglages › Aloi Plus › Restaurer</i>. Les demandes de remboursement se font auprès d'Apple, selon ses conditions.</p>

<h2>7. Responsabilité</h2>
<p>IE DIGITAL met en œuvre les moyens raisonnables pour fournir des calculs exacts et des données à jour. Dans les limites autorisées par la loi, IE DIGITAL ne saurait être tenue responsable des décisions prises sur la base d'Aloi, ni des conséquences d'une donnée saisie inexacte. Rien dans ces conditions ne limite les droits que vous tenez du code de la consommation.</p>

<h2>8. Propriété intellectuelle</h2>
<p>L'application, sa méthode de notation et ses contenus sont la propriété d'IE DIGITAL. Les noms de produits et d'établissements cités appartiennent à leurs titulaires.</p>

<h2>9. Évolution et droit applicable</h2>
<p>Ces conditions peuvent évoluer ; toute modification importante sera signalée dans l'app. Elles sont soumises au droit français. En cas de litige, vous pouvez recourir gratuitement à un médiateur de la consommation ou à la plateforme européenne de règlement en ligne des litiges ; à défaut d'accord, les tribunaux compétents sont ceux prévus par la loi.</p>
""" + ALOI_EDITEUR, "Conditions d'utilisation de l'app iOS Aloi : outil de calcul et de comparaison, sans conseil, données de référence datées et sourcées.")

ALOI_BODIES["aloi-assistance.html"] = ("""
<p class="eyebrow"><a href="aloi.html">Aloi</a></p>
<h1>Assistance</h1>
<p class="lede">Aloi, application iOS · IE DIGITAL</p>

<p class="note"><b>Nous écrire : <a href="mailto:contact@iedigital.fr?subject=Aloi%20%E2%80%94%20assistance">contact@iedigital.fr</a></b><br>
Réponse sous 3 jours ouvrés. Indiquez le modèle de votre iPhone, la version d'iOS et celle d'Aloi. N'envoyez jamais vos montants, vos relevés ni vos numéros de contrat.</p>

<section id="signaler">
<h2>Signaler une donnée erronée</h2>
<p>Un frais, une date ou une caractéristique d'un contrat du catalogue vous paraît faux ? Écrivez à <a href="mailto:contact@iedigital.fr?subject=Aloi%20%E2%80%94%20donn%C3%A9e%20%C3%A0%20corriger">contact@iedigital.fr</a> avec le nom du contrat, la donnée concernée et, si possible, le lien vers le document officiel (DIC, notice, annexe tarifaire). Chaque signalement est vérifié sur la source primaire ; la correction est intégrée à la mise à jour suivante du catalogue et datée. Les établissements cités peuvent utiliser la même adresse.</p>
</section>

<section class="faq">
<h2>Questions fréquentes</h2>

<details>
<summary>Faut-il un compte ou connecter ma banque ?</summary>
<p>Non. Aloi fonctionne sans compte et sans connexion bancaire : vous saisissez vos contrats, ou vous importez un relevé PDF lu sur l'iPhone. Détails dans la <a href="aloi-confidentialite.html">politique de confidentialité</a>.</p>
</details>

<details>
<summary>Comment est calculée la note d'un contrat ?</summary>
<p>Par un barème public, le même pour tout le monde : frais tout compris, solidité de l'assureur, liquidité, fonds en euros, offre d'investissement et garanties, avec les critères de performance quand des données publiées existent. Les classements se lisent sous quatre angles, choisis librement. Voir la <a href="aloi-methode.html">méthode</a>.</p>
</details>

<details>
<summary>Aloi me dit-il quel contrat ouvrir ?</summary>
<p>Non. Aloi montre comment votre contrat se situe et quels contrats du marché sont mieux classés selon un barème identique pour tous. Ce n'est pas un conseil : avant toute décision, informez-vous auprès d'un professionnel habilité.</p>
</details>

<details>
<summary>Comment passer à un nouvel iPhone ?</summary>
<p>Activez la synchronisation iCloud dans <i>Réglages</i>, ou exportez vos données (fichier chiffré .aloi) sur l'ancien iPhone et importez-les sur le nouveau avec le même mot de passe.</p>
</details>

<details>
<summary>J'ai acheté Aloi Plus, il n'apparaît pas.</summary>
<p>Ouvrez <i>Réglages › Aloi Plus › Restaurer</i> avec le même compte Apple que lors de l'achat.</p>
</details>

<details>
<summary>D'où viennent les valeurs immobilières ?</summary>
<p>Des statistiques publiques des valeurs foncières (DVF, DGFiP) agrégées par commune, et de la carte des loyers (ANIL). Ce sont des estimations indicatives, qui ne remplacent pas l'avis d'un professionnel. DVF ne couvre ni l'Alsace, ni la Moselle, ni Mayotte.</p>
</details>
</section>
""", "Assistance de l'app iOS Aloi : questions fréquentes, contact et signalement d'une donnée erronée du catalogue.")

ALOI_BODIES["aloi-methode.html"] = ("""
<p class="eyebrow"><a href="aloi.html">Aloi</a></p>
<h1>Méthode de la note et du classement</h1>
<p class="lede">Version de l'algorithme 1.3 · catalogue 2026-10 · page du 8 octobre 2026</p>

<div class="note" style="margin-bottom:32px">
<p style="margin:0"><b>En bref.</b> Les classements des contrats du marché sont les mêmes pour tous : ils ne dépendent ni de votre profil, ni de vos objectifs, ni de votre situation. Aucun établissement ne paie pour y figurer ou pour être mieux classé. Le catalogue (175 contrats au 5 octobre 2026) n'est pas exhaustif.</p>
</div>

<h2>1. Ce qui est comparé</h2>
<p>Un contrat n'est classé qu'avec des contrats de la même enveloppe (assurance vie, PER, PEA, compte-titres, contrat de capitalisation). Les classements portent sur la gestion libre. Un champ « Montant à placer », vide par défaut, retire les contrats dont le versement minimal dépasse le montant que vous tapez ; rien n'y est prérempli depuis vos encours.</p>

<h2>2. La note d'un contrat : critères et poids</h2>
<table>
<thead><tr><th>Critère</th><th>Donnée</th><th>Poids</th><th>État au catalogue</th></tr></thead>
<tbody>
<tr><td>Frais tout compris</td><td>Frais annuels du contrat, du mode de gestion et des supports, publiés par l'établissement</td><td>35</td><td>mesuré</td></tr>
<tr><td>Solidité de l'assureur</td><td>Ratio de solvabilité publié dans le rapport SFCR</td><td>15</td><td>mesuré (107 contrats)</td></tr>
<tr><td>Liquidité de l'enveloppe</td><td>Règles de retrait de l'enveloppe</td><td>10</td><td>mesuré, identique dans une même enveloppe</td></tr>
<tr><td>Fonds en euros</td><td>Moyenne des taux servis sur les 5 derniers exercices publiés (3 au minimum)</td><td>10</td><td>mesuré (105 contrats)</td></tr>
<tr><td>Offre d'investissement</td><td>Nombre d'unités de compte, nombre d'ETF, gestion pilotée proposée</td><td>10</td><td>mesuré (78 contrats)</td></tr>
<tr><td>Garanties</td><td>Plancher décès (assurance vie, capitalisation) ; options de sortie (PER)</td><td>5</td><td>mesuré (63 contrats)</td></tr>
<tr><td>Performance</td><td>Performance annuelle publiée sur 5 ans, sinon 3 ans, sinon 1 an</td><td>7</td><td>non mesuré : aucune donnée publiée au catalogue</td></tr>
<tr><td>Volatilité et pertes passées</td><td>Volatilité et perte maximale publiées</td><td>4</td><td>non mesuré</td></tr>
<tr><td>Risque / performance</td><td>Performance annuelle ÷ volatilité</td><td>4</td><td>non mesuré</td></tr>
</tbody>
</table>
<p>Un critère sans donnée, ou sans objet pour l'enveloppe (fonds en euros et garanties pour un PEA ou un compte-titres), n'est jamais remplacé par une valeur inventée : il est retiré et son poids est redistribué sur les critères mesurés. Aujourd'hui, pour un contrat d'assurance vie dont toutes les données sont publiées, les poids effectifs sont : frais 41 %, solidité 18 %, liquidité 12 %, fonds en euros 12 %, offre 12 %, garanties 6 %.</p>

<h2>3. Les barèmes</h2>
<ul>
<li><b>Frais</b> : 100 à 0 % de frais ; puis une courbe par paliers. Assurance vie, PER et capitalisation : 88 à 0,80 %, 78 à 1,30 %, 66 à 1,70 %, 54 à 2,10 %, 42 à 2,60 %, 15 à 3,90 %. PEA et compte-titres : 88 à 0,30 %, 78 à 0,60 %, 66 à 1,20 %, 54 à 1,70 %, 42 à 2,20 %, 15 à 3,30 %. Entre deux paliers, la note est interpolée ; au-delà du dernier, 10.</li>
<li><b>Solidité</b> : ratio de solvabilité de 220 % ou plus : 90 ; de 180 % : 78 ; de 150 % : 62 ; en dessous : 45.</li>
<li><b>Liquidité</b> : compte-titres 90 ; assurance vie et capitalisation 80 ; PEA 75 ; PER 35.</li>
<li><b>Fonds en euros</b> : moyenne de 2,5 % ou plus : 85 ; de 2 % : 70 ; de 1,5 % : 55 ; en dessous : 40.</li>
<li><b>Offre d'investissement</b> (somme, 90 au plus) : unités de compte, 500 ou plus : 40 ; 200 : 30 ; 100 : 20 ; moins : 10. ETF, 50 ou plus : 30 ; 20 : 22 ; 5 : 12 ; moins : 0. Gestion pilotée proposée : 20.</li>
<li><b>Garanties</b> : plancher décès inclus 85, en option 65, absent 35. PER : sortie en capital et en rente 85, une seule des deux 65.</li>
<li><b>Performance</b> (quand elle sera publiée) : 7 % et plus par an : 90 ; 5 % : 78 ; 3 % : 65 ; 1 % : 50 ; 0 % : 40 ; en dessous : 25.</li>
<li><b>Volatilité</b> : 5 % ou moins : 90 ; 10 % : 75 ; 15 % : 60 ; 20 % : 45 ; au-delà : 30. <b>Perte maximale</b> : 10 % ou moins : 90 ; 20 % : 70 ; 30 % : 50 ; au-delà : 30.</li>
<li><b>Risque / performance</b> : 0,8 et plus : 90 ; 0,5 : 75 ; 0,3 : 60 ; 0,1 : 45 ; en dessous : 30.</li>
</ul>

<h2>4. Quatre angles de lecture</h2>
<p>Les classements du marché se lisent sous quatre angles, affichés côte à côte et choisis librement. Aucun n'est présélectionné à partir de votre profil ; à l'ouverture, l'angle « Équilibre » est actif pour tout le monde. La liquidité n'y figure pas, puisqu'elle ne départage pas deux contrats d'une même enveloppe.</p>
<table>
<thead><tr><th>Angle</th><th>Pondération</th></tr></thead>
<tbody>
<tr><td>Sécurité</td><td>solidité 35, fonds en euros 25, garanties 20, frais 20</td></tr>
<tr><td>Équilibre</td><td>frais 45, solidité 15, fonds en euros 15, offre 15, garanties 10</td></tr>
<tr><td>Frais</td><td>frais 85, solidité 15</td></tr>
<tr><td>Choix d'investissement</td><td>offre 50, frais des supports 35, solidité 15</td></tr>
</tbody>
</table>
<p><b>Frais des supports</b> (angle Choix d'investissement seulement) : 0,25 % ou moins : 90 ; 0,40 % : 75 ; 0,55 % : 60 ; 0,70 % : 45 ; au-delà : 30. Pour un PEA ou un compte-titres, où presque seuls les frais sont publiés, les quatre angles donnent un ordre proche ; l'app le signale.</p>

<h2>5. Comparer deux contrats</h2>
<p>L'outil s'ouvre sur deux cases vides : vous choisissez les deux contrats, parmi les vôtres ou dans le catalogue présenté par ordre alphabétique. Aloi affiche les données et les notes critère par critère, sans désigner de gagnant.</p>

<h2>6. Des notes aux lettres</h2>
<p>S : 85 et plus · A : 75 · B : 62 · C : 50 · D : 38 · E : en dessous. Les lettres résument la note ; elles ne sont pas un avis sur votre situation.</p>

<h2>7. Ce qui n'entre pas dans les classements</h2>
<ul>
<li><b>Votre profil</b> (horizon, tolérance au risque, objectifs) : jamais utilisé pour classer les contrats du marché.</li>
<li><b>Vos supports</b> : la diversification dépend des supports que vous choisissez, pas du contrat ; elle est montrée sur votre contrat, pas comparée.</li>
<li><b>Toute rémunération</b> : Aloi n'en perçoit aucune.</li>
</ul>

<h2>8. Valeur de marché d'un bien immobilier</h2>
<p>L'estimation indicative multiplie le prix médian au m² des ventes de la commune (24 derniers mois ou 5 ans, maisons ou appartements) par la surface du bien, avec la fourchette entre le premier et le troisième quartile. Avec 30 ventes ou plus, le chiffre est affiché ; de 10 à 29, il porte la mention « fiabilité faible » ; sous 10, Aloi passe à l'intercommunalité puis au département et le dit. Les cellules de moins de 5 ventes ne sont jamais publiées. Pour un immeuble, chaque lot est estimé à la médiane de sa typologie, puis les lots sont additionnés. Aucun rendement n'est calculé pour une résidence principale. Sources : demandes de valeurs foncières géolocalisées (Etalab, DGFiP), hors ventes en l'état futur d'achèvement, hors Alsace, Moselle et Mayotte ; loyers : estimations ANIL, à partir des données du Groupe SeLoger et de leboncoin.</p>

<h2>9. Sources et mises à jour</h2>
<p>Documents d'information clés et notices des contrats, annexes tarifaires, rapports SFCR des assureurs, taux servis publiés par les assureurs. Chaque donnée affiche dans l'app sa source, sa date de référence et sa date d'intégration. Une donnée de plus de douze mois est signalée comme datée. <a href="aloi-assistance.html#signaler">Signaler une donnée erronée</a>.</p>
""" + ALOI_EDITEUR, "Méthode publique de notation et de classement des contrats dans l'app Aloi : critères, poids, barèmes, sources.")
