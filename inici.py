from servopi import Servo
# Botons d'Inici i Parada

pulsador_dinici = 0
pulsador_stop = 0

# Configuracions Servos

servo_base = Servo(11, 'Mg995')
servo_pinza_superior = Servo(11, 'Mg995')
servo_pinza_inferior = Servo(11, 'Mg995')
servo_pinza_esquerra = Servo(11, 'Mg955')
servo_pinza_dreta = Servo(11, 'Mg955')
servo_rotatori_y = Servo(11, 'Mg955')
servo_rotatori_x = Servo(11, 'Mg955')

# Posicions Servo Base

posicio_rampa = 150
posicio_abans_camera = 80
posicio_camera = 70
posicio_compartiment_bons = 35
posicio_compartiment_dolents = 5

# Posicions Servos Pinzes Verticals

posicio_servo_inferior_obert = 30
posicio_servo_inferior_tancat = 50

posicio_servo_superior_obert = 120
posicio_servo_superior_tancat = 140

# Posicions Servos Pinzes Horitzontals

posicio_servo_esquerra_tancat = 0
posicio_servo_esquerra_obert = 10

posicio_servo_dreta_tancat = 15
posicio_servo_dreta_obert = 0
