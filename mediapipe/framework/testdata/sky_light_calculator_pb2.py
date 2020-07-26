# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/framework/testdata/sky_light_calculator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/framework/testdata/sky_light_calculator.proto',
  package='mediapipe',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n7mediapipe/framework/testdata/sky_light_calculator.proto\x12\tmediapipe\"@\n\x19SkyLightCalculatorOptions\x12\x11\n\tsky_color\x18\x01 \x01(\t\x12\x10\n\x08sky_grid\x18\x02 \x03(\x05\x62\x06proto3'
)




_SKYLIGHTCALCULATOROPTIONS = _descriptor.Descriptor(
  name='SkyLightCalculatorOptions',
  full_name='mediapipe.SkyLightCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sky_color', full_name='mediapipe.SkyLightCalculatorOptions.sky_color', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sky_grid', full_name='mediapipe.SkyLightCalculatorOptions.sky_grid', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=70,
  serialized_end=134,
)

DESCRIPTOR.message_types_by_name['SkyLightCalculatorOptions'] = _SKYLIGHTCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkyLightCalculatorOptions = _reflection.GeneratedProtocolMessageType('SkyLightCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _SKYLIGHTCALCULATOROPTIONS,
  '__module__' : 'mediapipe.framework.testdata.sky_light_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.SkyLightCalculatorOptions)
  })
_sym_db.RegisterMessage(SkyLightCalculatorOptions)


# @@protoc_insertion_point(module_scope)
