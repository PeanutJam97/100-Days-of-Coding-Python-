from game_data import data
from arthigherlower import logo
from art import vs
from replit import clear
import random



def check_answer(guess, a_followers, b_followers):
# if followers for A > followers for B and person chose a, return true else false vice versa
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'
    
def game():
  print(logo)

  gameABdictionary = {}
  currentscore = 0
  gameover = False
  randomindex = random.randint(0, len(data))
  randomindex1 = random.randint(0, len(data))
  
  while not gameover:
    randomindex = randomindex1
    randomindex1 = random.randint(0, len(data))

    while randomindex == randomindex1:
      randomindex1 = random.randint(0, len(data))
    
    print(f"Compare A: {data[randomindex]['name']}, a {data[randomindex]   ['description']}, from a {data[randomindex]['country']}.")
    print(vs)
    print(f"Compare B: {data[randomindex1]['name']}, a {data[randomindex1]['description']}, from {data[randomindex1]['country']}.")
    
    AorB = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    gameABdictionary.update({'A':data[randomindex]['follower_count']})
    gameABdictionary.update({'B':data[randomindex1]['follower_count']})

    iscorrect = check_answer(AorB, gameABdictionary['A'], gameABdictionary['B'])

    clear()
    print(logo)
    if iscorrect:
      currentscore += 1
      print(f"You're right! Current Score: {currentscore}")
    else:
      gameover = True
      print(f"Sorry, that's wrong. Final score: {currentscore}")

      
      
      
      
    
    

game()