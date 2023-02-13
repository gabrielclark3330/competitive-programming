num_islands, num_resources = [int(x) for x in input().split()]

islands = []
resource_is_on_islands = {resource:[] for resource in range(1, num_resources+1)}

for island_index in range(num_islands):
    island = [int(x) for x in input().split()]
    island.pop()
    islands.append(island)
    for resource in island:
        resource_is_on_islands[resource].append(island_index)


ones_turn = True
island_left_to_pick = True
p1_islands = []
p1_resources = set([])
p2_islands = []
p2_resources = set([])

def find_island_not_picked():
    for island_index in range(num_islands):
        if island_index not in p1_islands and island_index not in p2_islands:
            return island_index

while 1:
    if p1_resources==p2_resources:
        find_island_not_picked()
        if ones_turn:
            p1_islands.append(island_to_pick_next)
            p1_resources.add(islands[island_to_pick_next])
        else:
            p2_islands.append(island_to_pick_next)
            p2_resources.add(islands[island_to_pick_next])
    else:
        if ones_turn:
            pass
        else:
            pass


''' sample 1
adj_mat_islands = [[1 for k in range(num_islands)] for j in range(num_islands)]
for island_index in range(num_islands):
    for resource in islands[island_index]:
        exclude_islands = resource_is_on_islands[resource]
        for island_to_exclude in exclude_islands:
            adj_mat_islands[island_index][island_to_exclude] = 0
            adj_mat_islands[island_to_exclude][island_index] = 0

[ 0  1  2  3  4  5  6 <- to
0[1, 1, 1, 0, 0, 1, 1]
1[1, 1, 0, 1, 1, 0, 1]
2[1, 0, 1, 1, 0, 1, 1]
3[0, 1, 1, 1, 1, 1, 0]
4[0, 1, 0, 1, 1, 0, 1]
5[1, 0, 1, 1, 0, 1, 1]
6[1, 1, 1, 0, 1, 1, 1]]
^
|
from
for row in adj_mat_islands:
    print(row)
'''

'''
if satisfiable:
    print("YES")
else:
    print("NO")
'''

