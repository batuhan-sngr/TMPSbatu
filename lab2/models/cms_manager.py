class CMSManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CMSManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.articles = []
        self.authors = []
        self.comments = {}

    def add_article(self, article):
        self.articles.append(article)
        self.comments[article] = []  # Initialize empty list of comments for the article

    def add_author(self, author):
        self.authors.append(author)

    def add_comment(self, article, comment):
        if article in self.comments:
            self.comments[article].append(comment)
        else:
            print("Article not found.")

    def get_articles(self):
        return self.articles

    def get_comments(self, article):
        return self.comments.get(article, [])
