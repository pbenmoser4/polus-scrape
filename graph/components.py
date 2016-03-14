# Defining the basic edge and vertex classes

##########################################################
#   Polus Vertex Base Class
##########################################################

class POLVertex(object):
    """
    The base class for all vertices in the Polus Scraper project

    Properties:
    * string label - the label of the vertex
    * dictionary props - a dictionary containing the properties of this vertex
    * array inE - the POLEdges coming into this vertex
    * array outE - the POLEdges going out of this vertex
    """

    def __init__(self, label = "", props = {}):
        """
        Initialize a POLVertex

        @param string label - the label of the vertex
        @param dictionary props - String -> value dictionary of vertex properties
        """
        self.label = label if type(label) is str else None
        self.props = props if type(props) is dict else {}
        self.inE = []
        self.outE = []

    def __str__(self):
        """
        Return a string representation of the vertex

        label,prop1,val1,prop2,val2,...,propN,valN
        ->out1,Eprop1,Eval1,...,EpropN,EvalN
        ->out2,Eprop1,Eval1,...,EpropN,EvalN
        <-in1,Eprop1,Eval1,...,EpropN,EvalN
        <-in2,Eprop1,Eval1,...,EpropN,EvalN
        ...

        @return string retString - a string representation of the vertex
        """
        retString = ''
        retString += str(self.label)
        for k, v in self.props.items():
            retString += ',' + str(k), str(v)
        for edge in self.outE:
            #TODO implement the edge string representation
            pass

    def __json__(self):
        """
        Convert the vertex into a JSON representation
        """
        #TODO implement the __json__ function
        pass


##########################################################
#   Polus Edge Base     Class
##########################################################

class POLEdge(object):
    """
    Edges within the Polus graph framework
    """

    def __init__(self, label = "", props = {}, outV = None, inV = None):
        """
        Initialize a POLEdge object

        @param string label - The label of this edge
        @param dictionary props - Properties dictionary for this POLEdge
        @param POLVertex inV - The `in` vertex of this edge (the vertex it's going to)

        """

        self.label = label if type(label) is str else ''
        self.props = props if type(props) is dict else {}
        self.inV = inV if isinstance(inV, POLVertex) else None
        self.outV = outV if isinstance(outV, POLVertex) else None
