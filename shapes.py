from itertools import chain

def catalan(n: int):
    """
    """
    pass

def stairs(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-2) , ... , (n-1,0)
    """
    return chain.from_iterable(((i,j) for j in range(n-i)) for i in range(n))

def rectangle(n: int):
    """
    (0,0) , ... , (0, n-1) , (1,0) , ... , (1,n-1) , ... , (n-1,n-1)
    """
    return chain.from_iterable(((i,j) for j in range(n)) for i in range(n))
