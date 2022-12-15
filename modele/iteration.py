from datetime import datetime

class Iteration:
    def __init__(self, *args) -> None:
        nbArgs = len(args)

        #Validation du nombre
        if nbArgs > 4:
            raise TypeError("Le constructeur Iteration prend 4 ou 5 paramètres.")
        if nbArgs == 4:
            self._id = None
            self._seanceId = int(args[0])
            self._distance = float(args[1])
            self._lumiere = float(args[2])
            self._indicateurDanger = int(args[3])
            self._date = datetime.now()
        else:
            self._id = int(args[0])
            self._seanceId = int(args[1])
            self._distance = float(args[2])
            self._lumiere = float(args[3])
            self._indicateurDanger = int(args[4])
            self._date = datetime.now()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, new_id):
        #Validation du paramètre
        if not isinstance(new_id, int):
            raise TypeError("L'id du joueur doit être un entier.")
        
        self._id = new_id
          
    @property
    def seanceId(self):
        return self._seanceId

    @seanceId.setter
    def seanceId(self, new_seanceId):
        #Validation du paramètre
        if not isinstance(new_seanceId, int):
            raise TypeError("L'id du joueur doit être un entier.")
        
        self._seanceId = new_seanceId

    @property
    def distance(self):
        return self._distance

    @distance.setter
    def distance(self, new_distance):
        #Validation du paramètre
        if not isinstance(new_distance, float):
            raise TypeError("La distance mesurée d'une iteration doit être un float.")
        
        self._distance = new_distance
        
    @property
    def lumiere(self):
        return self._lumiere

    @lumiere.setter
    def lumiere(self, new_lumiere):
        #Validation du paramètre
        if not isinstance(new_lumiere, float):
            raise TypeError("La mesure du niveau de lumière d'une iteration doit être un float.")
        
        self._lumiere = new_lumiere
        
    @property
    def indicateurDanger(self):
        return self._indicateurDanger

    @indicateurDanger.setter
    def indicateurDanger(self, new_indicateurDanger):
        #Validation du paramètre
        if not isinstance(new_indicateurDanger, int):
            raise TypeError("L'indicateur de danger d'une iteration doit être un entier.")
        
        self._indicateurDanger = new_indicateurDanger
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, new_date):
        #Validation du paramètre
        if not isinstance(new_date, datetime):
            raise TypeError("La date d'une iteration doit être de type datetime")
        
        self._date = new_date

    def __str__(self):
        if self.id is None:
            idStr = "non défini"
            seance = str(self._seanceId)
            distance = str(self._distance)
            lumiere = str(self._lumiere)
            indiceDanger = str(self._indicateurDanger)
            date = self._date.strftime("%d-%m-%Y, %H:%M:%S")
        else:
            idStr = str(self.id)
            seance = str(self._seanceId)
            distance = str(self._distance)
            lumiere = str(self._lumiere)
            indiceDanger = str(self._indicateurDanger)
            date = self._date.strftime("%d-%m-%Y, %H:%M:%S")
        resultat = ""+idStr+" "+seance+" "+distance+" "+lumiere+" "+indiceDanger+" "+date
        return resultat