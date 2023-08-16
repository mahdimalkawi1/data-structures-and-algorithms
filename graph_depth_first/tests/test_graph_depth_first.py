import pytest
from graph_depth_first.graph_depth_first import Graph, Vertix, depth_first  

def test_depth_first_traversal_function():
    graph = Graph()
    A = graph.add_vertix('A')
    B = graph.add_vertix('B')
    C = graph.add_vertix('C')
    D = graph.add_vertix('D')
    E = graph.add_vertix('E')
    F = graph.add_vertix('F')
    G = graph.add_vertix('G')
    H = graph.add_vertix('H')
    graph.add_edge(A, B)
    graph.add_edge(A, C)
    graph.add_edge(A, G)
    graph.add_edge(B, D)
    graph.add_edge(B, E)
    graph.add_edge(C, F)
    graph.add_edge(G, H)

    result = depth_first(graph, A)
    assert result == ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H']

def test_depth_first_traversal_function_complex():
    graph = Graph()
    A = graph.add_vertix('A')
    B = graph.add_vertix('B')
    C = graph.add_vertix('C')
    D = graph.add_vertix('D')
    E = graph.add_vertix('E')
    F = graph.add_vertix('F')
    G = graph.add_vertix('G')
    H = graph.add_vertix('H')
    I = graph.add_vertix('I')
    graph.add_edge(A, B)
    graph.add_edge(A, C)
    graph.add_edge(B, D)
    graph.add_edge(B, E)
    graph.add_edge(C, F)
    graph.add_edge(C, G)
    graph.add_edge(G, H)
    graph.add_edge(H, I)

    result = depth_first(graph, A)
    assert result == ['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H', 'I']

def test_depth_first_traversal_function_single_vertex():
    graph = Graph()
    A = graph.add_vertix('A')

    result = depth_first(graph, A)
    assert result == ['A']

