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


#Colonna A
def ChiediCognome():
    error = True
    while error:
        error = False
        cognome = input("Inserisci il tuo cognome: ").capitalize()
        if not cognome.isdigit():
            print("Errore: caratteri non validi")
            error = True
        else:
            if len(cognome) < 2 or len(cognome) > 30:
                print("Errore: cognome troppo corto o troppo lungo")
                error = True
            else:
                rimuoviLettereAccentate()
                rimuoviSpazi()
                return cognome
            
def  chiediDataNascita():
    error = True
    while error:
        error = False
        try:
            dataStr = input("Inserisci la tua data di nascita (formato: DD-MM-YYYY): ")
            data_nascita = datetime.datetime.strptime(dataStr, "%d-%m-%Y").date()
            if data_nascita > datetime.datetime.today().date():
                print("Errore: La data di nascita non può essere nel futuro")
                error = True
            else:
                return data_nascita
        except:
            print("Formato non valido")
            error = True

def calcolaCodiceComune():
    comuni_codici = {
        "Alpette": "A221",
        "Lesa": "E544",
        "Galliate": "A432",
        "Bra": "A511",
        "Moiola": "A603",
        "Valgrana": "A714",
        "Castellero": "A755",
        "Robella": "A818",
        "Cartosio": "A881",
        "Magnano": "A059"  
    }
    error = True
    while error:
        error = False 
        comune = chiedicomune(comuni)
        
        if comune in comuni_codici:
            return comuni_codici[comune] 
        else:
            print("Errore: comune inserito non valido. Riprova.")
            error = True

def calcolaCodiceAnno(data_nascita):
    return str(data_nascita.year)[-2:]

def calcolaCodiceCognome(cognome):
    consonanti = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vocali = "aeiouAEIOU"
    
    risultato = ""

    for c in cognome:
        if c in consonanti:
            risultato += c
        if len(risultato) == 3:
            return risultato

    for c in cognome:
        if c in vocali:
            risultato += c
        if len(risultato) == 3:
            return risultato

    while len(risultato) < 3:
        risultato += "X"
    
    return risultato
