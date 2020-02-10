def load_config(filename="config.json"):
    import json
    print("Config: Loading")
    config = json.loads(open(filename).read())
    print("Config:")
    print(config)
    return config


def wifi_setup(config):
    import network
    print("WiFi: Deactivate AP")
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    print("WiFi: Activate")
    wifi = network.WLAN(network.STA_IF)
    wifi.active(True)

    print("WiFi: Configure SSID")
    wifi.connect(config["ssid"], config["pass"])
    while not wifi.isconnected():
        pass
    print('WiFi: Network config:', wifi.ifconfig())


def webrepl_setup(config):
    import webrepl
    print("Webrepl: configure")
    webrepl.start(password=config["pass"])


# https://worldtimeapi.org/timezone/
def updatetime(timezone="Europe/Berlin"):
    import ntptime
    import urequests
    import json
    import utime
    import machine
    print("Time: Timezone will be " + timezone)
    ntptime.settime()
    print("Time: " + str(utime.localtime()) + " UTC")
    response = urequests.get("https://worldtimeapi.org/api/timezone/" + timezone + ".json")
    json = response.json()
    offset = json['raw_offset']
    newtime = utime.time() + offset
    tm = utime.localtime(newtime)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
    print("Time " + str(utime.localtime()) + " " + timezone)
