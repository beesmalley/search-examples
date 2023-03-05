
import graphviz

'''

  for loading and visualizing graphs G = (V,E) of vertices V with
  integer heuristic values h(v), for each v in V, and edges E with
  integer weights w(e), for each e in E

'''

# load a graph as a triple h, N, w: the heuristic h(v) and the set
# N(v) of neighbours, for each vertex v in V, and the weight w(e), for
# each edge e in E
def load(lines) :

    v, *heur, es = (x.strip() for x in lines.readline().split(','))
    assert v == 'v'
    assert es == 'es'

    if heur :
        assert len(heur) == 1
        heur = heur[0]
        assert heur == 'h'

    h = {} # heuristic value h(v), for each v in V
    N = {} # set N(v) of neighbours, for each v in V
    w = {} # weight w(e), for each e in E
    for line in lines :
        v, *es = (x.strip() for x in line.split(','))

        h[v] = 0 # h(v) 0 by default
        if heur :
            h[v] = int(es[0])
            es = es[1:]

        N[v] = []
        for e in es :
            u, *W = (x.strip() for x in e.split(':'))

            N[v].append(u)

            w[(v,u)] = 1 # w(e) 1 by default
            if W :
                assert len(W) == 1
                W = W[0]
                w[(v,u)] = int(W)

        N[v] = sorted(N[v])

    return h, N, w


# given a graph, specified by h(v), for each v in V, and w(e), for
# each e in E, color source green and goal red, and dump to filename
def visualize(h, w, source = None, goal = None, filename = 'G') :

    dot = graphviz.Digraph(comment = 'digraph {}'.format(filename))

    # vertices

    heur = False
    for v in h :
        if h[v] :
            heur = True

    for v in h :
        dot.node(v, xlabel = 'h({}) = {}'.format(v,h[v]) if heur else '')

        if v == source :
            dot.node(v, style = 'filled', fillcolor = 'green')

        if v == goal :
            dot.node(v, style = 'filled', fillcolor = 'red')

    # edges (with weights)

    weights = False
    for e in w :
        if w[e] > 1 :
            weights = True

    for e in w :
        v, u = e

        dot.edge(v, u, label = str(w[e]) if weights else '', fontcolor = 'blue')

    dot.render(filename).replace('\\', '/')
