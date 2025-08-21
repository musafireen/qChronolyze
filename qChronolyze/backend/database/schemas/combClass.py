from ....shared.constants import sameVrsIndicator, lngL, lngD, lng2InpSchD, inpLngSchD
# from backend.utils import rtTrns

from .strObjClass import StrObjClass

class CombClass:
    strLSt = []
    wrdDisSt = sameVrsIndicator
    # combObjSt = {
    #     "strL": [],
    #     "wrdDis": 0,
    # }
    def __init__(
            self,strL=[],
            wrdDis=sameVrsIndicator,
            qyArLegSch=None,lbl=''
    ):
    #   global strObjClass
      # print(combsLsA)
      strL = self.strLSt if (strL==[] or strL==None) else strL
      wrdDis = self.wrdDisSt if (wrdDis == sameVrsIndicator or wrdDis == None) else wrdDis
      self.wrdDis = wrdDis
      # print(strL)
      # for strObj in [{"stri":"EiysaY"}]:
      #     print(strObjClass(strObj).strObj)
    #   print([strObjClass(**strObj).strObj for strObj in strL ])
    #   print(f"strLSt in comb init: {self.strLSt}")
    #   print(f"strL in comb init: {strL}")
    #   self.strL = [ strObjClass(**strObj).strObj for strObj in strL  ]
    #   self.strL = [ strObjClass(**strObj) for strObj in self.strLSt  ]
      qyArLegSch = lng2InpSchD["arabic"][-1] if qyArLegSch == None else qyArLegSch
    #   print("qyArLegSch is ",qyArLegSch)
      self.strL = [ 
            StrObjClass(**strObj,qyArLegSch=qyArLegSch) if strObj==strL[0]  
            else StrObjClass(wrdDisPos=wrdDis,**strObj,qyArLegSch=qyArLegSch) if ("wrdDisPos" not in strObj.keys()) 
            else StrObjClass(**strObj,qyArLegSch=qyArLegSch)
            for strObj in strL  
        ]

    #   fltJoin =   ' '.join([ 
    #                     strObj.flt for 
    #                     # f'{strObj["stri"]} ({strObj["flt"]})' for 
    #                     strObj 
    #                     in self.strL
    #                 ]) 
    #   striJoin = ' '.join([ 
    #             rtTrns(
    #                 strObj.stri,
    #                 lngD[strObj.inpLng],
    #                 inpLngSchD[strObj.inpSch],
    #                 # "bkwSch",
    #                 outSch=inpLngSchD[qyArLegSch] 
    #                 # outSch="arbSch"
    #                 if strObj.inpLng == "arabic" 
    #                 else None
    #             # f'{strObj["stri"]} ({strObj["flt"]})' for 
    #             ) for strObj 
    #             in self.strL
    #         ])
    #   self.lbl = lbl if lbl != '' else striJoin + (
    #             f" ({fltJoin})" if len(fltJoin) > (len(self.strL)-1) else ''
    #         ) + (
    #             '-' if wrdDis == -1 else '' if wrdDis == sameVrsIndicator else f'<{str(wrdDis)}>'
    #         )
      self.lbl = ' '.join([
          strObj.strLbl for strObj in self.strL
      ])
    #   print(f"strL in comb after str obj: {self.strL}")
    #   print([strObjClass(**strObj).strObj for strObj in self.strL ])
      # for strObj in strL:
      #     self.strL.append(strObjClass(strObj))
    #   self.combObj = {
    #       "strL": self.strL,
    #       "wrdDis": self.wrdDis,
    #   }
