test_cases = int(input())

for test_case in range(test_cases):
    printers = []
    for printer in range(3):
        printers.append([int(x) for x in input().split()])
    
    #for printer in printers:
    ink_totals = []
    for ink_carterage in range(4):
        ink_totals.append(min([printer[ink_carterage] for printer in printers]))

    if sum(ink_totals) < (10**6):
        print(f"Case #{test_case+1}: IMPOSSIBLE")
    else:
        running_sum = 0
        ink_drawn_from_carterages = []
        for ink_carterage in range(4):
            if running_sum+ink_totals[ink_carterage]<=(10**6):
                ink_drawn_from_carterages.append(ink_totals[ink_carterage])
                running_sum += ink_totals[ink_carterage]
            elif running_sum+ink_totals[ink_carterage]>(10**6):
                ink_drawn_from_carterages.append((10**6)-running_sum)
                running_sum = 10**6
        print(f"Case #{test_case+1}: ", end='')
        for value in ink_drawn_from_carterages:
            print(value,"", end='')
        print()
