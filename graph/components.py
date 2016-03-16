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


    def hasOutEdge(self, edge):
        """
        Figure out if the current POLVertex contains the given edge

        This connection is also a test for if the current vertex has a certain outVertex

        @param POLEdge edge - the edge in the connection you're testing
        @param POLVertex vertex - the vertex in the connection you're testing
        """

        if not isinstance(edge, POLEdge):
            raise Exception("You must pass a POLEdge as the 'edge' argument")

        outVertex = edge.outV
        inVertex = edge.inV

        if not outVertex == self:
            # We're not even looking at an edge that comes out of this vertex, so it can't possibly have this edge
            return False

        #TODO implement features that check whether the edge's label and props match any edges in the existing outE dictionary. If they do, check the vertex that that edge goes into, and see if it is the same as the one on the edge passed in.

        pass

    def getOutVertices(self):
        """
        Get a list of vertices that the current vertex connects into

        The list will simply be an array of vertex ids
        """
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


    def __eq__(self, vertex):
        # Two vertices are equal if they have the same label and the same properties
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

    def getValuesString(self):

        valuesString = self.label
        for k,v in self.props:
            valuesString += ',' + str(k) + ',' + str(v)

        return valuesString

    def __str__(self):
        pass
