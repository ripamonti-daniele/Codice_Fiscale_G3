#file utilizzato per utilizzare le funzioni e realizzare il programma principale

from funzioni import *
from os import system
system("cls")

cognome = ChiediCognome()
nome = chiediNome()
data = chiediDataNascita()
sesso = chiediSesso()
c_cognome = calcolaCodiceCognome(cognome)
c_nome = calcolaCodiceNome(nome)
c_anno = calcolaCodiceAnno(data)
c_mese = calcolaCodiceMese(data)
c_giorno = calcolaCodiceGiorno(data, sesso)
c_comune = calcolaCodiceComune()
codice = (c_cognome + c_nome + c_anno + c_mese + c_giorno + c_comune).upper()
c_controllo = calcolaCodiceControllo(codice)
print(codice + c_controllo)