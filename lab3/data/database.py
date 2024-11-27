import psycopg2

class Database:
    def __init__(self):
        try:
            # Establishing a database connection
            self.connection = psycopg2.connect(
                host="localhost",
                port="5432",
                database="tmps",
                user="postgres",
                password="1924"
            )
            self.connection.autocommit = True  # Ensures changes are committed automatically
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            raise

    def create_tables(self):
        # SQL commands to create tables
        commands = (
            """
            CREATE TABLE authors (
                author_id SERIAL PRIMARY KEY,
                author_name VARCHAR(255) NOT NULL
            )
            """,
            """
            CREATE TABLE article (
                article_id SERIAL PRIMARY KEY,
                article_title VARCHAR(255) NOT NULL,
                article_body VARCHAR(255) NOT NULL,
                article_author_id INTEGER NOT NULL,
                FOREIGN KEY (article_author_id)
                    REFERENCES authors (author_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """,
            """
            CREATE TABLE comment (
                comment_id SERIAL PRIMARY KEY,
                comment_content VARCHAR(255) NOT NULL,
                comment_article_id INTEGER NOT NULL,
                comment_author_id INTEGER NOT NULL,
                FOREIGN KEY (comment_article_id)
                    REFERENCES article (article_id)
                    ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (comment_author_id)
                    REFERENCES authors (author_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
            )
            """
        )
        try:
            with self.connection.cursor() as cursor:
                for command in commands:
                    cursor.execute(command)
                print("Tables created successfully!")
        except Exception as e:
            print(f"Error creating tables: {e}")
            raise

    def close(self):
        # Closing the database connection
        if self.connection:
            self.connection.close()

# Main entry point
if __name__ == "__main__":
    db = Database()
    try:
        db.create_tables()
    finally:
        db.close()
