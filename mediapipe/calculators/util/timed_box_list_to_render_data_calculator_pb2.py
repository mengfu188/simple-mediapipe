# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/util/timed_box_list_to_render_data_calculator.proto

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
from mediapipe.util import color_pb2 as mediapipe_dot_util_dot_color__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/util/timed_box_list_to_render_data_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nImediapipe/calculators/util/timed_box_list_to_render_data_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a\x1amediapipe/util/color.proto\"\xcb\x01\n)TimedBoxListToRenderDataCalculatorOptions\x12#\n\tbox_color\x18\x01 \x01(\x0b\x32\x10.mediapipe.Color\x12\x14\n\tthickness\x18\x02 \x01(\x01:\x01\x31\x32\x63\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xce\x8a\x9e\x8a\x01 \x01(\x0b\x32\x34.mediapipe.TimedBoxListToRenderDataCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_util_dot_color__pb2.DESCRIPTOR,])




_TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS = _descriptor.Descriptor(
  name='TimedBoxListToRenderDataCalculatorOptions',
  full_name='mediapipe.TimedBoxListToRenderDataCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='box_color', full_name='mediapipe.TimedBoxListToRenderDataCalculatorOptions.box_color', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='thickness', full_name='mediapipe.TimedBoxListToRenderDataCalculatorOptions.thickness', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.TimedBoxListToRenderDataCalculatorOptions.ext', index=0,
      number=289899854, type=11, cpp_type=10, label=1,
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
  serialized_start=155,
  serialized_end=358,
)

_TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS.fields_by_name['box_color'].message_type = mediapipe_dot_util_dot_color__pb2._COLOR
DESCRIPTOR.message_types_by_name['TimedBoxListToRenderDataCalculatorOptions'] = _TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimedBoxListToRenderDataCalculatorOptions = _reflection.GeneratedProtocolMessageType('TimedBoxListToRenderDataCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.util.timed_box_list_to_render_data_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.TimedBoxListToRenderDataCalculatorOptions)
  })
_sym_db.RegisterMessage(TimedBoxListToRenderDataCalculatorOptions)

_TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS.extensions_by_name['ext'].message_type = _TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_TIMEDBOXLISTTORENDERDATACALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
