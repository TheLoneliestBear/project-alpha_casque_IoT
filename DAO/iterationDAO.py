import sqlite3

from DAO.DAO import DAO
from modele.iteration import Iteration

class IterationDAO(DAO):
    @classmethod
    def lireTous(cls):
        iterations = list()

        sql = "SELECT * FROM iterations"
        curseur = cls._executer_requete(sql)

        resultat = curseur.fetchall()
        for enregistrement in resultat:
            iterations.append(Iteration(enregistrement["id"], enregistrement["seanceId"], enregistrement["distance"], enregistrement["lumiere"], enregistrement["indiceDanger"], enregistrement["indiceDanger"]))
        return iterations

    @classmethod
    def chercherParId(cls, id):
        sql = "SELECT * FROM iterations WHERE id = ?"
        curseur = cls._executer_requete(sql, [id])

        resultat = curseur.fetchone()

        if resultat is None:
            iteration = None
        else:
            iteration = Iteration(enregistrement["idSeance"], enregistrement["distance"], enregistrement["lumiere"], enregistrement["indiceDanger"])
            iteration.date = enregistrement["date"]

        return iteration

    @classmethod
    def creer(cls, iteration):
      
        lignesAffectees = 0
        
        sql = "INSERT INTO iterations ('idSeance', 'distance', 'lumiere', 'indiceDanger', 'date') VALUES (?, ?, ?, ?, ?)"
        curseur = cls._executer_requete(sql, [iteration.seanceId, iteration.distance, iteration.lumiere, iteration.indicateurDanger, iteration.date.strftime("%d-%m-%Y, %H:%M:%S")])
        lignesAffectees = curseur.rowcount
        if lignesAffectees == 1:
            iteration.id = curseur.lastrowid
        else:
            raise sqlite3.OperationalError("L'itération n'a pas pu être ajoutée à la base de données.")

        return lignesAffectees

    @classmethod
    def effacerTous(cls):
        sql = "DELETE * FROM iterations"
        curseur = cls._executer_requete(sql)

        return curseur.rowcount