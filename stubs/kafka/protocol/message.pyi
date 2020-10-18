from kafka.codec import gzip_decode as gzip_decode, has_gzip as has_gzip, has_lz4 as has_lz4, has_snappy as has_snappy, lz4_decode as lz4_decode, lz4_decode_old_kafka as lz4_decode_old_kafka, snappy_decode as snappy_decode
from kafka.protocol.frame import KafkaBytes as KafkaBytes
from kafka.protocol.struct import Struct as Struct
from kafka.protocol.types import AbstractType as AbstractType, Bytes as Bytes, Int32 as Int32, Int64 as Int64, Int8 as Int8, Schema as Schema
from kafka.util import WeakMethod as WeakMethod, crc32 as crc32
from typing import Any, Optional

class Message(Struct):
    SCHEMAS: Any = ...
    SCHEMA: Any = ...
    CODEC_MASK: int = ...
    CODEC_GZIP: int = ...
    CODEC_SNAPPY: int = ...
    CODEC_LZ4: int = ...
    TIMESTAMP_TYPE_MASK: int = ...
    HEADER_SIZE: int = ...
    timestamp: Any = ...
    crc: Any = ...
    magic: Any = ...
    attributes: Any = ...
    key: Any = ...
    value: Any = ...
    encode: Any = ...
    def __init__(self, value: Any, key: Optional[Any] = ..., magic: int = ..., attributes: int = ..., crc: int = ..., timestamp: Optional[Any] = ...) -> None: ...
    @property
    def timestamp_type(self): ...
    @classmethod
    def decode(cls, data: Any): ...
    def validate_crc(self): ...
    def is_compressed(self): ...
    def decompress(self): ...
    def __hash__(self) -> Any: ...

class PartialMessage(bytes): ...

class MessageSet(AbstractType):
    ITEM: Any = ...
    HEADER_SIZE: int = ...
    @classmethod
    def encode(cls, items: Any, prepend_size: bool = ...): ...
    @classmethod
    def decode(cls, data: Any, bytes_to_read: Optional[Any] = ...): ...
    @classmethod
    def repr(cls, messages: Any): ...