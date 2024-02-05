#!/usr/bin/python3
 def fizbuzz():
     for Num in range (1, 101):
         if Num % 3 == 0:
             print(f"Fizz", end" ")
         elif Num % 5 == 0:
             print(f"Buzz", end" ")
         else:
             print(f"{Num}", end" ")
