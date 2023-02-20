import sys
import json

# dump input graph representation as prolog

def edgelist(N) :
    for u in sorted(N) :
        for v in sorted(N[u]) :
            print('edge({},{}).'.format(u.lower(), v.lower()))

# Main

N = json.load(open(sys.argv[1],'r'))

print()
print('% copy-paste this into https://swish.swi-prolog.org')
print()

edgelist(N)

print()
print('path(X,X,[X]).')
print('path(X,Y,[X|P]) :- edge(X,Z), path(Z,Y,P).')

print()
print('% path(s,g,P).  % <- and run this query')
print()
