
import sys
from graph import load
import search
import mysearch310 as mysearch

h, N, w = load(open(sys.argv[1],'r'))

start = 's'
goal = 'g'
if len(sys.argv) > 2 :
    start = sys.argv[2]
if len(sys.argv) > 3 :
    goal = sys.argv[3]

print()
print('Graph structures, h, N and w:')
print()

print('h = ', h)
print()

print('N = ', N)
print()

print('w = ', w)
print()

print('Search orders:')
print()

order = search.BFS(N, start, goal)
print('BFS:   ', *order)
print()

order, log = search.DFS(N, start, goal)
print('DFS:   ', *order, log)
print()

order, log = search.DFSrec(N, start, goal)
print('DFSrec:', *order, log)
print()

order, log = mysearch.UCS(N, w, start, goal)
print('UCS:   ', *order)
print()

fname = 'UCS.log'
with open(fname,'w') as f :
    print(*log, sep = '\n', file = f)
print('* log of UCS written to:', fname)
print()

order, log = mysearch.greedy(N, h, start, goal)
print('greedy:', *order, log)
print()

order, log = mysearch.Astar(N, w, h, start, goal)
print('A*:    ', *order)
print()

fname = 'Astar.log'
with open(fname,'w') as f :
    print(*log, sep = '\n', file = f)
print('* log of A* written to:', fname)
print()
