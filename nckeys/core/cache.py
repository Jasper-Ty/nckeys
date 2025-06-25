import os
from inspect import signature, getdoc
from typing import ParamSpec, TypeVar, Callable
from collections import defaultdict
from functools import wraps

CACHE = dict()
DATA_DIR = "./data"
if not os.path.isdir(DATA_DIR):
    os.mkdir(DATA_DIR)

CONTEXT = []
DEPS = defaultdict(set)

P = ParamSpec('P')
T = TypeVar('T')

def cache(f: Callable[P, T]) -> Callable[P, T]:
    """
    My personal memoizing wrapper.
    """
    
    func_dir = os.path.join(DATA_DIR, f.__name__)
    if not os.path.isdir(func_dir):
        os.mkdir(func_dir)
        
    with open(os.path.join(func_dir, "description.txt"), "w") as file:
        if (doc := getdoc(f)):
            file.write(doc)

    sig = signature(f)

    @wraps(f)
    def cached(*args, **kwargs):
        ba = sig.bind(*args, **kwargs)
        ba_str = "_".join(
            f"{param}={str(arg)}" for param, arg in ba.arguments.items()
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