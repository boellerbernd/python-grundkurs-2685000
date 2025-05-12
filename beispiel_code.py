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
            self._status == "ausgeliehen"
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