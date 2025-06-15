from ...shared.constants import lng2InpSchD

from ..database.schemas import combClass

def qLModder(qL,qyArLegSch=lng2InpSchD["arabic"][-1]):
    qLMod = [
                # [combClass(**comb).combObj for comb in optLs]
                [combClass(**comb,qyArLegSch=qyArLegSch) for comb in optLs]
                for optLs in qL
            ]
    return qLMod