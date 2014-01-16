

repairIfExt2() {
	echo "repairIfExt2..."
	noExt2=""
	(echo toto | grep titi ) || noExt2="true"
	if [ "$noExt2" = "true" ]; then
		echo xxx
		return
	fi
	echo yyyy
}
repairIfExt2

