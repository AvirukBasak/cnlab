import heapq

def bellman_ford(graph, start):
    # Initialize distances dictionary with start vertex distance set to 0
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Create a priority queue with (distance, vertex)
    minheap = [(0, start)]

    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                if distances[current_vertex] + weight < distances[neighbor]:
                    distances[neighbor] = distances[current_vertex] + weight
                    heapq.heappush(minheap, (distances[neighbor], neighbor))

    # Check for negative cycles
    for _ in range(len(graph)):
        for current_vertex in graph:
            for neighbor, weight in graph[current_vertex].items():
                if distances[current_vertex] + weight < distances[neighbor]:
                    raise ValueError("Graph contains negative cycle")

    return distances

# Example graph represented as adjacency list
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': -1, 'D': -5},
    'C': {'A': 2, 'D': 7},
    'D': {'B': 5, 'C': 7}
}

start = 'A'
mindits = bellman_ford(graph, start)
print(f"Shortest distances from {start}:")
for vertex, dist in mindits.items():
    print(f"To {vertex}:", dist)

''' OUTPUT:
Shortest distances from A:
To A: 0
To B: 4
To C: 2
To D: -1
'''
