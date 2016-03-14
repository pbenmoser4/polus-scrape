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
    assert v.inE == []
    assert v.outE == []

def test_init_label_vertex():
    label = 'label'

    v = POLVertex(label)

    assert v.label == 'label'
    assert v.props == {}
    assert v.inE == []
    assert v.outE == []

def test_init_props_vertex():
    props = {"field" : "value"}

    v = POLVertex(props = props)

    assert v.label == ''
    assert v.props == {"field" : "value"}
    assert v.inE == []
    assert v.outE == []

def test_init_label_props_vertex():
    label = 'label'
    props = {"field" : "value"}

    v = POLVertex(label, props)

    assert v.label == 'label'
    assert v.props == {"field" : "value"}
    assert v.inE == []
    assert v.outE == []

# Passing incorrect values during initialization




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
    outV = POLVertex('out', {"field", "value"})
    inV = POLVertex('in', {"field", "value"})

    edge = POLEdge(label, props, outV, inV)

    assert edge.label == 'label'
    assert edge.props == {'some' : 'value'}
    assert edge.outV == outV
    assert edge.inV == inV

def test_init_incorrect_edge():

    label = 5
    props = True
    outV = 'hello'
    inV = {"something" : "else"}

    edge = POLEdge(label, props, outV, inV)

    assert edge.label == ''
    assert edge.props == {}
    assert edge.outV == None
    assert edge.inV == None
