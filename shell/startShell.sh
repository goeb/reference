
FIFO=/tmp/fh.fifo
[ -p $FIFO ] || mkfifo $FIFO

python daemon.py $FIFO &
pid=$!
sleep 1000 > $FIFO &
pid2=$!

export PS1="subshell> "
export HISTFILE=.subshell_history
touch $HISTFILE

bash --norc --noprofile

kill $pid
kill $pid2
