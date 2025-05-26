class Author:
    all_authors = []

    def __init__(self, name):
        self.name = name
        self.articles = []
        Author.all_authors.append(self)

    def add_article(self, article):
        if article not in self.articles:
            self.articles.append(article)

    @property
    def magazines(self):
        # Return unique magazines author has written for
        return list(set(article.magazine for article in self.articles))

    def __repr__(self):
        return f"<Author: {self.name}>"


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
        Magazine.all_magazines.append(self)

    def add_article(self, article):
        if article not in self.articles:
            self.articles.append(article)

    @property
    def contributors(self):
        # Return unique authors who wrote for this magazine
        return list(set(article.author for article in self.articles))

    def __repr__(self):
        return f"<Magazine: {self.name}>"


class Article:
    all_articles = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        # Establish relationships
        author.add_article(self)
        magazine.add_article(self)

        Article.all_articles.append(self)

    def __repr__(self):
        return f"<Article: {self.title}>"