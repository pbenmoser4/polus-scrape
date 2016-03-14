from graph.components import POLVertex, POLEdge

if __name__ == "__main__":

    label = 'label'
    properties = {
        "field1" : "value1",
        "field2" : "value2"
    }

    vertex1 = POLVertex(label, properties)

    vertex2 = POLVertex('other', {"something", "else"})

    edge = POLEdge('oneToTwo', {"prop" : "value"}, vertex1, vertex2)

    print(vertex)
