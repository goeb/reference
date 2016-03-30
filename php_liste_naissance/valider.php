<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Resultat de la validation</title>
</head>
<body>
<center><h1>Résultat de votre validation</h1></center>

<?
include('db_file.php');
include('log_tools.php');

$log = new LogFile('valider.log');
// enregistrement des paramètres
ob_start();
var_export($_POST);
reset($_POST);
$post = ob_get_clean();
$log->write("Debut validation : $post");

$l = set_lock();
if (FALSE !== $l) {
	$err = 0;
	$email = trim($_POST['email']);
	$base = read_db();
	if (FALSE === $base) {
		$m = "Erreur interne d'accès à la base de données";
		echo "$m<br>\n";
		$log->write("Resultat validation : $m");
		$err ++;
	} elseif ($email == '') {
		$m = "Erreur : l'email n'est pas remplie.";
		echo "$m<br>\n";
		$log->write("Resultat validation : $m");
		$err ++;
	} else {
		foreach ($base as $id => $item) {
			$n = $_POST["field$id"];
			$max = $item['max'];
			$booked = $item['booked'];
			$remaining = $max - $booked;
			$name = $item['name'];
			if ($n < 0) {
				echo "Erreur : quantité négative ($n) pour \"$name\"<br>";
				$err ++;
			} elseif ($n > $remaining) {
				echo "Erreur : dépassement de la quantité maximale pour \"$name\" ";
				echo "($n choisi(s), mais $remaining disponible(s))<br>\n";
				$err ++;
			} else {
				$base[$id]['booked'] = $base[$id]['booked'] + $n;
			}
		}
		if ($err == 0) {
			$rc = write_db($base);
			if (FALSE !== $rc) {
				echo "Votre choix a été correctement enregistré. Envoi d'un email de confirmation...<br>\n";
				$log->write('Resultat validation : OK');
				// envoi mail admin
				$subject = "Confirmation liste de naissance";
				$message = "Voici la confirmation de votre choix :\n";
				foreach ($_POST as $key => $val) {
					$val = trim($val);
					if (substr($key, 0, 5) != 'field') continue;
					$id = substr($key, 5); // eg: field12 -> 12
					if ($val != '') $message .= $base[$id]['name'] . " : $val\n";
				}
				$message .= "\nMerci.\n\nPour toute information ou demande de modification, vous pouvez vous adresser à xxx.\n";
				$headers = "From: Liste de Naissance <xxx@free.fr>\r\n";
				$headers .= "Cc: xxx@free.fr\r\n";
				$rc = mail($email, $subject, $message, $headers);
				$log->write('Envoi du mail :  rc=$rc');
			} else {
				$m = "Erreur d'ecriture dans la base";
				echo "$m<br>\n";
				$log->write('Resultat validation : $m');
			}
		} else {
			// erreurs sur les quantités
			echo "veuillez refaire votre choix.<br>\n";
			$log->write('Resultat validation : Erreur sur les quantites');
		}
	}
	free_lock();
} else {
	echo "Votre choix n'a pas pu être validé, veuillez recommencer.<br>\n";
	$log->write('Resultat validation : erreur set_lock');
}
?>
<br>
<a href="liste_naissance.php">Revenir à la liste</a>

</body>
</html>
