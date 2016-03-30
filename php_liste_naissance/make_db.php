<?
include('db_file.php');

$base = array();
$base[] = array('name' => 'bavoirs', 'prix' => 5, 'max' => 5, 'image' => 'bavoirs.jpg');
$base[] = array('name' => 'couverture polaire', 'prix' => 15, 'max' => 1, 'image' => 'couverture.jpg');
$base[] = array('name' => "habits en 3 mois", 'prix' => '10-30', 'max' => 4, 'image' => 'habits3.jpg');
$base[] = array('name' => "habits en 6 mois", 'prix' => '10-30', 'max' => 4, 'image' => 'habits6.jpg');
$base[] = array('name' => "doudou ou peluche", 'prix' => '10-30', 'max' => 2, 'image' => 'doudou.jpg');
$base[] = array('name' => "peluche musicale", 'prix' => '15-35', 'max' => 1, 'image' => 'musicale.jpg');
$base[] = array('name' => "stérilisateur biberons pour micro-ondes de la marque Avent (normalement 2 biberons sont fournis avec)", 'prix' => 40, 'max' => 1, 'image' => 'sterilisateur.jpg');
$base[] = array('name' => "gigoteuse d'été taille 6 mois à 1 an", 'prix' => 40, 'max' => 1, 'image' => 'gigoteuse.jpg');
$base[] = array('name' => "tour de lit (décor animaux)",'prix' => 40,  'max' => 1, 'image' => 'tourdelit.jpg');
$base[] = array('name' => "mobile musical à accrocher au lit (décor animaux)", 'prix' => '30-50', 'max' => 1, 'image' => 'mobile.jpg');
$base[] = array('name' => "transat", 'prix' => 75, 'max' => 1, 'image' => 'transat.jpg');
$base[] = array('name' => "porte-bébé ventral Babybjörn ou Bébéconfort (pas d'écharpe de portage)", 'prix' => 60, 'max' => 1, 'image' => 'portebebe.jpg');
$base[] = array('name' => "chaise haute", 'prix' => '100-140', 'max' => 1, 'image' => 'chaisehaute.jpg');

foreach ($base as $id => $cell) {
	$base[$id]['booked'] = 0;
}

$rc = write_db($base);
echo "rc=$rc\n";
?>
