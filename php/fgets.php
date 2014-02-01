
<?php

$out = fopen("toto", "r");
fseek($out, 0, SEEK_END);

sleep(10);
$line = fgets($out);
echo "line=$line\n";
sleep(10);
$line = fgets($out);
echo "line=$line\n";
sleep(10);
$line = fgets($out);
echo "line=$line\n";
?>
