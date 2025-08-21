
def sAPFin(qL):
    from ...backend.database.schemas.combClass import CombClass
    from ...backend.utils import aggregLsts, qLModder
    if isinstance(qL,list):
        if len(qL) > 0:
            if isinstance(qL[0],list):
                if len(qL[0]) > 0:
                    if not isinstance(qL[0][0], CombClass):
                        qL = qLModder(qL)
    instLstAgg = aggregLsts(qL)
    sAPL = [
        f"{sur_ay}:{pos}"
        for inst in instLstAgg
        if (poss := inst.positions) and (sur_ay := inst.surah_ayah)
        for pos in poss
    ]
    # sAPL = []
    # for inst in instLstAgg:
    #     # print(inst)
    #     # Extract `positions` and `surah_ayah` if they exist
    #     poss = inst.positions
    #     sur_ay = inst.surah_ayah
        
    #     # If both are truthy, construct the pairs
    #     if poss and sur_ay:
    #         for pos in poss:
    #             sAPL.append(f"{sur_ay}:{pos}")
    return sAPL
