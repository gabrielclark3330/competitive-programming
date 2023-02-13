# https://open.kattis.com/problems/monumentmaker
num_lines, original_width, new_width = [int(x) for x in input().split()]

input_string = ""
for line_index in range(num_lines):
    if line_index%2==0:
        input_string +=input()
    else:
        input_string +=input()[::-1]

words = input_string.split(".")
current_line_length = 0
line_count = 1
for index, word in enumerate(words):
    if index+1==len(words):
        word = word.strip()

    if current_line_length==0:
        current_line_length += len(word)
    else:
        if current_line_length+len(word)+1 > new_width: # +1 for period
            line_count+=1
            current_line_length = len(word)
        else:
            current_line_length += (len(word)+1)

print(line_count)

