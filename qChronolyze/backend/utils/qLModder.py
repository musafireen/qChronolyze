from ...shared.constants import lng2InpSchD

def qLModder(qL,qyArLegSch=lng2InpSchD["arabic"][-1]):
    from ..database.schemas.combClass import CombClass
    qLMod = [
                # [combClass(**comb).combObj for comb in optLs]
                [CombClass(**comb,qyArLegSch=qyArLegSch) for comb in optLs]
                for optLs in qL
            ]
    return qLMod