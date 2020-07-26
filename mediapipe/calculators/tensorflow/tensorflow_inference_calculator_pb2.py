# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/tensorflow/tensorflow_inference_calculator.proto

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
  name='mediapipe/calculators/tensorflow/tensorflow_inference_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nFmediapipe/calculators/tensorflow/tensorflow_inference_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xc6\x02\n$TensorFlowInferenceCalculatorOptions\x12\x16\n\x0esignature_name\x18\x01 \x01(\t\x12\x12\n\nbatch_size\x18\x02 \x01(\x05\x12&\n\x18\x61\x64\x64_batch_dim_to_tensors\x18\x03 \x01(\x08:\x04true\x12\x1a\n\x12recurrent_tag_pair\x18\x04 \x03(\t\x12\'\n\x18skip_on_missing_features\x18\x05 \x01(\x08:\x05\x66\x61lse\x12&\n\x1bmax_concurrent_session_runs\x18\x06 \x01(\x05:\x01\x30\x32]\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\x8b\xe1\x9f\x36 \x01(\x0b\x32/.mediapipe.TensorFlowInferenceCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_TENSORFLOWINFERENCECALCULATOROPTIONS = _descriptor.Descriptor(
  name='TensorFlowInferenceCalculatorOptions',
  full_name='mediapipe.TensorFlowInferenceCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature_name', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.signature_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.batch_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='add_batch_dim_to_tensors', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.add_batch_dim_to_tensors', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recurrent_tag_pair', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.recurrent_tag_pair', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='skip_on_missing_features', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.skip_on_missing_features', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_concurrent_session_runs', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.max_concurrent_session_runs', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TensorFlowInferenceCalculatorOptions.ext', index=0,
      number=113766539, type=11, cpp_type=10, label=1,
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
  serialized_start=124,
  serialized_end=450,
)

DESCRIPTOR.message_types_by_name['TensorFlowInferenceCalculatorOptions'] = _TENSORFLOWINFERENCECALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TensorFlowInferenceCalculatorOptions = _reflection.GeneratedProtocolMessageType('TensorFlowInferenceCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TENSORFLOWINFERENCECALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.tensorflow.tensorflow_inference_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TensorFlowInferenceCalculatorOptions)
  })
_sym_db.RegisterMessage(TensorFlowInferenceCalculatorOptions)

_TENSORFLOWINFERENCECALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TENSORFLOWINFERENCECALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TENSORFLOWINFERENCECALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
