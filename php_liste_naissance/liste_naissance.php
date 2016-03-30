<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<link href="style.css" rel="stylesheet" type="text/css">
<link rel="shortcut icon" href="favicon.ico" />
<title>Liste de naissance</title>
</head>
<body>
<img src="nounours.jpg" style="margin:1em;float:left;">
<h1>Liste de naissance</h1>
<h1>Bienvenue !</h1>
<h2>Mode d'emploi</h2>
Cette liste a pour objet de canaliser votre générosité et répartir les cadeaux pour le bébé. Cela vous permettra, si vous le souhaitez, de faire un cadeau qui ne sera pas en 10 exemplaires.<br>
Le principe est le suivant:
<ol>
<li>Choisissez un cadeau dans la liste (exemple : entrez "2" dans la colonne "votre choix" si vous souhaitez offrir 2 bavoirs).</li>
<li>Entrez votre adresse e-mail en bas de la page et validez.</li>
<li>Votre futur cadeau est alors pris en compte (exemple : si vous avez choisi d'offrir la chaise haute, celle-ci ne sera plus disponible dans la liste).</li>
<li>C'est ensuite à vous d'aller choisir le cadeau dans le magasin de votre choix et au prix qui vous convient. Nous serons également ravis si c'est un objet d'occassion à condition qu'il soit assez récent (à cause des normes de sécurité), en bon état et propre. </li>
<li>Merci d'avance ! Le bébé a déjà hâte de vous rencontrer !</li>
</ol>
<div style="clear:both;"></div>
<h2>Attention</h2>
Nous avons déjà ou nous nous occupons nous-même de l'achat des articles suivants :
<ul>
<li>poussette, landeau, coque auto</li>
<li>table à langer et baignoire</li>
<li>lit</li>
<li>parc</li>
<li>vêtements taille naissance</li>
<li>sac à langer</li>
<li>nécessaire de toilette</li>
</ul>

<h2>Notes :</h2>
<ul>
<li>Vous pouvez ne pas utiliser cette liste si vous avez une autre idée.</li>
<li>Vous pouvez vous regrouper pour les gros cadeaux.</li>
<li>Un petit dessin est aussi un très beau cadeau qui se suffit à lui-même. Pensez-y !</li>
<li>Nous préférerions des couleurs mixtes, sauf "coup de c&#339;ur".</li>
</ul>
<h2>Faites votre choix</h2>
Sélectionnez les quantités dont vous vous chargez et validez votre choix.<br>
Les photos sont là à titre indicatif et ne désignent pas un modèle particulier.<br>
Les prix sont également un ordre de grandeur du cadeau (neuf) pour vous guider dans votre choix.<br>
<form method="post" action="valider.php">
<table>
<tr>
<td>Description</td>
<td>Ordre de grandeur du prix</td>
<td>Quantité max souhaitée</td>
<td>Quantité réservée</td>
<td>Votre choix</td>
<td></td>
</tr>
<?
//include('make_db.php'); echo "<h1>TODO remove make_db from here !! pour la mise en service</h1>";
include('db_file.php'); // TODO reset this for operational mode
include('log_tools.php');
$base = read_db();
$style = 0;
foreach ($base as $id => $item) {
	$style = 1 - $style;
	$name = $item['name'];
	$price = $item['prix'];
	$max = $item['max'];
	$booked = $item['booked'];
	$image = $item['image'];
	$remaining = $max - $booked;
	echo "<tr class=\"row$style\">";
	echo "<td><b>$name</b></td>";
	if ($price != '') echo "<td>$price &euro;</td>";
	else echo "<td></td>";
	echo "<td>";
	echo $max;
	echo "</td>";
	echo "<td>";
	echo $booked;
	echo "</td>";
	echo "<td>";
	if ($remaining > 0) {
		echo "<input type=\"text\" size=\"3\" name=\"field$id\"> ";
	} else echo "-";
	echo "</td>";
	echo "<td>";
	if ($image != '') echo "<img src=\"$image\">";
	echo "</td>";
	echo "</tr>\n";
}
echo "</table>";
?>
email: <input type="text" size="40" name="email"><br>
Un email de confirmation vous sera envoyé.<br>
<input type="submit" value="Valider">
</form>
<hr>
Pour tout renseignement, changer d'avis, ou un problème, vous pouvez nous contacter : xxx<br>
</body>
</html>
