from IngestorInterface import IngestorInterface
from Quote import QuoteModel
import pandas as pd
from typing import List

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        Quotes = []
        csv = pd.read_csv(path, header = 0)

        for index, row in csv.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            Quotes.append(new_quote)

        return Quotes

