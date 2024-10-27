# Topic: Creational Design Patterns
## Content Management System (CMS)

**Author:** Emre Batuhan Sungur, **Group:** FAF-221

## Objectives

The primary objectives of this project are:
1. To become familiar with Creational Design Patterns (CDPs).
2. To select a specific domain and define its classes and entities.
3. To implement at least three Creational Design Patterns to demonstrate optimized object instantiation.

## Domain

The domain chosen for this project is a **Content Management System** (CMS) that allows users to:
- Write new articles,
- View a list of articles,
- Read articles and comments,
- Add comments to articles.

## Used Design Patterns

1. **Singleton**: Ensures a single instance of the `CMSManager`, responsible for coordinating interactions between the articles, authors, and comments.
2. **Factory Method**: Utilized in the `ContentFactory` to create `Author`, `Article`, and `Comment` objects dynamically based on specified content type.
3. **Builder**: Applied in the `ArticleBuilder` class to facilitate the construction of complex `Article` objects with multiple optional attributes.

## Implementation

This CMS allows users to interact with the system via a menu to create new articles, view existing articles, and add comments. The Singleton pattern ensures there's only one instance of the CMS manager, which organizes and holds all the content. The Factory Method pattern is used to streamline creating different types of content, such as authors and comments. The Builder pattern allows for flexible and modular article creation, letting users add optional attributes such as tags without modifying the main construction logic.

### Code Snippets

**Factory Method:**

The `ContentFactory` class uses a Factory Method pattern to create different content types dynamically.

```python
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
```

**Singelton Pattern:**

`CMSManager` is implemented as a Singleton to ensure a single instance across the application.

```python
class CMSManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(CMSManager, cls).__new__(cls, *args, **kwargs)
        return cls._instance
```

**Builder Pattern::**

`ArticleBuilder` enables the construction of complex Article objects with optional parameters.

```python
class ArticleBuilder:
    def __init__(self):
        self.title = ""
        self.body = ""
        self.author = None
        self.tags = []

    def set_title(self, title):
        self.title = title
        return self

    def set_body(self, body):
        self.body = body
        return self

    def set_author(self, author):
        self.author = author
        return self

    def set_tags(self, tags):
        self.tags = tags
        return self

    def build(self):
        return Article(self.title, self.body, self.author, self.tags)
```

**Main Menu Functionality:**

```python
def main():
    cms = CMSManager()
    while True:
        print("\n1. Write a New Article\n2. View All Articles\n3. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            create_article(cms)
        elif choice == '2':
            view_articles(cms)
        elif choice == '3':
            cms.close()
            print("Exiting...")
            break
```

### Conclusions / Screenshots / Results

**Conclusions:**

This project serves as an in-depth application of Creational Design Patterns (CDPs) within a Content Management System (CMS), showing the advantages of structured object creation to improve both flexibility and maintainability. Through the Singleton, Factory Method, and Builder patterns, the CMS achieves a streamlined design that scales easily and provides a consistent, user-friendly experience.

1. Singleton Pattern: The Singleton pattern is applied to the CMSManager class, ensuring a single instance manages the CMS’s data, including articles, authors, and comments. This approach prevents duplicate instances, which could lead to inconsistencies in data handling. By centralizing content management in one instance, we guarantee data integrity across the system and simplify data access. This pattern also makes future scalability simpler, as any additional features or changes to CMSManager affect the entire system in a controlled, predictable way.

2. Factory Method Pattern: The Factory Method pattern offers a robust solution for creating diverse content types within the CMS. By using the ContentFactory, we ensure that article, author, and comment objects are created consistently, regardless of any variations in input. This reduces redundant code for object creation and allows us to add more content types in the future without major changes to the existing codebase. The pattern also improves code readability by encapsulating content creation logic, making the CMS more modular and easier to debug or expand.

3. Builder Pattern: The Builder pattern is used to simplify the creation of complex Article objects. By allowing optional fields like tags to be added flexibly, the pattern enhances user control over article attributes while maintaining code simplicity. This structure is particularly advantageous when working with complex objects that have multiple optional parameters, as it reduces potential errors and allows for cleaner, more readable code. Additionally, it improves maintainability because modifications to article attributes are isolated to the ArticleBuilder class, without impacting other parts of the system.

Overall, this CMS project demonstrates the effectiveness of CDPs in organizing complex systems. These design patterns not only help streamline the development process but also pave the way for future growth and modifications. The resulting CMS is adaptable, easier to debug, and primed for future expansion, such as adding new content types, permissions, or features like article categorization and content scheduling. The project provides a scalable foundation for building a fully-featured CMS, showcasing how CDPs can transform a basic structure into a robust, efficient solution for managing content in real-world applications.

**Screenshots:**

**Results:**

The CMS successfully allows for:

* Persistent article and comment storage,
* Clear author associations,
* Easy retrieval and display of content.
By using Creational Design Patterns, the codebase remains manageable, extensible, and ready for further enhancements.