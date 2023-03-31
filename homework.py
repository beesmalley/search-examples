import sys
from graph import load
from queue import PriorityQueue
import heapq

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

def UCS(N, w, start='s', goal='g'):
    visited = []
    pq = PriorityQueue()
    pq.put((0, start, []))  # (priority, node, path)

    while not pq.empty():
        (cost, node, path) = pq.get()
        if node not in visited:
            visited.append(node)
            path = path + [node]
            if node == goal:
                print("UCS Cost:", cost)
                return path, visited
            for neighbor in N[node]:
                if neighbor not in visited:
                    new_cost = cost + w[(node, neighbor)]
                    pq.put((new_cost, neighbor, path))
    return None

order, visited = UCS(N, w, start, goal)
print('UCS:    ', *order)
print('Visited order:', *visited)
print()

def Greedy(N, h, start='s', goal='g'):
    visited = []
    path = [start]
    current_node = start

    while current_node != goal:
        visited.append(current_node)
        neighbors = N[current_node]
        if not neighbors:
            return None
        min_h = float('inf')
        min_node = None
        for neighbor in neighbors:
            if neighbor not in visited:
                if h[neighbor] < min_h:
                    min_h = h[neighbor]
                    min_node = neighbor
        if not min_node:
            return None
        current_node = min_node
        path.append(current_node)

    visited.append(current_node)
    return path, visited

order, visited = Greedy(N, h, start, goal)
print('Greedy:    ', *order)
print('Visited order:', *visited)
print()

def astar(N, h, w, start='s', goal='g'):
    visited = []
    queue = [(0, start, [])]  # (f, node, path)
    while queue:
        f, node, path = heapq.heappop(queue)
        if node in visited:
            continue
        visited.append(node)
        path = path + [node]
        if node == goal:
            return path, visited
        for neighbor in N[node]:
            if neighbor not in visited:
                g = w[(node, neighbor)] + f
                heapq.heappush(queue, (g + h[neighbor], neighbor, path))
    return None

order, visited = astar(N, h, w, start, goal)
print('A* search:    ', *order)
print('Visited order:', *visited)
print()