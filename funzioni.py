# file per creare le funzioni
import datetime
#COLONNA C

comuni = {
    "Alpette","Lesa" ,"Galliate" ,"Bra","Moiola" ,"Valgrana","Castellero" ,"Robella" ,"Cartosio" , "Bergamo" 
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

def calcolaCodiceMese(data):
    alfabeto = ("A", "B" ,"C", "D", "E", "H", "L", "M", "P", "R", "S", "T")
    mese_nascita = data.month
    for i in range(12):
        if i + 1 == mese_nascita:
            codice = alfabeto[i]
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
        cognome = rimuoviLettereAccentate(cognome)
        cognome = rimuoviSpazi(cognome)
        if not cognome.isalpha():
            print("Errore: caratteri non validi")
            error = True
        else:
            if len(cognome) < 2 or len(cognome) > 30:
                print("Errore: cognome troppo corto o troppo lungo")
                error = True
            else:
                return cognome
            
def chiediDataNascita():
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
        "Bergamo": "A794"  
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

#colonna b
def chiediNome():
    while True:
        nome = input("Inserisci il tuo nome: ").capitalize().strip()
        nome = rimuoviLettereAccentate(nome)
        nome = rimuoviSpazi(nome)
        if not nome.isalpha():
            print("Errore: caratteri non validi")
        elif len(nome) < 2 or len(nome) > 30:
            print("Errore lunghezza nome (min 2 max 30)")
        else:
            return nome
        
def chiediSesso():
    while True:
        sesso = input("Inserisci il tuo sesso (m/f): ").strip().lower()
        
        if sesso != "m" and sesso != "f":
            print("errore: inserisci m oppure f")
        else:
            return sesso
        
def calcolaCodiceGiorno(data, sesso):   
    g = data.day
    if sesso == "f":
        g += 40
    g = str(g)
    if len(g) == 1:
        g = "0" + g
    
    return g

def calcolaCodiceControllo(codice):
    pari = ""
    dispari = ""
    for i in range(len(codice)):
        if (i + 1) % 2 == 0:
            pari += codice[i]
        else:
            dispari += codice[i]
            
    conv_dispari = {
        "0": 1, "1": 0, "2": 5, "3": 7, "4": 9, "5": 13, "6": 15, "7": 17, "8": 19, "9": 21, 
        "A": 1, "B": 0, "C": 5, "D": 7, "E": 9, "F": 13, "G": 15, "H": 17, "I": 19, "J": 21, "K": 2, "L": 4, "M": 18,
        "N": 20, "O": 11, "P": 3, "Q": 6, "R": 8, "S": 12, "T": 14, "U": 16, "V": 10, "W": 22, "X": 25, "Y": 24, "Z": 23
    }
    
    conv_pari = {}
    n = 0
    for i in ("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        conv_pari[i] = n
        if i == "9":
            n = 0
        else:
            n += 1
    
    tot = 0
    for i in pari:
        tot += conv_pari[i]
    for i in dispari:
        tot += conv_dispari[i]
        
    while tot >= 26:
        tot -= 26
    
    conversioni = {}
     
    lettere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(26):
        conversioni[i] = lettere[i]
        
    return conversioni[tot]