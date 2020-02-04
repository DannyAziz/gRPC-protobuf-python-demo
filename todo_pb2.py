# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: todo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='todo.proto',
  package='gRPC_demo',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ntodo.proto\x12\tgRPC_demo\x1a\x1fgoogle/protobuf/timestamp.proto\"D\n\x04Todo\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1e\n\x0e\x41\x64\x64TodoRequest\x12\x0c\n\x04\x62ody\x18\x01 \x01(\t2F\n\x0bTodoService\x12\x37\n\x07\x41\x64\x64Todo\x12\x19.gRPC_demo.AddTodoRequest\x1a\x0f.gRPC_demo.Todo\"\x00\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_TODO = _descriptor.Descriptor(
  name='Todo',
  full_name='gRPC_demo.Todo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='gRPC_demo.Todo.body', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='gRPC_demo.Todo.created_at', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=58,
  serialized_end=126,
)


_ADDTODOREQUEST = _descriptor.Descriptor(
  name='AddTodoRequest',
  full_name='gRPC_demo.AddTodoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='gRPC_demo.AddTodoRequest.body', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=128,
  serialized_end=158,
)

_TODO.fields_by_name['created_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
DESCRIPTOR.message_types_by_name['Todo'] = _TODO
DESCRIPTOR.message_types_by_name['AddTodoRequest'] = _ADDTODOREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Todo = _reflection.GeneratedProtocolMessageType('Todo', (_message.Message,), {
  'DESCRIPTOR' : _TODO,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_demo.Todo)
  })
_sym_db.RegisterMessage(Todo)

AddTodoRequest = _reflection.GeneratedProtocolMessageType('AddTodoRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDTODOREQUEST,
  '__module__' : 'todo_pb2'
  # @@protoc_insertion_point(class_scope:gRPC_demo.AddTodoRequest)
  })
_sym_db.RegisterMessage(AddTodoRequest)



_TODOSERVICE = _descriptor.ServiceDescriptor(
  name='TodoService',
  full_name='gRPC_demo.TodoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=160,
  serialized_end=230,
  methods=[
  _descriptor.MethodDescriptor(
    name='AddTodo',
    full_name='gRPC_demo.TodoService.AddTodo',
    index=0,
    containing_service=None,
    input_type=_ADDTODOREQUEST,
    output_type=_TODO,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TODOSERVICE)

DESCRIPTOR.services_by_name['TodoService'] = _TODOSERVICE

# @@protoc_insertion_point(module_scope)
