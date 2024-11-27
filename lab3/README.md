# Topic: Behavioral Design Patterns
## Content Management System (CMS)

**Author:** Emre Batuhan Sungur, **Group:** FAF-221

## Objectives

1. Study and understand the Behavioral Design Patterns.

2. As a continuation of the previous laboratory work, think about what communication between software entities might be involed in your system.

3. Implement some additional functionalities using behavioral design patterns.

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

This CMS allows users to interact with the system via a menu to create new articles, view existing articles, and add comments. In this CMS, I've introduced the Observer Pattern to handle dynamic updates when articles are created. The goal is to notify subscribers (e.g., users or other components) whenever a new article is published. This ensures that multiple system parts remain synchronized without tightly coupling them.("in theory/not actually functional")

### Code Snippets

**Observer Pattern:**
Subject Interface: The `Observable` interface is implemented by any class that needs to notify subscribers. In this case, the `CMSManager` acts as the observable subject, informing subscribers when new articles are added.

```python
class Observable:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, article):
        for observer in self._observers:
            observer.update(article)
```

Observer Interface: The `Observer` interface defines the update method, which is triggered whenever the subject notifies observers. Concrete implementations include classes like `EmailNotifier` and `Logger`.

```python
class Observer:
    def update(self, article):
        raise NotImplementedError
```

Concrete Observers: These classes implement specific behaviors upon receiving notifications. For example:

- `EmailNotifier`: Sends an email to subscribers about the new article.
- `Logger`: Logs the new article to a file for auditing purposes.

```python
class EmailNotifier(Observer):
    def update(self, article):
        print(f"Email Notification: New article published - {article.title} by {article.author.name}")

class Logger(Observer):
    def update(self, article):
        with open("article_log.txt", "a") as log_file:
            log_file.write(f"New Article: {article.title} by {article.author.name}\n")
```

```python
class CMSManager(Observable):
    def __init__(self, database_bridge):
        super().__init__()
        self.db_bridge = database_bridge

    def add_article(self, article):
        self.db_bridge.add_article(
            article.title, article.body, article.author.id, article.tags
        )
        self.notify(article)
```

Usage Example: Observers are attached to the `CMSManager`, ensuring they receive notifications upon article creation.

```python
cms_manager = CMSManager(SQLDatabaseBridge())
email_notifier = EmailNotifier()
logger = Logger()

cms_manager.attach(email_notifier)
cms_manager.attach(logger)

article = Article(title="Observer Pattern", body="Explaining the Observer pattern", author=Author("John Doe"))
cms_manager.add_article(article)
```

### Conclusions / Screenshots / Results

**Conclusions:**

The introduction of the Observer Pattern into the CMS project has enabled real-time notifications to various system components. This implementation showcases several important benefits and aligns with the core principles of Behavioral Design Patterns.

Real-Time Updates: By decoupling the notification logic, the system can now inform multiple observers (e.g., email systems, logging modules) about the creation of a new article in real-time. This ensures that every relevant part of the system is synchronized without requiring direct dependencies, making it especially useful in applications where timely updates are critical.

Loose Coupling: The `CMSManager` class, acting as the observable subject, has no knowledge of the internal workings of its observers. This loose coupling allows the system to remain modular and maintainable, as changes in one component (e.g., updating the logger to include timestamps) do not affect other parts of the codebase.

Extensibility: The design is inherently extensible, enabling the addition of new observer behaviors without altering existing logic. For instance, implementing an `SMSNotifier` or a `DashboardUpdater` is as simple as creating a new class that adheres to the `Observer` interface. This ensures that the system can adapt to future requirements without introducing unnecessary complexity.

Maintainability and Testing: By isolating the notification logic into its own pattern, the system becomes easier to maintain and test. Observers can be tested independently of the subject, and vice versa, promoting better code quality and reducing the risk of regressions during future development.

The Observer Pattern also aligns with real-world scenarios. For instance, in a content management system like this one, notifying users or administrators about new articles is a common requirement. With this pattern, we’ve created a scalable and future-proof approach to handle such updates. Furthermore, the pattern simplifies debugging and auditing by centralizing notifications, as seen in the `Logger` implementation, which ensures every new article is logged systematically.

Overall, integrating the Observer Pattern has added dynamic behavior to the CMS, allowing it to grow in functionality without sacrificing simplicity or readability. This pattern not only addresses immediate needs, like sending email notifications, but also lays the foundation for future enhancements. By using Behavioral Design Patterns effectively, my CMS project become a practical example of how thoughtful design improves functionality, adaptability, and system longevity. As in the last report these behavioral design pattern was also really helpful for me.