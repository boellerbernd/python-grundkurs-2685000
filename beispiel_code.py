#!/usr/bin/env python3

# Einführung in Vererbung: Tiere als Beispiel

class Tier:
    """Eine allgemeine Klasse für Tiere."""

    def __init__(self, name: str, alter: int):
        """Initialisiert das Tier mit einem Namen und einem Alter."""
        print("Ein neues Tier wurde erstellt.")
        self.name = name
        self.alter = alter

    def mach_geraeusch(self):
        """Gibt ein allgemeines Geräusch aus."""
        print(f"{self.name} macht ein Geräusch.")

    def beschreibung(self):
        print(f"Dies ist {self.name}, es ist {self.alter} Jahre alt")
    
    def __str__(self) -> str:
        return f"Tier: {self}, Alter: {self.alter}"

class Hund(Tier):
    def mach_geraeusch(self):
        print(f"{self.name} bellt")

class Katze(Tier):
    def __init__(self,name: str, alter: int):
        super().__init__(name,alter)
        print("Eine neue Katze wurde erstellt.")

    def mach_geraeusch(self):
        print(f"{self.name} miaut")

class Vogel(Tier):
    def __init__(self,name: str, alter: int):
        super().__init__(name,alter)
        print("Eine neuer Vogel wurde erstellt.")
    
    def mach_geraeusch(self):
        print(f"{self.name} zwitschert.")


#hund = Hund("Bello", 3)
#katze = Katze("Orang Utan Klaus", 2)

#hund.mach_geraeusch()
#katze.mach_geraeusch()

vogel = Vogel("Tweety",1)
vogel.beschreibung()
vogel.mach_geraeusch()