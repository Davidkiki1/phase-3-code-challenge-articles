class Article:
    all_articles = []

    def __init__(self, title, author, magazine):
        self.title = title
        self.author = author
        self.magazine = magazine
        Article.all_articles.append(self)