<?
	$description = "toto\n à la piscine\n.";
	echo "description=$description\n";
	$description = preg_replace("/[\n\r]/", "#", $description);
	echo "description=$description\n";
?>
