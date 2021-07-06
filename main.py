import random

numero = random.randint(0,10)
print(numero)
Guesses = 3 
Win = False
Active = True

while Active == True:
  while Guesses > 0:
    num = input("Guess a random number from 1 to 10: ")
    if num == numero:
      print("That's right! You win.")
      Active = False 

    else:
      Guesses = Guesses - 1
      print("Not quite. You have " + str(Guesses) + " tries left. Try again.")
  else: 
    print("You are out of guesses. Restart the program to play again.")
    Active = False

     