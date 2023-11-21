import random
#testing the pull request
def player_choice():
 player_input = input("Enter your choice (rock, paper, scissors), or 'quit' to exit: ").lower()
 return player_input

def opponent_choice():
 choices = ["rock", "paper", "scissors"]
 return random.choice(choices)

def determine_winner(player, opponent):
 if player == opponent:
  return "It's a draw!!!!"
 elif (player == "rock" and opponent == "scissors") or \
      (player == "paper" and opponent == "rock") or \
      (player == "scissors" and opponent == "paper"):

  return "You win!!!!"

 else:

  return "You lose!!!!"

def rps_game():
 player_wins = 0
 opponent_wins = 0
 draws = 0

 while True:
  user_choice = player_choice()

  if user_choice == "quit":
   print("Game over. Thanks for playing!")
   break

  computer_choice = opponent_choice()

  print(f"Your opponent chose: {computer_choice}")

  result = determine_winner(user_choice, computer_choice)
        
  print(result)

  if result == "You win!!!!":
   player_wins += 1

  elif result == "You lose!!!!":
   opponent_wins += 1

  else:
   draws += 1

  print(f"Score --- Wins: {player_wins}, --- Losses: {opponent_wins}, --- Draws: {draws}\n")


rps_game() #runs the game

