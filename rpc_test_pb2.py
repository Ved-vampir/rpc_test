# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rpc_test.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc_test.proto',
  package='',
  serialized_pb='\n\x0erpc_test.proto\"\x07\n\x05\x45mpty\"\x1f\n\x0cGetitRequest\x12\x0f\n\x07message\x18\x01 \x02(\t\"\x1e\n\x0bGivemeReply\x12\x0f\n\x07message\x18\x01 \x02(\t2U\n\x0fSomeRemoteClass\x12 \n\x06giveme\x12\x06.Empty\x1a\x0c.GivemeReply\"\x00\x12 \n\x05getit\x12\r.GetitRequest\x1a\x06.Empty\"\x00')




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=18,
  serialized_end=25,
)


_GETITREQUEST = _descriptor.Descriptor(
  name='GetitRequest',
  full_name='GetitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='GetitRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=27,
  serialized_end=58,
)


_GIVEMEREPLY = _descriptor.Descriptor(
  name='GivemeReply',
  full_name='GivemeReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='GivemeReply.message', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=60,
  serialized_end=90,
)

DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['GetitRequest'] = _GETITREQUEST
DESCRIPTOR.message_types_by_name['GivemeReply'] = _GIVEMEREPLY

class Empty(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _EMPTY

  # @@protoc_insertion_point(class_scope:Empty)

class GetitRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GETITREQUEST

  # @@protoc_insertion_point(class_scope:GetitRequest)

class GivemeReply(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _GIVEMEREPLY

  # @@protoc_insertion_point(class_scope:GivemeReply)


import abc
from grpc.early_adopter import implementations
from grpc.early_adopter import utilities
class EarlyAdopterSomeRemoteClassServicer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def giveme(self, request, context):
    raise NotImplementedError()
  @abc.abstractmethod
  def getit(self, request, context):
    raise NotImplementedError()
class EarlyAdopterSomeRemoteClassServer(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def start(self):
    raise NotImplementedError()
  @abc.abstractmethod
  def stop(self):
    raise NotImplementedError()
class EarlyAdopterSomeRemoteClassStub(object):
  """<fill me in later!>"""
  __metaclass__ = abc.ABCMeta
  @abc.abstractmethod
  def giveme(self, request):
    raise NotImplementedError()
  giveme.async = None
  @abc.abstractmethod
  def getit(self, request):
    raise NotImplementedError()
  getit.async = None
def early_adopter_create_SomeRemoteClass_server(servicer, port, root_certificates, key_chain_pairs):
  import rpc_test_pb2
  import rpc_test_pb2
  import rpc_test_pb2
  import rpc_test_pb2
  method_service_descriptions = {
    "getit": utilities.unary_unary_service_description(
      servicer.getit,
      rpc_test_pb2.GetitRequest.FromString,
      rpc_test_pb2.Empty.SerializeToString,
    ),
    "giveme": utilities.unary_unary_service_description(
      servicer.giveme,
      rpc_test_pb2.Empty.FromString,
      rpc_test_pb2.GivemeReply.SerializeToString,
    ),
  }
  return implementations.secure_server(method_service_descriptions, port, root_certificates, key_chain_pairs)
def early_adopter_create_SomeRemoteClass_stub(host, port):
  import rpc_test_pb2
  import rpc_test_pb2
  import rpc_test_pb2
  import rpc_test_pb2
  method_invocation_descriptions = {
    "getit": utilities.unary_unary_invocation_description(
      rpc_test_pb2.GetitRequest.SerializeToString,
      rpc_test_pb2.Empty.FromString,
    ),
    "giveme": utilities.unary_unary_invocation_description(
      rpc_test_pb2.Empty.SerializeToString,
      rpc_test_pb2.GivemeReply.FromString,
    ),
  }
  return implementations.insecure_stub(method_invocation_descriptions, host, port)
# @@protoc_insertion_point(module_scope)