from data.database_handler.py import DatabaseHandler

class CMSFacade:
    def __init__(self):
        self.db_handler = DatabaseHandler()

    def create_article(self, title, content, author_name, tags):
        author_id = self.db_handler.add_author(author_name)
        article_id = self.db_handler.add_article(title, content, author_id, tags)
        print(f"Article '{title}' created successfully with ID {article_id}!")

    def display_articles(self):
        articles = self.db_handler.get_articles()
        for article in articles:
            print(f"{article[1]} by {article[3]}\n{article[2]}\nTags: {article[4]}\n")
            comments = self.db_handler.get_comments_for_article(article[0])
            if comments:
                print("Comments:")
                for comment in comments:
                    print(f" - {comment[0]} by {comment[1]}")
            print()

    def add_comment(self, article_id, comment_content, author_name):
        author_id = self.db_handler.add_author(author_name)
        self.db_handler.add_comment(comment_content, author_id, article_id)
        print(f"Comment added to article ID {article_id} successfully.")
