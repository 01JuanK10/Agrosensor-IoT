import network
import time

def conectar_wifi(ssid, password, timeout=20):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Conectando a Wi-Fi...")
        wlan.connect(ssid, password)
        waited = 0
        while not wlan.isconnected() and waited < timeout:
            time.sleep(1)
            waited += 1

    if wlan.isconnected():
        print("Conectado a Wi-Fi:", wlan.ifconfig())
    else:
        print("No se pudo conectar a Wi-Fi.")
    return wlan


def obtener_mac():
    wlan = network.WLAN(network.STA_IF)
    mac_bytes = wlan.config("mac")
    mac = ":".join(["%02X" % b for b in mac_bytes])
    return mac
