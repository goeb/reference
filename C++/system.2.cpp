
#include <stdlib.h>
#include <iostream>
using namespace std;

main()
{
    string cmd = "/usr/bin/ssh -n csciint06 $COFLIGHT_HOME/PCVs/PcvDefault/CONFM_EXE_TSUP/share/STARTMNG/activatePcv -pcvToActivate PcvDefault -systemState TRAINING -systemContext 344";
    system(cmd.c_str());

}

