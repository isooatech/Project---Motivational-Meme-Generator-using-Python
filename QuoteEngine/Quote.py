class QuoteModel():
    def __init__(self, body: str, author: str):
        self.body = body.strip()
        self.author = author.strip()

    def __repr__(self):
        return f'<Quote: {self.body} by Author: {self.author}>'

