from DAO.DAO import DAO
import sqlite3

class SeanceDAO(DAO):

    @classmethod
    def effacerTous(cls): #à compléter pour prendre en compte les clés étranges
        sql = "DELETE * FROM seances"
        curseur = cls._executer_requete(sql)

        resultat = curseur.rowcount
        return resultat
        
    @classmethod
    def creer(cls, seance):
        
        lignesAffectees = 0
        sql = "INSERT INTO seances ('date') VALUES (?)"
        curseur = cls._executer_requete(sql, [seance.date])
        lignesAffectees += curseur.rowcount
        if lignesAffectees == 1:
            seance.id = curseur.lastrowid
        else:
            raise sqlite3.OperationalError("La seance n'a pas pu être ajoutée à la base de données.")

        return lignesAffectees