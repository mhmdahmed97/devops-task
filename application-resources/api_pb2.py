# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tapi.proto\x12\x03\x61pi\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x07Request\x12\n\n\x02op\x18\x01 \x01(\t\x12\r\n\x05image\x18\x02 \x01(\x0c\"R\n\x08Response\x12\n\n\x02Ip\x18\x01 \x01(\t\x12+\n\x07\x63reated\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05image\x18\x03 \x01(\x0c\x32:\n\nImageManip\x12,\n\x0bGetResponse\x12\x0c.api.Request\x1a\r.api.Response\"\x00\x42\x08Z\x06.;mainb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'api_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\006.;main'
  _globals['_REQUEST']._serialized_start=51
  _globals['_REQUEST']._serialized_end=87
  _globals['_RESPONSE']._serialized_start=89
  _globals['_RESPONSE']._serialized_end=171
  _globals['_IMAGEMANIP']._serialized_start=173
  _globals['_IMAGEMANIP']._serialized_end=231
# @@protoc_insertion_point(module_scope)