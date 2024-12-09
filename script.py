#!/usr/bin/env python3

# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgende Funktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer sollte aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt die erste Zahl ein.
# 2. Benutzer gibt die zweite Zahl ein.
# 3. Benutzer wählt die Operation (+, -, *, /).
# 4. Das Programm führt die Berechnung durch und gibt das Ergebnis aus.

# Optional: Erweitern Sie den Taschenrechner um weitere Funktionen wie Potenzierung oder Modulo.


zahl1 = input("Bitte geben Sie die erste Zahl ein: ")
zahl2 = input("Bitte geben Sie die zweite Zahl ein: ")
operation = input("Bitte geben Sie die Rechenoperation ein: ")

zahl1 = float(zahl1)
zahl2 = float(zahl2)

if operation == "+" :
  ergebnis = zahl1 + zahl2
elif operation == "-":
  ergebnis = zahl1 - zahl2
elif operation == "*":
  ergebnis = zahl1 * zahl2
elif operation == "/":
  ergebnis = zahl1 / zahl2
else:
  print(operation, " ist keine gültige Rechenoperation")
  ergebnis=""

if ergebnis!="":
  print(zahl1, operation, zahl2, "=", ergebnis )