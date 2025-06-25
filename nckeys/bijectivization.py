from itertools import chain

from .word import Word, Words
from .matrix import Matrix
from .core.cache import cache


class Bijectivization:
    """
    """

    def __init__(self, I, name=None, representative=max):
        """
        """
        self.E = []
        self.N = []
        self._name = name
        self._representative = representative

        for (lword, rword) in I:
            if rword is None:
                self.N.append(lword)
            else:
                self.E.append((lword, rword))

 
    def _neighbors(self, word: Word) -> set[Word]:
        """All the words reachable by one edge.
        """
        out = set()

        for lword, rword in self.E:
            out.update(word.rewrites(lword, rword))
            out.update(word.rewrites(rword, lword))

        return out

    
    def _component(self, word, visited=None):
        """Closure under taking neighbors.

        This is implemented as a variation of depth-first search.
        """
        if visited is None:
            visited = set()

        visited.add(word)
        for neighbor in self._neighbors(word):
            if neighbor not in visited:
                visited |= self._component(neighbor, visited)

        return visited

    
    def _components(self, W):
        visited = set()
        out = dict()

        for word in W:
            if word not in visited:
                component = self._component(word)
                visited |= component
                out[self._representative(component)] = component
        
        return out

    
    def _in_N(self, word):
        return any(True for _ in word.matches(*self.N))


    def _is_nonzero_component(self, component: set[Word]):
        return all(
            not self._in_N(word)
            for word in component
        )


    def _quotient(self, W):
        """
        Returns the matrix encoding the quotient map of the bijectivization `(B, M)`
        """
        components = {
            rep: component 
            for rep, component in self._components(W).items()
            if self._is_nonzero_component(component)
        }
        rows = W
        cols = list(components.keys())
        out = Matrix(rows, cols)
        for rep, component in components.items():
            for word in component:
                out[word, rep] = 1
        
        return out


    def quotient(self, deg, n):
        W = Words(deg, n)
        out = self._quotient(W)
        out._name = f"{self._name}"
        return out
