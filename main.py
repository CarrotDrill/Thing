import random

numero = random.randint(0,10)
Guesses = 3 
Win = False
Active = True



if Active == False and Win == True:
  print("That's right! You win. Restart the program to play again.")

while Active == True:
  while Guesses > 0:
    num = input("Guess a random number from 1 to 10: ")
    num = int(num)
    if num == numero:
      Win = True
      Guesses = 0 
    elif num > numero:
      Guesses = Guesses - 1
      if Guesses != 0:
        print("You have " + str(Guesses) + " tries left. Your number is too big, so guess lower.") 

    elif num < numero: 
      Guesses = Guesses - 1
      if Guesses != 0:
        print("You have " + str(Guesses) + " tries left. Your number is too small, so guess higher.")


  if Guesses == 0 and Win == False:
    print("You're out of guesses. The number was " + str(numero) + ".")
  
  if Win == True:
    print("That's right! You win.")

  
  
  Repeat = input("Do you want to play again? Y/N: ")

  if Repeat == "Y":
    Guesses = 3
    Win = False
    print("Okay, resetting the game.")
    numero = random.randint(0,10)
  else: 
    print("Ending the game.")
    Active = False

#I think it works now, thanks.