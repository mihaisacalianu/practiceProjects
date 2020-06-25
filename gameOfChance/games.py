import random

money = 100

#Write your game of chance functions here

# Coin Flip function
def coin_flip(guess,bet):
  global money
  coin = random.randint(1,2)
  if(guess.lower() == "heads" and coin == 1):
    print("Player wins!")
    money += bet
    print("You won " + str(bet))
    return bet;
  else:
    print("Computer wins!")
    money -= bet
    print("You lost " + str(bet))
    return bet - (bet * 2)

  if(guess.lower() == "tails" and coin == 2):
    print("Player wins!")
    money += bet
    print("You won " + str(bet))
    return bet;
  else:
    print("Computer wins!")
    money -= bet
    print("You lost " + str(bet))
    return bet - (bet * 2)


# rolling the dice function
def roll_dice(guess,bet):
  global money
  result = " "
  guess = guess.lower()
  dice_1 = random.randint(1,6)
  dice_2 = random.randint(1,6)
  sum_dice = dice_1 + dice_2
  result = "even"
  print("You rolled the dice ")
  print("Your dice was " + str(dice_1) + " and " + str(dice_2))
  if(sum_dice % 2 == 0):
    result = "even"
  else:
    result = "odd"
  if(guess == result):
    print("Player wins!")
    print("You won " + str(bet))
    money += bet
  else:
    print("Computer wins!")
    money -= bet
    print("You lost " + str(bet))

# pick a card function
def pick_a_card(bet):
  global money
  card_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13,14];
  user1_pick = card_deck[random.randint(0,13)]
  print("You picked " + str(user1_pick))
  computer_pick = card_deck[random.randint(0,13)]
  print("Computer picked " + str(computer_pick))
  if(user1_pick == computer_pick):
    print("It is a tie!")
    return 0
  elif(user1_pick > computer_pick):
    print("Player win!")
    print("You won " + str(bet))
    money += bet
  else:
    print("Computer wins!")
    money -= bet
    print("You lost " + str(bet))


# roulette function
def roulette(user_pick, bet, pick_color = "", odd_even = "", zero_picked = False, double_zero_picked = False):
  global money
  zero = 0
  doubleZero = 0
  computer_number =0
  computer_color = 0

  if(zero_picked == True):
     zero = 37
  if(double_zero_picked == True):
    doubleZero = 38

  computer_number = random.randint(1,38)
  computer_color = random.randint(1,2)
  computer_odd_even = random.randint(1,2)

  if(user_pick == computer_number ):
    win = bet * 35
    print("You guessed the number!")
    print("You won " + str(win))
    money += win
  else:
    print("You didn't guess the number")
    money -= bet

  if(len(pick_color) != 0):
    if(pick_color.lower() == "red" and computer_color == 1):
      print("You guessed the color")
      print("You won " + str(bet))
      money += bet
    elif(pick_color.lower() == "black" and computer_color == 2):
      print("You guessed the color")
      print("You won " + str(bet))
      money += bet
    elif(pick_color.lower() == "red" and computer_color == 2):
      print("Your didn't won on colours!")
      print("You lost " + str(bet))
      money -= bet
    elif(pick_color.lower() == "black" and computer_color == 1):
     print("Your didn't won on colours!")
     print("You lost " + str(bet))
     money -= bet
  if(len(odd_even) != 0):
    if(odd_even.lower() == "even" and computer_odd_even == 1):
      print("You guessed even/odd")
      print("You won " + str(bet))
      money += bet
    elif(odd_even.lower() == "odd" and computer_odd_even == 2):
      print("You guessed even/odd")
      print("You won " + str(bet))
      money += bet
    elif(odd_even.lower() == "even" and computer_odd_even == 2):
      print("Your didn't won on even/odd!")
      print("You lost " + str(bet))
      money -= bet
    elif(odd_even.lower() == "odd" and computer_odd_even == 1):
      print("Your didn't won on even/odd!")
      print("You lost " + str(bet))
      money -= bet
  if(zero_picked == True and computer_number == 37):
    money += bet * 35
    print("You choose 0 and you won!")
  else:
    print("You choose 0 and you didn't win!")
    print("You lost " + str(bet))
    money -= bet
  
  if(double_zero_picked == True and computer_number == 38):
    money += bet * 35
    print("You choose 00 and you won!")
  else:
    print("You choose 00 and you didn't win!")
    print("You lost " + str(bet))
    money -= bet
      


#Call your game of chance functions here
coin_flip("heads",23)
roll_dice("Odd",12)
pick_a_card(20)
roulette(20,1,"red","even",True,True)
print("Your balance now is: " + str(money))
