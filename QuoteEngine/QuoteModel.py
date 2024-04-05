"""Quote model contains details about a qoute."""


class QuoteModel:
    """Store details about the quote."""

    def __init__(self, body, author):
        """Construct the object."""
        self.body = body
        self.author = author

    def __str__(self):
        """Print details."""
        return f'{self.body} - {self.author}'