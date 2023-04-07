rows, cols = [int(x) for x in input().split()]

board = []
for row in range(rows):
	board.append([int(x) for x in input().split()])

#print(board)
	
countOfTwos = 0
countOfZeros = 0
countOfOnes = 0
for row in range(rows):
	for col in range(cols):
		if board[row][col] == 2:
			countOfTwos += 1
		if board[row][col] == 0:
			countOfZeros += 1
		if board[row][col] == 1:
			countOfOnes += 1
#print(countOfZeros, countOfOnes, countOfTwos)


if rows == 1 or cols == 1:
	if countOfZeros == 0:
		div, mod = divmod(countOfTwos, 2)
		amountOff = 2**(div+mod) - 2**div
		print(amountOff)

	elif countOfZeros == 1:
		if board[0][0] == 0:
			print(board[rows-1][cols-1])
		elif board[rows-1][cols-1] == 0:
			print(board[0][0])
		else:
			print(min(board[rows-1][cols-1], board[0][0]))

	elif countOfZeros >= 2:
		print(0)
else:
	if countOfZeros == 0:
		div, mod = divmod(countOfTwos, 2)
		#print(div, mod)
		amountOff = 2**(div+mod) - 2**div
		print(amountOff)

	elif countOfZeros == 1:
		if countOfOnes != 0:
			print(1)
		elif countOfTwos != 0:
			print(2)

	elif countOfZeros >= 2:
		print(0)
