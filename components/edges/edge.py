# POLEdge class and associated functions

class POLEdge:
    """
    Edges within the Polus graph framework

    These edges hold a label and a property list dictionary (string -> val)
    """
    def __init__(self, label = "", props = {}, inV = None, outV = None):
        self.label = label
        self.props = props
        self.inV = inV
        self.outV = outV
