from abc import ABC, abstractmethod
from typing import Optional, Sequence, Type

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
        
class ColumnFormatMixin:
    formats: list[str] = []
    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt,d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def print_table(objects: Sequence[object], attributes: list[str], formatter: TableFormatter):
    formatter.headings(attributes)
    for o in objects:
        rowdata = [getattr(o, attr) for attr in attributes]
        formatter.row(rowdata)
        

def create_formatter(fmt: str, column_formats=['%s', '%d', '%0.2f']):
    
    formatter: Optional[Type[CSVTableFormatter | TextTableFormatter]] = None
    if fmt == 'csv':
        formatter =  CSVTableFormatter
    elif fmt == 'text':
        formatter = TextTableFormatter
    
    if formatter is None:
        raise ValueError("Unsupported fmt")
        
    class formatter_cls(ColumnFormatMixin):
        formats = column_formats

    return formatter_cls()