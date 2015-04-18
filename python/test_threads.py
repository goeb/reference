
import threading
import time

def affiche(nb, nom = ''):
	for i in range(nb):
		print nom, i
		time.sleep(1)

a = threading.Thread(None, affiche, None, (10,), {'nom':'thread a'})
b = threading.Thread(None, affiche, None, (10,), {'nom':'thread b'})
a.start()
b.start()
