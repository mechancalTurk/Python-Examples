# Python Besonderheiten 
# HPI
# B. Ege

# Python ist Case-Sensitive!
# https://www.python.org/
# https://docs.python.org/3/tutorial/
# https://www.w3schools.com/python/

import sys
print("sys.version: ", sys.version)

print ('hello, world!')
print ("hello, world!")
print ("hello, world!", 'hello, world', 'hello, world3!')

myFilename = "xxx"
#print(Myfilename)   # würde einen NameError liefern, weil zu dieser Variable kein Wert zugewiesen ist
print(myFilename)   # Python ist Case-Sensitive!

###### STRINGS ######

# Mithilfe von + können Strings aneinander gehängt werden
print ("Hello" + " " + "Börtecin")

# Mithilfe von * können Strings mehrfach wiederholt werden
myName = "Börtecin"
vierMal_myName = 4 * myName
print(vierMal_myName)

# Länge von Strings
print("Die Länge des Strings Börtecin: " + str(len(myName)))

text = "Turkish Airlines"
anz = len(text)
print("Anzahl der Zeichen: " + str(anz))

# Platzhalter 
# {variable} dient als Platzhalter in f-Strings 
# Platzhalter werden nur innerhalb von einem f-String erkannt.
# Rein theoretisch muss ein f-String keine Platzhalter enthalten. 
person = "Börtecin"
speise = "Kuchen"
satz = f"{person} isst {speise}, weil er {speise} mag."
print(satz)

# Arithmetische Operationen mit print()
print(5+5)
print(5*5)
print(5-5)
print(10/2)
print(4+(3-1)*5)

alter = 12
alter = alter+1
print(alter)
print(alter*2)

print("3" + "4", 3+4)

for zahl in (0, 1, 2, 3):
    print(zahl);
for zahl in range(3):
    print(zahl);

verbleibendeZeit = 40;
while verbleibendeZeit >= 15:
    verbleibendeZeit = verbleibendeZeit - 15;
    print("Verbleibende Zeit: " + str(verbleibendeZeit));
print("Jetzt ist es Pause!")

a = 10
b = 1
while a > 3:   
    if a < 9:        
        print("Hallo")        
        a = a - 1;  
    a = a - 1;
    print("a: " + str(a))
b = b + 1;    
print("b: " + str(b))

# split()
my_string="Hello this is, a split operation!" 
print(my_string)
split_text = my_string.split(",")
print(split_text)

# strip()
my_string="     Hello this is, a strip operation!" 
trimmed = my_string.strip()
print(trimmed)

######## VARIABLEN ########
c=20
c:10
print("c: ", c)


########  LISTEN ##########
# Listen ermöglichen es, mehrere Daten zusammenzuspeichern
# Enthalten Elemente, die in eckige Klammern [] geschrieben und durch Kommata , getrennt werden
# Gleiche Elemente können mehrfach vorkommen
# Listen können mit + kombiniert und mit * wiederholt werden

myList = ["XXX", "Regenjacke", "Lampe"]
myList[0] = "Stift"
print("Meine Liste: " + str(myList));
print("Meine Liste: " + str(myList)*2);
print("Meine Liste: " + myList[0][3]);
anz = len(myList)
print("Anzahl der ListenElemente: " + str(anz))

# Hinzufügen eines neuen Elements in die LIste
myList.append("Taschenlampe")
print("Meine aktualisierte Liste: " + str(myList));

# Entfernen eines Elements von der Liste
myList.pop()
print("Meine aktualisierte Liste: " + str(myList));

# Entfernen eines Elements von der Liste
myList.pop(0)
print("Meine aktualisierte Liste: " + str(myList));
myList[-1] = "Regenschirm"
print("Meine aktualisierte Liste: " + str(myList));

# Elemente einer Liste können verschiedene Datentypen besitzen
# Eine Liste kann eine andere Liste as Element haben
# Zugriff über die verschachtelte Indexierung
# Slicing:
#         0       1      2       3      4       5
codes = ["rot", [1,8], "grün", [1,5], "gelb", [2,3]]
print("codes: " + str(codes));
print("codes[2:4]: " + str(codes[2:4]));
print("codes[4]: " + str(codes[4:]));

# Split()
# Teilt eine Zeichenkette in einzelne Wörter auf
# Gibt eine Liste zurück
satz = "Turkish Airlines is the best!"
geteilterSatz = satz.split();
print("geteilterSatz: " + str(geteilterSatz));

for wort in geteilterSatz:
    print(wort)

for wort in geteilterSatz:
    if (wort[0] == 't') or (wort[0] == 'T'):
        print(wort)

# Join()
# Fügt Liste von Strings zu einem String zusammen
verbundenerSatz = " ".join(geteilterSatz)
print("verbundenerSatz: " + verbundenerSatz);


###### FUNKTIONEN ##########
def funktion(a:int,b):
    ergebnis = a + b;
    return ergebnis;

c = funktion(3,4);
print("Ergebnis: " + str(c));


attraktionen = ["London Eye", "big Ben", "Bosphorus", "Bogazici"]

def startet_mit_b(attraktion, buchstabe):
    ergebnis = attraktion[0] == buchstabe
    return ergebnis;

def attraktionen_mit_b(liste):
    ergebnis = []
    for attraktion in liste:
        if startet_mit_b(attraktion, "B"):
            ergebnis.append(attraktion)
    return ergebnis;

print(attraktionen_mit_b(attraktionen));

######## DICTIONARIES ##########
wohnorte = {
    "Börtecin": "Wien",
    "Gülcin": "Izmir",
    "Behzat": "Stuttgart"
}

# Wert hinzufügen
wohnorte["Marion"] = "Erlangen"

anzahlPaare = len(wohnorte)
print("Dictionary-Größe: " + str(anzahlPaare));
print("Börtecin wohnt in", wohnorte["Börtecin"]);
print("Marion wohnt in", wohnorte["Marion"]);
del(wohnorte["Marion"]);
anzahlPaare = len(wohnorte)
print("Dictionary-Größe: " + str(anzahlPaare));

# Dictionary.keys()
# Gibt alle Schlüssel des Dictionaries zurück
# Man kann mit einer For-Schleife über diese iterieren
for schluessel in wohnorte.keys():
    print("Name: " + schluessel);

# Dictionary.values()
# Gibt alle Schlüssel des Dictionaries zurück
# Man kann mit einer For-Schleife über diese iterieren
for wert in wohnorte.values():
    print("Stadt: " + wert);
# Dictionary.items()
# Gibt alle Paare (Schlüssel und Wert) des Dictionaries zurück
# Man kann mit [0] auf dern Schlüssel zugreifen und mit [1 auf den Wert]
for paar in wohnorte.items():
    print(paar[0] + " wohnt in " + paar[1]);

##### ZUFALLSZAHLEN ########
# random() gibt eine zufällige Zahl zwischen 0 und 1 zurück (Float)
from random import random
zahl = random()
print(zahl)

# randint(start, ende)
# Gibt eine zufällige ganze Zahle zwischen diesen zurück (start und ende eingeschlossen)
from random import randint
zahl = randint(1,7)
print(zahl)

###### EINGABE ##########
#name = input("Wie heißt Du?")
#print(f"Hallo {name}")

try:
    anz_bisher = 10
    anz = int(input("Wie viele seid Ihr?"))
    print(f"Insgesamt sind wir {anz_bisher + anz}.")
except ValueError:
        print("Die Eingabe war nicht gültig!");


# \n means a new line!








