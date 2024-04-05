from abc import ABC, abstractmethod
from typing import List
from QuoteEngine.QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Abstract base class defining the structure for ingestor classes.

    This interface requires the definition of two class methods:
    - `can_ingest` to check if the file type is supported.
    - `parse` to extract quotes from files and produce a list of QuoteModel instances.
    """

    allowed_extensions: List[str] = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Determine if the given file can be ingested based on its extension.

        Args:
            path (str): The path to the file to be checked.

        Returns:
            bool: True if the file extension is in the list of allowed extensions, False otherwise.
        """
        ext = path.split('.')[-1].lower()
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the specified file and return a list of QuoteModel instances.

        This method must be implemented by subclasses to extract quotes from specific file formats.

        Args:
            path (str): The path to the file to be parsed.

        Returns:
            List[QuoteModel]: A list of QuoteModel instances extracted from the file.
        
        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        raise NotImplementedError("Subclasses must implement the parse method.")
