from patterns.facade import ContentManagerFacade
from models.comment import Comment
from models.author import Author
from models.article import Article
from data.database import Database 
from patterns.adapter import JSONExporter, XMLExporter

class CMSManager:
    def __init__(self, db_bridge):
        super().__init__()
        self.db = Database()
        self.facade = ContentManagerFacade(db_bridge)

    def add_author(self, author):
        author_id = self.facade.create_author(author.name)
        self.notify("new_author", {"name": author.name})
        return author_id

    def add_article(self, article):
        article_id = self.facade.create_article(
            title=article.title,
            body=article.body,
            author_id=article.author.id,
            tags=article.tags,
        )
        self.notify("new_article", {"title": article.title, "author": article.author.name})
        return article_id

    def add_comment(self, article, comment):
        self.facade.add_comment(
            content=comment.content,
            article_id=article.id,
            author_id=comment.author.id,
        )
        self.notify("new_comment", {
            "article_title": article.title,
            "author": comment.author.name,
            "content": comment.content,
        })
    
    def get_authors(self):
        authors_data = self.facade.list_authors()
        return [Author(name=a["name"]) for a in authors_data]

    def get_articles(self):
        articles_data = self.facade.list_articles()
        authors_data = {a["author_id"]: a["name"] for a in self.facade.list_authors()}

        articles = []
        for data in articles_data:
            author_name = authors_data.get(data["author_id"])
            article = Article(
                title=data["title"],
                body=data["body"],
                author=Author(author_name),
                tags=[]  # Assuming tags aren't stored yet
            )
            articles.append(article)
        return articles

    def get_comments(self, article):
        comments_data = self.facade.list_comments()
        authors_data = {a["author_id"]: a["name"] for a in self.facade.list_authors()}
        article_id = next(
            (a["article_id"] for a in self.facade.list_articles() if a["title"] == article.title),
            None,
        )
        if not article_id:
            return []

        comments = []
        for data in comments_data:
            if data["article_id"] == article_id:
                author_name = authors_data.get(data["author_id"])
                comment = Comment(content=data["content"], author=Author(author_name))
                comments.append(comment)
        return comments
    
    def export_articles(self, format_type="json"):
        articles = self.get_articles()
        if format_type == "json":
            exporter = JSONExporter()
        elif format_type == "xml":
            exporter = XMLExporter()
        else:
            raise ValueError("Unsupported format")
        return exporter.export(articles)


    def close(self):
        self.db.close()
