#!/usr/bin/env python3

# Bedingte Anweisungen in Python

# Variablen
x = 10
y = 5

# Einfache if Bedingung
if x > y:
  print("x ist größer als y")

# if-else-Bedingung
if x <= y:
  print("x ist kleiner als y")
else:
  print("x ist nicht kleiner als y")

# if-elif-else
if x == y:
  print("x ist gleich y")
elif x > y:
  print("x ist größer als y")
else:
  print("x ist kleiner als y")


a = 2.3
b = 5.9

if a >= b:
  print("a ist größer oder gleich b")
else:
  print("a ist kleiner als b")


z = 15
# and-Verknüpfung: Beide Bedingungen müssen wahr sein
if x > y and x < z:
  print("x ist größer als y und kleiner als z")

# or-Verknüpfung: eine Bedingung muss wahr sein
if x < y or x < z:
  print("x ist entweder kleiner als y oder kleiner als z")


var1 = 3
var2 = 6
var3 = 12

if var2 < var3 and var2 > var1:
  print("var3 ist in der Mitte")

if var3 > var2 or var3 > var1:
  print("var ist entweder größer als var2 oder als var1")