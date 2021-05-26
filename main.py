rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
choices = [rock, paper, scissors]
c2 = input("What do you want to put? 1 for rock, 2 for paper and 3 for scissors.")
if c2 == '1':
  print(rock)
elif c2 == '2':
  print(paper)
else:
  print(scissors)

print('\n')

print("The computer chose: ")
c1 = random.choice(choices)
print(c1)

print('\n')

if c2 == '1':
  if c1 == scissors:
    print("You win")
  elif c1 == rock:
    print("It is a draw")
  else:
    print("Computer wins")

if c2 == '2':
  if c1 == paper:
    print("It is a draw")
  elif c1 == rock:
    print("You win")
  else:
    print("Computer wins")

if c2 == '3':
  if c1 == scissors:
    print("It is a draw")
  elif c1 == paper:
    print("You win")
  else:
    print("Computer wins")

