
import ftplib

ftp = ftplib.FTP('ftpperso.free.fr')
ftp.login('fhoerni', '4qeygx8v')
ftp.makepasv()
ftp.dir()
