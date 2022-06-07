import random
from replit import clear
from art import logo, vs
from game_data import data

def random_num(list):
  """Generates a random number in a list length range"""
  return random.randint(0,len(list)-1)

def compare(dict_a,dict_b):
  """Compares the highest of two given values"""
  return max(dict_a["follower_count"],dict_b["follower_count"])

def generate_option():
  """Chooses a random dictionary"""
  return data[random_num(data)]

def new_comparison(o1,o2):
  """Prints to console new comparison"""  
  print(f"Compare A: {o1['name']}, a {o1['description']} from {o1['country']}.")
  print(vs)
  print(f"Against B: {o2['name']}, a {o2['description']} from {o2['country']}.")
  
a = generate_option()
b = generate_option()

print(logo)

new_comparison(a,b)
  
should_end = False
score = 0
highest = compare(a,b)
answer = input("Who has the more followers? Type 'A' or 'B': ")

while should_end == False:
  if answer == "A":
    if a["follower_count"] == highest:
      clear()
      print(logo)
      score += 1
      print(f"Correct! Current score: {score}")
      b = generate_option()
      new_comparison(a,b)
      highest = compare(a,b)
      answer = input("Who has the more followers? Type 'A' or 'B': ")
    else:
      clear()
      print(logo)
      print(f"Incorrect! Final score: {score}")
      should_end = True
  elif answer == "B":
    if b["follower_count"] == highest:
      clear()
      print(logo)
      score += 1
      print(f"Correct! Current score: {score}")
      a = b
      b = generate_option()
      new_comparison(a,b)
      highest = compare(a,b)
      answer = input("Who has the more followers? Type 'A' or 'B': ")
    else:
      clear()
      print(logo)
      print(f"Inorrect! Final score: {score}")
      should_end = True