import heapq

def dijkstra(graph, start):
    # Initialize distances dictionary with start vertex distance set to 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Initialize priority queue with (distance, vertex)
    minheap = [(0, start)]

    while minheap:
        curdist, curvert = heapq.heappop(minheap)

        # Skip if current distance is greater than recorded distance
        if curdist > distances[curvert]:
            continue

        for neighbor, weight in graph[curvert].items():
            dist = curdist + weight
            # Update distance if shorter path found
            if dist < distances[neighbor]:
                distances[neighbor] = dist
                heapq.heappush(minheap, (dist, neighbor))

    return distances

# Example graph represented as adjacency list
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 7},
    'D': {'B': 5, 'C': 7}
}

start = 'A'
mindists = dijkstra(graph, start)
print(f"Shortest distances from {start}:")
for vertex, dist in mindists.items():
    print(f"To {vertex}:", dist)

''' OUTPUT:
Shortest distances from A:
To A: 0
To B: 4
To C: 2
To D: 9
'''
