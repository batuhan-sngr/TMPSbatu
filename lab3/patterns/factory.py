from models.article import Article
from models.author import Author
from models.comment import Comment

class ContentFactory:
    def create_content(self, content_type, **kwargs):
        if content_type == "author":
            return Author(name=kwargs.get("name"))
        elif content_type == "article":
            return Article(
                title=kwargs.get("title"),
                body=kwargs.get("body"),
                author=kwargs.get("author"),
                tags=kwargs.get("tags", []),
            )
        elif content_type == "comment":
            return Comment(
                content=kwargs.get("content"),
                author=kwargs.get("author"),
            )
        else:
            raise ValueError(f"Unknown content type: {content_type}")

