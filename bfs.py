import sys
import json

# perform breadth-first search (BFS) on input graph representation
# using a (FIFO) queue

def bfs(q, N) :

    while q :

        u = q.pop(0)

        print(u if u != 'G' else '{} <- goal!'.format(u))

        q += [v for v in N[u]]

# Main

N = json.load(open(sys.argv[1],'r'))

q = ['S']
bfs(q, N)
