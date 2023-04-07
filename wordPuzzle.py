def count(txt, subs):
    m = len(txt)
    n = len(subs)
 
    # Create a table to store results of sub-problems
    lookup = [[0] * (n + 1) for i in range(m + 1)]
 
    # If first string is empty
    for i in range(n+1):
        lookup[0][i] = 0
 
    # If second string is empty
    for i in range(m + 1):
        lookup[i][0] = 1
 
    # Fill lookup[][] in bottom up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
             
            # If last characters are same, 
            # we have two options -
            # 1. consider last characters of 
            # both strings in solution
            # 2. ignore last character of first string
            if txt[i - 1] == subs[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
                 
            else:
                # If last character are different, ignore
                # last character of first string
                lookup[i][j] = lookup[i - 1][j]
 
    return lookup[m][n]


def countWithRotation(txt, subs): # does subs rotation to catch all possible rotations
    m = len(txt)
    n = len(subs)
 
    # Create a table to store results of sub-problems
    lookup = [[0] * (n + 1) for i in range(m + 1)]
 
    # If first string is empty
    for i in range(n+1):
        lookup[0][i] = 0
 
    # If second string is empty
    for i in range(m + 1):
        lookup[i][0] = 1
 
    # Fill lookup[][] in bottom up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
             
            # If last characters are same, 
            # we have two options -
            # 1. consider last characters of 
            # both strings in solution
            # 2. ignore last character of first string
            if txt[i - 1] == subs[j - 1]:
                lookup[i][j] = lookup[i - 1][j - 1] + lookup[i - 1][j]
            else:
                # If last character are different, ignore
                # last character of first string
                lookup[i][j] = lookup[i - 1][j]
 
    return lookup[m][n]




text = input()
substring = input()

rotatedSubstr = set()
for i in range(len(substring)):
	if i>0:
		rotation = substring[i:len(substring)] + substring[0:i]
	else:
		rotation = substring
	rotatedSubstr.add(rotation)

occuranceCount = 0

for substr in rotatedSubstr:
	occuranceCount += count(text, substr)

print(occuranceCount % 1000000007)


