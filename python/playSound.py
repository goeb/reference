file='tada.wav'
if os.name != 'posix' :
   from winsound import PlaySound, SND_FILENAME, SND_ASYNC
   PlaySound(file, SND_FILENAME|SND_ASYNC)
else :
   from wave import open as waveOpen
   from ossaudiodev import open as ossOpen
   s = waveOpen(file,'rb')
   (nc,sw,fr,nf,comptype, compname) = s.getparams( )
   dsp = ossOpen('/dev/dsp','w')
   try:
     from ossaudiodev import AFMT_S16_NE
   except ImportError:
     if byteorder == "little":
       AFMT_S16_NE = ossaudiodev.AFMT_S16_LE
     else:
       AFMT_S16_NE = ossaudiodev.AFMT_S16_BE
   dsp.setparameters(AFMT_S16_NE, nc, fr)
   data = s.readframes(nf)
   s.close()
   dsp.write(data)
   dsp.close()
