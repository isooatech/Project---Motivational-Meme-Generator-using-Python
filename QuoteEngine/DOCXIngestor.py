from IngestorInterface import IngestorInterface
from Quote import QuoteModel
import docx
from typing import List

class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        Quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parsed = para.text.split('-')
                new_quote = QuoteModel(parsed[0].strip('"'), parsed[1].strip('"'))
                Quotes.append(new_quote)

        return Quotes

