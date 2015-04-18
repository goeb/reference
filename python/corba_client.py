import sys, os
import CORBA


# ARGV=['toto', '-ORBInitRef', 'NameService=corbaloc::csciint06:26032/NameService']

orb = CORBA.ORB_init(sys.argv)
#poa = orb.resolve_initial_references("RootPOA")

# initNamingContext...
print "nameService=... ",
sys.stdout.flush()
nameService = orb.resolve_initial_references("NameService")
print nameService
sys.stdout.flush()

# getSystem ...
#mgr = poa.the_POAManager
#mgr.activate()

print "system=... ", 
sys.stdout.flush()
systemCorbaloc = 'corbaloc::csciint06:26032/CdmwPlatformMngtSupervision'
system = orb.string_to_object(systemCorbaloc)
print system
sys.stdout.flush()

