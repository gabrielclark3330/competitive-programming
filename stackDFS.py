### ORIGINAL DFS-Visit(u) ###
# graph of 4 nodes 0-3
Adj = [[3],[0],[1],[1,2]]

color = ["white" for i in range(len(Adj))]
d = [0 for i in range(len(Adj))]  # discover
f = [0 for i in range(len(Adj))]  # finished
pi = [None for i in range(len(Adj))] # parent?
time = [0]

def dfs_visit(u):
    color[u] = "gray"
    time += 1
    d[u] = time

    for v in Adj[u]:
        if color[v] == "white":
            pi[v] = u
            DFS_Visit(v)
    color[u] = "black"
    time += 1
    f[u] = time

### NEW DFS-Stack-Visit(u) ###
def dfs_stack_visit(u):
    dfs_stack = []
    dfs_stack.append(u)
    color[u] = "gray"
    time[0] += 1
    d[u] = time[0]

    while len(dfs_stack) > 0:
        stack_top = dfs_stack[-1]
        for index, v in enumerate(Adj[stack_top]): # find the first white node
            if color[v] == "white": # visit node
                pi[v] = stack_top
                dfs_stack.append(v)
                color[v] = "gray"
                time[0] += 1
                d[v] = time[0]
                break
            elif index==len(Adj[stack_top])-1 and color[v]!="white": # finish node if it has no more connections
                dfs_stack.pop()
                color[stack_top] = "black"
                time[0] += 1
                f[stack_top] = time[0]
        print("[ Stack State ]", dfs_stack)

dfs_stack_visit(0)
print("d:", d)
print("f:", f)
print("pi", pi)


