class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, city1, city2, cost):
        if city1 not in self.graph:
            self.graph[city1] = {}
        self.graph[city1][city2] = cost

    def get_cost(self, city1, city2):
        return self.graph.get(city1, {}).get(city2, None)

def business_trip(graph, cities):
    """
    Calculate the total cost of a business trip between given cities using direct flights.

    Args:
        graph (Graph): Graph with flight connections and costs between cities.
        cities (list): Sequence of city names for the trip.

    Returns:
        int or None: Total cost of the trip if possible, else None.
    """
    
    
    total_cost = 0

    for i in range(len(cities) - 1):
        cost = graph.get_cost(cities[i], cities[i+1])
        if cost is None:
            return None
        total_cost += cost

    return total_cost
