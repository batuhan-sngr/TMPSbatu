from models.article import Article

class ArticleBuilder:
    def __init__(self):
        self.article = Article()

    def set_title(self, title):
        self.article.title = title
        return self

    def set_body(self, body):
        self.article.body = body
        return self

    def set_author(self, author):
        self.article.author = author
        return self

    def set_tags(self, tags):
        self.article.tags = tags
        return self

    def build(self):
        return self.article
