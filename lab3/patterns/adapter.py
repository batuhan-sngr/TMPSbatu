import json

from xml.etree.ElementTree import Element, SubElement, tostring

class Exporter:
    def export(self, articles):
        raise NotImplementedError


class JSONExporter(Exporter):
    def export(self, articles):
        return json.dumps([article.__dict__ for article in articles], indent=4)

class XMLExporter(Exporter):
    def export(self, articles):
        root = Element("articles")
        for article in articles:
            article_elem = SubElement(root, "article")
            title = SubElement(article_elem, "title")
            title.text = article.title
            body = SubElement(article_elem, "body")
            body.text = article.body
            author = SubElement(article_elem, "author")
            author.text = article.author.name
        return tostring(root, encoding="unicode")
