import heapq


class Graph:
    def __init__(self):
        self.nodes = {}
        self.heuristics = {}

    def add_edge(self, start, end, distance):
        if start not in self.nodes:
            self.nodes[start] = []
        if end not in self.nodes:
            self.nodes[end] = []
        self.nodes[start].append((end, distance))
        self.nodes[end].append((start, distance))

    def set_heuristic(self, node, heuristic):
        self.heuristics[node] = heuristic

    def get_neighbors(self, node):
        return self.nodes.get(node, [])

    def get_heuristic(self, node):
        return self.heuristics.get(node, float("inf"))


def create_graph(filename):
    graph = Graph()
    with open(filename, "r") as file:
        for line in file:
            parts = line.split()
            node = parts[0]
            h = int(parts[1])
            graph.set_heuristic(node, h)
            for i in range(2, len(parts), 2):
                neighbor = parts[i]
                distance = int(parts[i + 1])
                graph.add_edge(node, neighbor, distance)
    return graph


def a_star_search(graph, start, goal):
    fringe = []
    heapq.heappush(fringe, (0 + graph.get_heuristic(start), start))
    parents = {}
    actual_cost = {start: 0}
    total_cost = {start: graph.get_heuristic(start)}

    while fringe:
        cost, current = heapq.heappop(fringe)

        if current == goal:
            path = []
            while current in parents:
                path.append(current)
                current = parents[current]
            path.append(start)
            path.reverse()
            total_distance = actual_cost[goal]
            return path, total_distance

        for neighbor, distance in graph.get_neighbors(current):
            new_cost = actual_cost[current] + distance

            if new_cost < actual_cost.get(neighbor, float("inf")):
                parents[neighbor] = current
                actual_cost[neighbor] = new_cost
                total_cost[neighbor] = new_cost + graph.get_heuristic(neighbor)
                heapq.heappush(fringe, (total_cost[neighbor], neighbor))

    return "NO PATH FOUND", None


graph = create_graph("input.txt")
start = input("Start node: ")
goal = input("Destination: ")
path, total_distance = a_star_search(graph, start, goal)

if path == "NO PATH FOUND":
    print("NO PATH FOUND")
else:
    print("Path:", " -> ".join(path))
    print("Total distance:", total_distance, "km")
