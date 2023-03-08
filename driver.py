
import sys
import graph
import search

h, N, w = graph.load(open(sys.argv[1],'r'))

order = search.BFS(N)
print('BFS:', *order)

order = search.DFS(N)
print('DFS:   ', *order)

order = search.DFSrec(N)
print('DFSrec:', *order)
