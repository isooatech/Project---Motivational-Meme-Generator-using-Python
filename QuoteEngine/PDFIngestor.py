from typing import List
import subprocess
import os
import random
from IngestorInterface import IngestorInterface
from Quote import QuoteModel


class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        tmp = f'./tmp/{random.randint(0, 100000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        file_ref = open(tmp, "r")
        Quotes = []


        for line in file_ref.readlines():
            line = line.rstrip()
            if len(line) > 0:
                parse = line.split(' "')
                for p in parse:
                    helper = p.split('-')
                    new_quote = QuoteModel(helper[0].strip('"'), helper[1].strip())
                    Quotes.append(new_quote)

        file_ref.close()
        os.remove(tmp)
        return Quotes

#PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf')
#print(PDFIngestor.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))