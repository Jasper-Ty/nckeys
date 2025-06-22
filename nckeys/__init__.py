"""
Package for playing around with noncommutative algebras
"""

from functools import wraps

CACHE = dict()

def cache(f):
    """
    Memoizing wrapper.
    """

    @wraps(f)
    def cached(*args, **kwargs):
        key = (f, args, frozenset(kwargs.items()))
        if key not in CACHE:
            CACHE[key] = f(*args, **kwargs)
        return CACHE[key]

    return cached


