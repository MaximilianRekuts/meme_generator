from typing import List
import subprocess
import os
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface

class PDFIngestor(IngestorInterface):
    """PDF Ingestor for parsing PDF files into a list of QuoteModel instances."""
    
    allowed_extensions = ['pdf']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the file extension is supported by the Ingestor."""
        extension = path.split('.')[-1].lower()
        return extension in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse a PDF file and return a list of QuoteModel instances."""
        if not cls.can_ingest(path):
            raise ValueError(f'Cannot ingest extension from {path}')

        tmp = f'temp.txt'
        try:
            # Convert PDF to text and store output in a temporary file
            subprocess.call(['pdftotext', path, tmp])

            with open(tmp, 'r', encoding='utf-8') as file:
                quotes = []
                for line in file:
                    parts = line.strip().split(' - ')
                    if len(parts) == 2:
                        quote_body, quote_author = parts
                        quotes.append(QuoteModel(quote_body.strip(), quote_author.strip()))
            return quotes
        except FileNotFoundError as e:
            raise FileNotFoundError('pdftotext command not found. Make sure it is installed and accessible in PATH.') from e
        finally:
            # Clean up by removing the temporary file
            if os.path.exists(tmp):
                os.remove(tmp)
