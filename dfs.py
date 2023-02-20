import sys
import json

# perform depth-first search (DFS) on input graph representation using
# a (LIFO) stack

def dfs(s, N) :

    while s :

        if not s[-1] :
            s.pop()
            continue

        u = s[-1].pop()

        print(u if u != 'G' else '{} <- goal!'.format(u))

        s.append([v for v in sorted(N[u], reverse = True)])
    
# Main

N = json.load(open(sys.argv[1],'r'))

s = [['S']]
dfs(s, N)
