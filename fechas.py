import time
import utime
import urequests

URL_SERVER_TIME = "http://192.168.137.1:8080/utilities/server-time"
server_time_offset = 0

def sincronizar_hora():
    global server_time_offset
    try:
        print("Obteniendo hora desde el servidor API...")
        response = urequests.get(URL_SERVER_TIME)
        if response.status_code == 200:
            data = response.json()
            server_time_str = data.get("dateTime")

            if not server_time_str:
                print("Error: respuesta sin campo 'dateTime'.")
                return False

            # Formato: YYYY-MM-DDTHH:MM:SS
            year, month, day = map(int, server_time_str[0:10].split("-"))
            hour, minute, second = map(int, server_time_str[11:19].split(":"))

            t_server = utime.mktime((year, month, day, hour, minute, second, 0, 0))
            t_local = time.time()

            server_time_offset = t_server - t_local
            print("Hora sincronizada desde servidor:", server_time_str)
            response.close()
            return True
        else:
            print("Error al obtener hora del servidor:", response.status_code)
            response.close()
    except Exception as e:
        print("Error al sincronizar hora desde API:", e)

    print("Usando hora interna del dispositivo (sin sincronización).")
    return False


def obtener_fecha_iso():
    timestamp = time.time() + server_time_offset
    t = utime.localtime(timestamp)
    return "{:04d}-{:02d}-{:02d}T{:02d}:{:02d}:{:02d}".format(*t[:6])
