class Observer:
    def update(self, event_type, data):
        raise NotImplementedError

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event_type, data):
        for observer in self.observers:
            observer.update(event_type, data)

class EmailNotifier(Observer):
    def update(self, event_type, data):
        if event_type == "new_article":
            print(f"EmailNotifier: New article published - {data['title']} by {data['author']}")
        elif event_type == "new_comment":
            print(f"EmailNotifier: New comment added to {data['article_title']} by {data['author']}")

class Logger(Observer):
    def update(self, event_type, data):
        if event_type == "new_article":
            print(f"Logger: Article '{data['title']}' by {data['author']} was added.")
        elif event_type == "new_comment":
            print(f"Logger: Comment on '{data['article_title']}' by {data['author']} was added.")

