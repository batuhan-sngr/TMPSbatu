from models.article import Article
from models.author import Author
from models.comment import Comment

class ContentFactory:
    def create_content(self, content_type, **kwargs):
        if content_type == 'article':
            return Article(**kwargs)
        elif content_type == 'author':
            return Author(**kwargs)
        elif content_type == 'comment':
            return Comment(**kwargs)
        else:
            raise ValueError("Unknown content type")
