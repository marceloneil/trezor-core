# Automatically generated by pb2py
import protobuf as p
from micropython import const
t = p.MessageType('EthereumGetAddress')
t.wire_type = const(56)
t.add_field(1, 'address_n', p.UVarintType, flags=p.FLAG_REPEATED)
t.add_field(2, 'show_display', p.BoolType)
EthereumGetAddress = t