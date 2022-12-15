from datetime import datetime

from modele.iteration import Iteration

class Seance:

    def __init__(self, *args) -> None:
        nbArgs = len(args)
        
        if nbArgs == 0:
            self._id = None
            self._date = datetime.now()
        elif nbArgs == 1:
            self._id = None
            self.date = args[0]
        else:
            self.id = args[0]
            self.date = args[1]

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, new_id):
        #Validation du paramètre
        if not isinstance(new_id, int):
            raise TypeError("L'id d'une seance doit être un entier.")
        
        self._id = new_id

    @property
    def date(self):
        return self._date

    def __str__(self):

        if self.id is None:
            idStr = "non défini"
        else:
            idStr = str(self.id)
        
        date = self._date.strftime("%d-%m-%Y, %H:%M:%S")
        strPartie = "ID : "+idStr+" - ["+date+"]"

        return strPartie