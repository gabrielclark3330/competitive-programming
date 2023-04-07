number_of_people = int(input())

people = []
for _ in range(number_of_people):
    person = [int(x) for x in input().split()]
    person.pop(0)
    person = set(person)
    people.append(person)

connection_value_lookup = {}

adj_list = {}
for i in range(len(people)):
    adj_list[i] = set()

for i in range(len(people)):
    for j in range(len(people)):
        intersection = people[i] & people[j]
        if i!=j and len(intersection)>0:
            elem = intersection.pop()
            connection_value_lookup[(i,j)] = elem
            connection_value_lookup[(j,i)] = elem
            if i in adj_list:
                adj_list[i].add(j)
            if j in adj_list:
                adj_list[j].add(i)

# def getMST(adj_list): # PRIMS returning edge (v1, v2)

visited = set()
tree_connections = []
def dfs(last_node, current_node):
    if current_node in visited:
        return
    visited.add(current_node)
    if last_node is not None:
        tree_connections.append((last_node, current_node, connection_value_lookup[(last_node, current_node)]))
    for connection in adj_list[current_node]:
        dfs(current_node, connection)

dfs(None,0)

if len(visited) != number_of_people:
    print("impossible")
else:
    for connection in tree_connections:
        print(connection[0]+1, connection[1]+1, connection[2])

