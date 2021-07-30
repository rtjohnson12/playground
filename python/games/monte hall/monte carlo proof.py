
import random

num_runs = int(1e6)
first_choice_wins = 0
change_doors_wins = 0

doors = ['a', 'b', 'c']
for i in range(num_runs):
  winner = random.choice(doors)
  pick = random.choice(doors)
  
  if pick == winner:
    first_choice_wins += 1
  else:
    change_doors_wins += 1
    
print("Wins with original pick - {:.2%}\nWins with changed pick  - {:.2%}".format(first_choice_wins / num_runs, change_doors_wins / num_runs))
