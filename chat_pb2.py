# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nchat.proto\x12\x04\x63hat\")\n\x07Message\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x07\n\x05Vazio2f\n\x04\x43hat\x12+\n\x0bSendMessage\x12\r.chat.Message\x1a\x0b.chat.Vazio\"\x00\x12\x31\n\x0fReceiveMessages\x12\x0b.chat.Vazio\x1a\r.chat.Message\"\x00\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chat_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGE._serialized_start=20
  _MESSAGE._serialized_end=61
  _VAZIO._serialized_start=63
  _VAZIO._serialized_end=70
  _CHAT._serialized_start=72
  _CHAT._serialized_end=174
# @@protoc_insertion_point(module_scope)
