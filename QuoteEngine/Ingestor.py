from typing import List, Type
from QuoteEngine.IngestorInterface import IngestorInterface
from QuoteEngine.CSVIngestor import CSVIngestor
from QuoteEngine.TextIngestor import TextIngestor
from QuoteEngine.DocxIngestor import DocxIngestor
from QuoteEngine.PDFIngestor import PDFIngestor
from QuoteEngine.QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """Ingestor that delegates to specific ingestors based on file type."""

    # Register all specific ingestor types
    _ingestors: List[Type[IngestorInterface]] = [CSVIngestor, TextIngestor, DocxIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the file at the given path and return a list of QuoteModel instances.

        This method delegates to the appropriate specific ingestor based on the file extension.
        
        Args:
            path (str): Path to the file to be ingested.
        
        Returns:
            List[QuoteModel]: A list of extracted quotes.
        
        Raises:
            ValueError: If no suitable ingestor is found for the file type.
        """
        for ingestor in cls._ingestors:
            if ingestor.can_ingest(path):
                try:
                    return ingestor.parse(path)
                except Exception as e:
                    raise Exception(f"Failed to parse file {path} with ingestor {ingestor.__name__}: {e}")
        
        # If no ingestor can handle the file type, raise an informative error.
        file_extension = path.split('.')[-1]
        supported_extensions = [ext for ingestor in cls._ingestors for ext in ingestor.allowed_extensions]
        raise ValueError(f"No ingestor found for file type '.{file_extension}'. Supported extensions are: {', '.join(supported_extensions)}")
