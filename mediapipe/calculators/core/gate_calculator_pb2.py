# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/core/gate_calculator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/core/gate_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n0mediapipe/calculators/core/gate_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\x87\x01\n\x15GateCalculatorOptions\x12\x1e\n\x16\x65mpty_packets_as_allow\x18\x01 \x01(\x08\x32N\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xdf\x9f\xe8| \x01(\x0b\x32 .mediapipe.GateCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_GATECALCULATOROPTIONS = _descriptor.Descriptor(
  name='GateCalculatorOptions',
  full_name='mediapipe.GateCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='empty_packets_as_allow', full_name='mediapipe.GateCalculatorOptions.empty_packets_as_allow', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.GateCalculatorOptions.ext', index=0,
      number=261754847, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=102,
  serialized_end=237,
)

DESCRIPTOR.message_types_by_name['GateCalculatorOptions'] = _GATECALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GateCalculatorOptions = _reflection.GeneratedProtocolMessageType('GateCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _GATECALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.core.gate_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.GateCalculatorOptions)
  })
_sym_db.RegisterMessage(GateCalculatorOptions)

_GATECALCULATOROPTIONS.extensions_by_name['ext'].message_type = _GATECALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_GATECALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
