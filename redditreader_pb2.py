# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: redditreader.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor.FileDescriptor(
  name='redditreader.proto',
  package='redditreader',
  syntax='proto3',
  serialized_options=b'\n\007ex.grpc\242\002\003HSW',
  serialized_pb=b'\n\x12redditreader.proto\x12\x0credditreader\"[\n\nRedditInfo\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x14\n\x0cnum_comments\x18\x04 \x01(\x05\x12\x0c\n\x04nsfw\x18\x05 \x01(\t\"\x0f\n\rRedditRequest2[\n\x0cRedditReader\x12K\n\x0egetRedditPosts\x12\x1b.redditreader.RedditRequest\x1a\x18.redditreader.RedditInfo\"\x00\x30\x01\x42\x0f\n\x07\x65x.grpc\xa2\x02\x03HSWb\x06proto3'
)

_REDDITINFO = _descriptor.Descriptor(
  name='RedditInfo',
  full_name='redditreader.RedditInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='redditreader.RedditInfo.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='redditreader.RedditInfo.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='redditreader.RedditInfo.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_comments', full_name='redditreader.RedditInfo.num_comments', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='nsfw', full_name='redditreader.RedditInfo.nsfw', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=36,
  serialized_end=127,
)


_REDDITREQUEST = _descriptor.Descriptor(
  name='RedditRequest',
  full_name='redditreader.RedditRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=129,
  serialized_end=144,
)

DESCRIPTOR.message_types_by_name['RedditInfo'] = _REDDITINFO
DESCRIPTOR.message_types_by_name['RedditRequest'] = _REDDITREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RedditInfo = _reflection.GeneratedProtocolMessageType('RedditInfo', (_message.Message,), {
  'DESCRIPTOR': _REDDITINFO,
  '__module__': 'redditreader_pb2'
  # @@protoc_insertion_point(class_scope:redditreader.RedditInfo)
})
_sym_db.RegisterMessage(RedditInfo)

RedditRequest = _reflection.GeneratedProtocolMessageType('RedditRequest', (_message.Message,), {
  'DESCRIPTOR': _REDDITREQUEST,
  '__module__': 'redditreader_pb2'
  # @@protoc_insertion_point(class_scope:redditreader.RedditRequest)
})
_sym_db.RegisterMessage(RedditRequest)

DESCRIPTOR._options = None

_REDDITREADER = _descriptor.ServiceDescriptor(
  name='RedditReader',
  full_name='redditreader.RedditReader',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=146,
  serialized_end=237,
  methods=[
    _descriptor.MethodDescriptor(
      name='getRedditPosts',
      full_name='redditreader.RedditReader.getRedditPosts',
      index=0,
      containing_service=None,
      input_type=_REDDITREQUEST,
      output_type=_REDDITINFO,
      serialized_options=None,
    ),
  ])
_sym_db.RegisterServiceDescriptor(_REDDITREADER)

DESCRIPTOR.services_by_name['RedditReader'] = _REDDITREADER

# @@protoc_insertion_point(module_scope)
