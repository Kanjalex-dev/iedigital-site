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
    ("methode.html", "Méthode"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
    ("mentions-legales.html", "Mentions légales"),
    ("forge-confidentialite.html", "Forge — Confidentialité"),
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
        if slug in ("index.html", "mentions-legales.html", "forge-confidentialite.html"):
            continue
        cur = ' aria-current="page"' if slug == current else ""
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
  <p><a class="more" href="forge-confidentialite.html">Politique de confidentialité de Forge Yourself</a></p>
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
    <div><dt>Capital social</dt><dd class="mono">200,00 euros</dd></div>
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

# --------------------------------------------- Forge · confidentialité
# Page exigée par Apple pour la soumission de l'application Forge Yourself.
# Son URL doit rester stable : elle est déclarée dans App Store Connect, et la
# changer casse la fiche produit.
BODIES["forge-confidentialite.html"] = ("""
<p class="eyebrow">Forge Yourself</p>
<h1>Politique de confidentialité</h1>
<p class="lede">Forge Yourself ne collecte aucune donnée personnelle. Cette page
dit ce que l'application fait de vos informations, et la réponse est courte :
elle les garde sur votre téléphone.</p>

<section>
  <h2>En résumé</h2>
  <ul>
    <li>Aucun compte à créer. Aucune adresse e-mail demandée.</li>
    <li>Aucune donnée transmise à IE DIGITAL, ni à un tiers.</li>
    <li>Aucun traceur, aucune publicité, aucun outil de mesure d'audience.</li>
    <li>Vos séances, vos charges et vos mensurations restent dans la mémoire de
    votre appareil.</li>
  </ul>
</section>

<section>
  <h2>Les données que l'application manipule</h2>
  <p>Forge Yourself enregistre, <strong>sur votre appareil uniquement</strong>,
  ce que vous y saisissez : votre prénom ou le nom que vous donnez à votre
  profil, vos réglages d'entraînement (niveau, objectif, matériel, jours), vos
  séances et les charges soulevées, vos éventuels relevés de poids et de tour de
  taille, et vos notes de séance.</p>
  <p>Ces informations ne quittent jamais votre téléphone, sauf dans les deux cas
  ci-dessous, que vous déclenchez vous-même.</p>
</section>

<section>
  <h2>Les deux cas où des données sortent de l'appareil</h2>
  <dl class="facts">
    <dt>La sauvegarde iCloud</dt>
    <dd>Si vous l'activez, vos données de profil sont synchronisées par
    <strong>iCloud</strong>, dans votre espace privé. IE DIGITAL n'y a pas accès
    et ne peut pas les lire. Le traitement relève alors de la politique de
    confidentialité d'Apple.</dd>
    <dt>L'export</dt>
    <dd>À votre demande, l'application produit un fichier contenant vos données,
    que vous choisissez d'enregistrer ou de partager. Ce que ce fichier devient
    ensuite ne dépend que de vous.</dd>
  </dl>
</section>

<section>
  <h2>Santé</h2>
  <p>Si vous l'autorisez, Forge Yourself peut écrire vos séances terminées dans
  l'application <strong>Santé</strong> d'Apple, et y lire votre poids. Cette
  autorisation se donne et se retire à tout moment dans les réglages de votre
  iPhone.</p>
  <p>Les données de santé qui entrent dans l'application <strong>ne sont jamais
  utilisées à des fins publicitaires ni transmises à qui que ce soit</strong>,
  conformément à la règle 5.1.3 des directives de l'App Store.</p>
</section>

<section>
  <h2>Abonnement</h2>
  <p>Les achats sont traités par <strong>Apple</strong>. IE DIGITAL ne reçoit ni
  votre moyen de paiement, ni votre identifiant Apple, ni votre adresse. L'accès
  à l'application est vérifié sur le reçu d'achat stocké localement sur votre
  appareil.</p>
</section>

<section>
  <h2>Vos droits</h2>
  <p>Le règlement général sur la protection des données vous donne un droit
  d'accès, de rectification, d'effacement, de limitation, d'opposition et de
  portabilité sur vos données personnelles.</p>
  <p>Comme IE DIGITAL ne détient aucune de vos données, ces droits s'exercent
  directement dans l'application : <strong>l'export</strong> assure la
  portabilité, et la <strong>suppression d'un profil</strong> — ou la
  désinstallation — efface tout. IE DIGITAL ne peut ni retrouver ni restaurer
  des données supprimées, parce qu'il n'en a jamais eu de copie.</p>
  <p>Pour toute question : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>.
  Vous pouvez également introduire une réclamation auprès de la
  <a href="https://www.cnil.fr" rel="noopener">CNIL</a>.</p>
</section>

<section>
  <h2>Durée de conservation</h2>
  <p>Vos données restent sur votre appareil aussi longtemps que vous y laissez
  l'application installée. Sans abonnement actif, Forge Yourself ne conserve rien
  au-delà de la journée en cours : les séances composées à la main ne sont pas
  reportées au lendemain.</p>
</section>

<section>
  <h2>Enfants</h2>
  <p>Forge Yourself n'est pas destinée aux enfants de moins de treize ans et ne
  leur demande aucune information.</p>
</section>

<section>
  <h2>Modifications</h2>
  <p>Toute évolution de cette politique sera publiée sur cette page, avec sa date
  d'entrée en vigueur. <strong>Version du 21 septembre 2026.</strong></p>
</section>
""", "Politique de confidentialité de l'application Forge Yourself : aucune donnée collectée, tout reste sur votre appareil.")


for slug, label in PAGES:
    body, desc = BODIES[slug]
    if slug == "index.html":
        title = "IE DIGITAL"
    elif slug == "forge-confidentialite.html":
        title = "Confidentialité — Forge Yourself"
    else:
        title = f"{label} — IE DIGITAL"
    (OUT / slug).write_text(render(slug, title, desc, body), encoding="utf-8")
    print(f"{slug:24} {label}")

print("\nSite généré dans", OUT)
