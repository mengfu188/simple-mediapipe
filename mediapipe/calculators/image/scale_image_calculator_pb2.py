# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mediapipe/calculators/image/scale_image_calculator.proto

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
from mediapipe.framework.formats import image_format_pb2 as mediapipe_dot_framework_dot_formats_dot_image__format__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mediapipe/calculators/image/scale_image_calculator.proto',
  package='mediapipe',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n8mediapipe/calculators/image/scale_image_calculator.proto\x12\tmediapipe\x1a$mediapipe/framework/calculator.proto\x1a.mediapipe/framework/formats/image_format.proto\"\x89\x06\n\x1bScaleImageCalculatorOptions\x12\x14\n\x0ctarget_width\x18\x01 \x01(\x05\x12\x15\n\rtarget_height\x18\x02 \x01(\x05\x12#\n\x15preserve_aspect_ratio\x18\x03 \x01(\x08:\x04true\x12\x1e\n\x10min_aspect_ratio\x18\x04 \x01(\t:\x04\x39/16\x12\x1e\n\x10max_aspect_ratio\x18\x05 \x01(\t:\x04\x31\x36/9\x12\x34\n\routput_format\x18\x06 \x01(\x0e\x32\x1d.mediapipe.ImageFormat.Format\x12Q\n\talgorithm\x18\x07 \x01(\x0e\x32\x35.mediapipe.ScaleImageCalculatorOptions.ScaleAlgorithm:\x07\x44\x45\x46\x41ULT\x12\x1e\n\x12\x61lignment_boundary\x18\x08 \x01(\x05:\x02\x31\x36\x12#\n\x15set_alignment_padding\x18\t \x01(\x08:\x04true\x12\x32\n#OBSOLETE_skip_linear_rgb_conversion\x18\n \x01(\x08:\x05\x66\x61lse\x12&\n\x1bpost_sharpening_coefficient\x18\x0b \x01(\x02:\x01\x30\x12\x33\n\x0cinput_format\x18\x0c \x01(\x0e\x32\x1d.mediapipe.ImageFormat.Format\x12\x1f\n\x14scale_to_multiple_of\x18\r \x01(\x05:\x01\x32\x12\x18\n\tuse_bt709\x18\x0e \x01(\x08:\x05\x66\x61lse\"h\n\x0eScaleAlgorithm\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06LINEAR\x10\x01\x12\t\n\x05\x43UBIC\x10\x02\x12\x08\n\x04\x41REA\x10\x03\x12\x0b\n\x07LANCZOS\x10\x04\x12\x1b\n\x17\x44\x45\x46\x41ULT_WITHOUT_UPSCALE\x10\x05\x32T\n\x03\x65xt\x12\x1c.mediapipe.CalculatorOptions\x18\xbb\xe5\xca\x1f \x01(\x0b\x32&.mediapipe.ScaleImageCalculatorOptions'
  ,
  dependencies=[mediapipe_dot_framework_dot_calculator__pb2.DESCRIPTOR,mediapipe_dot_framework_dot_formats_dot_image__format__pb2.DESCRIPTOR,])



_SCALEIMAGECALCULATOROPTIONS_SCALEALGORITHM = _descriptor.EnumDescriptor(
  name='ScaleAlgorithm',
  full_name='mediapipe.ScaleImageCalculatorOptions.ScaleAlgorithm',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LINEAR', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CUBIC', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='AREA', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='LANCZOS', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DEFAULT_WITHOUT_UPSCALE', index=5, number=5,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=745,
  serialized_end=849,
)
_sym_db.RegisterEnumDescriptor(_SCALEIMAGECALCULATOROPTIONS_SCALEALGORITHM)


_SCALEIMAGECALCULATOROPTIONS = _descriptor.Descriptor(
  name='ScaleImageCalculatorOptions',
  full_name='mediapipe.ScaleImageCalculatorOptions',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_width', full_name='mediapipe.ScaleImageCalculatorOptions.target_width', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='target_height', full_name='mediapipe.ScaleImageCalculatorOptions.target_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='preserve_aspect_ratio', full_name='mediapipe.ScaleImageCalculatorOptions.preserve_aspect_ratio', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='min_aspect_ratio', full_name='mediapipe.ScaleImageCalculatorOptions.min_aspect_ratio', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"9/16".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='max_aspect_ratio', full_name='mediapipe.ScaleImageCalculatorOptions.max_aspect_ratio', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=b"16/9".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='output_format', full_name='mediapipe.ScaleImageCalculatorOptions.output_format', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='mediapipe.ScaleImageCalculatorOptions.algorithm', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='alignment_boundary', full_name='mediapipe.ScaleImageCalculatorOptions.alignment_boundary', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='set_alignment_padding', full_name='mediapipe.ScaleImageCalculatorOptions.set_alignment_padding', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='OBSOLETE_skip_linear_rgb_conversion', full_name='mediapipe.ScaleImageCalculatorOptions.OBSOLETE_skip_linear_rgb_conversion', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='post_sharpening_coefficient', full_name='mediapipe.ScaleImageCalculatorOptions.post_sharpening_coefficient', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='input_format', full_name='mediapipe.ScaleImageCalculatorOptions.input_format', index=11,
      number=12, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='scale_to_multiple_of', full_name='mediapipe.ScaleImageCalculatorOptions.scale_to_multiple_of', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='use_bt709', full_name='mediapipe.ScaleImageCalculatorOptions.use_bt709', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
    _descriptor.FieldDescriptor(
      name='ext', full_name='mediapipe.ScaleImageCalculatorOptions.ext', index=0,
      number=66237115, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=True, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  nested_types=[],
  enum_types=[
    _SCALEIMAGECALCULATOROPTIONS_SCALEALGORITHM,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=158,
  serialized_end=935,
)

_SCALEIMAGECALCULATOROPTIONS.fields_by_name['output_format'].enum_type = mediapipe_dot_framework_dot_formats_dot_image__format__pb2._IMAGEFORMAT_FORMAT
_SCALEIMAGECALCULATOROPTIONS.fields_by_name['algorithm'].enum_type = _SCALEIMAGECALCULATOROPTIONS_SCALEALGORITHM
_SCALEIMAGECALCULATOROPTIONS.fields_by_name['input_format'].enum_type = mediapipe_dot_framework_dot_formats_dot_image__format__pb2._IMAGEFORMAT_FORMAT
_SCALEIMAGECALCULATOROPTIONS_SCALEALGORITHM.containing_type = _SCALEIMAGECALCULATOROPTIONS
DESCRIPTOR.message_types_by_name['ScaleImageCalculatorOptions'] = _SCALEIMAGECALCULATOROPTIONS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScaleImageCalculatorOptions = _reflection.GeneratedProtocolMessageType('ScaleImageCalculatorOptions', (_message.Message,), {
  'DESCRIPTOR' : _SCALEIMAGECALCULATOROPTIONS,
  '__module__' : 'mediapipe.calculators.image.scale_image_calculator_pb2'
  # @@protoc_insertion_point(class_scope:mediapipe.ScaleImageCalculatorOptions)
  })
_sym_db.RegisterMessage(ScaleImageCalculatorOptions)

_SCALEIMAGECALCULATOROPTIONS.extensions_by_name['ext'].message_type = _SCALEIMAGECALCULATOROPTIONS
mediapipe_dot_framework_dot_calculator__options__pb2.CalculatorOptions.RegisterExtension(_SCALEIMAGECALCULATOROPTIONS.extensions_by_name['ext'])

# @@protoc_insertion_point(module_scope)
