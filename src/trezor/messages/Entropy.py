# Automatically generated by pb2py
import protobuf as p


class Entropy(p.MessageType):
    MESSAGE_WIRE_TYPE = 10
    FIELDS = {
        1: ('entropy', p.BytesType, 0),  # required
    }

    def __init__(
        self,
        entropy: bytes = None
    ) -> None:
        self.entropy = entropy
