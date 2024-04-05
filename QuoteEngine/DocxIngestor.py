from typing import List
import docx
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface

class DocxIngestor(IngestorInterface):
    """Docx Ingestor class for parsing DOCX files into a list of QuoteModel instances."""

    allowed_extensions = ['docx']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if the given file can be ingested based on its extension."""
        extension = path.split('.')[-1].lower()
        return extension in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the DOCX file and return a list of QuoteModel instances."""
        if not cls.can_ingest(path):
            raise Exception(f'The file format {path.split(".")[-1]} is not supported by CustomDocxIngestor.')
        
        quote_list = []
        try:
            doc = docx.Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    # Splitting the paragraph text by ' - ' to separate the body and the author
                    parts = paragraph.text.split(' - ')
                    if len(parts) >= 2:
                        quote_body = parts[0].strip()
                        quote_author = parts[1].strip()
                        quote_list.append(QuoteModel(quote_body, quote_author))
        except FileNotFoundError:
            print(f"The file {path} was not found.")
        except Exception as e:
            print(f"An error occurred while processing the file {path}: {e}")
        
        return quote_list
