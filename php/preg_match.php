
<?php

function test_preg_match($pattern, $contents) {
	echo ">>> pattern=$pattern, contents=$contents\n";
	$x = preg_match($pattern, $contents, $matches);
	echo "x=$x\n";
	echo "matches[1]=".$matches[1]."\n";
}

test_preg_match("/xxx : ([^\s]*)\s/", "a = bbb - xxx : -2010\n");
test_preg_match("/xxx : ([0-9]*)\s/", "a = bbb - xxx : 0\n");

?>
