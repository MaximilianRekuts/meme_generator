from typing import List
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface

class TextIngestor(IngestorInterface):
    """Ingestor for parsing text files into a list of QuoteModel instances."""
    
    allowed_extensions = ['txt']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file extension is supported by the Ingestor."""
        extension = path.split('.')[-1].lower()
        return extension in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a text file and return a list of QuoteModel instances."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension from {path}')

        quotes = []
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parts = line.split(' - ')
                    if len(parts) == 2:
                        quote_body, quote_author = parts[0].strip(), parts[1].strip()
                        quotes.append(QuoteModel(quote_body, quote_author))
        return quotes
