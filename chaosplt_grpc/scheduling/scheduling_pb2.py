# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: scheduling/scheduling.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='scheduling/scheduling.proto',
  package='chaosplatform.scheduling',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1bscheduling/scheduling.proto\x12\x18\x63haosplatform.scheduling\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xea\x03\n\x08Schedule\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\t\x12\x0e\n\x06org_id\x18\x03 \x01(\t\x12\x14\n\x0cworkspace_id\x18\x04 \x01(\t\x12\x15\n\rexperiment_id\x18\x05 \x01(\t\x12\x10\n\x08token_id\x18\x06 \x01(\t\x12\x0e\n\x06job_id\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\x12\x10\n\x08interval\x18\t \x01(\x02\x12.\n\ncreated_on\x18\n \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x61\x63tive_from\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x30\n\x0c\x61\x63tive_until\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12(\n\x07results\x18\r \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x08settings\x18\x0e \x01(\x0b\x32\x17.google.protobuf.Struct\x12.\n\rconfiguration\x18\x0f \x01(\x0b\x32\x17.google.protobuf.Struct\x12(\n\x07secrets\x18\x10 \x01(\x0b\x32\x17.google.protobuf.Struct\".\n\nGetRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"@\n\x08GetReply\x12\x34\n\x08schedule\x18\x01 \x01(\x0b\x32\".chaosplatform.scheduling.Schedule\"3\n\x0eGetManyRequest\x12\x0b\n\x03ids\x18\x01 \x03(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"E\n\x0cGetManyReply\x12\x35\n\tschedules\x18\x01 \x03(\x0b\x32\".chaosplatform.scheduling.Schedule\"9\n\x10GetByUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"G\n\x0eGetByUserReply\x12\x35\n\tschedules\x18\x01 \x03(\x0b\x32\".chaosplatform.scheduling.Schedule\"7\n\x0fGetByOrgRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"F\n\rGetByOrgReply\x12\x35\n\tschedules\x18\x01 \x03(\x0b\x32\".chaosplatform.scheduling.Schedule\"C\n\x15GetByWorkspaceRequest\x12\x14\n\x0cworkspace_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"L\n\x13GetByWorkspaceReply\x12\x35\n\tschedules\x18\x01 \x03(\x0b\x32\".chaosplatform.scheduling.Schedule\"E\n\x16GetByExperimentRequest\x12\x15\n\rexperiment_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"M\n\x14GetByExperimentReply\x12\x35\n\tschedules\x18\x01 \x03(\x0b\x32\".chaosplatform.scheduling.Schedule\"A\n\x17GetByAccessTokenRequest\x12\x10\n\x08token_id\x18\x01 \x01(\t\x12\x14\n\x0cwith_payload\x18\x02 \x01(\x08\"M\n\x15GetByAccessTokenReply\x12\x34\n\x08schedule\x18\x01 \x01(\x0b\x32\".chaosplatform.scheduling.Schedule2\xe3\x05\n\x11SchedulingService\x12O\n\x03Get\x12$.chaosplatform.scheduling.GetRequest\x1a\".chaosplatform.scheduling.GetReply\x12[\n\x07GetMany\x12(.chaosplatform.scheduling.GetManyRequest\x1a&.chaosplatform.scheduling.GetManyReply\x12\x61\n\tGetByUser\x12*.chaosplatform.scheduling.GetByUserRequest\x1a(.chaosplatform.scheduling.GetByUserReply\x12^\n\x08GetByOrg\x12).chaosplatform.scheduling.GetByOrgRequest\x1a\'.chaosplatform.scheduling.GetByOrgReply\x12p\n\x0eGetByWorkspace\x12/.chaosplatform.scheduling.GetByWorkspaceRequest\x1a-.chaosplatform.scheduling.GetByWorkspaceReply\x12s\n\x0fGetByExperiment\x12\x30.chaosplatform.scheduling.GetByExperimentRequest\x1a..chaosplatform.scheduling.GetByExperimentReply\x12v\n\x10GetByAccessToken\x12\x31.chaosplatform.scheduling.GetByAccessTokenRequest\x1a/.chaosplatform.scheduling.GetByAccessTokenReplyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])




_SCHEDULE = _descriptor.Descriptor(
  name='Schedule',
  full_name='chaosplatform.scheduling.Schedule',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.scheduling.Schedule.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaosplatform.scheduling.Schedule.user_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='org_id', full_name='chaosplatform.scheduling.Schedule.org_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='chaosplatform.scheduling.Schedule.workspace_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='chaosplatform.scheduling.Schedule.experiment_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_id', full_name='chaosplatform.scheduling.Schedule.token_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='job_id', full_name='chaosplatform.scheduling.Schedule.job_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='chaosplatform.scheduling.Schedule.status', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interval', full_name='chaosplatform.scheduling.Schedule.interval', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_on', full_name='chaosplatform.scheduling.Schedule.created_on', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_from', full_name='chaosplatform.scheduling.Schedule.active_from', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='active_until', full_name='chaosplatform.scheduling.Schedule.active_until', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='results', full_name='chaosplatform.scheduling.Schedule.results', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settings', full_name='chaosplatform.scheduling.Schedule.settings', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='configuration', full_name='chaosplatform.scheduling.Schedule.configuration', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secrets', full_name='chaosplatform.scheduling.Schedule.secrets', index=15,
      number=16, type=11, cpp_type=10, label=1,
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
  serialized_start=121,
  serialized_end=611,
)


_GETREQUEST = _descriptor.Descriptor(
  name='GetRequest',
  full_name='chaosplatform.scheduling.GetRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='chaosplatform.scheduling.GetRequest.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetRequest.with_payload', index=1,
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
  serialized_start=613,
  serialized_end=659,
)


_GETREPLY = _descriptor.Descriptor(
  name='GetReply',
  full_name='chaosplatform.scheduling.GetReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule', full_name='chaosplatform.scheduling.GetReply.schedule', index=0,
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
  serialized_start=661,
  serialized_end=725,
)


_GETMANYREQUEST = _descriptor.Descriptor(
  name='GetManyRequest',
  full_name='chaosplatform.scheduling.GetManyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ids', full_name='chaosplatform.scheduling.GetManyRequest.ids', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetManyRequest.with_payload', index=1,
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
  serialized_start=727,
  serialized_end=778,
)


_GETMANYREPLY = _descriptor.Descriptor(
  name='GetManyReply',
  full_name='chaosplatform.scheduling.GetManyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='chaosplatform.scheduling.GetManyReply.schedules', index=0,
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
  serialized_start=780,
  serialized_end=849,
)


_GETBYUSERREQUEST = _descriptor.Descriptor(
  name='GetByUserRequest',
  full_name='chaosplatform.scheduling.GetByUserRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='user_id', full_name='chaosplatform.scheduling.GetByUserRequest.user_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetByUserRequest.with_payload', index=1,
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
  serialized_start=851,
  serialized_end=908,
)


_GETBYUSERREPLY = _descriptor.Descriptor(
  name='GetByUserReply',
  full_name='chaosplatform.scheduling.GetByUserReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='chaosplatform.scheduling.GetByUserReply.schedules', index=0,
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
  serialized_start=910,
  serialized_end=981,
)


_GETBYORGREQUEST = _descriptor.Descriptor(
  name='GetByOrgRequest',
  full_name='chaosplatform.scheduling.GetByOrgRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='org_id', full_name='chaosplatform.scheduling.GetByOrgRequest.org_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetByOrgRequest.with_payload', index=1,
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
  serialized_start=983,
  serialized_end=1038,
)


_GETBYORGREPLY = _descriptor.Descriptor(
  name='GetByOrgReply',
  full_name='chaosplatform.scheduling.GetByOrgReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='chaosplatform.scheduling.GetByOrgReply.schedules', index=0,
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
  serialized_start=1040,
  serialized_end=1110,
)


_GETBYWORKSPACEREQUEST = _descriptor.Descriptor(
  name='GetByWorkspaceRequest',
  full_name='chaosplatform.scheduling.GetByWorkspaceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='workspace_id', full_name='chaosplatform.scheduling.GetByWorkspaceRequest.workspace_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetByWorkspaceRequest.with_payload', index=1,
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
  serialized_start=1112,
  serialized_end=1179,
)


_GETBYWORKSPACEREPLY = _descriptor.Descriptor(
  name='GetByWorkspaceReply',
  full_name='chaosplatform.scheduling.GetByWorkspaceReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='chaosplatform.scheduling.GetByWorkspaceReply.schedules', index=0,
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
  serialized_start=1181,
  serialized_end=1257,
)


_GETBYEXPERIMENTREQUEST = _descriptor.Descriptor(
  name='GetByExperimentRequest',
  full_name='chaosplatform.scheduling.GetByExperimentRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='experiment_id', full_name='chaosplatform.scheduling.GetByExperimentRequest.experiment_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetByExperimentRequest.with_payload', index=1,
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
  serialized_start=1259,
  serialized_end=1328,
)


_GETBYEXPERIMENTREPLY = _descriptor.Descriptor(
  name='GetByExperimentReply',
  full_name='chaosplatform.scheduling.GetByExperimentReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedules', full_name='chaosplatform.scheduling.GetByExperimentReply.schedules', index=0,
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
  serialized_start=1330,
  serialized_end=1407,
)


_GETBYACCESSTOKENREQUEST = _descriptor.Descriptor(
  name='GetByAccessTokenRequest',
  full_name='chaosplatform.scheduling.GetByAccessTokenRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='token_id', full_name='chaosplatform.scheduling.GetByAccessTokenRequest.token_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='with_payload', full_name='chaosplatform.scheduling.GetByAccessTokenRequest.with_payload', index=1,
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
  serialized_start=1409,
  serialized_end=1474,
)


_GETBYACCESSTOKENREPLY = _descriptor.Descriptor(
  name='GetByAccessTokenReply',
  full_name='chaosplatform.scheduling.GetByAccessTokenReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='schedule', full_name='chaosplatform.scheduling.GetByAccessTokenReply.schedule', index=0,
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
  serialized_start=1476,
  serialized_end=1553,
)

_SCHEDULE.fields_by_name['created_on'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCHEDULE.fields_by_name['active_from'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCHEDULE.fields_by_name['active_until'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_SCHEDULE.fields_by_name['results'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SCHEDULE.fields_by_name['settings'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SCHEDULE.fields_by_name['configuration'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_SCHEDULE.fields_by_name['secrets'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
_GETREPLY.fields_by_name['schedule'].message_type = _SCHEDULE
_GETMANYREPLY.fields_by_name['schedules'].message_type = _SCHEDULE
_GETBYUSERREPLY.fields_by_name['schedules'].message_type = _SCHEDULE
_GETBYORGREPLY.fields_by_name['schedules'].message_type = _SCHEDULE
_GETBYWORKSPACEREPLY.fields_by_name['schedules'].message_type = _SCHEDULE
_GETBYEXPERIMENTREPLY.fields_by_name['schedules'].message_type = _SCHEDULE
_GETBYACCESSTOKENREPLY.fields_by_name['schedule'].message_type = _SCHEDULE
DESCRIPTOR.message_types_by_name['Schedule'] = _SCHEDULE
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
DESCRIPTOR.message_types_by_name['GetByExperimentRequest'] = _GETBYEXPERIMENTREQUEST
DESCRIPTOR.message_types_by_name['GetByExperimentReply'] = _GETBYEXPERIMENTREPLY
DESCRIPTOR.message_types_by_name['GetByAccessTokenRequest'] = _GETBYACCESSTOKENREQUEST
DESCRIPTOR.message_types_by_name['GetByAccessTokenReply'] = _GETBYACCESSTOKENREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Schedule = _reflection.GeneratedProtocolMessageType('Schedule', (_message.Message,), dict(
  DESCRIPTOR = _SCHEDULE,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.Schedule)
  ))
_sym_db.RegisterMessage(Schedule)

GetRequest = _reflection.GeneratedProtocolMessageType('GetRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetRequest)
  ))
_sym_db.RegisterMessage(GetRequest)

GetReply = _reflection.GeneratedProtocolMessageType('GetReply', (_message.Message,), dict(
  DESCRIPTOR = _GETREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetReply)
  ))
_sym_db.RegisterMessage(GetReply)

GetManyRequest = _reflection.GeneratedProtocolMessageType('GetManyRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETMANYREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetManyRequest)
  ))
_sym_db.RegisterMessage(GetManyRequest)

GetManyReply = _reflection.GeneratedProtocolMessageType('GetManyReply', (_message.Message,), dict(
  DESCRIPTOR = _GETMANYREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetManyReply)
  ))
_sym_db.RegisterMessage(GetManyReply)

GetByUserRequest = _reflection.GeneratedProtocolMessageType('GetByUserRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByUserRequest)
  ))
_sym_db.RegisterMessage(GetByUserRequest)

GetByUserReply = _reflection.GeneratedProtocolMessageType('GetByUserReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYUSERREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByUserReply)
  ))
_sym_db.RegisterMessage(GetByUserReply)

GetByOrgRequest = _reflection.GeneratedProtocolMessageType('GetByOrgRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYORGREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByOrgRequest)
  ))
_sym_db.RegisterMessage(GetByOrgRequest)

GetByOrgReply = _reflection.GeneratedProtocolMessageType('GetByOrgReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYORGREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByOrgReply)
  ))
_sym_db.RegisterMessage(GetByOrgReply)

GetByWorkspaceRequest = _reflection.GeneratedProtocolMessageType('GetByWorkspaceRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYWORKSPACEREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByWorkspaceRequest)
  ))
_sym_db.RegisterMessage(GetByWorkspaceRequest)

GetByWorkspaceReply = _reflection.GeneratedProtocolMessageType('GetByWorkspaceReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYWORKSPACEREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByWorkspaceReply)
  ))
_sym_db.RegisterMessage(GetByWorkspaceReply)

GetByExperimentRequest = _reflection.GeneratedProtocolMessageType('GetByExperimentRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYEXPERIMENTREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByExperimentRequest)
  ))
_sym_db.RegisterMessage(GetByExperimentRequest)

GetByExperimentReply = _reflection.GeneratedProtocolMessageType('GetByExperimentReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYEXPERIMENTREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByExperimentReply)
  ))
_sym_db.RegisterMessage(GetByExperimentReply)

GetByAccessTokenRequest = _reflection.GeneratedProtocolMessageType('GetByAccessTokenRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBYACCESSTOKENREQUEST,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByAccessTokenRequest)
  ))
_sym_db.RegisterMessage(GetByAccessTokenRequest)

GetByAccessTokenReply = _reflection.GeneratedProtocolMessageType('GetByAccessTokenReply', (_message.Message,), dict(
  DESCRIPTOR = _GETBYACCESSTOKENREPLY,
  __module__ = 'scheduling.scheduling_pb2'
  # @@protoc_insertion_point(class_scope:chaosplatform.scheduling.GetByAccessTokenReply)
  ))
_sym_db.RegisterMessage(GetByAccessTokenReply)



_SCHEDULINGSERVICE = _descriptor.ServiceDescriptor(
  name='SchedulingService',
  full_name='chaosplatform.scheduling.SchedulingService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1556,
  serialized_end=2295,
  methods=[
  _descriptor.MethodDescriptor(
    name='Get',
    full_name='chaosplatform.scheduling.SchedulingService.Get',
    index=0,
    containing_service=None,
    input_type=_GETREQUEST,
    output_type=_GETREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMany',
    full_name='chaosplatform.scheduling.SchedulingService.GetMany',
    index=1,
    containing_service=None,
    input_type=_GETMANYREQUEST,
    output_type=_GETMANYREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByUser',
    full_name='chaosplatform.scheduling.SchedulingService.GetByUser',
    index=2,
    containing_service=None,
    input_type=_GETBYUSERREQUEST,
    output_type=_GETBYUSERREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByOrg',
    full_name='chaosplatform.scheduling.SchedulingService.GetByOrg',
    index=3,
    containing_service=None,
    input_type=_GETBYORGREQUEST,
    output_type=_GETBYORGREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByWorkspace',
    full_name='chaosplatform.scheduling.SchedulingService.GetByWorkspace',
    index=4,
    containing_service=None,
    input_type=_GETBYWORKSPACEREQUEST,
    output_type=_GETBYWORKSPACEREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByExperiment',
    full_name='chaosplatform.scheduling.SchedulingService.GetByExperiment',
    index=5,
    containing_service=None,
    input_type=_GETBYEXPERIMENTREQUEST,
    output_type=_GETBYEXPERIMENTREPLY,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetByAccessToken',
    full_name='chaosplatform.scheduling.SchedulingService.GetByAccessToken',
    index=6,
    containing_service=None,
    input_type=_GETBYACCESSTOKENREQUEST,
    output_type=_GETBYACCESSTOKENREPLY,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SCHEDULINGSERVICE)

DESCRIPTOR.services_by_name['SchedulingService'] = _SCHEDULINGSERVICE

# @@protoc_insertion_point(module_scope)
