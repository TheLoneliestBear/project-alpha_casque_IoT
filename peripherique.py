import configparser
from gpiozero import LED
import time
import PCF8591 as ADC
import RPi.GPIO as GPIO

from exceptions.peripheriqueException import PeripheriqueException

class Peripherique:
    def __init__(self) -> None:
        
        #self._LEDs = list()
        #self.ultrasonicTRIG = null
        #self.ultrasonicECHO = null
        #self._photoresistorDO = null
        
        #LEDR = null
        #LEDG = null
        
        #DO = null
        
        #Buzzer = null
        
        #TRIG = null
        #ECHO = null
        
        GPIO.setmode(GPIO.BCM)
        
        #LED       
        self._LEDR = 20
        self._LEDG = 21
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._LEDR, GPIO.OUT)
        GPIO.output(self._LEDR, GPIO.LOW)
        GPIO.setup(self._LEDG, GPIO.OUT)
        GPIO.output(self._LEDG, GPIO.LOW)
            
        #Photoresistor
        self._DO = 25
        GPIO.setmode(GPIO.BCM)
        ADC.setup(0x48)
        GPIO.setup(self._DO, GPIO.IN)
            
            
        #Buzzer
        self._Buzzer = 27
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._Buzzer, GPIO.OUT)
        GPIO.output(self._Buzzer, GPIO.HIGH)
            
            
        #Ultrasonic
        self._TRIG = 24
        self._ECHO = 16
        #GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._TRIG, GPIO.OUT)
        GPIO.setup(self._ECHO, GPIO.IN)
            
            
        #PCF8591
        #?
        
        

    def setup(self, fichierConfig):
        #Lecture du fichier de configuration
        config_obj = configparser.ConfigParser()

        try:
            config_obj.read(fichierConfig)
            #LEDsParam = config_obj["LED"]
            
            #ultrasonicTRIG = (config_obj["TRIG"])
            #ultrasonicECHO = (config_obj["ECHO"])
            #photoresistorDO = (config_obj["DO"])

            #récupère la config des LED 
            #for led in LEDsParam:
                #self._LEDs.append(LED(LEDsParam[led]))
            
            
            
            

        except Exception as err:
            raise PeripheriqueException("Échec de la configuration des périphériques")

    @property   
    def LEDR(self):
        return self._LEDR
    
    @property   
    def LEDG(self):
        return self._LEDR
    
    @property   
    def DO(self):
        return self._DO
    
    @property   
    def Buzzer(self):
        return self._Buzzer
    
    @property   
    def TRIG(self):
        return self._TRIG
    
    @property   
    def ECHO(self):
        return self._ECHO

    def allumer_LEDR(self):
        GPIO.output(self._LEDR, GPIO.HIGH)

    def eteindre_LEDR(self):
        GPIO.output(self._LEDR, GPIO.LOW)
        
    def allumer_LEDG(self):
        GPIO.output(self._LEDG, GPIO.HIGH)

    def eteindre_LEDG(self):
        GPIO.output(self._LEDG, GPIO.LOW)
        
    def allumer_Buzzer(self, x):
        GPIO.output(self._Buzzer, GPIO.LOW)
        time.sleep(x)
        
    def eteindre_Buzzer(self):
        GPIO.output(self._Buzzer, GPIO.HIGH)
        
    def observerDistance(self):
        GPIO.output(self._TRIG, 0)
        time.sleep(0.000002)

        GPIO.output(self._TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(self._TRIG, 0)

        
        while GPIO.input(self._ECHO) == 0:
            a = 0
        time1 = time.time()
        while GPIO.input(self._ECHO) == 1:
            a = 1
        time2 = time.time()

        during = time2 - time1
        return during * 340 / 2 * 100
    
    def observerLumiere(self):
        return ADC.read(0)
