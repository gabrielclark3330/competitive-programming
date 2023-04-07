n, s = [int(x) for x in input().split()]

orderArray = []
tank = s
sumation = 0
for _ in range(n):
	line = input()
	num = 0
	if "L" in line:
		num = line[0:-1]
		num = int(num) + 1
	else:
		num = int(line)
	if tank - num < 0:
		sumation += 1
		tank = s
		tank -= num
	else:
		tank -= num	
print(sumation)
