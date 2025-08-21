from .rtTrns import rtTrns
from ...shared.constants import poSpD, lngD, strTypD, inpLngSchD, arbVwlsDict, surAyPosStrAdvWrdMD

def dataGrabber(strObj):
    flt = str(strObj.flt).lower()
    frm = strObj.frm
    strTyp = strObj.strTyp if strObj.strTyp in strTypD.values() else strTypD[strObj.strTyp]
    poSp = strObj.poSp if strObj.poSp in poSpD.values() else poSpD[strObj.poSp]
    inpLng = strObj.inpLng if strObj.inpLng in lngD.values() else lngD[strObj.inpLng]
    inpSch = strObj.inpSch if strObj.inpSch in inpLngSchD.values() else inpLngSchD[strObj.inpSch]
    stri = rtTrns(strObj.stri,inpLng,inpSch,) if inpLng == "arb" else strObj.stri.lower() if inpLng == 'eng' else strObj.stri
    isNotRoot = True if (any(char in stri for char in arbVwlsDict.values()) and inpLng == "arb" ) else False

    strArbSch = None if inpLng != "arb" else rtTrns(stri,"arb","bkwSch","arbSch")

    # print(stri,strTyp,frm,flt,poSp,isNotRoot,inpLng,inpSch)

    instLst = []
    import re

    for sur, ayD in surAyPosStrAdvWrdMD.items():
        for ay, posD in ayD.items():
            # surAy = ":".join([sur,ay])
            inst = [sur,ay,[]]

            for pos, wrdStrD in posD.items():
                if inpLng == "eng":
                    import re
                    engStrFound = re.findall(
                        "(?<![a-zA-Z])"
                        +
                        stri
                        +
                        "(?![a-rt-zA-RT-Z])"
                        ,
                        wrdStrD["mean"].lower()
                    )
                    engFltFound = []
                    if len(flt.strip()) > 0:
                        engFltFound = re.findall(
                            "(?<![a-zA-Z])"
                            +
                            flt
                            +
                            "(?![a-rt-zA-RT-Z])"
                            ,
                            wrdStrD["mean"].lower()
                        )
                    if len(engStrFound) > 0 or (len(engFltFound)>0):
                        if pos not in inst[2]:
                            inst[2].append(pos)
                elif inpLng == "arb":

                    curMean = wrdStrD["mean"].lower()
                    # mean = wrdStrD["mean"]
                    
                    if strTyp == "stem":
                        # wrdNV = remVwls(wrdStrD["wrd"],"arbSch").replace('_','')
                        # strArbSchNV = remVwls(strArbSch,"arbSch")
                        # wrdNV = wrdStrD["wrd"].replace('ـ','')
                        # strArbSchNV = strArbSch
                        # stemInWrd = strArbSchNV in wrdNV
                        wrdBkw = rtTrns(
                            wrdStrD["wrd"].replace('ـ',''),
                            "arb", "arbSch", "bkwSch"
                        )
                        stemInWrd = len(re.findall(stri, wrdBkw)) > 0
                        # print("at least got stem", strArbSch, strArbSchNV, wrdNV, stemInWrd)
                    
                    poSpMatch = True
                    frmMatch = True
                    strTypMatch = False
                    strMatch = False
                    fltMatch = False

                    for strD in wrdStrD["striDLs"]:
                        if strTyp == "stem":
                            strTypMatch = True
                            # poSpOnward(inst,curMean,strD,poSp,frm,flt)
                            if stemInWrd:
                                # print(wrdNV, strArbSchNV)
                                # poSpOnward(instD,wrdStrD,strD,poSp,frm,flt)
                                # poSpOnward(inst,curMean,strD,poSp,frm,flt)
                                strMatch = True
                        else:
                            # if strTyp == "stem":
                            #     # if remVwls(strD["stri"]) in remVwls(stri) or stemInWrd:
                            #     if remVwls(strD["stri"]) in remVwls(stri) or stemInWrd:
                            #         # poSpOnward(instD,wrdStrD,strD,poSp,frm,flt)
                            #         poSpOnward(inst,curMean,strD,poSp,frm,flt)
                            
                                # print(strD["stri"],stri)
                                if strD["strTyp"] == "All" or strTyp == 'All' or strD["strTyp"] == strTyp:
                                    if not (strD["strTyp"] == 'root' and strTyp == 'All' and isNotRoot == True):
                                        # poSpOnward(inst,curMean,strD,poSp,frm,flt)
                                        # pass
                                        strTypMatch = True
                                if strD["stri"] == stri:
                                    strMatch = True

                    # def poSpOnward(inst,curMean,strD,poSp,frm,flt):
                        if poSp != "All" and (strD["poSp"] != "All" and strD["poSp"] != poSp):
                            poSpMatch = False
                        if frm != "All" and (strD["frm"] != "All" and strD["frm"] != frm):
                            frmMatch = False
                        if ( 
                            flt == '' or
                            len(
                                re.compile(str(flt)).findall(
                                    # wrdStrD["mean"].lower()
                                    curMean
                                )
                            ) > 0 
                            or len(
                                re.compile(str(stri)).findall(
                                    # wrdStrD["mean"].lower()
                                    curMean
                                ) 
                            ) > 0 
                        ):
                            fltMatch = True
                                # inst[3].append(mean)

                    if (poSpMatch and frmMatch and strTypMatch and strMatch and fltMatch):
                        if pos not in inst[2]:
                            inst[2].append(pos)

            
            if len(inst[2]) > 0:
                instLst.append(inst)

    return instLst
