#!/usr/bin/env python3

# Eingaben über die Kommandozeile
# Einlesen eines Strings
name = input("Bitte geben Sie Ihren Namen ein: ")
print("Hallo, " + name + "!")

# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie Ihr Alter ein: ")
alter = int(alter)
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.")

# Berechnung mit der Eingabe
jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
  print("In " + str(jahre_bis_30) + " Jahren werden Sie 30.")
else:
  print("Sie sind bereits 30 Jahre alt oder älter.")



film = input("Nennen Sie bitte Ihren Lieblingsfilm: ")
zahl = input("Nennen Sie bitte Ihre Lieblingszahl: ")

neue_zahl = int(zahl) + 14.5

print("Ihr Lieblingsfilm lautet: " + film)
print("Ihre Lieblingszahl addiert mit 14.5 lautet:",neue_zahl)