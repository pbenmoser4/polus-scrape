# Constants for polus-scrape

class Constants:
    def __init__(self):

        self.VERTEX_LABEL_NONE = 'no_label'
        self.VERTEX_LABEL_COMPANY = 'company'
        self.VERTEX_LABEL_WEBSITE = 'website'
        self.VERTEX_LABEL_PERSON = 'person'
        self.VERTEX_LABEL_INVESTOR = 'investor'

        self.VERTEX_LABELS = [
            VERTEX_LABEL_COMPANY,
            VERTEX_LABEL_WEBSITE,
            VERTEX_LABEL_PERSON,
            VERTEX_LABEL_INVESTOR
        ]
