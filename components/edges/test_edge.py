from edges.edge import POLEdge
from vertices.vertex import POLVertex

def test_init_empty_edge():
    edge = POLEdge()

    assert edge.label == ''
    assert edge.props == {}
    assert edge.inV == None
    assert edge.outV == None

def test_init_label_edge():
    label = 'label'

    edge = POLEdge(label)

    assert edge.label == 'label'
    assert edge.props == {}
    assert edge.inV == None
    assert edge.outV == None

def test_init_props_edge():
    props = {"field" : "value"}

    edge = POLEdge(props = props)

    assert edge.label == ''
    assert edge.props == {"field" : "value"}
    assert edge.inV == None
    assert edge.outV == None

def test_init_inV_edge():

    v = POLVertex('label', {"field" : "value"})
    edge = POLEdge(inV = v)

    assert edge.label == ''
    assert edge.props == {}
    assert edge.inV == v
    assert edge.outV == None

def test_init_outV_edge():

    v = POLVertex('label', {"field" : "value"})
    edge = POLEdge(outV = v)

    assert edge.label == ''
    assert edge.props == {}
    assert edge.inV == None
    assert edge.outV == v

def test_init_all_edge():

    label = 'label'
    props = {"field" : "value"}
    inV = POLVertex('in', {"field" : "value"})
    outV = POLVertex('out', {"field" : "value"})
    edge = POLEdge(label, props, inV, outV)

    assert edge.label == 'label'
    assert edge.props == {"field" : "value"}
    assert edge.inV == inV
    assert edge.outV == outV
