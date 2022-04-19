# This is an automatically generated file.
# DO NOT EDIT or your changes may be overwritten
import base64
from enum import IntEnum
from xdrlib import Packer, Unpacker

__all__ = ["BucketEntryType"]


class BucketEntryType(IntEnum):
    """
    XDR Source Code::

        enum BucketEntryType
        {
            METAENTRY =
                -1, // At-and-after protocol 11: bucket metadata, should come first.
            LIVEENTRY = 0, // Before protocol 11: created-or-updated;
                           // At-and-after protocol 11: only updated.
            DEADENTRY = 1,
            INITENTRY = 2 // At-and-after protocol 11: only created.
        };
    """

    METAENTRY = -1
    LIVEENTRY = 0
    DEADENTRY = 1
    INITENTRY = 2

    def pack(self, packer: Packer) -> None:
        packer.pack_int(self.value)

    @classmethod
    def unpack(cls, unpacker: Unpacker) -> "BucketEntryType":
        value = unpacker.unpack_int()
        return cls(value)

    def to_xdr_bytes(self) -> bytes:
        packer = Packer()
        self.pack(packer)
        return packer.get_buffer()

    @classmethod
    def from_xdr_bytes(cls, xdr: bytes) -> "BucketEntryType":
        unpacker = Unpacker(xdr)
        return cls.unpack(unpacker)

    def to_xdr(self) -> str:
        xdr_bytes = self.to_xdr_bytes()
        return base64.b64encode(xdr_bytes).decode()

    @classmethod
    def from_xdr(cls, xdr: str) -> "BucketEntryType":
        xdr_bytes = base64.b64decode(xdr.encode())
        return cls.from_xdr_bytes(xdr_bytes)
