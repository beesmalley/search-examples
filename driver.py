
import sys
import graph
import search

h, N, w = graph.load(open(sys.argv[1],'r'))

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

order = search.BFS(N)
print('BFS:', *order)

order = search.DFS(N)
print('DFS:   ', *order)

order = search.DFSrec(N)
print('DFSrec:', *order)
