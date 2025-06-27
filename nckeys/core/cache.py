"""
Persistent function caching module

This module provides a lightweight decorator-based caching mechanism for functions,
persisting results to disk for reuse across Python sessions. It uses TOML for function 
metadata and Pickle for result serialization, creating a cache directory for each 
decorated function and its arguments.

Features:
- Automatically binds function arguments and creates a unique cache key.
- Stores metadata (e.g. docstring, signature, source code location) in `info.toml`.
- Caches return values in both a Pickle file (`serialized.pkl`) and human-readable text.
- Automatically reloads cached values at import time.

Usage:
    @cache
    def expensive_function(x, y):
        ...

On first call with a given argument combination, the function is executed and the result
is saved under `./data/{function_name}/cache/{args_str}/`. On subsequent calls with the
same arguments, the result is loaded from disk or memory.

Directory structure:
    ./data/
        └── function_name/
            ├── info.toml
            └── cache/
                └── param1=val1_param2=val2/
                    ├── serialized.pkl
                    └── human_readable.txt

Classes:
- CacheFunctionEntry: Handles metadata and filesystem layout per cached function.

Functions:
- cache(f): Decorator that memoizes function calls with persistent storage.

"""

import os
import inspect
import tomllib
import tomli_w

from sys import stderr
from typing import Any, ParamSpec, TypeVar, Callable, Tuple
from collections import defaultdict
from functools import wraps
from dataclasses import dataclass
import pickle

from .serialize import write_serializable, Serializable


P = ParamSpec('P')
T = TypeVar('T')

CACHE: dict[str, Any] = dict()
CACHE_DIR = "./data"
if not os.path.isdir(CACHE_DIR):
    os.mkdir(CACHE_DIR)


class _CacheFunctionEntry: 

    def __init__(self, f: Callable, name: str | None=None):
        self._f = f
        self._name = name

        if (doc := inspect.getdoc(f)) is None:
            self.doc = "This function does not have a documentation string."
        else:
            self.doc = doc

        self.sig = inspect.signature(f)
        self.source = inspect.getsource(f)
        self.location = f"{f.__module__.replace('.', '/')}.py:{inspect.getsourcelines(f)[1]}"

        if not os.path.isdir(self.directory):
            os.mkdir(self.directory)

        if not os.path.isdir(self.cache_dir):
            os.mkdir(self.cache_dir)

        with open(os.path.join(self.directory, "info.toml"), "wb") as file:
            tomli_w.dump(self.info, file, multiline_strings=True)

        with open(os.path.join(self.directory, "signature.pkl"), "wb") as file:
            pickle.dump(self.sig, file)


    @property
    def name(self) -> str:
        if self._name is None:
            return self._f.__name__
        else:
            return self._name

    
    @property
    def info(self) -> dict:
        return {
            "name": self.name,
            "signature": str(self.sig),
            "doc": self.doc,
            "location": self.location,
            "source": self.source,
        }


    @property
    def directory(self) -> str:
        return os.path.join(CACHE_DIR, self.name)

    
    @property
    def cache_dir(self) -> str:
        return os.path.join(self.directory, 'cache')


    def bind(self, *args, **kwargs) -> str:
        try:
            bound_args = self.sig.bind(*args, **kwargs)
        except TypeError as e:
            print(f"Unable to bind arguments", file=stderr)

        args_str = "_".join(
            f"{param}={str(arg)}" 
            for param, arg in bound_args.arguments.items()
        )
        return args_str
    

def cache(f: Callable[P, T]) -> Callable[P, T]:
    """
    Memoization decoratoor with persistent, disk-based caching.

    When applied, this decorator stores the output of the function based on its
    input arguments. On future calls with the same arguments, the cached result 
    is returned instead of recomputing. Cached data persists across sessions.

    How it works:
    - Creates a unique string key from the function's bound arguments.
    - Stores the result as a pickled object in `./data/{function_name}/cache/{args_str}/`.
    - Also writes a human-readable `.txt` version of the result.
    - Caches metadata about the function in a TOML file (`info.toml`).
    - Automatically loads existing cached results into memory at import time.

    Parameters:
        f (Callable): The function to be memoized. Can take any arguments.

    Returns:
        Callable: A wrapped version of `f` that returns cached results
                  when possible and stores new results otherwise.

    Example usage:
        @cache
        def compute(x, y=5):
            return x ** y

    Notes:
        - All function arguments must be serializable as strings for key creation.
        - Results are stored in memory and rehydrated from disk if available.
        - If argument binding fails, caching is skipped for that call.

    """
    
    entry = _CacheFunctionEntry(f)

    @wraps(f)
    def cached(*args, **kwargs):
        args_str = entry.bind(*args, **kwargs)
        key = f"{entry.name}:{args_str}"

        result_dir = os.path.join(entry.cache_dir, args_str)
        if not os.path.isdir(result_dir):
            os.mkdir(result_dir)

        if key not in CACHE:
            val = f(*args, **kwargs)

            with open(os.path.join(result_dir, "serialized"), "wb") as file:
                if isinstance(val, Serializable):
                    write_serializable(val, file)
                else:
                    try:
                        pickle.dump(val, file)
                    except:
                        pass
                    
            try:
                with open(os.path.join(result_dir, "human_readable.txt"), "w") as file:
                    file.write(str(val))
            except:
                pass

            CACHE[key] = val
        
        return CACHE[key]

    return cached


for name in os.listdir(CACHE_DIR):
    func_dir = os.path.join(CACHE_DIR, name)
    with open(os.path.join(func_dir, "signature.pkl"), "rb") as f:
        sig: inspect.Signature = pickle.load(f)
    return_type = sig.return_annotation

    cache_dir = os.path.join(func_dir, "cache")
    for args_str in os.listdir(cache_dir):
        key = f"{name}:{args_str}"
        filepath = os.path.join(cache_dir, args_str, "serialized")
        if os.path.exists(filepath):
            try:
                with open(filepath, "rb") as f:
                    if isinstance(return_type, Serializable):
                        CACHE[key] = return_type.deserialize(f.read())
                    else:
                        CACHE[key] = pickle.load(f)
            except:
                pass
                    