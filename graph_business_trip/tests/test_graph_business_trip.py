import pytest
from graph_business_trip.graph_business_trip import Graph, business_trip

@pytest.fixture
def sample_graph():
    g = Graph()
    g.add_edge('Metroville', 'Pandora', 82)
    g.add_edge('Arendelle', 'New Monstropolis', 42)
    g.add_edge('New Monstropolis', 'Naboo', 73)
    return g

def test_possible_trip(sample_graph):
    assert business_trip(sample_graph, ['Arendelle', 'New Monstropolis', 'Naboo']) == 115

def test_impossible_trip(sample_graph):
    assert business_trip(sample_graph, ['Naboo', 'Pandora']) is None

def test_partial_trip(sample_graph):
    assert business_trip(sample_graph, ['Metroville', 'Pandora', 'Arendelle']) is None
