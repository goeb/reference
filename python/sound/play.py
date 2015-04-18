
import ossaudiodev
import time
import wave

dsp = ossaudiodev.open('/dev/dsp','w')
filename = 'violet.wav'
s = wave.open(filename, 'r')
(nc, sw, fr, nf, comptype, compname) = s.getparams()
dsp.setparameters(ossaudiodev.AFMT_S16_NE, nc, fr)
print dir(dsp)
help(dsp.flush)

dsp.write(s.readframes(nf))
dsp.flush()
dsp.sync()
print "bufsize=", dsp.bufsize()
print "obufcount=", dsp.obufcount()
print "obuffree=", dsp.obuffree()
#dsp.write(s.readframes(nf))
#dsp.write(s.readframes(nf))

time.sleep(2)
s.close()
dsp.reset()
dsp.close()
