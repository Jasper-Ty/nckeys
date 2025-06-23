from .word import Word
from .matrix import Matrix


def rewrites(word, lword, rword):
    """
    Returns a list of all possible applications of the rule `lword` -> `rword` 
    for the word `word`
    """
    out = set()
    if rword is not None:
        l = len(lword)
        windows = ((word[:i], word[i:i+l], word[i+l:]) for i in range(len(word)-l+1))
        for prefix, subword, suffix in windows:
            if subword == lword:
                out.add(Word(*prefix, *rword, *suffix))

    return out


def bij_neighbors(word, I):
    out = set()

    for lword, rword in I:
        out |= rewrites(word, lword, rword)
        out |= rewrites(word, rword, lword)

    return out


def bij_component(word, I, visited=None):
    if visited is None:
        visited = { word }

    for neighbor in bij_neighbors(word, I):
        if neighbor not in visited:
            visited.add(neighbor)
            visited |= bij_component(neighbor, I, visited)

    return visited


def bij_components(W, I, representative=max):
    visited = set()
    out = dict()

    for word in W:
        if word not in visited:
            component = bij_component(word, I)
            visited |= component
            out[representative(component)] = component
            
    
    return out


def bij_quotient(W, I):
    """
    Returns the matrix encoding the quotient map of this bijectivization
    """
    components = bij_components(W, I)
    rows = W
    cols = list(components.keys())
    out = Matrix(
        rows,
        cols
    )
    for rep, component in components.items():
        for word in component:
            out[word, rep] = 1
    
    return out