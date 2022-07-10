from IngestorInterface import IngestorInterface
from Quote import QuoteModel
from typing import List
from PDFIngestor import PDFIngestor
from TXTIngestor import TXTIngestor
from DOCXIngestor import DocxIngestor
from CSVIngestor import CSVIngestor

class Ingestor(IngestorInterface):
    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)