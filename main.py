import random

numero = random.randint(0,10)
print(numero)
Guesses = 3 
Win = False
Active = True

if Guesses == 0:
  print("You're out of guesses. Restart the program to play again.")

elif Active == False and Win == True:
  print("That's right! You win. Restart the program to play again.")

while Active == True:
  while Guesses > 0:
    num = input("Guess a random number from 1 to 10: ")
    num = int(num)
    if num == numero:
      Active = False 
      Win = True
      Guesses = 0 
    elif num > numero:
      Guesses = Guesses - 1
      print("You have " + str(Guesses) + " tries left. Your number is too big, so guess lower.")
    elif num < numero: 
      Guesses = Guesses - 1
      print("You have " + str(Guesses) + " tries left. Your number is too small, so guess higher.")