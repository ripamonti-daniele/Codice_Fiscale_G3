# file per creare le funzioni
import datetime
#COLONNA C

comuni = {
    "Alpette","Lesa" ,"Galliate" ,"Bra","Moiola" ,"Valgrana","Castellero" ,"Robella" ,"Cartosio" , "Magnano" 
}
def rimuoviLettereAccentate(s):
    sostituzioni = {
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
        'À': 'A', 'È': 'E', 'Ì': 'I', 'Ò': 'O', 'Ù': 'U'
    }
    
    risultato = ""
    
    for c in s:
        if c in sostituzioni:
            risultato += sostituzioni[c]
        else:
            risultato += c
    
    return risultato

def chiedicomune(comuni):
    stop = True
    while stop:
        stop = False
        comune = input("inserisci il comune: ").capitalize()
        if comune in comuni:
            stop = True
            return comune
        else:
            print("Errore, il comune non e valido")

def calcolaCodiceMese():
    alfabeto = ("A", "B" ,"C", "D", "E", "H", "L", "M", "P", "R", "S", "T")
    data_input = input("Inserisci la tua data di nascita (formato YYYY-MM-DD): ")
    data_nascita = datetime.datetime.strptime(data_input, "%Y-%m-%d")
    mese_nascita = data_nascita.month
    for i in range(12):
        if i == mese_nascita:
            codice = alfabeto[i-1]
            return codice


def calcolaCodiceNome(nome):
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vocali = "aeiouAEIOU"
        
    risultato = ""
    count = 0

    for c in nome:
        if c in consonanti:
            risultato += c
            count += 1
        if count == 3:
            return risultato

    for c in nome:
        if c in vocali:
            risultato += c
            count += 1
        if count == 3:
            return risultato

    return risultato


def rimuoviSpazi(stringa):
    risultato = ""
    for c in stringa:
        if c != " ":
            risultato += c
    return risultato




