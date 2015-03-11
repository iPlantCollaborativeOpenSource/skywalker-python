#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,utf8strings
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class Provider(object):
  """
  Attributes:
   - uuid
   - name
   - hash
   - options
   - time
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'hash', None, None, ), # 3
    (4, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 4
    (5, TType.I32, 'time', None, None, ), # 5
  )

  def __init__(self, uuid=None, name=None, hash=None, options=None, time=None,):
    self.uuid = uuid
    self.name = name
    self.hash = hash
    self.options = options
    self.time = time

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.options = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString().decode('utf-8')
            _val6 = iprot.readString().decode('utf-8')
            self.options[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.time = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Provider')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.hash is not None:
      oprot.writeFieldBegin('hash', TType.STRING, 3)
      oprot.writeString(self.hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.options is not None:
      oprot.writeFieldBegin('options', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.options))
      for kiter7,viter8 in self.options.items():
        oprot.writeString(kiter7.encode('utf-8'))
        oprot.writeString(viter8.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I32, 5)
      oprot.writeI32(self.time)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.options is None:
      raise TProtocol.TProtocolException(message='Required field options is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.hash)
    value = (value * 31) ^ hash(self.options)
    value = (value * 31) ^ hash(self.time)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Identity(object):
  """
  Attributes:
   - uuid
   - name
   - hash
   - options
   - time
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRING, 'name', None, None, ), # 2
    (3, TType.STRING, 'hash', None, None, ), # 3
    (4, TType.MAP, 'options', (TType.STRING,None,TType.STRING,None), None, ), # 4
    (5, TType.I32, 'time', None, None, ), # 5
  )

  def __init__(self, uuid=None, name=None, hash=None, options=None, time=None,):
    self.uuid = uuid
    self.name = name
    self.hash = hash
    self.options = options
    self.time = time

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.MAP:
          self.options = {}
          (_ktype10, _vtype11, _size9 ) = iprot.readMapBegin()
          for _i13 in xrange(_size9):
            _key14 = iprot.readString().decode('utf-8')
            _val15 = iprot.readString().decode('utf-8')
            self.options[_key14] = _val15
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.time = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Identity')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 2)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.hash is not None:
      oprot.writeFieldBegin('hash', TType.STRING, 3)
      oprot.writeString(self.hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.options is not None:
      oprot.writeFieldBegin('options', TType.MAP, 4)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.options))
      for kiter16,viter17 in self.options.items():
        oprot.writeString(kiter16.encode('utf-8'))
        oprot.writeString(viter17.encode('utf-8'))
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I32, 5)
      oprot.writeI32(self.time)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.options is None:
      raise TProtocol.TProtocolException(message='Required field options is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.hash)
    value = (value * 31) ^ hash(self.options)
    value = (value * 31) ^ hash(self.time)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Instance(object):
  """
  Attributes:
   - uuid
   - machine_uuid
   - name
   - public_addresses
   - private_addresses
   - extra
   - project_id
   - provider_hash
   - identity_hash
   - time
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuid', None, None, ), # 1
    (2, TType.STRING, 'machine_uuid', None, None, ), # 2
    (3, TType.STRING, 'name', None, None, ), # 3
    (4, TType.LIST, 'public_addresses', (TType.STRING,None), None, ), # 4
    (5, TType.LIST, 'private_addresses', (TType.STRING,None), None, ), # 5
    (6, TType.STRING, 'extra', None, None, ), # 6
    (7, TType.STRING, 'project_id', None, None, ), # 7
    (8, TType.STRING, 'provider_hash', None, None, ), # 8
    (9, TType.STRING, 'identity_hash', None, None, ), # 9
    (10, TType.I32, 'time', None, None, ), # 10
  )

  def __init__(self, uuid=None, machine_uuid=None, name=None, public_addresses=None, private_addresses=None, extra=None, project_id=None, provider_hash=None, identity_hash=None, time=None,):
    self.uuid = uuid
    self.machine_uuid = machine_uuid
    self.name = name
    self.public_addresses = public_addresses
    self.private_addresses = private_addresses
    self.extra = extra
    self.project_id = project_id
    self.provider_hash = provider_hash
    self.identity_hash = identity_hash
    self.time = time

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.machine_uuid = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.name = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.public_addresses = []
          (_etype21, _size18) = iprot.readListBegin()
          for _i22 in xrange(_size18):
            _elem23 = iprot.readString().decode('utf-8')
            self.public_addresses.append(_elem23)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.private_addresses = []
          (_etype27, _size24) = iprot.readListBegin()
          for _i28 in xrange(_size24):
            _elem29 = iprot.readString().decode('utf-8')
            self.private_addresses.append(_elem29)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.extra = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.project_id = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.provider_hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.identity_hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.I32:
          self.time = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Instance')
    if self.uuid is not None:
      oprot.writeFieldBegin('uuid', TType.STRING, 1)
      oprot.writeString(self.uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.machine_uuid is not None:
      oprot.writeFieldBegin('machine_uuid', TType.STRING, 2)
      oprot.writeString(self.machine_uuid.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 3)
      oprot.writeString(self.name.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.public_addresses is not None:
      oprot.writeFieldBegin('public_addresses', TType.LIST, 4)
      oprot.writeListBegin(TType.STRING, len(self.public_addresses))
      for iter30 in self.public_addresses:
        oprot.writeString(iter30.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.private_addresses is not None:
      oprot.writeFieldBegin('private_addresses', TType.LIST, 5)
      oprot.writeListBegin(TType.STRING, len(self.private_addresses))
      for iter31 in self.private_addresses:
        oprot.writeString(iter31.encode('utf-8'))
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.extra is not None:
      oprot.writeFieldBegin('extra', TType.STRING, 6)
      oprot.writeString(self.extra.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.project_id is not None:
      oprot.writeFieldBegin('project_id', TType.STRING, 7)
      oprot.writeString(self.project_id.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.provider_hash is not None:
      oprot.writeFieldBegin('provider_hash', TType.STRING, 8)
      oprot.writeString(self.provider_hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.identity_hash is not None:
      oprot.writeFieldBegin('identity_hash', TType.STRING, 9)
      oprot.writeString(self.identity_hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I32, 10)
      oprot.writeI32(self.time)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuid is None:
      raise TProtocol.TProtocolException(message='Required field uuid is unset!')
    if self.machine_uuid is None:
      raise TProtocol.TProtocolException(message='Required field machine_uuid is unset!')
    if self.provider_hash is None:
      raise TProtocol.TProtocolException(message='Required field provider_hash is unset!')
    if self.time is None:
      raise TProtocol.TProtocolException(message='Required field time is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuid)
    value = (value * 31) ^ hash(self.machine_uuid)
    value = (value * 31) ^ hash(self.name)
    value = (value * 31) ^ hash(self.public_addresses)
    value = (value * 31) ^ hash(self.private_addresses)
    value = (value * 31) ^ hash(self.extra)
    value = (value * 31) ^ hash(self.project_id)
    value = (value * 31) ^ hash(self.provider_hash)
    value = (value * 31) ^ hash(self.identity_hash)
    value = (value * 31) ^ hash(self.time)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Instances(object):
  """
  Attributes:
   - instances
   - provider_hash
   - identity_hash
   - time
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'instances', (TType.STRUCT,(Instance, Instance.thrift_spec)), None, ), # 1
    (2, TType.STRING, 'provider_hash', None, None, ), # 2
    (3, TType.STRING, 'identity_hash', None, None, ), # 3
    (4, TType.I32, 'time', None, None, ), # 4
  )

  def __init__(self, instances=None, provider_hash=None, identity_hash=None, time=None,):
    self.instances = instances
    self.provider_hash = provider_hash
    self.identity_hash = identity_hash
    self.time = time

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.LIST:
          self.instances = []
          (_etype35, _size32) = iprot.readListBegin()
          for _i36 in xrange(_size32):
            _elem37 = Instance()
            _elem37.read(iprot)
            self.instances.append(_elem37)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.provider_hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.identity_hash = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.time = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Instances')
    if self.instances is not None:
      oprot.writeFieldBegin('instances', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.instances))
      for iter38 in self.instances:
        iter38.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.provider_hash is not None:
      oprot.writeFieldBegin('provider_hash', TType.STRING, 2)
      oprot.writeString(self.provider_hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.identity_hash is not None:
      oprot.writeFieldBegin('identity_hash', TType.STRING, 3)
      oprot.writeString(self.identity_hash.encode('utf-8'))
      oprot.writeFieldEnd()
    if self.time is not None:
      oprot.writeFieldBegin('time', TType.I32, 4)
      oprot.writeI32(self.time)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.instances is None:
      raise TProtocol.TProtocolException(message='Required field instances is unset!')
    if self.provider_hash is None:
      raise TProtocol.TProtocolException(message='Required field provider_hash is unset!')
    if self.time is None:
      raise TProtocol.TProtocolException(message='Required field time is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.instances)
    value = (value * 31) ^ hash(self.provider_hash)
    value = (value * 31) ^ hash(self.identity_hash)
    value = (value * 31) ^ hash(self.time)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class OpenStackException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('OpenStackException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class ConnectionException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('ConnectionException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class DeployException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString().decode('utf-8')
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('DeployException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message.encode('utf-8'))
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.message is None:
      raise TProtocol.TProtocolException(message='Required field message is unset!')
    return


  def __str__(self):
    return repr(self)

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.message)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
