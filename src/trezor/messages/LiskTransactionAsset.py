# Automatically generated by pb2py
import protobuf as p
if __debug__:
    try:
        from typing import List
    except ImportError:
        List = None
from .LiskDelegateType import LiskDelegateType
from .LiskMultisignatureType import LiskMultisignatureType
from .LiskSignatureType import LiskSignatureType


class LiskTransactionAsset(p.MessageType):
    FIELDS = {
        1: ('signature', LiskSignatureType, 0),
        2: ('delegate', LiskDelegateType, 0),
        3: ('votes', p.UnicodeType, p.FLAG_REPEATED),
        4: ('multisignature', LiskMultisignatureType, 0),
        5: ('data', p.UnicodeType, 0),
    }

    def __init__(
        self,
        signature: LiskSignatureType = None,
        delegate: LiskDelegateType = None,
        votes: List[str] = None,
        multisignature: LiskMultisignatureType = None,
        data: str = None
    ) -> None:
        self.signature = signature
        self.delegate = delegate
        self.votes = votes if votes is not None else []
        self.multisignature = multisignature
        self.data = data
