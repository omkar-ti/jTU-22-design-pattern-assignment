#Using the strategy desing pattern 

import random 

PLAYER_WON = 1
CPU_WON = -1
TIE = 0

game_history = []

move_roster = {
	"Rock":0,
	"Paper":1,
	"Scissors":2
} 



move_list = ("Rock", "Paper", "Scissors")


def get_result(player_move, cpu_move):
	if player_move == cpu_move:
		return TIE
	if (move_roster[player_move]+1)%len(move_roster) == move_roster[cpu_move]:
		return CPU_WON
	else:
		return PLAYER_WON

#Informal interface for all strategies
class Strategy:

	def get_next_move(self):
		pass


class RandomStrategy(Strategy):

	def get_next_move(self):
		return random.choice(move_list)


class MirrorStrategy(Strategy):

	def get_next_move(self):
		if len(game_history) == 0:
			return random.choice(move_list)
		return game_history[-1][0]


class CpuPlayer:

	#Keeping track of what strategy to use
	#The strategy implementation is outside CpuPlayer class
	strategy = RandomStrategy()
	curr_strategy = "RandomStrategy"
	#Ideally, strategy should be a reference of class Strategy pointing at one of the strategies

	#Changing strategy on runtime
	def flip_strategy(self):
		if self.curr_strategy == "RandomStrategy":
			self.strategy = MirrorStrategy()
			self.curr_strategy = "MirrorStrategy"
		else:
			self.strategy = RandomStrategy()
			self.curr_strategy = "RandomStrategy"

	def get_next_move(self):
		return self.strategy.get_next_move()


print("WELCOME TO ROCK PAPERS SCISSORS!")
print("A GAME WORTH 5 POINTS SHALL COMMENCE!\n\n")
print("START!")

cpu_player = CpuPlayer()
player_score = 0
cpu_score = 0

# test_data = ["Rock","Scissors","Change","Paper"]

print("CPU starts of with a random choose move strategy.")

for i in range(5):
	print("\nEnter your move. (Rock, Paper or Scissors).\nTo change CPU strategy, enter 'Change'.\n")
	player_move = input()


	if player_move == "Change":
		cpu_player.flip_strategy()
		i = i-1
		print("CPU strategy changed\n")

	elif player_move in move_roster:
		cpu_move = cpu_player.get_next_move()
		print(f"You played {player_move}")
		print(f"Opponent played {cpu_move}\n")
		if get_result(player_move, cpu_move) == PLAYER_WON:
			print(f"You WIN this time!\n")
			player_score += 1
		elif get_result(player_move, cpu_move) == CPU_WON:
			print(f"You LOST this time!\n")
			cpu_score += 1
		else:
			print(f"It was a TIE!\n")
			i = i-1
	else:
		print(f"Enter some valid move or the change command.\n")
		i = i-1

print()
print()
if player_score > cpu_score:
	print("You WIN the game!")
elif cpu_score > player_score:
	print("You LOST the game!")
else:
	print("Turing test FAILED")

uu = input()












