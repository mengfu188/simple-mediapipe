# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/video/opencv_video_encoder_calculator.proto

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
  name='mediapipe/calculators/video/opencv_video_encoder_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nAmediapipe/calculators/video/opencv_video_encoder_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\"\xd4\x01\n#OpenCvVideoEncoderCalculatorOptions\x12\r\n\x05\x63odec\x18\x01 \x01(\t\x12\x14\n\x0cvideo_format\x18\x02 \x01(\t\x12\x0b\n\x03\x66ps\x18\x03 \x01(\x01\x12\r\n\x05width\x18\x04 \x01(\x05\x12\x0e\n\x06height\x18\x05 \x01(\x05\x32\\\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xfb\xb9\x93\x63 \x01(\x0b\x32..mediapipe.OpenCvVideoEncoderCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_OPENCVVIDEOENCODERCALCULATOROPTIONS = _descriptor.Descriptor(
  name='OpenCvVideoEncoderCalculatorOptions',
  full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='codec', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.codec', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='video_format', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.video_format', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fps', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.fps', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.width', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.height', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.OpenCvVideoEncoderCalculatorOptions.ext', index=0,
      number=207936763, type=11, cpp_type=10, label=1,
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
  serialized_start=119,
  serialized_end=331,
)

DESCRIPTOR.message_types_by_name['OpenCvVideoEncoderCalculatorOptions'] = _OPENCVVIDEOENCODERCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OpenCvVideoEncoderCalculatorOptions = _reflection.GeneratedProtocolMessageType('OpenCvVideoEncoderCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _OPENCVVIDEOENCODERCALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.video.opencv_video_encoder_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.OpenCvVideoEncoderCalculatorOptions)
  })
_sym_db.RegisterMessage(OpenCvVideoEncoderCalculatorOptions)

_OPENCVVIDEOENCODERCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _OPENCVVIDEOENCODERCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_OPENCVVIDEOENCODERCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
