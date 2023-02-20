import sys
import json

# perform depth-first search (DFS) on input graph representation using recursion

def dfs(u, N) :

    print(u if u != 'G' else '{} <- goal!'.format(u))

    for v in N[u] :
        dfs(v, N)

# Main

N = json.load(open(sys.argv[1],'r'))

dfs('S', N)
