from art import logo
import random

def set_difficulty():
  
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
  if(difficulty=='easy'):
    return 10
  else:
    return 5
    
def check_answer(guess,number,turns):
  
  if(guess<number):
    print("Too Low ")
    return turns-1
  elif(guess>number):
    print("Too High")
    return turns-1
  else:
    print(f"You got it the answer was {number}")
  
def game():
  print(logo)
  print("Welcome to the number guessing game")
  print("I'm thinking of a number between 1 and 100")
  number=random.randint(0,100)
  turns=set_difficulty()
  guess=101
  while(guess!=number):
    print(f"You have {turns} turns left")
    guess=int(input("Make a Guess: "))
    turns=check_answer(guess,number,turns)
    if(turns==0):
      print(f"You ran out of turns try again {number} was the answer")
      return
    elif(guess!=number):
      print("Guess Again")
      
game()   
