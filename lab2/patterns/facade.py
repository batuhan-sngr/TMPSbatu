from patterns.builder import ArticleBuilder
from bridge import DatabaseBridge

class ContentManagerFacade:
    def __init__(self, database_bridge):
        self.db_bridge = database_bridge

    def create_author(self, name):
        return self.db_bridge.add_author(name)

    def create_article(self, title, body, author_id, tags):
        return self.db_bridge.add_article(title, body, author_id, tags)

    def add_comment(self, content, article_id, author_id):
        return self.db_bridge.add_comment(content, article_id, author_id)

    def list_authors(self):
        return self.db_bridge.list_authors()

    def list_articles(self):
        return self.db_bridge.list_articles()

    def list_comments(self):
        return self.db_bridge.list_comments()


    def create_author(self, name):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO authors (author_name) VALUES (%s) RETURNING author_id;",
                    (name,)
                )
                author_id = cursor.fetchone()[0]
            return {"author_id": author_id, "name": name}
        except Exception as e:
            print(f"Error creating author: {e}")
            raise

    def create_article(cms, factory):
        author_name = input("Enter the author's name: ")
        title = input("Enter the article title: ")
        body = input("Enter the article content: ")
        tags = input("Enter tags (comma-separated): ").split(',')

        # Fetch authors from CMSManager
        authors = cms.get_authors()
        author = next((a for a in authors if a.name == author_name), None)
        if not author:
            author = factory.create_content('author', name=author_name)
            cms.add_author(author)

        # Build the article
        article_builder = ArticleBuilder()
        article = (article_builder
                .set_title(title)
                .set_body(body)
                .set_author(author)
                .set_tags([tag.strip() for tag in tags])
                .build())
        cms.add_article(article)
        print(f"Article '{title}' created successfully!")


    def add_comment(self, article_title, comment_content, author_name):
        try:
            author = self.find_author_by_name(author_name)
            if not author:
                author = self.create_author(author_name)

            article = self.find_article_by_title(article_title)
            if not article:
                raise ValueError(f"Article with title '{article_title}' not found")

            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO comment (comment_content, comment_article_id, comment_author_id) VALUES (%s, %s, %s) RETURNING comment_id;",
                    (comment_content, article["article_id"], author["author_id"])
                )
                comment_id = cursor.fetchone()[0]
            return {"comment_id": comment_id, "content": comment_content, "article": article, "author": author}
        except Exception as e:
            print(f"Error adding comment: {e}")
            raise

    def find_author_by_name(self, name):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT author_id, author_name FROM authors WHERE author_name = %s;",
                    (name,)
                )
                row = cursor.fetchone()
                return {"author_id": row[0], "name": row[1]} if row else None
        except Exception as e:
            print(f"Error finding author: {e}")
            raise

    def find_article_by_title(self, title):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT article_id, article_title, article_body, article_author_id FROM article WHERE article_title = %s;",
                    (title,)
                )
                row = cursor.fetchone()
                if row:
                    return {
                        "article_id": row[0],
                        "title": row[1],
                        "body": row[2],
                        "author_id": row[3]
                    }
                return None
        except Exception as e:
            print(f"Error finding article: {e}")
            raise

    def list_articles(self):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT article_id, article_title, article_body, article_author_id FROM article;"
                )
                rows = cursor.fetchall()
                return [
                    {"article_id": row[0], "title": row[1], "body": row[2], "author_id": row[3]}
                    for row in rows
                ]
        except Exception as e:
            print(f"Error listing articles: {e}")
            raise

    def list_authors(self):
        query = "SELECT author_id, author_name FROM authors"
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(query)
                return [{"author_id": row[0], "name": row[1]} for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching authors: {e}")
            return []


    def list_comments(self):
        try:
            with self.db.connection.cursor() as cursor:
                cursor.execute(
                    "SELECT comment_id, comment_content, comment_article_id, comment_author_id FROM comment;"
                )
                rows = cursor.fetchall()
                return [
                    {
                        "comment_id": row[0],
                        "content": row[1],
                        "article_id": row[2],
                        "author_id": row[3],
                    }
                    for row in rows
                ]
        except Exception as e:
            print(f"Error listing comments: {e}")
            raise
