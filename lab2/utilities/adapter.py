class LegacyArticleAdapter:
    def __init__(self, legacy_article):
        self.legacy_article = legacy_article

    def get_title(self):
        # Adapts the legacy way of fetching the title
        return self.legacy_article['headline']

    def get_body(self):
        # Adapts the legacy way of fetching the content
        return self.legacy_article['text']

    def get_author(self):
        return self.legacy_article['writer']

    def get_tags(self):
        return self.legacy_article.get('categories', [])
