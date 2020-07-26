# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/examples/desktop/autoflip/calculators/face_to_region_calculator.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mediapipe.examples.desktop.autoflip.quality import visual_scorer_pb2 as mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_visual__scorer__pb2
from mediapipe.framework import calculator_pb2 as mediapipe_dot_framework_dot_calculator__pb2
try:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe_dot_framework_dot_calculator__options__pb2
except AttributeError:
  mediapipe_dot_framework_dot_calculator__options__pb2 = mediapipe_dot_framework_dot_calculator__pb2.mediapipe.framework.calculator_options_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/examples/desktop/autoflip/calculators/face_to_region_calculator.proto',
  package='mediapipe.autoflip',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nOmediapipe/examples/desktop/autoflip/calculators/face_to_region_calculator.proto\x12\x12mediapipe.autoflip\x1a?mediapipe/examples/desktop/autoflip/quality/visual_scorer.proto\x1a$mediapipe/framework/calculator.proto\"\xe0\x02\n\x1d\x46\x61\x63\x65ToRegionCalculatorOptions\x12?\n\x0escorer_options\x18\x01 \x01(\x0b\x32\'.mediapipe.autoflip.VisualScorerOptions\x12 \n\x11\x65xport_whole_face\x18\x02 \x01(\x08:\x05\x66\x61lse\x12/\n export_individual_face_landmarks\x18\x03 \x01(\x08:\x05\x66\x61lse\x12(\n\x1a\x65xport_bbox_from_landmarks\x18\x04 \x01(\x08:\x04true\x12\x1f\n\x11use_visual_scorer\x18\x05 \x01(\x08:\x04true2`\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xd2\xb3\xd4\x86\x01 \x01(\x0b\x32\x31.mediapipe.autoflip.FaceToRegionCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_visual__scorer__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,])




_FACETOREGIONCALCULATOROPTIONS = _descriptor.Descriptor(
  name='FaceToRegionCalculatorOptions',
  full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='scorer_options', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.scorer_options', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_whole_face', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.export_whole_face', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_individual_face_landmarks', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.export_individual_face_landmarks', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='export_bbox_from_landmarks', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.export_bbox_from_landmarks', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_visual_scorer', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.use_visual_scorer', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.autoflip.FaceToRegionCalculatorOptions.ext', index=0,
      number=282401234, type=11, cpp_type=10, label=1,
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
  serialized_start=207,
  serialized_end=559,
)

_FACETOREGIONCALCULATOROPTIONS.fields_by_name['scorer_options'].message_type = mediapipe_dot_examples_dot_desktop_dot_autoflip_dot_quality_dot_visual__scorer__pb2._VISUALSCOREROPTIONS
DESCRIPTOR.message_types_by_name['FaceToRegionCalculatorOptions'] = _FACETOREGIONCALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FaceToRegionCalculatorOptions = _reflection.GeneratedProtocolMessageType('FaceToRegionCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _FACETOREGIONCALCULATOROPTIONS,
  '__module__' : 'mediapipe.examples.desktop.autoflip.calculators.face_to_region_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.autoflip.FaceToRegionCalculatorOptions)
  })
_sym_db.RegisterMessage(FaceToRegionCalculatorOptions)

_FACETOREGIONCALCULATOROPTIONS.extensions_by_name['ext'].message_type = _FACETOREGIONCALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_FACETOREGIONCALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
