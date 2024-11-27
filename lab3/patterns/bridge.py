from data.database import Database  # Your existing database implementation


class DatabaseBridge:
    def add_author(self, name):
        raise NotImplementedError

    def add_article(self, title, body, author_id, tags):
        raise NotImplementedError

    def add_comment(self, content, article_id, author_id):
        raise NotImplementedError

    def list_authors(self):
        raise NotImplementedError

    def list_articles(self):
        raise NotImplementedError

    def list_comments(self):
        raise NotImplementedError


class SQLDatabaseBridge(DatabaseBridge):
    def __init__(self):
        self.db = Database()

    def add_author(self, name):
        with self.db.connection.cursor() as cursor:
            cursor.execute("INSERT INTO authors (author_name) VALUES (%s) RETURNING author_id", (name,))
            return cursor.fetchone()[0]

    def add_article(self, title, body, author_id, tags):
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO article (article_title, article_body, article_author_id) VALUES (%s, %s, %s) RETURNING article_id",
                (title, body, author_id)
            )
            article_id = cursor.fetchone()[0]
            for tag in tags:
                cursor.execute(
                    "INSERT INTO article_tags (article_id, tag) VALUES (%s, %s)", (article_id, tag)
                )
            return article_id

    def add_comment(self, content, article_id, author_id):
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO comment (comment_content, comment_article_id, comment_author_id) VALUES (%s, %s, %s)",
                (content, article_id, author_id)
            )

    def list_authors(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute("SELECT author_id, author_name FROM authors")
            return [{"author_id": row[0], "name": row[1]} for row in cursor.fetchall()]

    def list_articles(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute("SELECT article_id, article_title, article_body, article_author_id FROM article")
            return [
                {"article_id": row[0], "title": row[1], "body": row[2], "author_id": row[3]} for row in cursor.fetchall()
            ]

    def list_comments(self):
        with self.db.connection.cursor() as cursor:
            cursor.execute(
                "SELECT comment_id, comment_content, comment_article_id, comment_author_id FROM comment"
            )
            return [
                {
                    "comment_id": row[0],
                    "content": row[1],
                    "article_id": row[2],
                    "author_id": row[3],
                }
                for row in cursor.fetchall()
            ]
