#!/usr/bin/env python3

# Einführung in Klassen

class Buch:
    """Eine einfache Klasse zur Darstellung eines Buches im Bücherregal."""

    def __init__(self, titel:str, autor: str):
        """Initialisiert das Buch mit einem Titel und einem Autor"""
        self.titel = titel # Öffentliches Attribut
        self.autor = autor # Öffentliches Attribut
        self._status = "verfügbar" # Nicht öffentliches Attribut, das den Ausleihstatus darstellt

    def ausleihen(self):
        """Markiert das Buch als ausgeliehen wenn es verfügbar ist"""
        if self._status == "verfügbar":
            self._status = "ausgeliehen"
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits ausgeliehen.")

    def zurückgeben(self):
        """Markiert das Buch als verfügbar"""
        if self._status == "ausgeliehen":
            self._status = "verfügbar"
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' ist bereits verfügbar.")

    def get_status(self) -> str:
        """Gibt den aktuellen Ausliehstatus des Buches zurück."""
        return self._status

class Bücherregal:
    """Eine Klasse zur Verwaltung eines Bücherregals."""

    def __init__(self):
        """Initialisiert das Bücherregal als leeres Regal."""
        self._bücher = [] # Privates Attribut, das eine Liste von Büchern speichert
    
    def buch_hinzufuegen(self, buch: Buch):
        """Fügt ein Buch zum Bücherregal hinzu."""
        self._bücher.append(buch)
        print(f"Das Buch '{buch.titel}' wurde dem Regal hinzugefügt.")

    def buch_entfernen(self, buch: Buch):
        """Entfernt ein Buch aus dem Bücherregal."""
        if buch in self._bücher:
            self._bücher.remove(buch)
            print(f"Das Buch '{buch.titel}' wurde aus dem Regal entfernt.")
        else:
            print(f"Das Buch '{buch.titel}' ist nicht im Regal.")

    def alle_bücher_anzeigen(self):
        "Zeigt alle Bücher im Regal an."
        if self._bücher:
            print("Bücher im Regal:")
            for buch in self._bücher:
                status = buch.get_status()
                print(f"- {buch.titel} von {buch.autor} (Status: {status})")
        else:
            print("Das Bücherregal ist leer.")



# Erstellung von Büchern
"""buch1 = Buch("Der Hobbit", "J.R.R. Tolkien")
print("Titel lautet",buch1.titel)   # Zugriff auf das öffentliche Attribut 'titel'

buch2 = Buch("1984", "George Orwell")
print("Autor lautet", buch2.autor)  # Zugriff auf das öffentliche Attribut 'autor'
print("Status lautet", buch2.get_status())  # Zugriff auf das provate Attribut 'status' durch den getter

regal = Bücherregal()
regal.buch_hinzufuegen(buch1)
regal.buch_hinzufuegen(buch2)

regal.alle_bücher_anzeigen()
buch1.ausleihen()
regal.alle_bücher_anzeigen()"""

# Aufgabe:
# Erstellen Sie eine Klasse 'Ebike', die die Eigenschaften 'marke', 'modell' und 'reichweite' hat.
# - Implementieren Sie eine Methode 'tanken', die die Reichweite um einen gegebenen Wert erhöht.
# - Stellen Sie sicher, dass der Tankinhalt privat ist und nur über eine Methode abgefragt werden kann.
# - Instanzieren Sie ein Elektrofahrrad und testen Sie die Methoden.

class Ebike():
    def __init__(self, marke: str, modell: str):
        self.marke = marke
        self.modell = modell
        self._reichweite = 0
    
    def tanken(self, liter: int):
        self._reichweite = self._reichweite + liter
        print(f"Es wurden '{liter}' Liter getankt.")

    def get_reichweite(self) -> int:
        return self._reichweite
    
    def print_values(self):
        print("Marke:", self.marke)
        print("Modell:", self.modell)
        print("Reichweite:", self.get_reichweite())
    

Bike1 = Ebike("Honda","T1000")
Bike1.print_values()
Bike1.tanken(14)
Bike1.tanken(77)
Bike1.print_values()

