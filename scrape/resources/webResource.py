from resource import POLResource

class POLWebResource(POLResource):

    def __init__(self, url):
        POLResource.__init__(self, url, label='web')
        self.url = url
