
'''

  for performing various search strategies on graphs G = (V,E) of
  vertices V and edges E, input as the set N(v) of neighbours for each
  v in V

'''

# for a graph input as neighbourhood set N, perform breadth-first
# search (BFS) for a goal vertex starting from some start vertex
def BFS(N, start = 's', goal = 'g') :

    order = [] # the order in which vertices are visited

    queue = [start]
    while queue :

        v = queue.pop(0)
        order.append(v)

        if v == goal :
            return order

        queue += N[v]


# for a graph input as neighbourhood set N, perform depth-first
# search (DFS) for a goal vertex starting from some start vertex
def DFS(N, start = 's', goal = 'g', giveup = 100) :

    order = [] # the order in which vertices are visted

    stack = [[start]]
    i = 0
    while stack :

        i += 1
        if i > giveup :
            return order, '<- gave up after {} iterations'.format(giveup)

        # should the list at the top of the stack be empty
        if not stack[-1] :
            stack.pop()
            continue

        v = stack[-1].pop()
        order.append(v)

        if v == goal :
            return order, ''

        stack.append(list(reversed(N[v])))


# for a graph input as neighbourhood set N, perform depth-first search
# (DFS) for a goal vertex starting from some start vertex, using
# recursion to do so
def DFSrec(N, start = 's', goal = 'g', giveup = 100) :

    order = [] # the order in which vertices are visted

    DFSaux(order, start, N, goal, 0, giveup)

    log = ''
    if len(order) > giveup :
        log = '<- gave up after recursion depth {}'.format(giveup)

    return order, log


# auxiliary function for DFSrec which does the actual recursion,
# inspired by:
# https://stackoverflow.com/questions/70550888/how-i-can-stop-depth-first-search-at-specific-node
def DFSaux(order, v, N, goal, i, giveup) :

    order.append(v)

    if v == goal :
        return True

    if i > giveup :
        return True

    for u in N[v] :
        if DFSaux(order, u, N, goal, i+1, giveup) :
            return True

    return False
