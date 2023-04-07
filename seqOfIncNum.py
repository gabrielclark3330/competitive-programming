# Given a number n
# How many sequences of non-increasing numbers
# can you make where the sum of the numbers in the sequence equals n.

n = int(input())

solutions = set()

def backtrackNumbers(currentSolution):
    if sum(currentSolution) == n:
        solutions.add(tuple(currentSolution))
        return
    elif sum(currentSolution) > n:
        return

    for i in range(1, currentSolution[-1]+1):
        currentSolution.append(i)
        backtrackNumbers(currentSolution)
        currentSolution.pop()


for i in range(1, n+1):
    backtrackNumbers([i])

print(solutions) #len(solutions)
