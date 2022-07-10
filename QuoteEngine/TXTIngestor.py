from typing import List
from IngestorInterface import IngestorInterface
from Quote import QuoteModel


class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        Quotes = []

        with open(path) as f:
            for line in f:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0].strip(), parse[1].strip())
                Quotes.append(new_quote)

        return Quotes

