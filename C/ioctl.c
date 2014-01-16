#include <stdio.h>
#include <linux/ioctl.h> /* for _IOW/_IOR*/

#define IRQ_MODULE_IOC_MAGIC 'a'
#define SET_MODEM_WAN1			_IOW(IRQ_MODULE_IOC_MAGIC, 26, int)
#define SET_WATCHDOG_INPUT		_IOW(IRQ_MODULE_IOC_MAGIC, 24, int)


main()
{
	printf("SET_WATCHDOG_INPUT=0x%x\n", SET_WATCHDOG_INPUT);	
	printf("SET_MODEM_WAN1=0x%x\n", SET_MODEM_WAN1);	
}
