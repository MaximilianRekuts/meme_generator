from typing import List
import pandas as pd
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.IngestorInterface import IngestorInterface

class CSVIngestor(IngestorInterface):
    """CSV Ingestor class for parsing CSV files into a list of QuoteModel instances."""
    
    allowed_extensions = ['csv']

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Verify if the given file can be ingested based on its extension."""
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse the CSV file and return a list of QuoteModel instances."""
        if not cls.can_ingest(path):
            raise Exception(f'The file format {path.split(".")[-1]} is not supported by CSVIngestor.')

        quote_list = []
        try:
            quotes_df = pd.read_csv(path)
            for _, row in quotes_df.iterrows():
                new_quote = QuoteModel(row['body'], row['author'])
                quote_list.append(new_quote)
        except FileNotFoundError:
            print(f"The file {path} was not found.")
        except Exception as e:
            print(f"An error occurred while processing the file {path}: {e}")
        
        return quote_list
