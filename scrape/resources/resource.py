class POLResource(object):

    def __init__(self, resource, label = 'default', tags = [], permissions = []):
        """
        Initialize a new POLResource instance

        @param object resource - the resource to be stored
        @param string label - resource label
        @param array tags - resource tags
        @param array permissions - resource permissions
        """
        self.__resource = resource
        self.label = label
        self.tags = tags
        self.permissions = permissions

    def getResource(self):
        """
        Get this POLResource's resource object

        @return resource - this POLResource's resource
        """
        return self.__resource

    def setResource(self, newResource):
        """
        Set this POLResource's resource

        @param object newResource - the resource to set
        @return bool success - true if the set was successful, fals otherwise
        """
        self.__resource = newResource
        return True
