from ...shared.constants import arbSch2bkwSch, bkwSch2arbSch, iasSch2arbSch, bkwSch2iasSch, bkw2Ala, bkw2Simpl, arbBen2arbSch, arbBen2bkwSch, arbBenSimp2arbSch, arbBenSimp2bkwSch
from ...shared.constants import bkw2Ben, bkw2SimpBen


def rtTrns(rt,inpLng,inpSch,outSch=None):
    # print(outSch)
    lngSts = {
        "arb": "bkwSch",
        # "arb": "arbSch",
        "eng": "engSch",
        "bng": "bngSch"
    }

    global arbSch2bkwSch
    global bkwSch2arbSch
    global iasSch2arbSch
    global bkwSch2iasSch

    lngDefOutLs = {
        # "arb": "arbSch",
        "arb": "bkwSch",
        "eng": "engSch",
    }

    chrOut = {
        "arb": {
            "bkwSch": {
                "arbSch": bkwSch2arbSch,
                "bkwSch": None,
                "alaSch": bkw2Ala,
                "simplSch": bkw2Simpl,
                "arbBenSch": bkw2Ben,
                "arbBenSimpSch": bkw2SimpBen,
            },
            "iasSch": {
                "arbSch": iasSch2arbSch,
                "iasSch": None
            },
            "arbSch": {
                "bkwSch": arbSch2bkwSch,
                "arbSch": None,
                "alaSch": None, # arb2Ala,
                "simplSch": None, # arb2Simpl,
            },
            "arbBenSch": {
                "arbSch": arbBen2arbSch,
                "bwkSch": arbBen2bkwSch,
            },
            "arbBenSimpSch": {
                "arbSch": arbBenSimp2arbSch,
                "bwkSch": arbBenSimp2bkwSch,
            },
        },
        "eng": {
            "engSch": {
                "engSch": None,
            },
            
        },
        "bng": {
            "bngSch": {
                "bngSch":None
            }
        },
    }

    chrTrnsTbl = None if inpSch == outSch else chrOut[inpLng][inpSch][outSch] if outSch != None else chrOut[inpLng][inpSch][lngDefOutLs[inpLng]]
    # print(chrTrnsTbl)
    rtTrn = ''
    # print("\n",inpSch,outSch,"\n")
    if (chrTrnsTbl != None):
        if outSch == 'alaSch' or outSch == 'simplSch':
            import re
            rtTrn = rt
            for chTrns in chrTrnsTbl:
                try:
                    rtTrn =re.sub(
                        chTrns[0],
                        chTrns[1],
                        rtTrn,
                    )
                except:
                    print(chTrns)
            rtTrn = rtTrn.capitalize()
        else:
            for chr in rt:
                if chr in chrTrnsTbl.keys():
                    chrTrns = chrTrnsTbl[chr]
                else:
                    chrTrns = chr
                rtTrn += chrTrns
            # print("language schema is present\ncharacter transform: ", chrTrns)
    else:
        rtTrn = rt
    
    return rtTrn
