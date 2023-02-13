# https://open.kattis.com/problems/thecolonizationofelgarizm
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
p1_islands = set([])
p1_resources = set([])
p2_islands = set([])
p2_resources = set([])

def find_island_not_picked():
    for island_index in range(len(islands)):
        if island_index not in p1_islands and island_index not in p2_islands:
            return island_index
    return None

satisfiable = None
# manage end state
while satisfiable is None:
    if p1_resources==p2_resources:
        island_to_pick_next = find_island_not_picked()
        if island_to_pick_next is None:
            satisfiable = True
            break
        if ones_turn:
            p1_islands.add(island_to_pick_next)
            p1_resources.update(islands[island_to_pick_next])
        else:
            p2_islands.add(island_to_pick_next)
            p2_resources.update(islands[island_to_pick_next])
        ones_turn = not ones_turn
    else:
        if ones_turn: # p1s turn
            # find the elements that p2 has but p1 doesn't
            diff = p2_resources.difference(p1_resources)
            # find the islands assosiated with them
            islands_to_add = set()
            for resource in diff:
                # if islands taken then sim not satisfiable break
                # else add each island and island resources to p1
                islands_arr = resource_is_on_islands[resource]
                if len(islands_arr) != 2:
                    print("ERROR")
                if islands_arr[0] not in p2_islands:
                    islands_to_add.add(islands_arr[0])
                elif islands_arr[1] not in p2_islands:
                    islands_to_add.add(islands_arr[1])
                else:
                    satisfiable = False
                    break
                for island in islands_to_add:
                    p1_islands.add(island)
                    p1_resources.update(islands[island])
            # flip turn
            ones_turn = not ones_turn
        else: # p2s turn
            # find the elements that p2 has but p1 doesn't
            diff = p1_resources.difference(p2_resources)
            # find the islands assosiated with them
            islands_to_add = set()
            for resource in diff:
                # if islands taken then sim not satisfiable break
                # else add each island and island resources to p1
                islands_arr = resource_is_on_islands[resource]
                if len(islands_arr) != 2:
                    print("ERROR")
                if islands_arr[0] not in p1_islands:
                    islands_to_add.add(islands_arr[0])
                elif islands_arr[1] not in p1_islands:
                    islands_to_add.add(islands_arr[1])
                else:
                    satisfiable = False
                    break
                for island in islands_to_add:
                    p2_islands.add(island)
                    p2_resources.update(islands[island])
            # flip turn
            ones_turn = not ones_turn
    '''
    print("1turn", ones_turn)
    print("p1i", p1_islands)
    print("p1r", p1_resources)
    print("p2i", p2_islands)
    print("p2r", p2_resources)
    print("---")
    '''

if satisfiable:
    print("YES")
else:
    print("NO")

