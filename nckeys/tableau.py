from collections.abc import Sequence, Iterator
from itertools import chain

from .word import Word


class Tableau:
    pass


def get_rows(seq):
    m = len(seq)
    ascents = [0, *filter(lambda i: seq[i] > seq[i-1], range(1,m)), m]
    return [seq[ascents[i]:ascents[i+1]] for i in range(len(ascents)-1)]


def row_insert(row, k):
    try:
        idx = next(i for i, x in enumerate(row) if x > k)
        bumped, row[idx] = row[idx], k
        return bumped
    except StopIteration:
        row.append(k)
        return None
        

def tableau(seq):
    """Computes the tableau of `seq`.
    """
    rows = []
    for to_insert in seq:
        k = to_insert
        for row in rows:
            k = row_insert(row, k)
            if k is None:
                break
        else:
            rows.append([k])
    return rows


def tableau_word(seq):
    return Word(*chain.from_iterable(reversed(tableau(seq))))
