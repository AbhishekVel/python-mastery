

from typing import Sequence


def print_table(objects: Sequence[object], attributes: list[str]):
    print(' '.join('%10s' % attr for attr in attributes))
    print(('-'*10 + ' ')*len(attributes))
    for record in objects:
        print(' '.join('%10s' % getattr(record, attr) for attr in attributes))
