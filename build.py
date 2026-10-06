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
    ("essor.html", "Essor"),
    ("vespra.html", "Vespra"),
    ("methode.html", "Méthode"),
    ("a-propos.html", "À propos"),
    ("contact.html", "Contact"),
    ("mentions-legales.html", "Mentions légales"),
    ("forge-confidentialite.html", "Forge — Confidentialité"),
    ("forge-assistance.html", "Forge — Assistance"),
    ("essor-confidentialite.html", "Essor — Confidentialité"),
    ("essor-assistance.html", "Essor — Assistance"),
    ("essor-methode.html", "Essor — Méthode de l'indice"),
    ("vespra-confidentialite.html", "Vespra — Confidentialité"),
    ("vespra-assistance.html", "Vespra — Assistance"),
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
                    "forge-assistance.html", "essor-confidentialite.html", "essor-assistance.html",
                    "essor-methode.html", "vespra-confidentialite.html", "vespra-assistance.html"):
            continue
        # Les sous-pages d'une application allument l'entrée de l'application dans la navigation.
        actif = current
        if current.startswith("forge-"):
            actif = "forge.html"
        elif current.startswith("essor-"):
            actif = "essor.html"
        elif current.startswith("vespra-"):
            actif = "vespra.html"
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
  <p>Essor, application iOS de bien-être&nbsp;: trois gestes par jour, une recette
  française le soir, un indice d'habitudes qui explique ses calculs. Sans compte ni
  collecte de données.</p>
  <p><a class="more" href="essor.html">Essor : présentation, assistance, confidentialité</a></p>
  <p>Vespra, application iOS du soir et de la nuit&nbsp;: un geste pour mieux préparer
  son coucher, puis l'écoute des ronflements de la nuit, analysée sur l'iPhone. Sans
  compte ni collecte de données, achat unique sans abonnement.</p>
  <p><a class="more" href="vespra.html">Vespra : présentation, assistance, confidentialité</a></p>
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
    <div><dt>Téléphone</dt><dd><a href="tel:+33986139551">09&nbsp;86&nbsp;13&nbsp;95&nbsp;51</a></dd></div>
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
<p>Dans <i>Profil › Toi › Abonnement</i>, ou dans les réglages de l'iPhone : <i>Réglages › ton nom › Abonnements › Forge</i>. La résiliation prend effet à la fin de la période en cours ; tu gardes l'accès jusque-là, et ton historique reste consultable ensuite.</p>
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
<p>Si tu l'actives dans <i>Profil › Données › Santé</i>, Forge lit ton poids, ta taille et tes pas pour éviter une double saisie. Sur l'iPhone, Forge n'écrit rien dans Santé. Si tu l'acceptes, l'Apple Watch y enregistre les séances lancées sur la montre : durée, énergie active et fréquence cardiaque. Ces données restent sur tes appareils. Pour retirer l'accès : <i>Réglages › Santé › Accès aux données et appareils › Forge</i>.</p>
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
<p class="eyebrow"><a href="forge.html">Forge Yourself</a></p>
<h1>Politique de confidentialité</h1>
<p class="lede">Forge Yourself, application iOS et application web · version du 6 octobre 2026</p>

<div class="note" style="margin-bottom:32px">
<p style="margin:0"><b>En bref : nous ne recevons aucune de tes données d'entraînement ni de santé.</b> Il n'y a pas de compte, pas de serveur Forge, pas de publicité, pas de traceur. Ce que tu saisis est traité par l'application sur ton appareil. Quand la synchronisation iCloud arrivera (prochaine version), si tu es abonné et que tu l'utilises, une copie de ton programme et de tes séances partira dans <b>ton</b> espace iCloud, auquel nous n'avons pas accès. Tes mesures corporelles, ce qui vient de l'app Santé, ton journal de repas et ses photos ne sont jamais copiés par Forge, ni dans iCloud ni ailleurs.</p>
</div>

<h2>Qui édite l'application</h2>
<p><b>IE DIGITAL</b>, SARL à associé unique immatriculée au RCS de Lille Métropole sous le numéro 822 744 116, dont le siège est situé 31 rue du Président Kennedy, 59237 Verlinghem, France. Pour toute question sur cette page ou sur tes données : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. C'est aussi l'adresse de la personne responsable de la protection des renseignements personnels (le gérant d'IE DIGITAL), pour les personnes qui résident au Québec.</p>

<h2>Ce que l'application traite, et où</h2>
<ul>
<li><b>Ton programme, tes séances, tes charges et tes notes</b> : enregistrés dans le stockage de l'application, sur ton appareil.</li>
<li><b>Ton poids, ta taille, ton âge, tes mensurations</b> : même endroit. Ils servent à tracer ta courbe de suivi et, à partir de 18 ans, à calculer des repères alimentaires généraux. Ils ne sont transmis à personne, nous compris.</li>
<li><b>Sur l'app web</b>, tout est gardé dans le stockage de ton navigateur. Vider les données du site les efface. L'app web ne se synchronise pas avec iCloud.</li>
</ul>
<p>Nous n'avons pas accès à ces données : nous ne pouvons ni les lire, ni les corriger, ni les supprimer à ta place. Tu les gères toi-même dans l'application ; <i>Profil › Données › Supprimer ce profil</i> efface le profil et tout son historique, sur l'appareil et, tant que la synchronisation est active, dans ta copie iCloud. Supprimer l'application efface ses données de l'appareil, mais pas ta copie iCloud (voir ci-dessous).</p>

<h2>La synchronisation iCloud (iPhone, abonnés)</h2>

<p><b>Cette fonction arrive avec une prochaine version de l'application.</b> Tant qu'elle n'y est pas, rien ne part dans iCloud. Quand elle sera là : avec un abonnement actif et un compte iCloud sur ton iPhone, Forge copie tes <b>profils</b> — programme, séances, charges, notes, médailles et réglages — dans la base de données <b>privée</b> que ton compte iCloud réserve à l'application. C'est ce qui te permet de les retrouver sur un autre iPhone.</p>
<ul>
<li><b>Ce qui n'y va jamais</b> : ton poids, ta taille, ton âge et tes mensurations, qu'ils viennent de Forge ou de l'app Santé ; ton journal de repas et ses photos ; la séance en cours. Ces données restent sur l'iPhone où tu les as saisies.</li>
<li><b>Qui y a accès</b> : toi, à travers ton compte Apple. Cette copie est stockée par Apple, sur ton quota iCloud, selon les conditions d'iCloud que tu as acceptées. Elle ne passe par aucun serveur d'IE DIGITAL, et nous ne pouvons pas la consulter.</li>
<li><b>Sans compte iCloud, ou sans abonnement</b>, rien ne part : tes données restent sur l'iPhone.</li>
<li><b>À ne pas confondre</b> avec la sauvegarde de ton iPhone (dans iCloud ou sur un ordinateur), que gère iOS et non Forge : comme pour toute application, elle contient les données de Forge présentes sur l'appareil, photos du journal exceptées.</li>
<li><b>Pour arrêter</b> : désactive Forge dans <i>Réglages › ton nom › iCloud</i>. Si ton abonnement prend fin, la synchronisation s'arrête ; la copie déjà faite reste dans ton iCloud jusqu'à ce que tu l'effaces.</li>
<li><b>Pour effacer ta copie iCloud</b> : supprime tes profils dans Forge tant que la synchronisation est active, ou efface les données de Forge dans <i>Réglages › ton nom › iCloud › Gérer le stockage</i>.</li>
</ul>

<h2>Le journal de repas (iPhone, facultatif)</h2>
<p>Le journal ne s'ouvre qu'avec ton accord explicite. Il garde, pour chaque repas, sa composition, une taille d'assiette et, si tu le veux, une photo. La photo est prise avec l'appareil photo de l'iPhone, analysée <b>sur ton iPhone</b> pour te proposer une composition que tu confirmes toi-même, réduite, puis effacée au bout de 7 jours. Le journal et ses photos restent sur ton iPhone : Forge ne les copie ni dans iCloud ni chez nous, et les photos sont exclues des sauvegardes de l'iPhone. L'indicateur de pertinence est désactivé par défaut ; activé, il est calculé sur l'iPhone. <i>Tout effacer</i> supprime les repas et les photos ; retirer ton accord efface tout le journal.</p>

<h2>L'app Santé (iPhone, facultatif)</h2>
<p>Si tu actives <i>Profil › Données › Santé</i>, Forge t'explique d'abord ce qu'il lit, puis iOS te laisse choisir donnée par donnée. Forge <b>lit</b> dans l'app Santé ton <b>poids</b> et ta <b>taille</b>, pour remplir ta courbe de suivi et tes repères sans double saisie, et ton <b>nombre de pas</b>, pour afficher ta moyenne quotidienne dans l'onglet Suivi. Sur l'iPhone, <b>Forge n'écrit rien dans Santé.</b></p>
<p><b>L'Apple Watch (facultatif).</b> Si tu l'acceptes au lancement d'une séance sur la montre, Forge <b>enregistre dans Santé</b> chaque séance lancée sur ton Apple Watch, comme un entraînement de musculation : sa <b>durée</b>, l'<b>énergie active</b> et la <b>fréquence cardiaque</b> mesurées par la montre. Pendant la séance, la montre lit aussi ta fréquence cardiaque et ton énergie active pour te les afficher. Ces données restent dans Santé, sur tes appareils : elles ne nous sont jamais envoyées, ne sont jamais utilisées à des fins publicitaires ni transmises à un tiers. Tu peux refuser, retirer l'accès à tout moment dans <i>Réglages › Santé › Accès aux données et appareils › Forge</i>, et supprimer ces entraînements dans l'app Santé.</p>
<p>Les données lues dans Santé restent sur ton iPhone : elles ne partent ni dans iCloud, ni dans la sauvegarde par fichier, ni chez nous. Elles ne sont jamais utilisées à des fins publicitaires ni transmises à un tiers. Tu peux retirer l'accès à tout moment dans <i>Réglages › Santé › Accès aux données et appareils › Forge</i>.</p>

<h2>La sauvegarde par fichier</h2>
<p><i>Profil › Données › Sauvegarder ce profil</i> crée un fichier que tu ranges où tu veux (Fichiers, iCloud Drive, e-mail…). Il contient ton profil, mensurations saisies comprises, mais rien de ce qui vient de Santé. Forge ne l'envoie nulle part : c'est toi qui choisis sa destination, et le service que tu choisis applique alors ses propres règles. Ce fichier te permet aussi de récupérer tes données dans un format lisible et de les emporter ailleurs.</p>

<h2>Les achats</h2>
<p>Les abonnements et l'achat à vie passent entièrement par Apple, qui en est responsable. Nous ne recevons ni ton nom, ni ton adresse, ni tes moyens de paiement. L'application vérifie sur ton appareil le justificatif signé par Apple pour savoir quelles fonctions ouvrir. La gestion et la résiliation se font dans les réglages de ton compte Apple.</p>

<h2>La demande d'avis</h2>
<p>De temps en temps, après une séance, Forge peut faire apparaître la fenêtre d'avis de l'App Store. C'est une fenêtre d'Apple : iOS décide si elle s'affiche et en limite la fréquence, et ce que tu y réponds va à Apple, pas à nous. Pour choisir le moment, l'application ne se sert que de données restées sur ton iPhone (nombre de séances, records, date du dernier renouvellement). Si tu publies un avis, Apple l'affiche sur l'App Store sous ton pseudonyme, selon ses propres règles ; nous pouvons y répondre publiquement.</p>

<h2>Les notifications</h2>
<p>Le minuteur de repos peut t'envoyer des notifications et s'afficher sur l'écran verrouillé, si tu l'autorises. Elles sont créées par l'application sur ton iPhone ; aucun serveur ne les envoie.</p>

<h2>Les statistiques</h2>
<p>Forge n'intègre aucun outil de mesure d'audience. Apple nous fournit, dans son espace développeur, des statistiques agrégées : installations, plantages, abonnements. Les chiffres d'usage et les rapports de plantage ne proviennent que des personnes qui ont accepté, dans les réglages de leur iPhone, de partager leurs données d'analyse avec les développeurs ; ils ne nous permettent pas de t'identifier. L'app web ne mesure rien.</p>

<h2>L'hébergement de l'app web et de cette page</h2>
<p>L'app web et cette page sont hébergées par <b>GitHub</b> (GitHub, Inc., filiale de Microsoft, États-Unis). Comme tout hébergeur, GitHub peut enregistrer des données techniques de connexion, dont l'adresse IP, pour la sécurité de son service. Nous n'y avons pas accès. Voir la <a href="https://docs.github.com/fr/site-policy/privacy-policies/github-general-privacy-statement">déclaration de confidentialité de GitHub</a>.</p>

<h2>Si tu nous écris</h2>
<p>Si tu nous écris à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>, nous utilisons ton adresse et le contenu de ton message pour te répondre, et seulement pour cela. C'est notre intérêt légitime à répondre aux personnes qui nous contactent, ou, si tu es client, l'exécution de ce que nous te devons. Seuls le gérant d'IE DIGITAL et notre prestataire de messagerie, qui l'héberge pour notre compte, y ont accès. Nous conservons ces messages le temps de traiter ta demande, puis au plus trois ans après notre dernier échange. N'y joins pas de données de santé : elles ne nous sont pas nécessaires.</p>

<h2>Combien de temps</h2>
<ul>
<li><b>Sur ton appareil</b> : jusqu'à ce que tu supprimes le profil, les données du site ou l'application.</li>
<li><b>Dans ton iCloud</b> (programme et séances) : jusqu'à ce que tu supprimes le profil ou effaces les données de Forge dans iCloud.</li>
<li><b>Photos du journal de repas</b> : 7 jours, sur l'iPhone.</li>
<li><b>Tes messages</b> : au plus trois ans après notre dernier échange.</li>
</ul>

<h2>Les mineurs</h2>
<p>L'âge est déclaré par toi, il n'est pas vérifié. En dessous de 18 ans, Forge n'affiche ni repères caloriques ni macronutriments.</p>

<h2>Tes droits</h2>
<p>Pour les données traitées sur ton appareil ou copiées dans ton iCloud, tu exerces toi-même tes droits dans l'application : consulter, modifier, exporter (<i>Profil › Données › Sauvegarder ce profil</i>), supprimer. Pour ce qui passe par Apple (achats, iCloud, avis), tes droits s'exercent auprès d'Apple. Pour les messages que tu nous as envoyés, tu peux nous demander l'accès, la rectification, l'effacement, la limitation, t'opposer à leur traitement, ou nous laisser des directives sur leur sort après ton décès, à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Tu peux aussi saisir la CNIL (<a href="https://www.cnil.fr">cnil.fr</a>) ou l'autorité de protection des données de ton pays.</p>

<h2>Changements</h2>
<p>Si le fonctionnement change, cette page est mise à jour avant la version de l'application concernée, et la date en tête de page change. Un changement qui envoie de nouvelles données hors de ton appareil te sera annoncé dans l'application.</p>

<h2>Mentions légales</h2>
<ul>
<li><b>Éditeur</b> : IE DIGITAL, SARL à associé unique, RCS Lille Métropole 822 744 116, TVA intracommunautaire FR42 822 744 116. Siège : 31 rue du Président Kennedy, 59237 Verlinghem, France. E-mail : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Voir aussi les <a href="https://iedigital.fr/mentions-legales.html">mentions légales</a>.</li>
<li><b>Directeur de la publication</b> : Alexandre Elard, gérant.</li>
<li><b>Hébergeur de cette page et de l'app web</b> : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</li>
<li><b>Distribution de l'application iOS</b> : App Store, exploité par Apple Distribution International Ltd., Hollyhill Industrial Estate, Hollyhill, Cork, Irlande.</li>
</ul>
""", "Politique de confidentialité de l'application Forge Yourself : aucune donnée collectée, tout reste sur votre appareil.")

# ---------------------------------------------------------- Essor · section
# Section de l'application Essor : présentation, assistance, confidentialité,
# méthode de l'indice. Les URL essor-assistance.html, essor-confidentialite.html
# et essor/flags.json sont inscrites dans l'app et dans App Store Connect :
# ne jamais les renommer.
BODIES["essor.html"] = ("""
<p class="eyebrow">Application iOS</p>
<h1>Essor</h1>
<p class="lede">L'art de vivre longtemps, au quotidien. Trois gestes par jour, une
recette française le soir, et un indice qui explique ses calculs.</p>

<section>
  <h2>En bref</h2>
  <dl class="facts">
    <div><dt>Plateforme</dt><dd>iPhone, iOS 26 et plus. Réservée aux personnes de 18 ans ou plus.</dd></div>
    <div><dt>Compte</dt><dd>Aucun. Pas de serveur Essor, pas de publicité, pas de traceur.</dd></div>
    <div><dt>Données</dt><dd>Enregistrées et chiffrées sur l'iPhone. Export chiffré et effacement depuis l'app.</dd></div>
    <div><dt>Formules</dt><dd>Gestes, cuisine, indice et bilans gratuits ; idées liées aux bilans, observations et idées de dîner illimitées avec Essor Premium.</dd></div>
    <div><dt>Nature</dt><dd>Application de bien-être. Elle ne remplace pas l'avis d'un médecin et ne pose aucun diagnostic.</dd></div>
    <div><dt>Éditeur</dt><dd>IE DIGITAL</dd></div>
  </dl>
</section>

<section>
  <h2>Aide et informations</h2>
  <ul>
    <li><a href="essor-assistance.html">Assistance et questions fréquentes</a></li>
    <li><a href="essor-confidentialite.html">Politique de confidentialité</a></li>
    <li><a href="essor-methode.html">Méthode de l'Indice Essor et de l'Âge d'habitudes</a></li>
    <li><a href="mailto:contact@iedigital.fr?subject=Essor%20%E2%80%94%20assistance">Nous écrire : contact@iedigital.fr</a></li>
  </ul>
</section>
""", "Essor, application iOS de bien-être éditée par IE DIGITAL : gestes du jour, cuisine française, indice d'habitudes expliqué. Assistance, confidentialité, méthode.")

BODIES["essor-assistance.html"] = ("""
<p class="eyebrow"><a href="essor.html">Essor</a></p>
<h1>Assistance</h1>
<p class="lede">Essor, application iOS · IE DIGITAL</p>

<p class="note"><b>Nous écrire : <a href="mailto:contact@iedigital.fr?subject=Essor%20%E2%80%94%20assistance">contact@iedigital.fr</a></b><br>
Réponse sous 3 jours ouvrés. Indiquez le modèle de votre iPhone, la version d'iOS et celle d'Essor (<i>Profil › À propos</i>). N'envoyez jamais vos bilans ni vos valeurs de santé.</p>

<section class="faq">
<h2>Questions fréquentes</h2>

<details>
<summary>Faut-il créer un compte ?</summary>
<p>Non. Essor fonctionne sans compte et sans serveur : vos données sont enregistrées et chiffrées sur votre iPhone. Détails dans la <a href="essor-confidentialite.html">politique de confidentialité</a>.</p>
</details>

<details>
<summary>Comment changer d'iPhone sans rien perdre ?</summary>
<p>Les données d'Essor ne partent pas dans la sauvegarde iCloud. Sur l'ancien iPhone : <i>Profil › Confidentialité › Exporter mes données</i>, choisissez une phrase de passe et enregistrez le fichier .essor. Sur le nouvel iPhone : <i>Importer un export</i>, avec la même phrase de passe.</p>
</details>

<details>
<summary>Mon indice ne bouge pas ou affiche « — »</summary>
<p>Vérifiez l'accès à Apple Santé dans <i>Réglages › Santé › Accès aux données › Essor</i>. Une donnée absente n'est jamais inventée : la dimension concernée reste vide et la confiance de l'indice baisse. Voir la <a href="essor-methode.html">méthode de l'indice</a>.</p>
</details>

<details>
<summary>Comment importer un bilan sanguin ?</summary>
<p>Onglet <i>Bilans › Importer un bilan</i>, puis choisissez le PDF de votre laboratoire. Vérifiez chaque valeur avant de confirmer. L'import et l'affichage sont gratuits. « Pour mon rendez-vous » prépare ensuite un PDF que vous relisez avant de le montrer à votre médecin.</p>
</details>

<details>
<summary>À quoi sert le jour sans pression ?</summary>
<p>Un jour par semaine (le dimanche par défaut, réglable dans <i>Progrès</i>) où rien n'est attendu : s'il se passe sans geste, votre série continue.</p>
</details>

<details>
<summary>Les widgets n'affichent pas mes gestes</summary>
<p>Ouvrez Essor une fois : les widgets se mettent à jour à chaque ouverture. Sur l'écran verrouillé, l'option <i>Profil › Confidentialité › Texte neutre</i> remplace le titre du geste par « Votre geste du jour ».</p>
</details>

<details>
<summary>Qu'apporte Essor Premium ?</summary>
<p>Les idées générales liées aux repères de vos bilans, les observations sur vos habitudes, et des idées de dîner illimitées. Les gestes, la cuisine du jour, l'Indice Essor et son explication, l'import et l'affichage des bilans restent gratuits.</p>
</details>

<details>
<summary>Comment résilier ou restaurer mon abonnement ?</summary>
<p>Résilier : <i>Profil › Abonnement › Gérer ou résilier l'abonnement</i>, ou <i>Réglages › votre nom › Abonnements</i>, au moins 24 heures avant l'échéance. Restaurer après une réinstallation : <i>Restaurer mes achats</i>, avec le même identifiant Apple. Les remboursements sont gérés par Apple sur <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
</details>

<details>
<summary>Comment tout effacer ?</summary>
<p><i>Profil › Confidentialité › Tout effacer</i>, puis confirmez. Toutes les données d'Essor sur l'iPhone sont supprimées. Restent en place les données d'Apple Santé (Essor n'y écrit rien), les ingrédients ajoutés aux Rappels et les fichiers que vous avez partagés ou exportés.</p>
</details>

<details>
<summary>Essor remplace-t-il un avis médical ?</summary>
<p>Non. Essor est une application de bien-être, pas un dispositif médical : elle n'interprète pas vos résultats et ne pose aucun diagnostic. Pour un résultat qui vous interroge, parlez-en à votre médecin.</p>
</details>
</section>
""", "Assistance de l'application Essor : questions fréquentes, abonnement, changement d'iPhone, contact.")

BODIES["essor-methode.html"] = ("""
<p class="eyebrow"><a href="essor.html">Essor</a></p>
<h1>Méthode de l'Indice Essor</h1>
<p class="lede">Ce que l'indice mesure, comment il est calculé, et ses limites. Formule
« score-v1 ». L'indice reflète vos habitudes, pas votre santé.</p>

<section>
  <h2>Ce que c'est</h2>
  <p>L'Indice Essor est une note de 0 à 100 qui résume vos habitudes des sept derniers
  jours, calculée sur votre iPhone. Les poids sont des choix éditoriaux d'IE DIGITAL,
  publiés ici ; ils ne prétendent à aucune validation scientifique. L'indice ne mesure
  ni votre état de santé ni un risque, et ne remplace pas l'avis d'un médecin.</p>
</section>

<section>
  <h2>Six dimensions</h2>
  <dl class="facts">
    <div><dt>Activité · 25 %</dt><dd>Moyenne de deux notes sur 7 jours : les minutes d'exercice, ramenées au repère de l'OMS (2020) de 150 à 300 minutes d'activité modérée par semaine (150 min donnent 80, 300 min donnent 100) ; et les pas quotidiens (2 000 pas donnent 0, 10 000 pas donnent 100).</dd></div>
    <div><dt>Sommeil · 20 %</dt><dd>Durée moyenne, comparée au repère de la National Sleep Foundation (7 à 9 h par nuit pour un adulte de 26 à 64 ans : 100 dans cette plage), et régularité de l'heure de coucher (écart type de 30 min ou moins : 100 ; 2 h ou plus : 0).</dd></div>
    <div><dt>Récupération · 15 %</dt><dd>Fréquence cardiaque au repos et variabilité cardiaque du jour, comparées à votre propre moyenne des 28 derniers jours (14 jours au minimum) : 50 correspond à votre moyenne habituelle.</dd></div>
    <div><dt>Forme · 10 %</dt><dd>VO2max estimée par l'Apple Watch, comparée à la médiane de votre âge et de votre sexe dans le registre FRIEND (Kaminsky et al., Mayo Clinic Proceedings, 2022) : la médiane donne 50, 10 points au-dessus donnent 100.</dd></div>
    <div><dt>Nutrition · 15 %</dt><dd>Fibres (repère de l'ANSES : 30 g par jour) et diversité des végétaux sur 7 jours (30 végétaux distincts donnent 100), d'après les repas notés dans Essor.</dd></div>
    <div><dt>Habitudes · 15 %</dt><dd>Part des gestes clés faits sur 7 jours (3 par jour).</dd></div>
  </dl>
</section>

<section>
  <h2>Calcul</h2>
  <p>Chaque dimension donne une note de 0 à 100. L'indice est leur moyenne pondérée, sur
  les seules dimensions disponibles : une donnée absente n'est jamais inventée, les poids
  restants sont répartis et la confiance affichée baisse. La valeur affichée est lissée
  sur 7 jours (moyenne mobile exponentielle). Le détail de chaque dimension, de ses
  données et de sa contribution est visible dans l'app : <i>Aujourd'hui › Pourquoi … ?</i></p>
</section>

<section>
  <h2>Âge d'habitudes</h2>
  <p>L'Âge d'habitudes traduit les mêmes dimensions en années, à côté de votre âge civil :
  une dimension à 100 rapproche de −8 ans, à 0 de +8 ans, l'écart total étant plafonné à
  8 ans. Il faut au moins 7 jours de données. Ce n'est pas un âge biologique : il reflète
  vos habitudes, pas votre santé.</p>
</section>

<section>
  <h2>Bilans sanguins</h2>
  <p>Vos bilans n'entrent jamais dans l'indice ni dans l'Âge d'habitudes.</p>
</section>
""", "Méthode de l'Indice Essor et de l'Âge d'habitudes : dimensions, poids, repères publics, limites.")

BODIES["essor-confidentialite.html"] = ("""
<p class="eyebrow"><a href="essor.html">Essor</a></p>
<h1>Politique de confidentialité</h1>
<p class="lede">Essor, application iOS · version du 3 octobre 2026</p>

<div class="note" style="margin-bottom:32px">
<p style="margin:0"><b>En bref.</b> Essor n'a ni compte, ni serveur, ni outil de mesure d'audience, ni publicité. Vos données sont enregistrées sur votre iPhone, chiffrées et exclues de la sauvegarde iCloud. IE DIGITAL, l'éditeur, ne reçoit aucune de vos données et ne peut pas y accéder. Certaines fonctions d'iOS que vous activez (widgets, Activité en direct, Siri, Rappels, partage) affichent ou transmettent des informations par l'intermédiaire d'Apple ou vers la destination que vous choisissez : elles sont détaillées à la section 6. Vous pouvez exporter ou effacer toutes vos données Essor à tout moment, depuis l'app.</p>
</div>

<h2>1. Qui est responsable</h2>
<p>Le responsable du traitement est <b>IE DIGITAL</b>, SARL à associé unique immatriculée au RCS de Lille Métropole sous le numéro 822 744 116, dont le siège est au 31 rue du Président Kennedy, 59237 Verlinghem, France. Directeur de la publication : Alexandre Elard, gérant. Contact : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. IE DIGITAL n'a pas désigné de délégué à la protection des données ; pour toute question sur vos données, écrivez à cette adresse.</p>

<h2>2. Les données utilisées par Essor</h2>
<ul>
<li><b>Année de naissance, objectifs</b> : adapter les gestes et vérifier que vous avez 18 ans ou plus. Sur l'iPhone.</li>
<li><b>Profil facultatif (sexe, grossesse, diabète)</b> : écarter les gestes ou recettes inadaptés. Sur l'iPhone.</li>
<li><b>Données Apple Santé, en lecture seule</b> (pas, minutes d'exercice, durée du sommeil, heure de coucher, fréquence cardiaque au repos, variabilité de la fréquence cardiaque, VO2max) : calculer l'Indice Essor et l'Âge d'habitudes, afficher vos moyennes. Lues dans Apple Santé, traitées sur l'iPhone.</li>
<li><b>Gestes cochés, jour sans pression</b> : suivre vos habitudes. Sur l'iPhone.</li>
<li><b>Journal des repas, contenu du frigo, critères de cuisine</b> : proposer des recettes et la liste de courses. Sur l'iPhone.</li>
<li><b>Bilans sanguins importés (PDF) et valeurs que vous avez vérifiées</b> : afficher vos résultats tels qu'imprimés, préparer « Pour mon rendez-vous ». Sur l'iPhone, dans un espace séparé.</li>
<li><b>Journal de vos consentements</b> : prouver vos choix et vous permettre de les retirer. Sur l'iPhone.</li>
<li><b>Réglages des rappels</b> : envoyer les notifications que vous avez choisies. Sur l'iPhone.</li>
<li><b>Résumé pour les widgets</b> (gestes du jour, dîner, Indice Essor ; jamais de donnée de bilan) : afficher les widgets. Sur l'iPhone, dans un espace partagé entre l'app et ses widgets.</li>
</ul>
<p>Essor ne vous demande ni nom, ni adresse électronique, ni numéro de téléphone.</p>

<h2>3. Bases légales</h2>
<ul>
<li><b>Données de santé</b> (Apple Santé, profil facultatif, bilans) : votre consentement explicite (articles 6.1.a et 9.2.a du RGPD), demandé séparément pour Apple Santé et pour les bilans. Vous pouvez le retirer à tout moment dans <i>Profil › Confidentialité</i>, sans effet sur ce qui a été fait avant le retrait.</li>
<li><b>Fonctionnement de l'app, rappels et notifications, widgets, Activité en direct, Siri, liste de courses</b> : l'exécution du service que vous utilisez (article 6.1.b du RGPD). Les notifications, l'accès aux Rappels et Siri exigent aussi votre autorisation dans iOS.</li>
<li><b>Lecture du fichier de configuration</b> (section 6) : l'intérêt légitime d'IE DIGITAL à pouvoir désactiver à distance une fonction défaillante (article 6.1.f du RGPD).</li>
<li><b>Échanges par courriel avec IE DIGITAL</b> : l'intérêt légitime à vous répondre (article 6.1.f du RGPD).</li>
</ul>

<h2>4. Apple Santé</h2>
<p>Essor lit uniquement les données listées à la section 2 et n'écrit rien dans Apple Santé. Vous choisissez chaque catégorie dans l'écran d'autorisation d'iOS et pouvez modifier ce choix dans <i>Réglages › Santé › Accès aux données</i>. Ces données ne servent jamais à la publicité ou au marketing, et ne sont jamais vendues ni communiquées à un tiers.</p>

<h2>5. Bilans sanguins</h2>
<p>Les PDF que vous importez restent sur votre iPhone, dans un espace séparé. Vous vérifiez chaque valeur avant qu'elle soit enregistrée. Essor affiche les valeurs telles qu'imprimées ; il n'interprète pas vos résultats et ne pose aucun diagnostic.</p>
<p><b>« Pour mon rendez-vous »</b> génère sur l'iPhone un PDF que vous devez relire avant export. Il contient les valeurs recopiées de votre bilan, le nom du laboratoire et, dans une section séparée, vos moyennes de sommeil, de pas, de minutes d'activité et les gestes cochés. Il ne contient ni l'Indice Essor ni l'Âge d'habitudes. Il est créé dans un dossier temporaire protégé de l'app, puis supprimé après le partage.</p>
<p>Vos bilans ne sont jamais utilisés par une fonction d'intelligence artificielle.</p>

<h2>6. Ce qui peut sortir de l'app</h2>
<p>IE DIGITAL ne reçoit rien. Les flux ci-dessous n'existent que si vous utilisez la fonction concernée.</p>
<ul>
<li><b>Fichier de configuration.</b> Au lancement, Essor télécharge le fichier iedigital.fr/essor/flags.json pour savoir si une fonction doit être désactivée. Aucune de vos données n'est envoyée. Comme pour toute connexion Internet, votre adresse IP est transmise à l'hébergeur, GitHub, Inc. (États-Unis), qui peut la conserver dans ses journaux techniques.</li>
<li><b>Achats.</b> Les achats et abonnements sont traités par Apple. IE DIGITAL ne reçoit ni votre identité ni vos moyens de paiement, seulement des statistiques de ventes non nominatives.</li>
<li><b>Widgets et Activité en direct.</b> Les widgets de l'écran d'accueil et de l'écran verrouillé affichent vos gestes du jour, le dîner du soir et, si vous l'ajoutez, l'Indice Essor. Sur l'écran verrouillé, le contenu reste générique ; l'option « Texte neutre » remplace le titre du geste par « Votre geste du jour ». Le minuteur de cuisine affiche le nom de la recette, l'étape et le temps restant sur l'écran verrouillé et dans la Dynamic Island. Selon vos réglages iOS, le minuteur peut aussi s'afficher sur votre Apple Watch. Ces éléments sont lisibles par toute personne qui voit l'écran.</li>
<li><b>Siri et Raccourcis.</b> Les actions Essor s'exécutent sur l'iPhone ; celles qui lisent ou modifient vos données exigent que l'appareil soit déverrouillé. Votre demande vocale est traitée par Apple selon ses propres règles de confidentialité.</li>
<li><b>Liste de courses (Rappels).</b> Si vous l'autorisez, Essor ajoute les ingrédients manquants à l'app Rappels, dans la liste « Courses » ou dans votre liste par défaut. iOS n'accorde qu'un accès complet aux Rappels, mais Essor ne lit aucun autre rappel. Selon vos réglages, Apple peut synchroniser vos Rappels par iCloud ; cette synchronisation ne dépend pas d'Essor.</li>
<li><b>Partages.</b> Le PDF « Pour mon rendez-vous », la carte « Bilan du dimanche » (gestes accomplis et noms des recettes, jamais d'indice, de sommeil ni de bilan) et l'export chiffré ne sortent que si vous les partagez vous-même avec la feuille de partage d'iOS. Une fois partagés, ils relèvent du service que vous avez choisi. Aucune récompense n'est liée au partage.</li>
<li><b>Liens vers des sources.</b> Quand vous ouvrez un lien, le site consulté reçoit votre adresse IP selon sa propre politique.</li>
</ul>

<h2>7. Intelligence artificielle</h2>
<p>Essor n'utilise aucun service d'intelligence artificielle, et aucune de vos données n'est envoyée à un tel service. Cette politique sera mise à jour avant toute évolution sur ce point.</p>

<h2>8. Mesure d'audience, publicité, traceurs</h2>
<p>Essor ne contient aucun outil de mesure d'audience, aucune publicité, aucun traceur et aucun kit tiers de collecte. Si vous avez accepté dans iOS de partager vos analyses avec les développeurs, Apple peut transmettre à IE DIGITAL des rapports de plantage et des statistiques non nominatives ; vous pouvez modifier ce choix dans <i>Réglages › Confidentialité et sécurité › Analyse et améliorations</i>.</p>

<h2>9. Sécurité et sauvegarde</h2>
<p>Les données d'Essor bénéficient de la protection complète d'iOS : elles sont chiffrées et illisibles tant que l'iPhone est verrouillé, et exclues de la sauvegarde iCloud. Le résumé destiné aux widgets est lisible après le premier déverrouillage qui suit le démarrage de l'iPhone, ce qui est nécessaire pour que les widgets s'affichent ; il ne contient aucune donnée de bilan et il est lui aussi exclu de la sauvegarde iCloud. Conséquence : si vous perdez ou changez d'iPhone sans avoir fait d'export, vos données sont perdues.</p>

<h2>10. Export, import, effacement</h2>
<ul>
<li><b>Export</b> : toutes vos données dans un fichier .essor chiffré (AES-256) avec une phrase de passe que vous choisissez. IE DIGITAL ne connaît pas cette phrase et ne peut pas la récupérer.</li>
<li><b>Import</b> : le fichier .essor se réimporte dans Essor.</li>
<li><b>Effacement</b> : « Tout effacer » supprime toutes les données d'Essor sur l'iPhone ; désinstaller l'app a le même effet. Restent en place les données d'Apple Santé (Essor n'y écrit rien), les ingrédients ajoutés aux Rappels et les fichiers que vous avez partagés ou exportés, que vous pouvez supprimer depuis les apps concernées.</li>
</ul>

<h2>11. Durée de conservation</h2>
<ul>
<li>Les données d'Essor sont conservées sur votre iPhone jusqu'à ce que vous les effaciez ou désinstalliez l'app.</li>
<li>Le PDF « Pour mon rendez-vous » est supprimé du dossier temporaire après le partage.</li>
<li>Le résumé des widgets est remplacé à chaque mise à jour ; l'Activité en direct se termine à la fin du minuteur.</li>
<li>Les courriels échangés avec IE DIGITAL sont conservés au plus 3 ans après le dernier échange.</li>
</ul>

<h2>12. Rappels et notifications</h2>
<p>Si vous les autorisez, Essor envoie des notifications générées sur l'iPhone, sans passer par un serveur : au plus deux par jour (« Vos gestes du jour sont prêts », « Une idée de dîner vous attend ») ; le dimanche à 18 h (« Votre semaine à la française est prête ») ; pendant l'essai, un rappel 2 jours avant sa fin. Vous pouvez les désactiver une par une dans Essor, ou toutes à la fois dans <i>Réglages › Notifications</i>.</p>

<h2>13. Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, de portabilité et d'opposition, ainsi que du droit de retirer votre consentement. Vous pouvez aussi définir des directives sur le sort de vos données après votre décès. Comme IE DIGITAL ne détient aucune de vos données d'Essor, vous exercez la plupart de ces droits directement dans l'app : <i>Profil › Confidentialité</i>, export, « Tout effacer ». Pour toute autre demande, écrivez à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a> ; une réponse vous sera apportée sous un mois.</p>
<p>Vous pouvez introduire une réclamation auprès de la CNIL, 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 (<a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

<h2>14. Décision automatisée</h2>
<p>L'Indice Essor et l'Âge d'habitudes sont des calculs faits sur votre iPhone à partir de vos habitudes (voir la <a href="essor-methode.html">méthode</a>). Ils n'entraînent aucune décision produisant des effets juridiques à votre égard ou vous affectant de manière significative, au sens de l'article 22 du RGPD. Ils reflètent vos habitudes, pas votre santé.</p>

<h2>15. Transferts hors de l'Union européenne</h2>
<p>IE DIGITAL ne transfère aucune de vos données d'Essor. Seule l'adresse IP utilisée pour télécharger le fichier de configuration (section 6) est reçue par GitHub, Inc., aux États-Unis, qui adhère au cadre de protection des données UE–États-Unis (Data Privacy Framework). Les services d'Apple (achats, Siri, iCloud, Rappels) relèvent de la politique de confidentialité d'Apple.</p>

<h2>16. Âge minimum</h2>
<p>Essor est réservé aux personnes de 18 ans ou plus.</p>

<h2>17. Évolution de cette politique</h2>
<p>Toute modification importante vous sera signalée dans l'app avant de s'appliquer. La date de version figure en tête de cette page.</p>

<h2>Mentions légales</h2>
<ul>
<li><b>Éditeur</b> : IE DIGITAL, SARL à associé unique, RCS Lille Métropole 822 744 116, TVA intracommunautaire FR42 822 744 116. Siège : 31 rue du Président Kennedy, 59237 Verlinghem, France. E-mail : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Voir aussi les <a href="https://iedigital.fr/mentions-legales.html">mentions légales</a>.</li>
<li><b>Directeur de la publication</b> : Alexandre Elard, gérant.</li>
<li><b>Hébergeur de cette page</b> : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</li>
<li><b>Distribution de l'application</b> : App Store, exploité par Apple Distribution International Ltd., Hollyhill Industrial Estate, Hollyhill, Cork, Irlande.</li>
</ul>
""", "Politique de confidentialité de l'application Essor : aucune donnée transmise à l'éditeur, tout reste sur votre iPhone.")


# ---------------------------------------------------------- Vespra · section
# Les URL vespra-confidentialite.html et vespra-assistance.html sont inscrites
# dans l'app (Moi › À propos) et dans App Store Connect : ne jamais les renommer.
# Les mentions « dispositif médical » ont été relues côté réglementaire (MDR) :
# ne pas les reformuler sans nouvelle relecture.
BODIES["vespra.html"] = ("""
<p class="eyebrow">Application iOS</p>
<h1>Vespra</h1>
<p class="lede">Ton soir, puis l'écoute. Un seul geste pour préparer le coucher, et le
relevé des ronflements de la nuit, analysé sur l'iPhone.</p>

<section>
  <h2>En bref</h2>
  <dl class="facts">
    <div><dt>Plateforme</dt><dd>iPhone, iOS 18 et plus.</dd></div>
    <div><dt>Compte</dt><dd>Aucun. Pas de serveur Vespra, pas de publicité, pas de traceur.</dd></div>
    <div><dt>Données</dt><dd>Analysées et conservées sur l'iPhone, exclues de la sauvegarde iCloud. Effacement depuis l'app.</dd></div>
    <div><dt>Formule</dt><dd>Trois nuits d'écoute gratuites, puis un achat unique, sans abonnement.</dd></div>
    <div><dt>Nature</dt><dd>Vespra n'est pas un dispositif médical au sens du règlement (UE) 2017/745. Elle n'est destinée ni au diagnostic, ni à la prévention, ni à la surveillance d'une maladie. Les sons relevés ne sont pas interprétés. Pour toute question sur votre sommeil, consultez un médecin.</dd></div>
    <div><dt>Éditeur</dt><dd>IE DIGITAL</dd></div>
  </dl>
</section>

<section>
  <h2>Aide et informations</h2>
  <ul>
    <li><a href="vespra-assistance.html">Assistance et questions fréquentes</a></li>
    <li><a href="vespra-confidentialite.html">Politique de confidentialité</a></li>
    <li><a href="mailto:contact@iedigital.fr?subject=Vespra%20%E2%80%94%20assistance">Nous écrire : contact@iedigital.fr</a></li>
  </ul>
</section>
""", "Vespra, application iOS éditée par IE DIGITAL : un geste le soir, l'écoute des ronflements la nuit, analysée sur l'iPhone. Assistance et confidentialité.")

BODIES["vespra-assistance.html"] = ("""
<p class="eyebrow"><a href="vespra.html">Vespra</a></p>
<h1>Assistance</h1>
<p class="lede">Vespra, application iOS · IE DIGITAL</p>

<p class="note"><b>Nous écrire : <a href="mailto:contact@iedigital.fr?subject=Vespra%20%E2%80%94%20assistance">contact@iedigital.fr</a></b><br>
Réponse sous 3 jours ouvrés. Indiquez le modèle de votre iPhone et la version d'iOS. N'envoyez jamais d'extrait audio ni d'export de vos nuits.</p>

<section class="faq">
<h2>Questions fréquentes</h2>

<details>
<summary>Faut-il créer un compte ?</summary>
<p>Non. Vespra fonctionne sans compte et sans serveur. Tout est analysé et conservé sur votre iPhone. Détails dans la <a href="vespra-confidentialite.html">politique de confidentialité</a>.</p>
</details>

<details>
<summary>L'écoute démarre-t-elle toute seule ?</summary>
<p>Non. iOS ne permet pas à une app d'ouvrir le micro sans vous. Le soir, ouvrez l'onglet <i>La nuit</i>, touchez <i>Armer la nuit</i>, puis posez l'iPhone face vers le bas, branché si possible. Le matin, touchez <i>Arrêter l'écoute</i>.</p>
</details>

<details>
<summary>Que relève Vespra pendant la nuit ?</summary>
<p>Deux types de sons : les ronflements (avec leur durée) et les silences de 10 secondes ou plus entre deux sons captés. Vespra garde des extraits de 20 secondes pour que vous puissiez les réécouter ; ils s'effacent seuls au bout de 30 jours. Vespra ne mesure ni la respiration ni la santé, et n'interprète pas ces sons.</p>
</details>

<details>
<summary>Nous dormons à deux</summary>
<p>Activez <i>Nous sommes deux ce soir</i> avant d'armer la nuit. Vespra ne sait pas de qui viennent les sons et l'indique sur le relevé de la nuit.</p>
</details>

<details>
<summary>Une écoute très courte ne compte pas</summary>
<p>Une écoute de moins d'une heure est considérée comme un essai : elle n'utilise pas une de vos trois nuits gratuites et n'apparaît pas dans votre historique.</p>
</details>

<details>
<summary>Comment changer d'iPhone ?</summary>
<p>Les données de Vespra ne partent pas dans la sauvegarde iCloud : c'est un choix de confidentialité. Avant de changer d'iPhone, exportez vos nuits depuis <i>Moi › Exporter mes nuits</i> (PDF) ou <i>Exporter le journal</i>. Votre achat se restaure sur le nouvel iPhone avec <i>Restaurer mon achat</i>, sur le même identifiant Apple.</p>
</details>

<details>
<summary>Comment fonctionne l'achat ?</summary>
<p>Trois nuits d'écoute sont gratuites. Ensuite, un achat unique débloque Vespra définitivement : pas d'abonnement, rien ne se renouvelle. Les remboursements sont gérés par Apple sur <a href="https://reportaproblem.apple.com">reportaproblem.apple.com</a>.</p>
</details>

<details>
<summary>Comment tout effacer ?</summary>
<p><i>Moi › Tout effacer</i>, puis confirmez. Toutes les données et tous les extraits audio de Vespra sur l'iPhone sont supprimés. Supprimer l'app a le même effet. Les fichiers que vous avez exportés ou partagés restent là où vous les avez envoyés.</p>
</details>

<details>
<summary>Vespra remplace-t-elle un avis médical ?</summary>
<p>Non. Vespra n'est pas un dispositif médical : elle décrit des sons, ne les interprète pas et ne pose aucun diagnostic. Pour toute question sur votre sommeil, consultez un médecin.</p>
</details>
</section>
""", "Assistance de l'application Vespra : écoute de nuit, achat unique, changement d'iPhone, effacement, contact.")

BODIES["vespra-confidentialite.html"] = ("""
<p class="eyebrow"><a href="vespra.html">Vespra</a></p>
<h1>Politique de confidentialité</h1>
<p class="lede">Vespra, application iOS · version du 6 octobre 2026</p>

<div class="note" style="margin-bottom:32px">
<p style="margin:0"><b>En bref.</b> Vespra n'a ni compte, ni serveur, ni outil de mesure d'audience, ni publicité. Le son de votre chambre est analysé sur votre iPhone et n'est jamais envoyé. Ce que Vespra conserve reste sur l'iPhone, exclu de la sauvegarde iCloud. IE DIGITAL, l'éditeur, ne reçoit aucune de vos données et ne peut pas y accéder. Vous pouvez tout effacer à tout moment, depuis l'app.</p>
</div>

<h2>1. Qui est responsable</h2>
<p>L'éditeur de Vespra est <b>IE DIGITAL</b>, SARL à associé unique immatriculée au RCS de Lille Métropole sous le numéro 822 744 116, dont le siège est au 31 rue du Président Kennedy, 59237 Verlinghem, France. Directeur de la publication : Alexandre Elard, gérant. Contact : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. IE DIGITAL ne reçoit aucune donnée issue de l'application et n'a pas désigné de délégué à la protection des données ; pour toute question, écrivez à cette adresse.</p>

<h2>2. Le microphone</h2>
<p>Quand vous armez une nuit, Vespra écoute la chambre avec le microphone de l'iPhone, jusqu'à ce que vous arrêtiez l'écoute. Le son est analysé en continu, sur l'iPhone, pour noter deux types de sons : les ronflements et les silences de 10 secondes ou plus entre deux sons captés. Aucun son n'est envoyé : Vespra n'a pas de serveur.</p>
<p>Seuls des extraits de 20 secondes autour de ces sons sont enregistrés, pour que vous puissiez les réécouter. Ils sont supprimés automatiquement au bout de 30 jours. Le reste du son n'est jamais enregistré.</p>
<p>Si une autre personne dort dans la pièce, ses sons peuvent être captés. Vespra ne sait pas de qui viennent les sons. Prévenez-la avant d'armer la nuit.</p>

<h2>3. Les données conservées sur l'iPhone</h2>
<ul>
<li><b>Extraits audio de 20 secondes</b> : réécoute. Supprimés au bout de 30 jours.</li>
<li><b>Journal des nuits</b> (heures de début et de fin, horaires et durées des ronflements et des silences, interruptions, niveau de batterie, présence de deux personnes) : afficher vos nuits et votre historique. Aucun son.</li>
<li><b>Réglages et réponses</b> (heure de lever, heure de coucher visée, geste du soir, réponses du soir et du matin, sujet de l'essai « Soir → nuit ») : préparer votre soirée et comparer vos soirs.</li>
<li><b>Réglages des rappels</b> : envoyer les notifications que vous avez choisies.</li>
</ul>
<p>Les sons de votre nuit (ronflements, silences) peuvent révéler des informations sur votre santé. Ils sont analysés et conservés uniquement sur votre iPhone. IE DIGITAL n'y a jamais accès et ne les reçoit pas.</p>
<p>Vespra ne vous demande ni nom, ni adresse électronique, ni numéro de téléphone, et n'utilise pas Apple Santé.</p>

<h2>4. Ce qui peut sortir de l'app</h2>
<p>IE DIGITAL ne reçoit rien. Les flux ci-dessous n'existent que si vous utilisez la fonction concernée.</p>
<ul>
<li><b>Exports.</b> L'export de vos nuits (PDF) et du journal (fichier JSON) ne sortent que si vous les partagez vous-même avec la feuille de partage d'iOS. Vous choisissez seul à qui les envoyer ; une fois partagés, ils relèvent du service choisi.</li>
<li><b>Achat.</b> L'achat unique est traité par Apple. IE DIGITAL ne reçoit ni votre identité ni vos moyens de paiement, seulement des statistiques de ventes non nominatives.</li>
<li><b>Notifications.</b> Les rappels du soir et du matin sont programmés sur l'iPhone, sans serveur.</li>
<li><b>Fichiers.</b> Le journal des nuits est visible dans l'app Fichiers, dans le dossier de Vespra sur l'iPhone.</li>
</ul>

<h2>5. Mesure d'audience, publicité, traceurs, intelligence artificielle</h2>
<p>Vespra ne contient aucun outil de mesure d'audience, aucune publicité, aucun traceur, aucun kit tiers et aucun service d'intelligence artificielle. Si vous avez accepté dans iOS de partager vos analyses avec les développeurs, Apple peut transmettre à IE DIGITAL des rapports de plantage et des statistiques non nominatives ; vous pouvez modifier ce choix dans <i>Réglages › Confidentialité et sécurité › Analyse et améliorations</i>.</p>

<h2>6. Sécurité et sauvegarde</h2>
<p>Les données de Vespra sont protégées par le chiffrement d'iOS et exclues de la sauvegarde iCloud. Conséquence : si vous perdez ou changez d'iPhone sans avoir exporté vos nuits, elles sont perdues.</p>

<h2>7. Durée de conservation et effacement</h2>
<ul>
<li>Extraits audio : 30 jours, puis suppression automatique.</li>
<li>Journal, réglages et réponses : sur votre iPhone, jusqu'à ce que vous les effaciez.</li>
<li><i>Moi › Tout effacer</i> supprime toutes les données et tous les extraits de Vespra ; supprimer l'app a le même effet.</li>
<li>Les courriels échangés avec IE DIGITAL sont conservés au plus 3 ans après le dernier échange.</li>
</ul>

<h2>8. Vos droits</h2>
<p>Vous disposez d'un droit d'accès, de rectification, d'effacement, de limitation, de portabilité et d'opposition. Comme IE DIGITAL ne détient aucune de vos données de Vespra, vous les exercez directement dans l'app (export, « Tout effacer »). Pour toute autre demande, écrivez à <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a> ; une réponse vous sera apportée sous un mois. Vous pouvez introduire une réclamation auprès de la CNIL, 3 place de Fontenoy, TSA 80715, 75334 Paris Cedex 07 (<a href="https://www.cnil.fr">www.cnil.fr</a>).</p>

<h2>9. Nature de l'application</h2>
<p>Vespra n'est pas un dispositif médical : elle décrit des sons sans les interpréter (voir la <a href="vespra.html">présentation</a>). Elle ne prend aucune décision vous concernant au sens de l'article 22 du RGPD.</p>

<h2>10. Évolution de cette politique</h2>
<p>Toute modification importante vous sera signalée dans l'app avant de s'appliquer. La date de version figure en tête de cette page.</p>

<h2>Mentions légales</h2>
<ul>
<li><b>Éditeur</b> : IE DIGITAL, SARL à associé unique, RCS Lille Métropole 822 744 116, TVA intracommunautaire FR42 822 744 116. Siège : 31 rue du Président Kennedy, 59237 Verlinghem, France. E-mail : <a href="mailto:contact@iedigital.fr">contact@iedigital.fr</a>. Voir aussi les <a href="https://iedigital.fr/mentions-legales.html">mentions légales</a>.</li>
<li><b>Directeur de la publication</b> : Alexandre Elard, gérant.</li>
<li><b>Hébergeur de cette page</b> : GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis.</li>
<li><b>Distribution de l'application</b> : App Store, exploité par Apple Distribution International Ltd., Hollyhill Industrial Estate, Hollyhill, Cork, Irlande.</li>
</ul>
""", "Politique de confidentialité de l'application Vespra : aucune donnée transmise à l'éditeur, le son est analysé et conservé sur votre iPhone.")


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
    elif slug == "essor.html":
        title = "Essor — IE DIGITAL"
    elif slug == "essor-confidentialite.html":
        title = "Confidentialité — Essor"
    elif slug == "essor-assistance.html":
        title = "Assistance — Essor"
    elif slug == "vespra.html":
        title = "Vespra — IE DIGITAL"
    elif slug == "vespra-confidentialite.html":
        title = "Confidentialité — Vespra"
    elif slug == "vespra-assistance.html":
        title = "Assistance — Vespra"
    elif slug == "essor-methode.html":
        title = "Méthode de l'indice — Essor"
    else:
        title = f"{label} — IE DIGITAL"
    (OUT / slug).write_text(render(slug, title, desc, body), encoding="utf-8")
    print(f"{slug:24} {label}")

print("\nSite généré dans", OUT)
