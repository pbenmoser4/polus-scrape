# tests for the components.py file
# testing the POLEdge and POLVertex classes

from graph.components import POLVertex, POLEdge

def test_init_empty_vertex():
    v = POLVertex();

    # The POLVertex's label field should be an empty string
    assert v.label == ""

    # We need to have a field called `props` that stores the POLVertex's properties
    assert v.props == {}

    # We should have `inE` and `outE` fields representing edges. Both should be empty
    assert v.inE == {}
    assert v.outE == {}

def test_init_correct_vertex():

    label = 'label'
    props = {'field' : 'value'}

    v = POLVertex(label, props)

    assert v.label == 'label'
    assert v.props == {'field' : 'value'}
    assert v.inE == {}
    assert v.outE == {}

# Passing incorrect values during initialization

# Creating two vertices at almost the same time should not have the same created_date

def test_created_date_same():

    v1 = POLVertex()
    v2 = POLVertex()

    assert v1.created_date != v2.created_date

# Testing Vertex equality

def test_vertex_equals_self():

    v = POLVertex()
    assert v == v

def test_two_empty_vertices_are_equal():

    v1 = POLVertex()
    v2 = POLVertex()

    assert v1 == v2

def test_vertex_label_props_edges_equality():

    label = 'label'
    props = {"field" : "value"}

    v1 = POLVertex(label)
    v2 = POLVertex()

    assert v1 != v2

    v2.label = label

    assert v1 == v2

    v1.props = props

    assert v1 != v2

    v2.props = props

    assert v1 == v2

    v3 = POLVertex()

# Testing Edges

def test_init_empty_edge():
    edge = POLEdge()

    assert edge.label == ''
    assert edge.props == {}
    assert edge.inV == None
    assert edge.outV == None

def test_init_correct_edge():

    label = 'label'
    props = {"some" : "value"}

    edge = POLEdge(label, props)

    assert edge.label == 'label'
    assert edge.props == {'some' : 'value'}
    assert edge.outV == None
    assert edge.inV == None

def test_init_incorrect_edge():

    label = 5
    props = True

    edge = POLEdge(label, props)

    assert edge.label == ''
    assert edge.props == {}
    assert edge.outV == None
    assert edge.inV == None
