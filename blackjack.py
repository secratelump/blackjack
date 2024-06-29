computer_cards = []
user_cards = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from art import logo
print(logo)

while len(user_cards) != 2:
  user_cards.append(random.choice(cards))
  computer_cards.append(random.choice(cards))

user_score = sum(user_cards)
computer_score = sum(computer_cards)
print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
print(f"The computers first card is {computer_cards[0]}")
fact = True
while fact == True:
  choice = input("Would you like to hit or stand? Type 'y' for hit or 'n' for stand: ")
  if choice == "y":
    user_cards.append(random.choice(cards))
    user_score = sum(user_cards)
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
  else:
    fact = False

while computer_score < 17:
  computer_cards.append(random.choice(cards))
  computer_score = sum(computer_cards)

if user_score == 21:
  print(f"You win with a blackjack! Your score was {user_score} and the computers score was {computer_score}")

elif computer_score == 21:
  print(f"The computer wins with a blackjack! Your score was {user_score} and the computers score was {computer_score}")

elif user_score > 21:
  print(f"You went over. You lose. Your score was {user_score} and the computers score was {computer_score}")

elif computer_score > 21:
  print(f"The computer went over. You win! Your score was {user_score} and the computers score was {computer_score}")

elif user_score > computer_score:
  print(f"You win! Your score was {user_score} and the computers score was {computer_score}")

elif user_score < computer_score:
  print(f"You lose! Your score was {user_score} and the computers score was {computer_score}")

elif user_score == computer_score:
  print(f"It's a draw! Your score was {user_score} and the computers score was {computer_score}")
