# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensorflow/tensor_to_vector_float_calculator_options.proto

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
  name='mediapipe/calculators/tensorflow/tensor_to_vector_float_calculator_options.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nPmediapipe/calculators/tensorflow/tensor_to_vector_float_calculator_options.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xbd\x01\n$TensorToVectorFloatCalculatorOptions\x12\x1b\n\x0ctensor_is_2d\x18\x01 \x01(\x08:\x05\x66\x61lse\x12\x19\n\nflatten_nd\x18\x02 \x01(\x08:\x05\x66\x61lse2]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xf5\xf1\xd0\x39 \x01(\x0b\x32/.mediapipe.TensorToVectorFloatCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TENSORTOVECTORFLOATCALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorToVectorFloatCalculatorOptions',
  full_name='mediapipe.TensorToVectorFloatCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tensor_is_2d', full_name='mediapipe.TensorToVectorFloatCalculatorOptions.tensor_is_2d', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='flatten_nd', full_name='mediapipe.TensorToVectorFloatCalculatorOptions.flatten_nd', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorToVectorFloatCalculatorOptions.ext', index=0,
      number=120862965, type=11, cpp_type=10, label=1,
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
  serialized_start=134,
  serialized_end=323,
)

DESCRIPTOR.message_types_by_name['TensorToVectorFloatCalculatorOptions'] = _TENSORTOVECTORFLOATCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorToVectorFloatCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorToVectorFloatCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TENSORTOVECTORFLOATCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensorflow.tensor_to_vector_float_calculator_options_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorToVectorFloatCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorToVectorFloatCalculatorOptions)

_TENSORTOVECTORFLOATCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORTOVECTORFLOATCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORTOVECTORFLOATCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
