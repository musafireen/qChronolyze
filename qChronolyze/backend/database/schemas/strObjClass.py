from ....shared.constants import sameVrsIndicator, lngL, lngD, lng2InpSchD, inpLngSchD
from ...utils.rtTrns import rtTrns

class StrObjClass:
    # idx = 0
    wrdDisPosSt = sameVrsIndicator
    wrdDisNegSt = -sameVrsIndicator
    strUnwantedSt = False
    # parentIdx = 1
    striSt = ''
    fltSt=''
    # strTypSt='root'
    strTypSt='All'
    frmSt='All'
    poSpSt='All'
    inpLngSt=lngL[0]
    inpSchSt=lng2InpSchD["arabic"][0]
    inpSchArSt=lng2InpSchD["arabic"][1]


    def __init__(self,                
                stri = striSt,
                flt = fltSt,
                strTyp = None,
                frm = None,
                poSp = None,
                inpLng = None,
                inpSch = None ,
                strUnwanted=False,
                wrdDisPos=sameVrsIndicator,
                wrdDisNeg=-sameVrsIndicator,
                qyArLegSch = None,
                # stri = striSt,
                # flt = fltSt,
                # strTyp = strTypSt,
                # frm = frmSt,
                # poSp = poSpSt,
                # inpLng = inpLngSt,
                # inpSch = inpSchSt ,
                #  strSt=strObjStClass()
                #  **kwargs
                ):
        
        # print(
        #     "args in str init: ",
        #     "stri: ", stri,
        #     "flt:", flt,
        #     "strTyp:", strTyp,
        #     "frm:", frm,
        #     "poSp:", poSp,
        #     "inpLng:", inpLng,
        #     "inpSch:", inpSch,
        # )
        qyArLegSch = lng2InpSchD["arabic"][-1] if qyArLegSch == None else qyArLegSch
        wrdDisPos = self.wrdDisPosSt if (wrdDisPos == sameVrsIndicator or wrdDisPos == None) else wrdDisPos
        self.wrdDisPos = wrdDisPos
        wrdDisNeg = self.wrdDisNegSt if (wrdDisNeg == -sameVrsIndicator or wrdDisNeg == None) else wrdDisNeg
        self.wrdDisNeg = -self.wrdDisPos if (wrdDisNeg == -sameVrsIndicator and self.wrdDisPos != sameVrsIndicator) else wrdDisNeg
        self.stri = stri
        self.flt = flt
        self.strTyp = strTyp if strTyp != None else self.strTypSt
        self.frm = frm if frm != None else self.frmSt
        self.poSp = poSp if poSp != None else self.poSpSt
        self.inpLng = inpLng if inpLng != None else self.inpLngSt
        self.inpSch = inpSch if inpSch != None else self.inpSchSt
        self.strUnwanted = strUnwanted
        wrdDisYes = wrdDisPos != sameVrsIndicator
        self.strLbl = (
            "-" if self.strUnwanted == True else ''
            ) + (
                    f'<{str(self.wrdDisPos)}' if wrdDisYes else ''
                ) + (
                    f',{str(self.wrdDisNeg)}' if self.wrdDisNeg != -self.wrdDisPos and wrdDisYes else ""
                ) + ('>' if wrdDisYes else '') + rtTrns(
                    self.stri,
                    lngD[self.inpLng],
                    inpLngSchD[self.inpSch],
                    # "bkwSch",
                    outSch=inpLngSchD[self.inpSch]
                    if self.strTyp == "stem" 
                    else inpLngSchD[qyArLegSch] 
                    # outSch="arbSch"
                    if self.inpLng == "arabic" 
                    else None
                # f'{strObj["stri"]} ({strObj["flt"]})' for 
                ) + (f" {self.frm}" if self.strTyp == 'root' and self.frm != 'All' else '') + (f" ({self.flt})" if self.flt != '' else '')
        # self.strObj = {
        #     "stri": stri,
        #     "flt": flt,
        #     "strTyp": strTyp,
        #     "frm": frm,
        #     "poSp": poSp,
        #     "inpLng": inpLng,
        #     "inpSch": inpSch,
        # }
        # print(
        #     "props set in str init: ",
        #     "stri: ", self.stri,
        #     "flt:",self.flt,
        #     "strTyp:", self.strTyp,
        #     "frm:", self.frm,
        #     "poSp:", self.poSp,
        #     "inpLng:", self.inpLng,
        #     "inpSch:", self.inpSch,
        # )
        # print(
        #     self.stri,
        #     self.flt,
        #     self.strTyp,
        #     self.frm,
        #     self.poSp,
        #     self.inpLng,
        #     self.inpSch,
        # )