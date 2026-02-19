import time
from gpiozero import InputDevice, Motor

# --- CONFIGURATION CAPTEURS ---
line_pin_left = 22
line_pin_middle = 27
line_pin_right = 17

left_sensor = InputDevice(pin=line_pin_left)
middle_sensor = InputDevice(pin=line_pin_middle)
right_sensor = InputDevice(pin=line_pin_right)

# --- CONFIGURATION MOTEURS ---
# On définit les pins de direction et le pin PWM (enable) pour la vitesse
motor_left = Motor(forward=26, backward=21, enable=4)
motor_right = Motor(forward=13, backward=12, enable=5)

# --- CONFIGURATION LEDS ---
led = Adeept_SPI_LedPixel(8, 100)
led.start()

def move_forward(speed):
    motor_left.forward(speed)
    motor_right.forward(speed)
    led.set_all_led_color_data(0, 255, 0) # Vert
    led.show()

def turn_left(speed):
    motor_left.backward(speed)
    motor_right.forward(speed)
    led.set_all_led_color_data(255, 165, 0) # Orange
    led.show()

def turn_right(speed):
    motor_left.forward(speed)
    motor_right.backward(speed)
    led.set_all_led_color_data(255, 165, 0) # Orange
    led.show()

def stop():
    motor_left.stop()
    motor_right.stop()
    led.set_all_led_color_data(255, 0, 0) # Rouge
    led.show()

def run():
    # Lecture des capteurs (1 = Noir/Ligne, 0 = Blanc/Sol)
    status_L = left_sensor.value
    status_M = middle_sensor.value
    status_R = right_sensor.value
    
    speed = 0.4 # Vitesse entre 0 et 1 (commencez doucement !)

    # LOGIQUE DE SUIVI DE LIGNE
    if status_M == 1:
        # Si le capteur du milieu est sur la ligne, on avance
        move_forward(speed)
    elif status_L == 1:
        # Si le capteur gauche touche la ligne, on tourne à gauche
        turn_left(speed)
    elif status_R == 1:
        # Si le capteur droit touche la ligne, on tourne à droite
        turn_right(speed)
    else:
        # Si on ne voit plus rien, on s'arrête
        stop()

if __name__ == '__main__':
    print("Démarrage du suivi de ligne...")
    try:
        while True:
            run()
            time.sleep(0.01) # Boucle rapide pour plus de précision
    except KeyboardInterrupt:
        print("\nArrêt...")
        stop()
        led.led_close()
