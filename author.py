class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.articles = []
        Author.all_authors.append(self)

    def write_article(self, title, magazine):
        article = Article(title, self, magazine)
        self.articles.append(article)
        magazine.articles.append(article)
        return article

    def magazines(self):
        return list(set(article.magazine for article in self.articles))


# Import here to avoid circular imports in this minimal setup
from article import Article