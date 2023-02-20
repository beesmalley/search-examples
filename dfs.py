import sys
import json

# perform depth-first search (DFS) on input graph representation

def dfs(u, N) :

    c = ''
    if u == 'G' :
        c = ' <- goal!'

    print(u, c, sep = '')

    for v in N[u] :
        dfs(v, N)

# Main

N = json.load(open(sys.argv[1],'r'))

dfs('S', N)
