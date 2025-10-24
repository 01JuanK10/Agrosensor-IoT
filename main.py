import time
import ujson
from conexion_internet import conectar_wifi
from fechas import sincronizar_hora
from peticiones_api import registrar_dispositivo, registrar_usuario_dispositivo, generar_medicion, enviar_medicion

SSID = "PC_DE_JUANK"
PASSWORD = "12345678"


def main():
    conectar_wifi(SSID, PASSWORD)
    sincronizar_hora()

    if not registrar_usuario_dispositivo():
        print("No se pudo registrar el usuario. Abortando.")
        return

    if registrar_dispositivo():
        while True:
            medicion = generar_medicion()
            print("\n--- Medición simulada ---")
            print(ujson.dumps(medicion))
            enviar_medicion(medicion)
            print("------------------------\n")
            time.sleep(60)
    else:
        print("\nNo se ha podido registrar dispositivo")



if __name__ == "__main__":
    main()
