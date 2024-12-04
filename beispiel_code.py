#!/usr/bin/env python3

# Schlefen in Python

# for-Schleife: Iteration über eine Liste von Zahlen
zahlen =[1, 2, 3, 4, 5] 
for zahl in zahlen:
  print("Zahl aus der Liste:",zahl)

# for-Schleife: Iteration über einen Bereich (range)
for i in range(1,6):
  print("Aktueller Wert von i:",i)

# while-Schleife: Solange eine Bedingung wahr ist
count = 0
while count < 5:
   print("count ist:",count)
   #count = count + 1 
   count += 1

# while-Schleife mit eienr Bedingung
n = 10
while n > 0:
  print("n ist:", n)
  n -= 2

for i in range(1,11):
  print("i ist:",i)

n=10
while n > 0:
  print("n ist:", n)
  n -=1
