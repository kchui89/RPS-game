import random
#testing the pull request
def player_choice():
 
 choice_maps = {"r": "rock", "p": "paper", "s": "scissors", "sci": "scissors", "pa": "paper", "ro": "rock"}
 valid_choices = set(choice_maps.values())

 while True:
  player_input = input("Enter your choice (rock, paper, scissors), or 'quit' to exit: ").lower()
  
  if player_input == "quit":
   return "quit"
  
  if player_input in choice_maps:
    return choice_maps[player_input]
  
  elif player_input in valid_choices:
    return player_input
  
  else:
   print("Invalid input. Please enter rock/r/ro for 'rock', scissors/s/sci for 'scissors' or paper/p/pa for 'paper' ")
  
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

