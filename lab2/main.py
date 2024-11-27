from cms_manager import CMSManager
from patterns.factory import ContentFactory
from patterns.builder import ArticleBuilder
from patterns.bridge import SQLDatabaseBridge
from patterns.observer import EmailNotifier, Logger


def display_menu():
    print("\nContent Management System")
    print("1. Write a New Article")
    print("2. View All Articles")
    print("3. Export Articles")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice

def create_article(cms, factory):
    author_name = input("Enter the author's name: ")
    title = input("Enter the article title: ")
    body = input("Enter the article content: ")
    tags = input("Enter tags (comma-separated): ").split(',')

    # Create or find the author
    author = next((a for a in cms.get_authors() if a.name == author_name), None)
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

def view_articles(cms, factory):
    articles = cms.get_articles()
    if not articles:
        print("No articles available.")
        return

    print("\nArticles:")
    for i, article in enumerate(articles):
        print(f"{i+1}. {article.title} by {article.author.name}")

    choice = input("\nEnter the number of the article to view or 'b' to go back: ")
    if choice.lower() == 'b':
        return
    try:
        article_index = int(choice) - 1
        if 0 <= article_index < len(articles):
            selected_article = articles[article_index]
            display_article(selected_article, cms, factory)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def display_article(article, cms, factory):
    print(f"\nTitle: {article.title}")
    print(f"Author: {article.author.name}")
    print(f"Content: {article.body}")
    print(f"Tags: {', '.join(article.tags)}")
    comments = cms.get_comments(article)
    print("\nComments:")
    if comments:
        for comment in comments:
            print(f"- {comment.content} by {comment.author.name}")
    else:
        print("No comments yet.")

    # Option to add a comment
    choice = input("\nDo you want to add a comment? (y/n): ")
    if choice.lower() == 'y':
        create_comment(article, cms, factory)

def create_comment(article, cms, factory):
    author_name = input("Enter your name: ")
    content = input("Enter your comment: ")

    # Create or find the author
    author = next((a for a in cms.authors if a.name == author_name), None)
    if not author:
        author = factory.create_content('author', name=author_name)
        cms.add_author(author)

    # Create the comment and add it to the article
    comment = factory.create_content('comment', content=content, author=author)
    cms.add_comment(article, comment)
    print("Comment added successfully!")

def export_articles(cms):
    format_type = input("Enter export format (json/xml): ").strip().lower()
    try:
        exported_data = cms.export_articles(format_type)
        print(f"Exported Articles:\n{exported_data}")
    except ValueError as e:
        print(e)

def main():
    cms = CMSManager(db_bridge)
    db_bridge = SQLDatabaseBridge()
    factory = ContentFactory()

    # Attach observers
    email_notifier = EmailNotifier()
    logger = Logger()
    cms.attach(email_notifier)
    cms.attach(logger)

    try:
        while True:
            choice = display_menu()
            if choice == '1':
                create_article(cms, factory)
            elif choice == '2':
                view_articles(cms, factory)
            elif choice == '3':
                export_articles(cms)
            elif choice == '4':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        cms.close()

if __name__ == "__main__":
    main()

