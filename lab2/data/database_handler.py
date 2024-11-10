import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='cms_database.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        # Creating tables for authors, articles, and comments
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL UNIQUE)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS articles (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                content TEXT NOT NULL,
                                author_id INTEGER,
                                tags TEXT,
                                FOREIGN KEY (author_id) REFERENCES authors(id))''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS comments (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                content TEXT NOT NULL,
                                author_id INTEGER,
                                article_id INTEGER,
                                FOREIGN KEY (author_id) REFERENCES authors(id),
                                FOREIGN KEY (article_id) REFERENCES articles(id))''')
        self.connection.commit()

    def add_author(self, name):
        try:
            self.cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            self.connection.commit()
            return self.cursor.lastrowid
        except sqlite3.IntegrityError:
            self.cursor.execute("SELECT id FROM authors WHERE name = ?", (name,))
            return self.cursor.fetchone()[0]

    def add_article(self, title, content, author_id, tags):
        self.cursor.execute("INSERT INTO articles (title, content, author_id, tags) VALUES (?, ?, ?, ?)",
                            (title, content, author_id, ','.join(tags)))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_comment(self, content, author_id, article_id):
        self.cursor.execute("INSERT INTO comments (content, author_id, article_id) VALUES (?, ?, ?)",
                            (content, author_id, article_id))
        self.connection.commit()

    def get_articles(self):
        self.cursor.execute('''SELECT articles.id, articles.title, articles.content, authors.name, articles.tags
                               FROM articles
                               JOIN authors ON articles.author_id = authors.id''')
        return self.cursor.fetchall()

    def get_comments_for_article(self, article_id):
        self.cursor.execute('''SELECT comments.content, authors.name
                               FROM comments
                               JOIN authors ON comments.author_id = authors.id
                               WHERE comments.article_id = ?''', (article_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        self.connection.close()
