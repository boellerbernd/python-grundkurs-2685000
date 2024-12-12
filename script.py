#!/usr/bin/env python3

import argparse

# Aufgabe: Erstellen Sie ein Skript, das einfache mathematische Operationen basierend auf Befehlszeilenargumenten durchführt.

# 1. Das Skript soll zwei Pflichtargumente akzeptieren, die als ganze Zahlen eingegeben werden.
#    - 'zahl1': Die erste Zahl, die verwendet wird.
#    - 'zahl2': Die zweite Zahl, die verwendet wird.

# 2. Es soll ein optionales Argument '--operation' geben, das die gewünschte mathematische Operation festlegt:
#    - Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).
#    - Wenn keine Operation angegeben wird, soll standardmäßig die Addition ausgeführt werden.

# 3. Implementieren Sie die Berechnungslogik für die oben genannten Operationen:
#    - Bei der Division soll eine Fehlerbehandlung implementiert werden, um eine Division durch Null zu vermeiden.

# 4. Geben Sie das Ergebnis der Berechnung aus.

import argparse

parser = argparse.ArgumentParser("")
parser.add_argument("zahl1", help="Erste Zahl", type=int)
parser.add_argument("zahl2", help="Zweite Zahl", type=int)
#parser.add_argument("--operation", help="Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).")
parser.add_argument("--operation", choices=["add","sub","mul","div"],default="add", help="Mögliche Optionen: 'add' (Addition), 'sub' (Subtraktion), 'mul' (Multiplikation), 'div' (Division).")
args = parser.parse_args()
ergebnis = None

if args.operation == "add":
    ergebnis = args.zahl1 + args.zahl2
elif args.operation == "sub":
    ergebnis = args.zahl1 - args.zahl2
elif args.operation == "mul":
    ergebnis = args.zahl1 * args.zahl2
elif args.operation == "div":
    if args.zahl2 == 0:
        print("Division durch Null nicht möglich")
    else:
        ergebnis = args.zahl1 / args.zahl2
else:
    print("Operation ungültig")

if ergebnis != None:
    print("Ergebnis:",ergebnis)