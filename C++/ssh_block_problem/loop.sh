
i=.5

while [ `echo "$i > 0" | bc -l` -eq 1 ]; do
	echo "--- i=$i ---"
	./a.out  /home/fred/openSSL/openssh-3.9p1/ssh $i
	i=`echo $i - 0.01 | bc -l`
done
