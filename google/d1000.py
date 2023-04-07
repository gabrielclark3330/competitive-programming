test_cases = int(input())

for test_case in range(test_cases):
    input()
    dice = [int(x) for x in input().split()]
    dice.sort()

    counter=1
    for dice_index in range(len(dice)):
        if dice[dice_index] >= counter:
            counter+=1

    print(f"Case #{test_case+1}: {counter-1}")
