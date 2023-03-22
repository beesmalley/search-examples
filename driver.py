
import sys
import graph
import search

h, N, w = graph.load(open(sys.argv[1],'r'))

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

order = search.DFS(N, start, goal)
print('DFS:   ', *order)
print()

order = search.DFSrec(N, start, goal)
print('DFSrec:', *order)
print()
