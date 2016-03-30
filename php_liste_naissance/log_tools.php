<?
class LogFile {
    var $fd;
    function LogFile($filename) {
        $this->fd = fopen($filename, 'a');
    }

    function write($message) {
        $m = $this->format_message($message);
        fwrite($this->fd, $m);
    }

    function format_message($message) {
        $date = date('Y-m-d H:i:s');
        return $date . ' # ' . $message . "\n";
    }
	function close() {
		fclose($this->fd);
	}
}

//$log = new LogFile('toto.tmp');
//$log->write('yo man');

?>
