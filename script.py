#!/usr/bin/env python3

# Aufgabe: Erstellen Sie eine Klasse 'BankAccount', die ein einfaches Bankkonto repräsentiert.

# 1. Die Klasse soll die folgenden Attribute (Member-Variablen) haben:
#    - Inhaber: Der Name des Kontoinhabers (öffentlich).
#    - Kontonummer: Eine eindeutige Kontonummer (öffentlich).
#    - __kontostand: Der aktuelle Kontostand (nicht öffentlich).

# 2. Implementieren Sie die folgenden Methoden:
#    - __init__: Initialisiert den Kontoinhaber, die Kontonummer und den anfänglichen Kontostand.
#    - einzahlen: Erhöht den Kontostand um einen bestimmten Betrag.
#    - abheben: Verringert den Kontostand um einen bestimmten Betrag, wenn genügend Guthaben vorhanden ist.
#    - get_kontostand: Gibt den aktuellen Kontostand zurück.

# 3. Implementieren Sie außerdem eine Methode __str__, die eine benutzerfreundliche Darstellung des Kontos zurückgibt.

# Optional:
# - Erstellen Sie eine Methode, die Transaktionen protokolliert und eine Liste von Ein- und Auszahlungen ausgibt.


class BankAccount:

    def __init__(self, Inhaber: str, Kontonummer: int):
        self.Inhaber = Inhaber
        self.Kontonummer = Kontonummer
        self._kontostand = 0
        self.transaktionen = []

    def __str__(self) -> str:
        return(f"Konto '{self.Kontonummer}' von {self.Inhaber} mit Kontostand von {self._kontostand}")

    def einzahlen(self, betrag: int):        
        self._kontostand = self._kontostand + betrag
        self.transaktionen.append(f"+{betrag}")

    def abheben(self, betrag: int):
        if betrag <= self._kontostand:
            self._kontostand = self._kontostand - betrag
            self.transaktionen.append(f"-{betrag}")
        else:
            print("Kontostand nicht ausreichend.")
    
    def get_kontostand(self) -> int:
        return self._kontostand

konto = BankAccount("Benny", 12345)

print(konto)

konto.einzahlen(5)
konto.einzahlen(7)

konto.abheben(13)
konto.abheben(6)

print(konto)
print(konto.transaktionen)

        
