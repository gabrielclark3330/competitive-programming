num_tests = int(input())

for test in range(num_tests):
    print(f"Case #{test+1}:")
    rows, cols = [int(x) for x in input().split()]

    card = []
    for row in range(rows):
        rowArr = ["",""]
        for col in range(cols):
            if row==0 and col==0:
                rowArr[0] = rowArr[0] +".."
                rowArr[1] = rowArr[1] +".."
            else:
                rowArr[0] = rowArr[0] + "+-"
                rowArr[1] = rowArr[1] + "|."
        rowArr[0] = rowArr[0] + "+"
        rowArr[1] = rowArr[1] + "|"
        card.append(rowArr[0])
        card.append(rowArr[1])
    last_col_str = ""
    for col in range(cols):
        last_col_str = last_col_str + "+-"
    last_col_str = last_col_str + "+"
    card.append(last_col_str)

    for string in card:
        print(string)
