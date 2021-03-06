# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: execution/execution.proto

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
  name='execution/execution.proto',
  package='chaosplatform.execution',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x65xecution/execution.proto\x12\x17\x63haosplatform.execution\x1a\x1fgoogle/protobuf/timestamp.proto\"\xb5\x01\n\tExecution\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rexperiment_id\x18\x02 \x01(\t\x12\x0f\n\x07user_id\x18\x03 \x01(\t\x12\x0e\n\x06org_id\x18\x04 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x05 \x01(\t\x12\x0e\n\x06status\x18\x06 \x01(\t\x12-\n\ttimestamp\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07payload\x18\x08 \x01(\t\".\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"A\n\x08GetReply\x12\x35\n\texecution\x18\x01 \x01(\x0b\x32\".chaosplatform.execution.Execution\"3\n\x0eGetManyRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"F\n\x0cGetManyReply\x12\x36\n\nexecutions\x18\x01 \x03(\x0b\x32\".chaosplatform.execution.Execution\"9\n\x10GetByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"H\n\x0eGetByUserReply\x12\x36\n\nexecutions\x18\x01 \x03(\x0b\x32\".chaosplatform.execution.Execution\"7\n\x0fGetByOrgRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"G\n\rGetByOrgReply\x12\x36\n\nexecutions\x18\x01 \x03(\x0b\x32\".chaosplatform.execution.Execution\"C\n\x15GetByWorkspaceRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"M\n\x13GetByWorkspaceReply\x12\x36\n\nexecutions\x18\x01 \x03(\x0b\x32\".chaosplatform.execution.Execution2\xeb\x03\n\x10\x45xecutionService\x12M\n\x03Get\x12#.chaosplatform.execution.GetRequest\x1a!.chaosplatform.execution.GetReply\x12Y\n\x07GetMany\x12\'.chaosplatform.execution.GetManyRequest\x1a%.chaosplatform.execution.GetManyReply\x12_\n\tGetByUser\x12).chaosplatform.execution.GetByUserRequest\x1a\'.chaosplatform.execution.GetByUserReply\x12\\\n\x08GetByOrg\x12(.chaosplatform.execution.GetByOrgRequest\x1a&.chaosplatform.execution.GetByOrgReply\x12n\n\x0eGetByWorkspace\x12..chaosplatform.execution.GetByWorkspaceRequest\x1a,.chaosplatform.execution.GetByWorkspaceReplyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_EXECUTION = _descriptor.Descriptor(
  name='Execution',
  full_name='chaosplatform.execution.Execution',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.execution.Execution.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='chaosplatform.execution.Execution.experiment_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaosplatform.execution.Execution.user_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org_id', full_name='chaosplatform.execution.Execution.org_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='chaosplatform.execution.Execution.workspace_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='chaosplatform.execution.Execution.status', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='chaosplatform.execution.Execution.timestamp', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payload', full_name='chaosplatform.execution.Execution.payload', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=88,
  serialized_end=269,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='chaosplatform.execution.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.execution.GetRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.execution.GetRequest.with_payload', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=271,
  serialized_end=317,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='chaosplatform.execution.GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='execution', full_name='chaosplatform.execution.GetReply.execution', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=319,
  serialized_end=384,
)


_GETMANYREQUEST = _descriptor.Descriptor(
  name='GetManyRequest',
  full_name='chaosplatform.execution.GetManyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='chaosplatform.execution.GetManyRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.execution.GetManyRequest.with_payload', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=386,
  serialized_end=437,
)


_GETMANYREPLY = _descriptor.Descriptor(
  name='GetManyReply',
  full_name='chaosplatform.execution.GetManyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executions', full_name='chaosplatform.execution.GetManyReply.executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=439,
  serialized_end=509,
)


_GETBYUSERREQUEST = _descriptor.Descriptor(
  name='GetByUserRequest',
  full_name='chaosplatform.execution.GetByUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaosplatform.execution.GetByUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.execution.GetByUserRequest.with_payload', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=511,
  serialized_end=568,
)


_GETBYUSERREPLY = _descriptor.Descriptor(
  name='GetByUserReply',
  full_name='chaosplatform.execution.GetByUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executions', full_name='chaosplatform.execution.GetByUserReply.executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=570,
  serialized_end=642,
)


_GETBYORGREQUEST = _descriptor.Descriptor(
  name='GetByOrgRequest',
  full_name='chaosplatform.execution.GetByOrgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='chaosplatform.execution.GetByOrgRequest.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.execution.GetByOrgRequest.with_payload', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=644,
  serialized_end=699,
)


_GETBYORGREPLY = _descriptor.Descriptor(
  name='GetByOrgReply',
  full_name='chaosplatform.execution.GetByOrgReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executions', full_name='chaosplatform.execution.GetByOrgReply.executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=701,
  serialized_end=772,
)


_GETBYWORKSPACEREQUEST = _descriptor.Descriptor(
  name='GetByWorkspaceRequest',
  full_name='chaosplatform.execution.GetByWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='chaosplatform.execution.GetByWorkspaceRequest.workspace_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.execution.GetByWorkspaceRequest.with_payload', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=774,
  serialized_end=841,
)


_GETBYWORKSPACEREPLY = _descriptor.Descriptor(
  name='GetByWorkspaceReply',
  full_name='chaosplatform.execution.GetByWorkspaceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executions', full_name='chaosplatform.execution.GetByWorkspaceReply.executions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=843,
  serialized_end=920,
)

_EXECUTION.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETREPLY.fields_by_name['execution'].message_type = _EXECUTION
_GETMANYREPLY.fields_by_name['executions'].message_type = _EXECUTION
_GETBYUSERREPLY.fields_by_name['executions'].message_type = _EXECUTION
_GETBYORGREPLY.fields_by_name['executions'].message_type = _EXECUTION
_GETBYWORKSPACEREPLY.fields_by_name['executions'].message_type = _EXECUTION
DESCRIPTOR.message_types_by_name['Execution'] = _EXECUTION
DESCRIPTOR.message_types_by_name['GetRequest'] = _GETREQUEST
DESCRIPTOR.message_types_by_name['GetReply'] = _GETREPLY
DESCRIPTOR.message_types_by_name['GetManyRequest'] = _GETMANYREQUEST
DESCRIPTOR.message_types_by_name['GetManyReply'] = _GETMANYREPLY
DESCRIPTOR.message_types_by_name['GetByUserRequest'] = _GETBYUSERREQUEST
DESCRIPTOR.message_types_by_name['GetByUserReply'] = _GETBYUSERREPLY
DESCRIPTOR.message_types_by_name['GetByOrgRequest'] = _GETBYORGREQUEST
DESCRIPTOR.message_types_by_name['GetByOrgReply'] = _GETBYORGREPLY
DESCRIPTOR.message_types_by_name['GetByWorkspaceRequest'] = _GETBYWORKSPACEREQUEST
DESCRIPTOR.message_types_by_name['GetByWorkspaceReply'] = _GETBYWORKSPACEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Execution = _reflection.GeneratedProtocolMessageType('Execution', (_message.Message,), dict(
  DESCRIPTOR = _EXECUTION,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.Execution)
  ))
_sym_db.RegisterMessage(Execution)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), dict(
  DESCRIPTOR = _GETREPLY,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetReply)
  ))
_sym_db.RegisterMessage(GetReply)

GetManyRequest = _reflection.GeneratedProtocolMessageType('GetManyRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMANYREQUEST,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetManyRequest)
  ))
_sym_db.RegisterMessage(GetManyRequest)

GetManyReply = _reflection.GeneratedProtocolMessageType('GetManyReply', (_message.Message,), dict(
  DESCRIPTOR = _GETMANYREPLY,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetManyReply)
  ))
_sym_db.RegisterMessage(GetManyReply)

GetByUserRequest = _reflection.GeneratedProtocolMessageType('GetByUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREQUEST,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByUserRequest)
  ))
_sym_db.RegisterMessage(GetByUserRequest)

GetByUserReply = _reflection.GeneratedProtocolMessageType('GetByUserReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREPLY,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByUserReply)
  ))
_sym_db.RegisterMessage(GetByUserReply)

GetByOrgRequest = _reflection.GeneratedProtocolMessageType('GetByOrgRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYORGREQUEST,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByOrgRequest)
  ))
_sym_db.RegisterMessage(GetByOrgRequest)

GetByOrgReply = _reflection.GeneratedProtocolMessageType('GetByOrgReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYORGREPLY,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByOrgReply)
  ))
_sym_db.RegisterMessage(GetByOrgReply)

GetByWorkspaceRequest = _reflection.GeneratedProtocolMessageType('GetByWorkspaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYWORKSPACEREQUEST,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByWorkspaceRequest)
  ))
_sym_db.RegisterMessage(GetByWorkspaceRequest)

GetByWorkspaceReply = _reflection.GeneratedProtocolMessageType('GetByWorkspaceReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYWORKSPACEREPLY,
  __module__ = 'execution.execution_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.execution.GetByWorkspaceReply)
  ))
_sym_db.RegisterMessage(GetByWorkspaceReply)



_EXECUTIONSERVICE = _descriptor.ServiceDescriptor(
  name='ExecutionService',
  full_name='chaosplatform.execution.ExecutionService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=923,
  serialized_end=1414,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='chaosplatform.execution.ExecutionService.Get',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMany',
    full_name='chaosplatform.execution.ExecutionService.GetMany',
    index=1,
    containing_service=None,
    input_type=_GETMANYREQUEST,
    output_type=_GETMANYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByUser',
    full_name='chaosplatform.execution.ExecutionService.GetByUser',
    index=2,
    containing_service=None,
    input_type=_GETBYUSERREQUEST,
    output_type=_GETBYUSERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByOrg',
    full_name='chaosplatform.execution.ExecutionService.GetByOrg',
    index=3,
    containing_service=None,
    input_type=_GETBYORGREQUEST,
    output_type=_GETBYORGREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByWorkspace',
    full_name='chaosplatform.execution.ExecutionService.GetByWorkspace',
    index=4,
    containing_service=None,
    input_type=_GETBYWORKSPACEREQUEST,
    output_type=_GETBYWORKSPACEREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EXECUTIONSERVICE)

DESCRIPTOR.services_by_name['ExecutionService'] = _EXECUTIONSERVICE

# @@protoc_insertion_point(module_scope)
