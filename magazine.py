class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
        Magazine.all_magazines.append(self)

    def article_titles(self):
        return [article.title for article in self.articles]

    def contributing_authors(self):
        authors_count = {}
        for article in self.articles:
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]