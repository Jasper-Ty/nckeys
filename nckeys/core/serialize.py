from typing import runtime_checkable, TypeVar, Protocol, BinaryIO
from abc import abstractmethod


@runtime_checkable
class Serializable(Protocol):
    """
    A protocol for objects that can be serialized to bytes and deserialized back.

    Any class implementing this protocol should provide:
    - A `serialize()` method that returns a string representation.
    - A `deserialize()` class method that takes a string and returns an instance.
    """

    @abstractmethod
    def serialize(self) -> bytes:
        raise NotImplementedError
    

    @classmethod
    @abstractmethod
    def deserialize(cls, obj: bytes) -> "Serializable":
        raise NotImplementedError


def write_serializable(obj: Serializable, stream: BinaryIO) -> None:
    stream.write(obj.serialize())