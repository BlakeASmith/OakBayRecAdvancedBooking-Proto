# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VenueService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='VenueService.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x12VenueService.proto\"/\n\tLoginInfo\x12\x10\n\x08username\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\"%\n\x11LoginVerification\x12\x10\n\x08verified\x18\x01 \x01(\x08\"H\n\x0e\x42ookingRequest\x12\x12\n\nsessionIDs\x18\x01 \x03(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\xda\x01\n\x14\x42ookingRequestResult\x12\x31\n\x06\x62ooked\x18\x01 \x03(\x0b\x32!.BookingRequestResult.BookedEntry\x12\x31\n\x06\x65rrors\x18\x02 \x03(\x0b\x32!.BookingRequestResult.ErrorsEntry\x1a-\n\x0b\x42ookedEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\x1a-\n\x0b\x45rrorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x32l\n\x05Venue\x12\x30\n\x04\x42ook\x12\x0f.BookingRequest\x1a\x15.BookingRequestResult\"\x00\x12\x31\n\rValidateLogin\x12\n.LoginInfo\x1a\x12.LoginVerification\"\x00\x62\x06proto3'
)




_LOGININFO = _descriptor.Descriptor(
  name='LoginInfo',
  full_name='LoginInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='username', full_name='LoginInfo.username', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='LoginInfo.password', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=22,
  serialized_end=69,
)


_LOGINVERIFICATION = _descriptor.Descriptor(
  name='LoginVerification',
  full_name='LoginVerification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='verified', full_name='LoginVerification.verified', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=71,
  serialized_end=108,
)


_BOOKINGREQUEST = _descriptor.Descriptor(
  name='BookingRequest',
  full_name='BookingRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sessionIDs', full_name='BookingRequest.sessionIDs', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='BookingRequest.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='BookingRequest.password', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=110,
  serialized_end=182,
)


_BOOKINGREQUESTRESULT_BOOKEDENTRY = _descriptor.Descriptor(
  name='BookedEntry',
  full_name='BookingRequestResult.BookedEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BookingRequestResult.BookedEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='BookingRequestResult.BookedEntry.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=311,
  serialized_end=356,
)

_BOOKINGREQUESTRESULT_ERRORSENTRY = _descriptor.Descriptor(
  name='ErrorsEntry',
  full_name='BookingRequestResult.ErrorsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='BookingRequestResult.ErrorsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='BookingRequestResult.ErrorsEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=358,
  serialized_end=403,
)

_BOOKINGREQUESTRESULT = _descriptor.Descriptor(
  name='BookingRequestResult',
  full_name='BookingRequestResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='booked', full_name='BookingRequestResult.booked', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='errors', full_name='BookingRequestResult.errors', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_BOOKINGREQUESTRESULT_BOOKEDENTRY, _BOOKINGREQUESTRESULT_ERRORSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=403,
)

_BOOKINGREQUESTRESULT_BOOKEDENTRY.containing_type = _BOOKINGREQUESTRESULT
_BOOKINGREQUESTRESULT_ERRORSENTRY.containing_type = _BOOKINGREQUESTRESULT
_BOOKINGREQUESTRESULT.fields_by_name['booked'].message_type = _BOOKINGREQUESTRESULT_BOOKEDENTRY
_BOOKINGREQUESTRESULT.fields_by_name['errors'].message_type = _BOOKINGREQUESTRESULT_ERRORSENTRY
DESCRIPTOR.message_types_by_name['LoginInfo'] = _LOGININFO
DESCRIPTOR.message_types_by_name['LoginVerification'] = _LOGINVERIFICATION
DESCRIPTOR.message_types_by_name['BookingRequest'] = _BOOKINGREQUEST
DESCRIPTOR.message_types_by_name['BookingRequestResult'] = _BOOKINGREQUESTRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginInfo = _reflection.GeneratedProtocolMessageType('LoginInfo', (_message.Message,), {
  'DESCRIPTOR' : _LOGININFO,
  '__module__' : 'VenueService_pb2'
  # @@protoc_insertion_point(class_scope:LoginInfo)
  })
_sym_db.RegisterMessage(LoginInfo)

LoginVerification = _reflection.GeneratedProtocolMessageType('LoginVerification', (_message.Message,), {
  'DESCRIPTOR' : _LOGINVERIFICATION,
  '__module__' : 'VenueService_pb2'
  # @@protoc_insertion_point(class_scope:LoginVerification)
  })
_sym_db.RegisterMessage(LoginVerification)

BookingRequest = _reflection.GeneratedProtocolMessageType('BookingRequest', (_message.Message,), {
  'DESCRIPTOR' : _BOOKINGREQUEST,
  '__module__' : 'VenueService_pb2'
  # @@protoc_insertion_point(class_scope:BookingRequest)
  })
_sym_db.RegisterMessage(BookingRequest)

BookingRequestResult = _reflection.GeneratedProtocolMessageType('BookingRequestResult', (_message.Message,), {

  'BookedEntry' : _reflection.GeneratedProtocolMessageType('BookedEntry', (_message.Message,), {
    'DESCRIPTOR' : _BOOKINGREQUESTRESULT_BOOKEDENTRY,
    '__module__' : 'VenueService_pb2'
    # @@protoc_insertion_point(class_scope:BookingRequestResult.BookedEntry)
    })
  ,

  'ErrorsEntry' : _reflection.GeneratedProtocolMessageType('ErrorsEntry', (_message.Message,), {
    'DESCRIPTOR' : _BOOKINGREQUESTRESULT_ERRORSENTRY,
    '__module__' : 'VenueService_pb2'
    # @@protoc_insertion_point(class_scope:BookingRequestResult.ErrorsEntry)
    })
  ,
  'DESCRIPTOR' : _BOOKINGREQUESTRESULT,
  '__module__' : 'VenueService_pb2'
  # @@protoc_insertion_point(class_scope:BookingRequestResult)
  })
_sym_db.RegisterMessage(BookingRequestResult)
_sym_db.RegisterMessage(BookingRequestResult.BookedEntry)
_sym_db.RegisterMessage(BookingRequestResult.ErrorsEntry)


_BOOKINGREQUESTRESULT_BOOKEDENTRY._options = None
_BOOKINGREQUESTRESULT_ERRORSENTRY._options = None

_VENUE = _descriptor.ServiceDescriptor(
  name='Venue',
  full_name='Venue',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=405,
  serialized_end=513,
  methods=[
  _descriptor.MethodDescriptor(
    name='Book',
    full_name='Venue.Book',
    index=0,
    containing_service=None,
    input_type=_BOOKINGREQUEST,
    output_type=_BOOKINGREQUESTRESULT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ValidateLogin',
    full_name='Venue.ValidateLogin',
    index=1,
    containing_service=None,
    input_type=_LOGININFO,
    output_type=_LOGINVERIFICATION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_VENUE)

DESCRIPTOR.services_by_name['Venue'] = _VENUE

# @@protoc_insertion_point(module_scope)
