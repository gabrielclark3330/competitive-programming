# https://open.kattis.com/problems/protectingthecollection
room_size, laser_col, sensor_row = [int(x) for x in input().split()]

room = []
for _ in range(room_size):
    room.append(input().split())

# laser pass
cell = [-1, laser_col-1] # row, col
direction = [1, 0] # row, col
while 1:
    cell = [cell[0]+direction[0], cell[1]+direction[1]]
    if cell[0] < room_size and cell[0] >= 0 and cell[1] < room_size and cell[1] >= 0:
        if room[cell[0]][cell[1]] == "\\":
            if direction==[1,0]: # down 
                direction = [0, 1]
            elif direction==[-1,0]: # up
                direction = [0, -1]
            elif direction==[0,1]: # right
                direction = [1, 0]
            elif direction==[0,-1]: # left
                direction = [-1, 0]

        elif room[cell[0]][cell[1]] == "/":
            if direction==[1,0]: # down 
                direction = [0, -1]
            elif direction==[-1,0]: # up
                direction = [0, 1]
            elif direction==[0,1]: # right
                direction = [-1, 0]
            elif direction==[0,-1]: # left
                direction = [1, 0]
        elif room[cell[0]][cell[1]] == ".":
            room[cell[0]][cell[1]] = "l" # laser path

    else:
        break # we hit a wall

# sensor pass
cell = [sensor_row-1, room_size] # row, col
direction = [0, -1] # row, col
intersection = None
while 1:
    cell = [cell[0]+direction[0], cell[1]+direction[1]]
    if cell[0] < room_size and cell[0] >= 0 and cell[1] < room_size and cell[1] >= 0:
        if room[cell[0]][cell[1]] == "l":
            intersection = cell
        elif room[cell[0]][cell[1]] == "\\":
            if direction==[1,0]: # down 
                direction = [0, 1]
            elif direction==[-1,0]: # up
                direction = [0, -1]
            elif direction==[0,1]: # right
                direction = [1, 0]
            elif direction==[0,-1]: # left
                direction = [-1, 0]

        elif room[cell[0]][cell[1]] == "/":
            if direction==[1,0]: # down 
                direction = [0, -1]
            elif direction==[-1,0]: # up
                direction = [0, 1]
            elif direction==[0,1]: # right
                direction = [-1, 0]
            elif direction==[0,-1]: # left
                direction = [1, 0]
        elif room[cell[0]][cell[1]] == ".":
            room[cell[0]][cell[1]] = "s" # sensor path

    else:
        break # we hit a wall

'''
print(intersection)

for row in room:
    print(row)
'''

if intersection is not None:
    print("YES")
else:
    print("NO")
