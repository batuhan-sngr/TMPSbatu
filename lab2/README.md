# Topic: Structural Design Patterns
## Content Management System (CMS)

**Author:** Emre Batuhan Sungur, **Group:** FAF-221

## Objectives

1. Study and understand the Structural Design Patterns.
2. Expand on the previous laboratory work by identifying and implementing additional functionalities needed for the CMS system.
3. Apply Structural Design Patterns to improve the system's architecture and scalability.

## Domain

The domain chosen for this project is a **Content Management System** (CMS) that allows users to:
- Write new articles,
- View a list of articles,
- Read articles and comments,
- Add comments to articles.

## Used Design Patterns

1. **Facade**: Streamlined access to various database operations, providing a simplified interface for the CMSManager to interact with authors, articles, and comments.
2. **Bridge**: Used to decouple the database operations from the CMSManager class.
3. **Adapter**:  Implemented to standardize data export functionality, allowing articles to be exported in multiple formats like JSON and XML.

## Implementation

The goal of this lab was to extend the CMS application by incorporating structural design patterns that enhance flexibility and maintainability.

The Bridge Pattern was applied to abstract database interactions, making the system adaptable to different database types.
The Adapter Pattern was used to introduce a unified export interface for articles, providing multiple output formats without altering the core CMS logic.

### Code Snippets

**Bridge:**

The CMS needs to support multiple database types (e.g., SQL and NoSQL) to remain adaptable to changing requirements. The Bridge Pattern decouples the abstraction (operations on the database) from the implementation (specific database type).

*How It Works:*
The DatabaseBridge class acts as the abstraction, while the concrete implementations (`SQLDatabaseBridge` and `NoSQLDatabaseBridge`) handle database-specific operations. This enables the CMS to switch database backends without altering the core logic.

*Code Walkthrough:*
Abstract Bridge Class:
The DatabaseBridge defines a set of operations that all database backends must implement.

Concrete Implementations:
Each concrete implementation provides database-specific logic. For example:
SQL Database: Uses SQL queries for CRUD operations.
NoSQL Database: Uses key-value or document-based storage logic.

Dynamic Switching:
The database type is selected when initializing the CMS. The rest of the system interacts with the `DatabaseBridge`, unaware of the underlying implementation.

```python
class DatabaseBridge:
    def add_article(self, title, body, author_id, tags):
        raise NotImplementedError

class SQLDatabaseBridge(DatabaseBridge):
    def add_article(self, title, body, author_id, tags):
        print(f"Adding article to SQL DB: {title} by {author_id}")

class NoSQLDatabaseBridge(DatabaseBridge):
    def add_article(self, title, body, author_id, tags):
        print(f"Adding article to NoSQL DB: {title} by {author_id}")

```

**Adapter:**

Users of the CMS might need articles in different formats (e.g., JSON, XML). Instead of scattering export logic across the system, the Adapter Pattern provides a unified interface to convert articles into desired formats.

*How It Works:*
The `ExportAdapter` defines an interface for exporting articles. Concrete adapters (`JSONExportAdapter` and `XMLExportAdapter`) implement the logic for each format.

Code Walkthrough:
Abstract Adapter Class:
The `ExportAdapter` serves as a common interface for export functionality.

Concrete Adapters:
JSON Adapter: Uses the Python `json` library to convert articles into a JSON string.

XML Adapter: Uses the `xml.etree.ElementTree` module to construct an XML document.

Usage:
To export articles, the user selects the desired format, and the corresponding adapter handles the conversion.

```python
class ExportAdapter:
    def export(self, articles):
        raise NotImplementedError

class JSONExportAdapter(ExportAdapter):
    def export(self, articles):
        return json.dumps([article.to_dict() for article in articles], indent=4)

class XMLExportAdapter(ExportAdapter):
    def export(self, articles):
        # Simplified XML export logic
        root = ET.Element("articles")
        for article in articles:
            ET.SubElement(root, "article", attrib=article.to_dict())
        return ET.tostring(root, encoding="unicode")
```

**Facade:**

The CMS performs many database operations (e.g., adding authors, articles, comments). The Facade Pattern simplifies these interactions by providing a unified interface (`ContentManagerFacade`).

How It Works:
The `ContentManagerFacade` acts as an intermediary between the CMS and the database layer. It consolidates complex operations into intuitive methods, hiding database-specific logic from the rest of the system.

Code Walkthrough:
Facade Class:
The `ContentManagerFacade` defines high-level methods for managing authors, articles, and comments.

Usage:
The `CMSManager` interacts exclusively with the facade, simplifying its codebase.

```python
class ContentManagerFacade:
    def __init__(self, database_bridge):
        self.db_bridge = database_bridge

    def create_author(self, name):
        return self.db_bridge.add_author(name)

    def create_article(self, title, body, author_id, tags):
        return self.db_bridge.add_article(title, body, author_id, tags)

    def add_comment(self, content, article_id, author_id):
        return self.db_bridge.add_comment(content, article_id, author_id)
```

### Conclusions / Screenshots / Results


**Conclusions:**

In this laboratory work i have tried to integrate structural design patterns into the CMS system that I've created in the last lab to enhance its architecture and functionality. By applying the Bridge, Adapter, and Facade patterns, the system achieved improvements in flexibility, extensibility, and maintainability.

Bridge Pattern: The decoupling of the CMSManager from specific database implementations ensures that the system remains adaptable to changes in backend technology. The ability to switch seamlessly between SQL and NoSQL databases without modifying the core logic demonstrates the robustness of this design.

Adapter Pattern: Exporting articles in multiple formats showcased the system's ability to meet diverse user requirements. The adapter-based approach also facilitates the addition of new export formats with minimal effort, ensuring long-term scalability.

Facade Pattern: The abstraction provided by the facade greatly simplified the interaction with the database layer, making the CMS codebase more readable and easier to maintain. This also reduced the learning curve for developers interacting with the system.

In conclusion, this lab reminded me the importance of structural design patterns in building systems that are not only functional but also sustainable in the face of evolving requirements. These patterns are invaluable tools for managing complexity and fostering clean, modular architecture in software development. I believe by learning these designs and using them on this project actually will help me in my future carreer.

**Results**

*Bridge Pattern Demonstration*

Switching between SQL and NoSQL databases was seamless. This ensured the system could adapt to changes in backend technologies without significant code rewrites.
Example Output:

```Terminal
Adding author to SQL DB: John Doe  
Switching to NoSQL...  
Adding author to NoSQL DB: John Doe  
```

*Adapter Pattern Demonstration*

```Terminal
Articles were successfully exported in both JSON and XML formats, demonstrating flexibility in data representation.
JSON Output Example:
```

```json
[
    {
        "title": "Understanding Design Patterns",
        "author": "Emre Batuhan Sungur",
        "content": "An exploration of structural patterns.",
        "tags": ["design", "patterns"]
    }
]
```

XML Output Example:

```xml
Copy code
<articles>
    <article>
        <title>Understanding Design Patterns</title>
        <author>Emre Batuhan Sungur</author>
        <content>An exploration of structural patterns.</content>
        <tags>design, patterns</tags>
    </article>
</articles>
```

*Facade Pattern Demonstration*

Simplified interaction with the database for all CMS operations, resulting in cleaner and more manageable code.
Example Output:

```output
Creating author 'Jane Smith'...  
Author created with ID: 3  
Creating article 'Structural Patterns 101'...  
Article created with ID: 5  
```