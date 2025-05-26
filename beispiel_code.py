#!/usr/bin/env python3

# Einführung Abfangen von Exception
#print('Code snippet ohne try-except-Block')
#user_input = input("Bitte geben Sie ein ganze Zahl ein: ")
#number = int(user_input) # Versuch, die Eingabe in einen Integer zu konvertieren

#print('Code snippet mit try-except-Block')
#try:
#    user_input = input("Bitte geben Sie ein ganze Zahl ein: ")
#    number = int(user_input) #Versuch, die Eingabe in einen Integer zu konvertieren
#    print(f'Die eingegeben Zahl ist: {number}') 
#except ValueError:
#    print('Ungültige Eingabe! Bitte geben Sie eine gültige ganze Zahl ein.')

def überprüfe_positiven_wert(wert: int) -> None:
    if wert <= 0:
        raise ValueError(f"Der Wert {wert} ist nicht positiv! Der Wert muss größer als 0 sein.")
    print (f"Der Wert {wert} ist positiv.")

try:
    zahl = int(input("Bitte geben Sie eine positie Zahl ein: "))
    überprüfe_positiven_wert(zahl)
except ValueError as e:
    print(f"Fehler {e}")
