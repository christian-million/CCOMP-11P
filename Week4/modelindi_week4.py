# 'modelindi_week4.py'
# CCOMP-11P-4316 - Fall 2020
# Written By: Christian Million
# Last Modified: 2020-08-17
#
# PROMPT:
# Meet Indi, who is the most adorbs. I wrote a simulator for him (Links to an external site.), but I didn't put any comments into it.
# I'd like for you to create a fork of it for yourself, figure out how it works, and comment the whole thing.
# Pat on the back on this is for finding a clearly better way to do some particular part of it.
# 


# Model Indi Assignment Template
# written by Joe Manlove
# last revision 5/31/20
# the assingment is to comment this, ergo there are no comments past this

from random import choice

locations = []
humans = []
dogs = []

def ballString(balls):
  if len(balls) == 0:
    return 'no balls'
  elif len(balls) == 1:
    return f'{balls[0].name}'
  elif len(balls) == 2:
    return f'{balls[0].name} and {balls[1].name}'
  else:
    returnString = ''
    for ball in balls[:-1]:
      returnString += ball.name + ', '
    returnString += f'and {balls[-1].name}'
    return returnString


class Human:
  def __init__(self, name):
    self.balls = []
    self.name = name
  
  def action(self):
    if self.balls != []:
      print(f'\nYou now have {ballString(self.balls)} in your hands...')
      action = input('Throw the ball?\n')
      if action.lower() in ['yes', 'y']:
        self.throwBall(choice(self.balls), choice(locations))
      else:
        print('You really are heartless aren\'t you?')

  def throwBall(self, ball, targetLocation):
    targetLocation.balls.append(ball)
    self.balls.remove(ball)
    print(f'You have thrown {ball.name}, it is now in the {targetLocation.name}.\n')

class Location:
  def __init__(self, name, balls):
    self.name = name
    self.balls = balls
    

class Ball:
  def __init__(self, name):
    self.name = name

class Dog:
  def __init__(self, name):
    self.name = name
    self.balls = []

  def action(self):
    if self.balls != []:
      self.giveBall(choice(humans), choice(self.balls))
    else:
      self.lookForBall(choice(locations))

  def giveBall(self, human, ball):
    self.balls.remove(ball)
    human.balls.append(ball)
    print(f'{self.name} has given the {ball.name} to {human.name}')

  def lookForBall(self, targetLocation):
    if targetLocation.balls != []:
      targetBall = choice(targetLocation.balls)
      self.balls.append(targetBall)
      targetLocation.balls.remove(targetBall)
      print(f'{self.name} has found the {targetBall.name} in the {targetLocation.name}.')
    else:
      print(f'{self.name} looks hopelessly about after searching the {targetLocation.name}.')

locations = [Location('Living Room', [Ball('Pink Torus')]),
              Location('Kitchen', [Ball('Sal the Snake'), Ball('Pink Ellipsoid'), Ball('Blue Chuckit')]),
              Location('Under the Couch', [Ball('Pink Ball'), Ball('Green Ellipsoid'), Ball('Blue Torus')]),
              Location('Dining Room', []),
              Location('Yard', [Ball('Larry the Lizard'), Ball('Hook Dongle')])
            ] 
Joe = Human('Joe')
humans.append(Joe)
Indi = Dog('Indi')
dogs.append(Indi)

while True:
  Indi.action()
  Joe.action()