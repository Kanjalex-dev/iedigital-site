#!/usr/bin/env python3
"""Génère le site d'IE DIGITAL. Un gabarit, sept pages, aucune duplication."""
import pathlib

OUT = pathlib.Path(__file__).parent
DOMAIN = "iedigital.fr"
MAIL = "contact@iedigital.fr"

PAGES = [
    ("index.html", "Accueil"),
    ("expertises.html", "Conseil produit"),
    ("applications.html", "Applications"),
    ("forge.html", "Forge Yourself"),
    ("methode.html", "Méthode"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
    ("mentions-legales.html", "Mentions légales"),
    ("forge-confidentialite.html", "Forge — Confidentialité"),
    ("forge-assistance.html", "Forge — Assistance"),
]

HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://{domain}/{slug}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<link rel="stylesheet" href="assets/style.css">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="icon" href="assets/favicon-32.png" sizes="32x32">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
</head>
<body>
<div class="shell">
<header class="rail">
  <a class="wordmark" href="index.html" aria-label="IE DIGITAL, accueil">
    <svg class="mark" viewBox="0 0 32 32" aria-hidden="true" focusable="false">
      <rect x="4"  y="4"    width="4" height="24" fill="currentColor"></rect>
      <rect x="11" y="7"    width="4" height="18" fill="currentColor"></rect>
      <rect x="18" y="10.5" width="4" height="11" fill="currentColor"></rect>
      <rect x="25" y="13.5" width="3" height="5"  fill="var(--accent)"></rect>
    </svg>
    <span>IE DIGITAL</span>
  </a>
  <nav aria-label="Navigation principale">
{nav}
  </nav>
  <div class="rail-foot">
    <p>Conseil produit<br>Applications mobiles</p>
    <p>Lille<br>{mail}</p>
  </div>
</header>
<main>
<article class="page">
"""

FOOT = """
<footer class="foot">
  <p class="legal">IE DIGITAL, SARL &middot; SIREN 822&nbsp;744&nbsp;116</p>
  <p><a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a> &middot; <a href="mentions-legales.html">Mentions légales</a></p>
</footer>
</article>
</main>
</div>
</body>
</html>
"""


def nav_for(current: str) -> str:
    out = []
    for slug, label in PAGES:
        if slug in ("index.html", "mentions-legales.html", "forge-confidentialite.html",
                    "forge-assistance.html"):
            continue
        # Les pages Forge allument l'entrée « Forge Yourself » de la navigation.
        actif = current if not current.startswith("forge-") else "forge.html"
        cur = ' aria-current="page"' if slug == actif else ""
        out.append(f'    <a href="{slug}"{cur}>{label}</a>')
    return "\n".join(out)


def render(slug: str, title: str, desc: str, body: str) -> str:
    head = HEAD.format(title=title, desc=desc, domain=DOMAIN,
                       slug="" if slug == "index.html" else slug,
                       nav=nav_for(slug), mail=MAIL)
    return head + body.strip() + "\n" + FOOT


BODIES = {}

# ------------------------------------------------------------------ accueil
BODIES["index.html"] = ("""
<p class="eyebrow">IE DIGITAL &middot; Lille &middot; depuis 2016</p>
<h1>Conseil produit.<br>Développement d'applications mobiles.</h1>
<p class="lede">Deux métiers qui se tiennent&nbsp;: décider quoi construire, puis le
construire. Celui qui vous répond est celui qui fait le travail.</p>

<ul class="index">
  <li><a href="#conseil">
    <span class="t">Conseil produit</span>
    <span class="d">Parcours d'achat e-commerce&nbsp;: panier, checkout, paiement, retours, marketplace</span>
  </a></li>
  <li><a href="#applications">
    <span class="t">Développement d'applications mobiles</span>
    <span class="d">iOS natif en Swift et SwiftUI, de la maquette à l'App Store</span>
  </a></li>
</ul>

<p><a class="cta" href="contact.html">Parler d'un projet</a></p>

<section id="conseil">
  <h2>Conseil produit</h2>
  <p>J'interviens là où se joue la conversion&nbsp;: panier, checkout, paiement, retours,
  marketplace. Un taux de conversion se déplace rarement par un redesign, souvent par
  une contrainte levée au bon endroit — un moyen de paiement absent, une
  authentification forte mal posée, une adresse qu'on demande deux fois.</p>
  <div class="stack">
    <div class="entry">
      <span class="kicker">Cadrage</span>
      <h3>Un diagnostic, en deux à quatre semaines</h3>
      <p>Lecture des données d'entonnoir, entretiens avec les équipes, revue du parcours
      réel sur mobile et desktop. Livrable&nbsp;: ce qu'il faut traiter d'abord, et
      pourquoi.</p>
    </div>
    <div class="entry">
      <span class="kicker">Renfort produit</span>
      <h3>Un PM senior dans votre équipe, à temps partagé</h3>
      <p>Je tiens le backlog d'un domaine — checkout, paiement, retours — je rédige
      les spécifications, j'arbitre avec la tech et je suis la mise en production.
      Deux à trois jours par semaine, sur plusieurs mois.</p>
    </div>
  </div>
  <p><a class="more" href="expertises.html">Checkout, paiement, retours&nbsp;: le détail</a></p>
</section>

<section id="applications">
  <h2>Développement d'applications mobiles</h2>
  <p>IE DIGITAL conçoit, développe et publie des applications iOS natives. Je prends le
  projet de l'idée à l'App Store, pour un produit neuf ou quand vous n'avez pas d'équipe
  mobile à mobiliser. Je développe aussi des applications web quand le besoin s'y
  prête.</p>
  <dl class="facts">
    <div><dt>Cadrage et maquettes</dt><dd>Public visé, périmètre de la première version,
    modèle économique. Maquettes validées avant la première ligne de code.</dd></div>
    <div><dt>Développement</dt><dd>iOS natif, en Swift et SwiftUI.</dd></div>
    <div><dt>Achats intégrés</dt><dd>Abonnements et achats in-app avec StoreKit, écrans
    d'abonnement conformes aux règles d'Apple.</dd></div>
    <div><dt>Conformité</dt><dd>Directives de l'App Store, RGPD, politique de
    confidentialité et étiquette de confidentialité de la fiche App Store.</dd></div>
    <div><dt>Publication</dt><dd>Fiche App Store, soumission, échanges avec l'équipe de
    revue d'Apple.</dd></div>
    <div><dt>Maintenance</dt><dd>Mises à jour pour les nouvelles versions d'iOS,
    corrections, évolutions.</dd></div>
  </dl>
  <p class="note">Application en cours de développement&nbsp;:
  <strong>Forge Yourself</strong>, application iOS de musculation, écrite en SwiftUI,
  avec abonnement intégré, liaison avec l'app Santé et aucune donnée collectée. Elle
  n'est pas encore publiée&nbsp;; elle le sera par IE DIGITAL.</p>
  <p><a class="more" href="applications.html">Le détail de l'offre</a></p>
</section>

<section>
  <h2>Ce que ce n'est pas</h2>
  <p class="note">Ni une agence créative, ni une ESN qui facture des jours-hommes. Pas
  de refonte vendue avant le diagnostic, pas d'application chiffrée avant d'avoir été
  cadrée, pas d'équipe junior placée sous un nom senior. Si le problème que vous
  décrivez ne relève pas de mon domaine, je vous le dis et je m'arrête là.</p>
</section>
""", "Conseil produit sur les parcours d'achat et développement d'applications mobiles iOS, de la maquette à l'App Store.")

# --------------------------------------------------------------- expertises
BODIES["expertises.html"] = ("""
<p class="eyebrow">Conseil produit</p>
<h1>Le parcours d'achat, bout en bout</h1>
<p class="lede">Le cœur du métier est là&nbsp;: tout ce qui se passe entre le moment où
un client décide d'acheter et celui où la commande est livrée, payée et parfois
retournée.</p>

<section>
  <h2>Checkout et parcours d'achat</h2>
  <p>Identification et parcours invité, saisie et validation d'adresse, choix du mode
  de livraison, récapitulatif, confirmation. Chaque étape ajoutée coûte des clients&nbsp;;
  chaque étape retirée sans précaution coûte des commandes en erreur. L'arbitrage se
  fait sur les données, pas sur l'avis du dernier qui a parlé.</p>
  <ul class="plain">
    <li>Réduction du nombre d'étapes et des champs de saisie</li>
    <li>Parcours invité, création de compte différée, connexion sociale</li>
    <li>Gestion des erreurs&nbsp;: ce que le client lit quand ça échoue</li>
    <li>Parcours mobile, où se joue l'essentiel du décrochage</li>
  </ul>
</section>

<section>
  <h2>Paiement</h2>
  <p>Un moyen de paiement manquant est une commande perdue, et une authentification
  forte mal intégrée est un tunnel qui se vide au dernier écran. Le sujet est autant
  réglementaire que produit&nbsp;: DSP2, 3-D Secure, exemptions, taux d'acceptation
  bancaire.</p>
  <ul class="plain">
    <li>Choix et priorisation des moyens de paiement selon le panier et le marché</li>
    <li>Authentification forte&nbsp;: friction réelle contre taux de fraude</li>
    <li>Paiement en plusieurs fois, portefeuilles, paiement en un clic</li>
    <li>Analyse des échecs d'autorisation et des relances</li>
  </ul>
</section>

<section>
  <h2>Panier et pré-checkout</h2>
  <p>Le panier est l'endroit où le client compte. Frais de port affichés trop tard,
  disponibilité incertaine, code promo qui ne s'applique pas&nbsp;: ce sont des sorties
  de tunnel qu'on impute souvent, à tort, au checkout.</p>
</section>

<section>
  <h2>Retours et après-vente</h2>
  <p>La politique de retour se décide avant l'achat et s'exécute après. Un parcours de
  retour lisible fait vendre en amont&nbsp;; un parcours opaque génère des contacts au
  service client, qui coûtent plus cher que le retour lui-même.</p>
</section>

<section>
  <h2>Marketplace</h2>
  <p>Ouvrir sa marketplace, c'est accepter que le parcours d'achat ne soit plus
  entièrement sous son contrôle&nbsp;: délais hétérogènes, paniers multi-vendeurs,
  retours éclatés, paiement à reverser. Les arbitrages produit changent de nature.</p>
</section>

<section>
  <h2>Hors e-commerce</h2>
  <p>La conception d'applications et de produits digitaux, le conseil et l'assistance
  en systèmes informatiques relèvent du même objet social et des mêmes méthodes. Les
  parcours d'achat sont le terrain que je connais le mieux, pas le seul sur lequel
  j'interviens.</p>
</section>
""", "Checkout, paiement, panier, retours et marketplace : les domaines d'intervention d'IE DIGITAL sur les parcours d'achat.")

# ------------------------------------------------------------- applications
BODIES["applications.html"] = ("""
<p class="eyebrow">Applications mobiles</p>
<h1>Développement d'applications iOS</h1>
<p class="lede">IE DIGITAL conçoit, développe et publie des applications iOS natives,
de la première maquette à la fiche App Store, puis les maintient.</p>

<section>
  <h2>Ce qui est livré</h2>
  <dl class="facts">
    <div><dt>Cadrage et maquettes</dt><dd>Public visé, périmètre de la première version,
    modèle économique. Maquettes validées avant la première ligne de code.</dd></div>
    <div><dt>Développement</dt><dd>iOS natif, en Swift et SwiftUI. Applications web quand
    le besoin s'y prête.</dd></div>
    <div><dt>Achats intégrés</dt><dd>Abonnements et achats in-app avec StoreKit, écrans
    d'abonnement conformes aux règles d'Apple.</dd></div>
    <div><dt>Conformité</dt><dd>Directives de l'App Store, RGPD, politique de
    confidentialité et étiquette de confidentialité de la fiche App Store.</dd></div>
    <div><dt>Publication</dt><dd>Fiche App Store, soumission, échanges avec l'équipe de
    revue d'Apple.</dd></div>
    <div><dt>Maintenance</dt><dd>Mises à jour pour les nouvelles versions d'iOS,
    corrections, évolutions.</dd></div>
  </dl>
</section>

<section>
  <h2>En cours de développement</h2>
  <p>Forge Yourself, application iOS de musculation&nbsp;: séances, charges et
  mensurations, liaison avec l'app Santé, abonnement intégré. Écrite en SwiftUI, sans
  compte ni collecte de données. Elle n'est pas encore publiée&nbsp;; elle le sera par
  IE DIGITAL.</p>
  <p><a class="more" href="forge.html">Forge Yourself : présentation, assistance, confidentialité</a></p>
</section>

<section>
  <h2>Pour démarrer</h2>
  <p>Décrivez l'idée, le public visé et l'échéance. Je vous dis si le projet est pour
  moi, et ce que coûterait une première version, une fois le périmètre établi.</p>
  <p><a class="cta" href="contact.html">Parler d'un projet</a></p>
</section>
""", "IE DIGITAL conçoit, développe et publie des applications iOS natives en Swift et SwiftUI : maquettes, achats intégrés, conformité App Store et RGPD, publication, maintenance.")

# ------------------------------------------------------------------ méthode
BODIES["methode.html"] = ("""
<p class="eyebrow">Méthode</p>
<h1>Établir avant de construire</h1>
<p class="lede">Quatre temps. Ils s'enchaînent dans cet ordre parce que chacun rend le
suivant décidable — c'est la seule raison pour laquelle ils sont numérotés.</p>

<ol class="steps">
  <li>
    <h3>Établir</h3>
    <p>Lire les données d'entonnoir telles qu'elles sont, refaire le parcours moi-même
    sur un vrai téléphone, écouter les équipes qui reçoivent les réclamations. On
    cherche l'endroit où les gens s'arrêtent, pas l'endroit où l'interface déplaît.</p>
    <p class="out">Sortie&nbsp;: les points de décrochage, chiffrés et classés.</p>
  </li>
  <li>
    <h3>Trancher</h3>
    <p>Tout ne se traite pas. On retient ce qui a un effet mesurable et un coût connu,
    on écarte le reste en écrivant pourquoi — c'est ce qui évite de se le voir
    represcrire six mois plus tard.</p>
    <p class="out">Sortie&nbsp;: une liste courte, ordonnée, avec l'effet attendu et
    ce qui a été écarté.</p>
  </li>
  <li>
    <h3>Spécifier</h3>
    <p>Des spécifications qu'une équipe de développement peut exécuter sans revenir
    poser trois questions&nbsp;: règles de gestion, cas limites, états d'erreur, et des
    critères d'acceptation vérifiables un par un.</p>
    <p class="out">Sortie&nbsp;: des spécifications fonctionnelles et des critères
    d'acceptation.</p>
  </li>
  <li>
    <h3>Livrer et mesurer</h3>
    <p>Je reste jusqu'à la production. Ce qui n'est pas mesuré après coup n'a pas
    été livré&nbsp;: on regarde si le point de décrochage s'est déplacé, et on
    accepte le verdict, y compris quand il est négatif.</p>
    <p class="out">Sortie&nbsp;: la mise en production, et l'écart entre l'effet
    attendu et l'effet constaté.</p>
  </li>
</ol>

<section>
  <h2>Comment je travaille au quotidien</h2>
  <ul class="plain">
    <li>Dans vos outils et vos rituels, pas dans un dispositif parallèle.</li>
    <li>Par écrit&nbsp;: une décision qui n'est pas écrite n'a pas été prise.</li>
    <li>En désaccord quand il le faut. Vous ne me payez pas pour valider un plan.</li>
    <li>Sans rétention&nbsp;: ce que je produis reste chez vous, exploitable sans moi.</li>
  </ul>
</section>
""", "Quatre temps — établir, trancher, spécifier, livrer et mesurer — et ce que chacun produit.")

# --------------------------------------------------------------- références
# ---------------------------------------------------------------- à propos
BODIES["a-propos.html"] = ("""
<p class="eyebrow">À propos</p>
<h1>Ingénieur de formation, product manager de métier</h1>
<p class="lede">IE DIGITAL est une société de conseil et de conception de produits
digitaux, immatriculée au RCS de Lille Métropole depuis 2016. Une personne, pas une
structure&nbsp;: celle qui vous répond est celle qui fait le travail.</p>

<p>Je suis ingénieur en génie logiciel de formation. J'ai commencé côté société de
services informatiques, sur des projets pour de grands comptes. J'interviens aujourd'hui
en mission longue, intégré aux équipes d'un annonceur — là où l'on ne livre pas un projet
avant de partir, mais où l'on tient un produit dans la durée et où l'on vit avec les
conséquences de ses arbitrages.</p>

<p>C'est aussi la façon dont je travaille le mieux&nbsp;: dans l'équipe, sur un domaine,
avec les mêmes indicateurs que ceux à qui je rends des comptes. Pas en surplomb, pas au
forfait.</p>

<p>Aujourd'hui, mon métier est la conception de produits digitaux&nbsp;: décider quoi
construire, dans quel ordre, et pourquoi. La technique reste le socle — elle me permet
d'arbitrer avec une équipe de développement plutôt que de lui transmettre une demande.</p>

<section>
  <h2>Terrains</h2>
  <p>Distribution spécialisée et bricolage, équipement automobile, financement
  spécialisé, e-commerce généraliste, à des échelles allant du réseau national au
  groupe international. Le point commun&nbsp;: des parcours d'achat à fort volume, où
  un détail de conception se traduit directement en commandes gagnées ou perdues.</p>
  <p class="note">Les missions sont couvertes par des engagements de confidentialité.
  Les noms et les chiffres se discutent en rendez-vous, pas sur une page publique.</p>
</section>

<section>
  <h2>Façon de travailler</h2>
  <p>Produit d'abord, méthode ensuite. Scrum, Kanban, OKR sont des outils&nbsp;: ils
  servent à cadencer, à rendre visible et à aligner, pas à donner l'illusion qu'on
  avance. Je les emploie là où ils apportent quelque chose, et je le dis quand ce
  n'est pas le cas.</p>
  <p>Le principe qui tient l'ensemble&nbsp;: <strong>l'expérience du client décide de la
  conception</strong>, pas l'inverse. Un parcours ne se dessine pas depuis
  l'organigramme de l'entreprise ni depuis les contraintes du back-office — il se
  dessine depuis ce que vit la personne qui essaie d'acheter, et le reste s'y adapte.</p>
</section>

<section>
  <h2>Travaux personnels</h2>
  <p>Je conçois et développe mes propres applications. C'est ce qui me tient à jour sur
  la fabrication plutôt que sur la seule spécification&nbsp;: quand on a soi-même livré
  une application de bout en bout, on estime différemment ce qu'on demande à une
  équipe.</p>
</section>
""", "IE DIGITAL : ingénieur en génie logiciel de formation, product manager spécialisé sur les parcours d'achat.")

# ----------------------------------------------------------------- contact
BODIES["contact.html"] = ("""
<p class="eyebrow">Contact</p>
<h1>Décrivez le chantier, je vous dis s'il est pour moi</h1>
<p class="lede">La réponse la plus utile que je puisse donner est parfois «&nbsp;ce n'est
pas mon domaine&nbsp;». Elle arrive vite, et elle ne coûte rien.</p>

<section>
  <dl class="facts">
    <div><dt>E-mail</dt><dd><a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a></dd></div>
    <div><dt>Zone d'intervention</dt><dd>Lille, Paris, et à distance</dd></div>
  </dl>
</section>

<section>
  <h2>Ce qui aide à répondre vite</h2>
  <ul class="plain">
    <li>Le parcours concerné&nbsp;: panier, checkout, paiement, retours, autre.</li>
    <li>Ce que vous observez, chiffré si vous l'avez&nbsp;: taux de conversion, point de
    sortie, volume de commandes.</li>
    <li>Ce qui a déjà été tenté.</li>
    <li>L'échéance, et qui décide.</li>
  </ul>
  <p><a class="cta" href="mailto:contact@iedigital.fr">Écrire à IE DIGITAL</a></p>
</section>

<section>
  <h2>Modalités</h2>
  <p>Interventions en cadrage court, en renfort produit à temps partagé, ou en
  conception complète. Les conditions tarifaires sont communiquées après le premier
  échange, une fois le périmètre établi — un tarif annoncé avant d'avoir compris le
  problème n'engage personne.</p>
</section>
""", "Contacter IE DIGITAL : e-mail, zone d'intervention et informations utiles pour cadrer une demande.")

# --------------------------------------------------------- mentions légales
BODIES["mentions-legales.html"] = ("""
<p class="eyebrow">Mentions légales</p>
<h1>Mentions légales</h1>
<p class="lede">Informations reprises de l'extrait Kbis délivré par le greffe du
tribunal de commerce de Lille Métropole, à jour au 17 septembre 2026.</p>

<section>
  <h2>Éditeur du site</h2>
  <dl class="facts">
    <div><dt>Raison sociale</dt><dd>IE DIGITAL</dd></div>
    <div><dt>Forme juridique</dt><dd>Société à responsabilité limitée (société à associé unique)</dd></div>
    <div><dt>Siège social</dt><dd>31 rue du Président Kennedy, 59237 Verlinghem, France</dd></div>
    <div><dt>SIREN</dt><dd class="mono">822 744 116</dd></div>
    <div><dt>Identifiant européen (EUID)</dt><dd class="mono">FR5910.822744116</dd></div>
    <div><dt>Date d'immatriculation</dt><dd class="mono">4 octobre 2016</dd></div>
    <div><dt>TVA intracommunautaire</dt><dd class="mono">FR&nbsp;42&nbsp;822&nbsp;744&nbsp;116</dd></div>
    <div><dt>Gérant et directeur de la publication</dt><dd>Alexandre Elard</dd></div>
    <div><dt>Contact</dt><dd><a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a></dd></div>
  </dl>
</section>

<section>
  <h2>Activités déclarées</h2>
  <p>L'activité de consultant en informatique et notamment la planification et la
  conception de systèmes informatiques intégrant les technologies du matériel, des
  logiciels et des communications&nbsp;; le conseil et l'assistance en systèmes et
  logiciels informatiques&nbsp;; et plus généralement le développement informatique,
  consulting informatique, architecture informatique, prestation et conseil en
  informatique, formation professionnelle. La création et le développement d'outils
  informatiques se rapportant aux secteurs de la publicité et de la communication.</p>
</section>

<section>
  <h2>Hébergement</h2>
  <dl class="facts">
    <div><dt>Hébergeur</dt><dd>GitHub, Inc. (service GitHub Pages)</dd></div>
    <div><dt>Adresse</dt><dd>88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis</dd></div>
    <div><dt>Nom de domaine</dt><dd>OVH SAS, 2 rue Kellermann, 59100 Roubaix, France</dd></div>
  </dl>
</section>

<section>
  <h2>Propriété intellectuelle</h2>
  <p>L'ensemble des contenus de ce site — textes, structure, mise en forme — est la
  propriété d'IE DIGITAL, sauf mention contraire. Toute reproduction ou représentation,
  totale ou partielle, sans autorisation écrite préalable est interdite.</p>
</section>

<section>
  <h2>Données personnelles</h2>
  <p>Ce site ne dépose aucun cookie et ne collecte aucune donnée de navigation. Les
  seules données traitées sont celles que vous transmettez volontairement par e-mail,
  utilisées uniquement pour répondre à votre demande et conservées le temps de la
  relation commerciale puis pendant la durée légale applicable.</p>
  <p>Conformément au règlement (UE) 2016/679 et à la loi n°&nbsp;78-17 du 6 janvier
  1978 modifiée, vous disposez d'un droit d'accès, de rectification, d'effacement, de
  limitation, d'opposition et de portabilité sur ces données. Ces droits s'exercent
  auprès de <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Vous pouvez
  introduire une réclamation auprès de la CNIL.</p>
</section>

<section>
  <h2>Limitation de responsabilité</h2>
  <p>IE DIGITAL s'efforce de maintenir ce site exact et à jour, sans garantir
  l'exactitude, l'exhaustivité ni l'actualité des informations qui y figurent. Les
  informations légales ci-dessus reprennent l'extrait Kbis à sa date de délivrance et
  peuvent avoir évolué depuis.</p>
</section>
""", "Informations légales d'IE DIGITAL : éditeur, hébergement, propriété intellectuelle et données personnelles.")

# ---------------------------------------------------------- Forge · section
# Section de l'application Forge Yourself : présentation, assistance,
# confidentialité. Les URL forge-assistance.html et forge-confidentialite.html
# sont déclarées dans App Store Connect : ne jamais les renommer.
BODIES["forge.html"] = ("""
<p class="eyebrow">Application iOS</p>
<h1>Forge Yourself</h1>
<p class="lede">Programme de musculation et suivi de force. Forge construit ton programme
sur ton matériel, ton niveau et tes jours, puis règle la charge de chaque exercice
séance après séance, d'après ce que tu déclares.</p>

<section>
  <h2>En bref</h2>
  <dl class="facts">
    <div><dt>Plateforme</dt><dd>iPhone, iOS 17 et plus. En préparation, pas encore publiée sur l'App Store.</dd></div>
    <div><dt>Compte</dt><dd>Aucun. Pas de serveur Forge, pas de publicité, pas de traceur.</dd></div>
    <div><dt>Données</dt><dd>Enregistrées sur l'iPhone. Export d'une sauvegarde à tout moment.</dd></div>
    <div><dt>Formules</dt><dd>Carnet du jour gratuit ; programme, progression automatique et historique avec l'abonnement.</dd></div>
    <div><dt>Éditeur</dt><dd>IE DIGITAL</dd></div>
  </dl>
</section>

<section>
  <h2>Aide et informations</h2>
  <ul>
    <li><a href="forge-assistance.html">Assistance et questions fréquentes</a></li>
    <li><a href="forge-confidentialite.html">Politique de confidentialité</a></li>
    <li><a href="mailto:contact@iedigital.fr?subject=Forge%20%E2%80%94%20assistance">Nous écrire : contact@iedigital.fr</a></li>
  </ul>
</section>
""", "Forge Yourself, application iOS de musculation éditée par IE DIGITAL : programme, charges qui s'ajustent, suivi. Assistance et confidentialité.")

BODIES["forge-assistance.html"] = ("""
<p class="eyebrow"><a href="forge.html">Forge Yourself</a></p>
<h1>Assistance</h1>
<p class="lede">Forge Yourself, application iOS · IE DIGITAL</p>

<p class="note"><b>Nous écrire : <a href="mailto:contact@iedigital.fr?subject=Forge%20%E2%80%94%20assistance">contact@iedigital.fr</a></b><br>
Réponse sous 3 jours ouvrés. Pour un problème, indique ce que tu faisais, ce qui s'est passé, le modèle de ton iPhone et sa version d'iOS (Réglages › Général › Informations). Une capture d'écran aide beaucoup.</p>

<section class="faq">
<h2>Questions fréquentes</h2>

<details>
<summary>Faut-il créer un compte ?</summary>
<p>Non. Forge fonctionne sans compte et sans serveur : ton programme, tes séances et tes relevés sont enregistrés sur ton iPhone.</p>
</details>

<details>
<summary>Comment sauvegarder mes données, ou les passer sur un nouvel iPhone ?</summary>
<p><i>Profil › Données › Sauvegarder ce profil</i> crée un fichier que tu ranges où tu veux (Fichiers, iCloud Drive, e-mail). Sur le nouvel iPhone, à l'écran « Qui s'entraîne ? », touche <i>Restaurer une sauvegarde</i> et choisis ce fichier : Forge te montre ce qu'il contient avant d'importer. L'import ajoute un profil, il n'en écrase jamais un.</p>
</details>

<details>
<summary>Comment gérer ou résilier mon abonnement ?</summary>
<p>Dans <i>Profil › Abonnement</i>, ou dans les réglages de l'iPhone : <i>Réglages › ton nom › Abonnements › Forge</i>. La résiliation prend effet à la fin de la période en cours ; tu gardes l'accès jusque-là, et ton historique reste consultable ensuite.</p>
</details>

<details>
<summary>J'ai changé d'iPhone et je ne retrouve pas mon achat</summary>
<p>Ouvre l'écran d'abonnement et touche <i>Restaurer mes achats</i>, avec le même identifiant Apple que lors de l'achat. L'abonnement et l'achat à vie sont liés à ton identifiant Apple, pas à l'iPhone.</p>
</details>

<details>
<summary>Comment demander un remboursement ?</summary>
<p>Les paiements passent par Apple, qui seul peut rembourser : <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>, puis « Demander un remboursement ». Nous ne voyons ni ne gérons tes paiements.</p>
</details>

<details>
<summary>À quoi sert l'app Santé, et comment couper l'accès ?</summary>
<p>Si tu l'actives dans <i>Profil › Données › Santé</i>, Forge lit ton poids, ta taille et tes pas pour éviter une double saisie. Forge n'écrit rien dans Santé, et ces données restent sur ton iPhone. Pour retirer l'accès : <i>Réglages › Santé › Accès aux données et appareils › Forge</i>.</p>
</details>

<details>
<summary>Comment effacer mes données ?</summary>
<p><i>Profil › Données › Supprimer ce profil</i> efface le profil et tout son historique. Supprimer l'application efface toutes ses données de l'iPhone.</p>
</details>

<details>
<summary>Le minuteur ne sonne pas ou ne vibre pas</summary>
<ul>
<li>Vérifie le son et la vibration dans <i>Profil › Programme › Pendant la séance</i>.</li>
<li>Le son de fin suit le bouton silencieux de l'iPhone : en mode silencieux, seule la vibration reste.</li>
<li>Pour être prévenu téléphone verrouillé, autorise les notifications : <i>Réglages › Notifications › Forge</i>.</li>
</ul>
</details>

<details>
<summary>Forge remplace-t-il un avis médical ?</summary>
<p>Non. Les programmes et les repères de nutrition sont des repères d'entraînement, pas un avis médical. En cas de douleur, de blessure, de maladie, de grossesse ou de trouble alimentaire, demande l'avis d'un professionnel de santé avant de t'entraîner.</p>
</details>
</section>

<section>
<h2>Liens utiles</h2>
<ul>
<li><a href="forge-confidentialite.html">Politique de confidentialité</a></li>
<li><a href="mentions-legales.html">Mentions légales</a> — IE DIGITAL, SARL, RCS Lille Métropole 822 744 116</li>
</ul>
</section>
""", "Assistance de Forge Yourself : contact, sauvegarde et changement d'iPhone, abonnement, remboursement, app Santé, suppression des données.")

# --------------------------------------------- Forge · confidentialité
# Page exigée par Apple pour la soumission de l'application Forge Yourself.
# Son URL doit rester stable : elle est déclarée dans App Store Connect, et la
# changer casse la fiche produit.
BODIES["forge-confidentialite.html"] = ("""
<p class="eyebrow">Forge Yourself</p>
<h1>Politique de confidentialité</h1>
<p class="lede">Forge Yourself, application iOS et application web · version du 24 septembre 2026</p>

<p class="note"><b>En bref : nous ne recevons aucune de tes données d'entraînement ni de santé.</b> Il n'y a pas de compte, pas de serveur Forge, pas de publicité, pas de traceur. Ce que tu saisis est traité par l'application sur ton appareil, et y reste.</p>

<section>
<h2>Qui édite l'application</h2>
<p><b>IE DIGITAL</b>, SARL immatriculée au RCS de Lille Métropole sous le numéro 822 744 116. Pour toute question sur cette page ou sur tes données : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>.</p>
</section>
<section>
<h2>Ce que l'application traite, et où</h2>
<ul>
<li><b>Ton programme, tes séances et tes charges</b> : enregistrés dans le stockage de l'application, sur ton appareil.</li>
<li><b>Ton poids, ta taille, ton âge, tes mensurations</b> : même endroit. Ils servent à tracer ta courbe de suivi et, à partir de 18 ans, à calculer des repères alimentaires généraux. Ils ne sont transmis à personne, nous compris.</li>
<li><b>Sur l'app web</b>, tout est gardé dans le stockage de ton navigateur. Vider les données du site les efface.</li>
</ul>
<p>Nous n'avons pas accès à ces données : nous ne pouvons ni les lire, ni les corriger, ni les supprimer à ta place. Tu les gères toi-même dans l'application ; <i>Profil › Supprimer ce profil</i> efface le profil et tout son historique. Supprimer l'application efface aussi ses données de l'appareil.</p>
</section>
<section>
<h2>La sauvegarde</h2>
<p><i>Profil › Sauvegarde</i> crée un fichier que tu ranges où tu veux (Fichiers, iCloud Drive, e-mail…). Il contient ton profil complet, mensurations comprises. Forge ne l'envoie nulle part : c'est toi qui choisis sa destination, et le service que tu choisis applique alors ses propres règles.</p>
</section>
<section>
<h2>L'app Santé (iPhone, facultatif)</h2>
<p>Si tu actives <i>Profil › Santé</i>, Forge lit dans l'app Santé ton <b>poids</b> et ta <b>taille</b>, pour remplir ta courbe de suivi sans double saisie, et ton <b>nombre de pas</b>, pour afficher ta moyenne quotidienne dans l'onglet Suivi. Forge n'écrit rien dans Santé. Les données lues restent sur ton téléphone, ne sont jamais utilisées à des fins publicitaires et ne sont jamais transmises à un tiers. Tu peux retirer l'accès à tout moment dans <i>Réglages › Santé › Accès aux données et appareils › Forge</i>.</p>
</section>
<section>
<h2>Les achats</h2>
<p>Les abonnements et l'achat à vie passent entièrement par Apple, qui en est responsable. Nous ne recevons ni ton nom, ni ton adresse, ni tes moyens de paiement. L'application vérifie sur ton appareil le justificatif signé par Apple pour savoir quelles fonctions ouvrir. La gestion et la résiliation se font dans les réglages de ton compte Apple.</p>
</section>
<section>
<h2>Les statistiques</h2>
<p>Forge n'intègre aucun outil de mesure d'audience. Apple nous fournit, dans son espace développeur, des statistiques agrégées : installations, plantages, abonnements. Les chiffres d'usage et les rapports de plantage ne proviennent que des personnes qui ont accepté, dans les réglages de leur iPhone, de partager leurs données d'analyse avec les développeurs ; ils ne nous permettent pas de t'identifier. L'app web ne mesure rien.</p>
</section>
<section>
<h2>L'hébergement de l'app web et de cette page</h2>
<p>L'app web et cette page sont hébergées par <b>GitHub</b> (GitHub, Inc., filiale de Microsoft, États-Unis). Comme tout hébergeur, GitHub peut enregistrer des données techniques de connexion, dont l'adresse IP, pour la sécurité de son service. Nous n'y avons pas accès. Voir la <a href="https://docs.github.com/fr/site-policy/privacy-policies/github-general-privacy-statement">déclaration de confidentialité de GitHub</a>.</p>
</section>
<section>
<h2>Si tu nous écris</h2>
<p>Si tu nous écris à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>, nous utilisons ton adresse et le contenu de ton message pour te répondre, et seulement pour cela. Nous les conservons le temps de traiter ta demande, puis au plus trois ans après notre dernier échange. N'y joins pas de données de santé : elles ne nous sont pas nécessaires.</p>
</section>
<section>
<h2>Les mineurs</h2>
<p>L'âge est déclaré par toi, il n'est pas vérifié. En dessous de 18 ans, Forge n'affiche ni repères caloriques ni macronutriments.</p>
</section>
<section>
<h2>Tes droits</h2>
<p>Pour les données traitées sur ton appareil, tu exerces toi-même tes droits dans l'application : consulter, modifier, exporter, supprimer. Pour les messages que tu nous as envoyés, tu peux nous demander l'accès, la rectification ou l'effacement à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Tu peux aussi saisir la CNIL (<a href="https://www.cnil.fr">cnil.fr</a>).</p>
</section>
<section>
<h2>Changements</h2>
<p>Si le fonctionnement change, par exemple avec une synchronisation par iCloud, cette page sera mise à jour avant la version de l'application concernée, et la date en tête de page changera.</p>
</section>
""", "Politique de confidentialité de l'application Forge Yourself : aucune donnée collectée, tout reste sur votre appareil.")


for slug, label in PAGES:
    body, desc = BODIES[slug]
    if slug == "index.html":
        title = "IE DIGITAL"
    elif slug == "forge-confidentialite.html":
        title = "Confidentialité — Forge Yourself"
    elif slug == "forge-assistance.html":
        title = "Assistance — Forge Yourself"
    elif slug == "forge.html":
        title = "Forge Yourself — IE DIGITAL"
    else:
        title = f"{label} — IE DIGITAL"
    (OUT / slug).write_text(render(slug, title, desc, body), encoding="utf-8")
    print(f"{slug:24} {label}")

print("\nSite généré dans", OUT)
