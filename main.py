from inici import *
from funcionament import *
import time

def main():

# Inicialitzacions

# Inicia camara
# Configurar Inici Stop
    while (not(pulsador_stop_pulsat()) and pulsador_inici_pulsat()):
        obrir_pinzes_verticals()
        if (not(pulsador_stop_pulsat())):
            obrir_pinzes_horitzontals()
        if (not (pulsador_stop_pulsat())):
            anar_rampa()
        if (not (pulsador_stop_pulsat())):
            time.sleep(3)
        if (not (pulsador_stop_pulsat())):
            tancar_pinzes_verticals()
        if (not (pulsador_stop_pulsat())):
            tancar_pinzes_horitzontals()
        if (not (pulsador_stop_pulsat())):
            anar_camera()
        
if __name__ == "__main__":
    main()



