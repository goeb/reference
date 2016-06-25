<?

//
$db_filename = "database_liste";
$lockfile = '.db_lock';
$line1 = array('id' => 1, 'name' => 'mushroom', 'initial' => 3, 'current' => 2);
$line2 = array('id' => 2, 'name' => 'noodles', 'initial' => 500, 'current' => 350);
$line3 = array('id' => 3, 'name' => 'salad', 'initial' => 1, 'current' => 1);
$full_list = array($line1, $line2, $line3);

function read_db() {
	global $db_filename;
	$fd = fopen($db_filename, 'r');
	if ($fd === FALSE) {
		echo "Error:read_db: cannot open $db_filename\n";
		return FALSE;
	}
	$contents = fread($fd, filesize($db_filename));
	if (FALSE === $contents) {
		echo "Error:read_db: cannot read\n";
		return FALSE;
	}
	$a = unserialize($contents);
	return $a;
}

function write_db($db_array) {
	global $db_filename;
	if (file_exists($db_filename)) {
		$rc = rename($db_filename, $db_filename.".back");
		if (FALSE == $rc) {
			echo "Error: cannot rename $db_filename, $db_filename.back.\n";
			return FALSE;
		}
	}
	$db = fopen($db_filename, "w");
	if (FALSE === $db) {
		echo "Error: cannot open DB file.\n";
		return FALSE;
	}
	$contents = serialize($db_array);
	$rc = fwrite($db, $contents);
	if (FALSE === $rc) {
		echo "Error: cannot write contents\n";
		return FALSE;
	}
	return TRUE;
}

function set_lock() {
	global $lockfile;
	$lock = fopen($lockfile, 'x');
	if (FALSE === $lock) {
		printf("Error: cannot get lock\n");
		return FALSE;
	}
	fclose($lock);
}

function free_lock() {
	global $lockfile;
	$rc = unlink($lockfile);
	if ($rc === FALSE) {
		echo "Warning: lock file cannot be removed !\n";
	}
}


?>
