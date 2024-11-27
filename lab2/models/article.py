class Article:
    def __init__(self, title="", body="", author=None, tags=None):
        self.title = title
        self.body = body
        self.author = author
        self.tags = tags or []
