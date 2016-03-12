# Polus Vertex class

from edges.edge import POLEdge

class POLVertex:
    """
    The base class for all vertices in the Polus Scraper project
    """
    def __init__(self, label = "", props = {}):
        """
        Initialize a POLVertex

        @param string label - the label of the vertex
        @param dictionary props - String -> value dictionary of vertex properties
        """
        self.label = label
        self.props = props
        self._out = []
        self._in = []

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
        for edge in self._out:
            #TODO implement the edge string representation
            pass

    def __json__(self):
        """
        Convert the vertex into a JSON representation
        """
        #TODO implement the __json__ function
        pass
