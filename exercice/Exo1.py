import time
from RobotLight import Adeept_SPI_LedPixel
# Importez ici la bibliothèque de contrôle moteur de votre robot
# de type : from adeept_motor import Motor 

class LineFollower:
    def __init__(self):
        # Initialisation des LEDs (votre code)
        self.led = Adeept_SPI_LedPixel(8, 100)
        self.led.start() # Démarre le thread des LEDs
        
        # Initialisation des moteurs (exemple théorique)
        # self.motor = Motor() 
        
        # Pins des capteurs (à adapter selon votre modèle de robot)
        self.sensor_L = 16
        self.sensor_M = 19
        self.sensor_R = 21

    def run(self):
        print("Démarrage du suivi de ligne...")
        self.led.breath(0, 255, 0) # Vert pour indiquer le fonctionnement
        
        try:
            while True:
                # Lecture des capteurs (0 = Blanc, 1 = Noir)
                # L_val = GPIO.input(self.sensor_L)
                # M_val = GPIO.input(self.sensor_M)
                # R_val = GPIO.input(self.sensor_R)

                # LOGIQUE DE DECISION
                if L_val == 0 and M_val == 1 and R_val == 0:
                    # Tout droit
                    # self.motor.forward(50)
                    self.led.set_all_led_color_data(0, 255, 0) # Vert
                
                elif L_val == 1:
                    # Tourner à gauche
                    # self.motor.left(40)
                    self.led.set_all_led_color_data(255, 165, 0) # Orange
                
                elif R_val == 1:
                    # Tourner à droite
                    # self.motor.right(40)
                    self.led.set_all_led_color_data(255, 165, 0) # Orange
                
                else:
                    # Ligne perdue : on s'arrête ou on cherche
                    # self.motor.stop()
                    self.led.set_all_led_color_data(255, 0, 0) # Rouge
                
                self.led.show()
                time.sleep(0.01)

        except KeyboardInterrupt:
            self.led.led_close()
            # self.motor.stop()

if __name__ == '__main__':
    robot = LineFollower()
    robot.run()
