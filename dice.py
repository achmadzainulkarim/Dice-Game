from random import randint

player = 4
dice = 4
status = [[0 for x in range(player)] for y in range(dice)]
dice_num = [[0 for x in range(player)] for y in range(dice)]

# function to roll dice number
def roll():
	roll = randint(1,6)
	return roll

# Giving status value every dice from every player
for i in range(player):
	for j in range(dice):
		status[i][j] = 1

# Rolling dice and check whether player get a special number or not
while True:
	number_of_dice = []
	for i in range(player):
		for j in range(dice):
			dice_num[i][j] = roll()
		print "PLAYER " + str(i+1)
		print dice_num[i]
		print "Number of dices = "+str(sum(status[i]))
		if 6 in dice_num[i]:
			status[i][dice_num[i].index(6)] = 0
		else:
			if 1 in dice_num[i]:
				status[i][dice_num[i].index(1)] = 0
			else:
				pass
		number_of_dice.append(sum(status[i]))

	print ""
	print number_of_dice
	if 1 in number_of_dice:
		winner = [i for i, x in enumerate(number_of_dice) if x == 1]
		if len(winner) == 1:
			print "The Winner is..."
		else:
			print "The Winners are..."
		for x in winner:
			print "Player "+ str(x+1)
		break