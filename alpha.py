from modele.iteration import Iteration
from modele.seance import Seance

from DAO.DAO import DAO
from DAO.iterationDAO import IterationDAO
from DAO.seanceDAO import SeanceDAO
import RPi.GPIO as GPIO

from peripherique import Peripherique

from exceptions.peripheriqueException import PeripheriqueException
from exceptions.bdconfigexception import BdConfigException

from datetime import datetime
import time

class Alpha() :

    def __init__(self, fichierConfig) -> None:
        
        self.__peripherique = None
        self.__seance = None    
        self.__configuration = fichierConfig
        self._derniereIteration = Iteration(0,0,0,0)
        

    def _lancerAlerteSonore(self, x):
        print("ATTENTION - Operateur statique")
        self.__peripherique.allumer_Buzzer(x)
        
    def _arreterAlerteSonore(self):
        self.__peripherique.eteindre_Buzzer()
        
    def _allumerLampe(self):
        print("ATTENTION - Niveau de lumière faible... lampe allumée\n\n")
        self.__peripherique.allumer_LEDG()
    
    def _eteindreLampe(self):
        print("Niveau de lumière normale... lampe éteinte\n\n")
        self.__peripherique.eteindre_LEDG()

    def __effectuerIteration(self, y, z): 
        
        distance = round(self.__peripherique.observerDistance(),0)
        lumiere = self.__peripherique.observerLumiere()
        args = list()
        args.append(y)
        args.append(distance)
        args.append(float(lumiere))
        args.append(int(z))
        print(args)
        iteration = Iteration(y, distance, float(lumiere), z)
        return iteration
    
        
    @property
    def seance(self):
        return self.__seance
    
    @property
    def derniereIteration(self):
        return self._derniereIteration


    def main(self):

        try:
    
            #Configuration des capteurs/effecteurs
            self.__peripherique = Peripherique()
            self.__peripherique.setup(self.__configuration)
            i = 0
            
            #Configuration de la bd
            DAO.setup(self.__configuration)

            #Créer une seance
            self.__seance = Seance()
            d = self.__seance.date.strftime("%d-%m-%Y  %H:%M:%S")
            print("\nSeance - START\t" + d + "\n")
            resultat = SeanceDAO.creer(self.__seance)

            #Effectuer une itération
            print("_ ___ Iteration start ___ _")
            while True :
                
                print("\n\nseance ID : "+str(self.__seance.id))#---
                print("derniere iteration : "+str(self._derniereIteration))
                it = self.__effectuerIteration(self.__seance.id, self._derniereIteration.indicateurDanger)
                print("Distance de l'itération actuelle : " + str(round(it.distance, 0)))
                print("Distance de la dernière itération : "+str(round(self._derniereIteration.distance, 0)))
                if round(it.distance, 0) == round(self._derniereIteration.distance, 0) :
                    it.indicateurDanger += 10
                else :
                    it.indicateurDanger = 0

                #Enregistrer l'itération dans la bd
                IterationDAO.creer(it)

                print(it)
                
                if it.indicateurDanger > 50 :
                    self._lancerAlerteSonore(1)
                else:
                    self._arreterAlerteSonore()
                    
                if it.lumiere < 100 :
                    self._allumerLampe()
                else:
                    self._eteindreLampe()
         
                self._derniereIteration = it
                time.sleep(1)

        except PeripheriqueException as err:
            print(err)
            traceback.print_exc()

        except BdConfigException as err:
            print(err)
            traceback.print_exc()

        #except Exception as err:
            #print("une erreur inatendue est survenue ", err)
            #traceback.print_exc()
            
    
if __name__ == "__main__":
    alpha = Alpha("config.ini")
    #alpha._setup()
    try:
        alpha.main()
    except KeyboardInterrupt:
        #etteindre leds, capteurs, etc.
        GPIO.cleanup()
            