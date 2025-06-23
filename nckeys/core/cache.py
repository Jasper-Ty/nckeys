from typing import Tuple
from dataclass import dataclass

CACHE = dict()
DATA_DIR = "./data"
CONTEXT = []

# Keeps track of which cached functions call which cached functions
DEPS = defaultdict(set)

@dataclass(frozen=True)
class NamedComputation:
    function_name: str
    bound_arguments: tuple(Tuple[str, Any])

    def __init__(self, f, args, kwargs):
        self.fun
    
    @property
    def func_dir(self):
        out = os.path.join(DATA_DIR, f.__name__)
        if not os.path.isdir(out):
            os.mkdir(out)
        return out



def cache(f):
    """
    My personal memoizing wrapper.

    TODO: trace, pickling
    """
    
    func_dir = os.path.join(DATA_DIR, f.__name__)
    if not os.path.isdir(func_dir):
        os.mkdir(func_dir)

    sig = signature(f)

    @wraps(f)
    def cached(*args, **kwargs):
        ba = list(sig.bind(*args, **kwargs).arguments.items())
        ba_str = "_".join(
            f"{param}={str(arg)}" for param, arg in ba
        )
        key = (f.__name__, ba_str)
        key_str = f"{key[0]}_{key[1]}.txt"
        key_dir = os.path.join(func_dir, ba_str)
        if not os.path.isdir(key_dir):
            os.mkdir(key_dir)

        if CONTEXT:
            caller = CONTEXT[-1]
            caller_str = f"{caller[0]}_{caller[1]}.txt"
            DEPS[caller].add(key_str)
            caller_dir = os.path.join(DATA_DIR, *caller)
            with open(os.path.join(caller_dir, "dependencies.txt"), "w") as file:
                file.write("\n".join(DEPS[caller]))

        CONTEXT.append(key)

        if key not in CACHE:
            val = f(*args, **kwargs)

            with open(os.path.join(key_dir, key_str), "w") as file:
                file.write(str(val))

            CACHE[key] = val

        CONTEXT.pop()
        
        return CACHE[key]

    return cached
