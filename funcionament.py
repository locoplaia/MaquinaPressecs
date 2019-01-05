from inici import *

# ************************************
# Accions Pulsador
# ************************************
def pulsador_stop_pulsat():
    # llegir estat pulsador stop
    return False


def pulsador_inici_pulsat():
    return True


# ************************************
#   Accions de la base
# ************************************
def anar_rampa():
    servo_base.write_angle(posicio_rampa)


def anar_camera():
    servo_base.write_angle(posicio_abans_camera)
    servo_base.write_angle(posicio_camera)


def anar_compartiment_bo():
    servo_base.write_angle(posicio_compartiment_bons)


def anar_compartiment_dolent():
    servo_base.write_angle(posicio_compartiment_dolents)


# ************************************
#   Accions de les pinzes verticals
# ************************************
def obrir_pinzes_verticals():
    servo_pinza_inferior.write_angle(posicio_servo_inferior_tancat)
    servo_pinza_superior.write_angle(posicio_servo_superior_obert)


def tancar_pinzes_verticals():
    servo_pinza_inferior.write_angle(posicio_servo_inferior_tancat)
    servo_pinza_superior.write_angle(posicio_servo_superior_tancat)


def expulsar():
    servo_pinza_inferior.write_angle(posicio_servo_inferior_obert)
    servo_pinza_superior.write_angle(posicio_servo_superior_obert)


# ************************************
#   Accions de les pinzes horitzontals
# ************************************
def obrir_pinzes_horitzontals():
    servo_pinza_dreta.write_angle(posicio_servo_dreta_obert)
    servo_pinza_esquerra.write_angle(posicio_servo_esquerra_obert)


def tancar_pinzes_horitzontals():
    servo_pinza_dreta.write_angle(posicio_servo_dreta_tancat)
    servo_pinza_esquerra.write_angle(posicio_servo_esquerra_tancat)


    # ************************************
    #   Accions dels servos rotatoris
    # ************************************

def girar_quart_servo_vertical():


def girar_quart_servo_horitzontal():


def girar_mitja_volta_servo_horitzontal():