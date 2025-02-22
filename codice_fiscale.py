#file utilizzato per utilizzare le funzioni e realizzare il programma principale

from funzioni import *
from os import system
system("cls")

def crea_codice():
    codice = ""
    cognome = ChiediCognome()
    nome = chiediNome()
    data = chiediDataNascita()
    sesso = chiediSesso()
    codice += calcolaCodiceCognome(cognome)
    codice += calcolaCodiceNome(nome)
    codice += calcolaCodiceAnno(data)
    codice += calcolaCodiceMese(data)
    codice += calcolaCodiceGiorno(data, sesso)
    codice += calcolaCodiceComune()
    codice = codice.upper()
    codice += calcolaCodiceControllo(codice)
    
    return codice

codice = crea_codice()
print(f"il tuo codice fiscale è: {codice}")
