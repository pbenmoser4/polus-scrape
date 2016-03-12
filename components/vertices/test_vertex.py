from vertex import POLVertex

def test_init_empty_vertex():
    v = POLVertex();

    # The POLVertex's label field should be an empty string
    assert v.label == ""

    # We need to have a field called `props` that stores the POLVertex's properties
    assert v.props == {}

    # We should have `_in` and `_out` fields representing edges. Both should be empty
    assert v._in == []
    assert v._out == []

def test_init_label_vertex():
    label = 'label'

    v = POLVertex(label)

    assert v.label == 'label'
    assert v.props == {}
    assert v._in == []
    assert v._out == []

def test_init_props_vertex():
    props = {"field" : "value"}

    v = POLVertex(props = props)

    assert v.label == ''
    assert v.props == {"field" : "value"}
    assert v._in == []
    assert v._out == []

def test_init_label_props_vertex():
    label = 'label'
    props = {"field" : "value"}

    v = POLVertex(label, props)

    assert v.label == 'label'
    assert v.props == {"field" : "value"}
    assert v._in == []
    assert v._out == []
