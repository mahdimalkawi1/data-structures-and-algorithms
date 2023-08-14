# Graph Implementation 
## Author: Mahdi Malkawi

This Python code demonstrates a basic implementation of a graph data structure along with a breadth-first search traversal method. The graph is represented using classes for vertices, edges, and the graph itself. The code creates a graph, adds vertices and edges, and performs a breadth-first search starting from a specified vertex.

## Classes
1. **Queue**: A simple queue class using a deque from the collections module, used for BFS traversal.

2. **Vertex**: Represents a vertex in the graph. It has a value and a string representation method.

3. **Edge**: Represents an edge connecting two vertices, with an optional weight.

4. **Graph**: Defines the main graph class. It includes methods to add vertices and edges, get vertices, find the size of the graph, get neighbors of a vertex, and perform a breadth-first search.

## Usage
Create an instance of the Graph class.
Add vertices using the add_vertex(value) method.
Add edges between vertices using the add_edge(start_vertex, end_vertex, weight) method.
Call the breadth_first(start_vertex) method to perform a breadth-first search starting from the given vertex.
The example provided in the __main __ block demonstrates how to use the graph class. Vertices 'A', 'B', 'C', 'D', and 'E' are added, and edges are established between them. Then, a breadth-first search is performed starting from vertex 'A', and the result is printed.