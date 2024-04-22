from abc import ABC, abstractmethod
from typing import Sequence

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        raise NotImplementedError()

    @abstractmethod
    def row(self, rowdata):
        raise NotImplementedError()
    


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))
    
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(str(item) for item in headers))

    def row (self, rowdata):
        print(','.join(str(item) for item in rowdata))

def print_table(objects: Sequence[object], attributes: list[str], formatter: TableFormatter):
    formatter.headings(attributes)
    for o in objects:
        rowdata = [getattr(o, attr) for attr in attributes]
        formatter.row(rowdata)
        

def create_formatter(fmt: str) -> TableFormatter:
    if fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'text':
        return TextTableFormatter()
    else:
        raise ValueError("Unsupported fmt")