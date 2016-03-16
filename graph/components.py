# Defining the basic edge and vertex classes

from uuid import *
from datetime import *

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
        self.inE = {}
        self.outE = {}

        self.created_date = datetime.utcnow()
        self.updated_date = self.created_date
        self._id = uuid4()

    def connectToVertex(self, outV, edgeLabel = '', edgeProps = {}):
        """
        Connect the current POLVertex to another POLVertex

        This creates an edge that connects the two POLVertex instances

        @param POLVertex outV - the vertex you're connecting out to
        @param string edgeLabel - the label of the connecting edge
        @param dictionary edgeProps - the properties of the connecting edge
        @return boolean - true if the connection succeeded
        """

        if not isinstance(outV, POLVertex):
            # If the object passed in isn't a POLVertex, raise an exception
            raise Exception("You can only create a connection to another POLVertex")

        # Check if this vertex is already connected
        if self.hasOutVertex(outV):
            pass

        edge = POLEdge(edgeLabel, edgeProps)
        # The vertex that was passed in is an 'out' vertex from the point
        # of view of `self`, but, to the created edge, `self` is the 'out'
        # vertex (the edge comes *out* of that vertex), and the passed
        # vertex is the 'in' vertex (the edge goes *into* that vertex)
        edge.outV = self
        edge.inV = outV
        self.outE.push(edge)

        #TODO deal with duplicate connections

    def hasOutVertex(self, vertex):
        """
        Figure out if self is connected to the passed vertex

        @param POLVertex vertex - The vertex we are checking
        @return boolean - true if it has the passed vertex as an out vertex, false otherwise
        """
        outVertices = (e.inV for e in self.outE)

        #TODO implement

        return False

    def getOutVertices(self):
        #TODO implement getOutVertices
        pass

    def getInVertices(self):
        #TODO implement getInVertices


    def __str__(self):
        """
        Return a string representation of the vertex

        label,prop1,val1,prop2,val2,...,propN,valN
        ->out1,ELabel,EProp1,EVal1,...,EPropN,EValN
        <-in1,ELabel,EProp1,EVal1,...,EPropN,EValN
        ...

        @return string retString - a string representation of the vertex
        """
        retString = ''
        retString += str(self.label)
        for k, v in self.props.items():
            retString += ',' + str(k) + ',' + str(v)
        for edge in self.outE:
            retString += '\n->' # start off on a new line
            retString += edge.inV.label if edge.inV else ''
            retString += ',' + edge.getValuesString()

        for edge in self.inE:
            retString += '\n<-' # start off on a new line
            retString += edge.outV.label if edge.outV else ''
            retString += ',' + edge.getValuesString()

        return retString

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, vertex):
        return isinstance(vertex, POLVertex) and self._id == vertex._id

    def __json__(self):
        """
        Convert the vertex into a JSON representation
        """
        #TODO implement the __json__ function
        pass


##########################################################
#   Polus Edge Base Class
##########################################################

class POLEdge(object):
    """
    Edges within the Polus graph framework
    """

    def __init__(self, label = "", props = {}):
        """
        Initialize a POLEdge object

        @param string label - The label of this edge
        @param dictionary props - Properties dictionary for this POLEdge
        """

        self.label = label if type(label) is str else ''
        self.props = props if type(props) is dict else {}
        self.inV = None
        self.outV = None

        self.created_date = datetime.utcnow()
        self.updated_date = self.created_date
        self._id = uuid4()

    def getValuesString(self):

        valuesString = self.label
        for k,v in self.props:
            valuesString += ',' + str(k) + ',' + str(v)

        return valuesString

    def __str__(self):
        pass

    def __hash__(self):
        return hash(self._id)
