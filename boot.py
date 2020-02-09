# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
gc.collect()

import utils

config = utils.load_config()
utils.wifi_setup(config["wifi"])
utils.webrepl_setup()
utils.updatetime()
