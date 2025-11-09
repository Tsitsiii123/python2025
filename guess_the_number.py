import pygame
import random
import math

random.seed()
x=random.random() 
#Απο την βιβλιοθηκη random χρησιμοποιουμε τη συναρτηση random για να παραχθει ενας τυχαιος αριθμος μεταξυ 0 και 1
print("Random number: ", x)

y=math.floor(x*100)+1
#Απο την βιβλιοθηκη math χρησιμοποιουμε τη συναρτηση floor για να στρογγυλοποιησουμε τον αριθμο που παραχθηκε απο την random
#και τον κανει ακεραιο μεταξυ 1 και 100
print("The number to guess is: ", y)

counter = 0
guess = 0

while guess != y:
    guess = int(input("Enter your guess (1-100): "))
    counter += 1
    if guess < y:
        print("Too low! Try again.")
    elif guess > y:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {y} in {counter} attempts.")