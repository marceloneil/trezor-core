# Automatically generated by pb2py
import protobuf as p


class StellarAssetType(p.MessageType):
    FIELDS = {
        1: ('type', p.UVarintType, 0),
        2: ('code', p.UnicodeType, 0),
        3: ('issuer', p.BytesType, 0),
    }

    def __init__(
        self,
        type: int = None,
        code: str = None,
        issuer: bytes = None
    ) -> None:
        self.type = type
        self.code = code
        self.issuer = issuer
