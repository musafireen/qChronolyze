from .imports import widg
# from backend.database.schemas.strObjClass import strObjClass
from .sortChron import sortchron
from ..shared.constants import lng2InpSchD


def finish_query_f(button,container=widg.VBox([]),qL=[],pres='plot',refLng='english',qyArLegSch=lng2InpSchD["arabic"][-1]):
    # qlGetter()
    from ..backend.database.schemas.combClass import CombClass
    # global qL
    print("qyArLegSch in finished query is ",qyArLegSch)
    for k in range(len(container.children)-1,-1,-1):
        optStC = container.children[k].children[1]
        optSt = []
        for l in range(len(optStC.children)-1,-1,-1):
            combC = optStC.children[l]
            if not len(combC.children) < 2:
                wrdDisFld = combC.children[0].children[0]
                qyLblFld = combC.children[0].children[1]
                # print(wrdDisFld.description, wrdDisFld.value)
                # combObj = combClass()
                CombClass.wrdDisSt = wrdDisFld.value
                CombClass.strLSt = []
                # combObj = {"strL":[],"wrdDis":wrdDisFld.value}
                for i in range(len(combC.children)-1,0,-1):
                    strCs = combC.children[i]
                # for strObj in comb.children:
                    # print('\n', strCs)
                    strCFlds = strCs.children
                    # print(strCFlds)
                    strAtts = ["stri","flt","strTyp","poSp","frm","inpLng","inpSch"]
                    # if True:
                    # strD = strObjClass()
                    strD = {}
                    # if strCFlds[0].value != '' or strCFlds[1].value != '':
                    if strCFlds[0].value != '':
                        # for j in range(7):
                        #     fld = strCFlds[j]
                        #     # print(fld.description, fld.value)
                        #     # print(strD[strAtts[j]], fld.value)
                        #     # strD.strObj[strAtts[j]] = fld.value
                        #     strD[strAtts[j]] = fld.value
                        # print(strD)
                        # print(strD.strObj)
                        # combObj.strL.append(strD.strObj)
                        # combObj["strL"].append(strD)
                        CombClass.strLSt.append(
                            # strObjClass(
                            #     stri=strCFlds[0].value,
                            #     flt=strCFlds[1].value,
                            #     strTyp=strCFlds[2].value,
                            #     poSp=strCFlds[3].value,
                            #     frm=strCFlds[4].value,
                            #     inpLng=strCFlds[5].value,
                            #     inpSch=strCFlds[6].value,
                            # )
                            {
                                "stri" :strCFlds[0].value,
                                "flt":strCFlds[1].value,
                                "strTyp":strCFlds[2].value,
                                "poSp":strCFlds[3].value,
                                "frm":strCFlds[4].value,
                                "inpLng":strCFlds[5].value,
                                "inpSch":strCFlds[6].value,
                                "wrdDisPos":strCFlds[7].value,
                                "wrdDisNeg":strCFlds[8].value,
                                "strUnwanted":strCFlds[9].value,
                            }
                        )
                        # print(f"combClass.strLSt: {combClass.strLSt}")
                # if len(combObj["strL"]) > 0:
                if len(CombClass.strLSt) > 0:
                    # print(f"combClass.strL while appending to optSt: {combClass.strLSt}")
                    # print(f"optSt before appending comb:{optSt}")
                    optSt.append(CombClass(lbl=qyLblFld.value,qyArLegSch=qyArLegSch))
                    # print(f"comb.strL appended to optSt: {optSt[-1].strL}")
                    # print(f"optSt after appending comb:{optSt}")
            if len(optSt) > 0:
                # print(f"qL before appending optSt:{qL}")
                qL.append(optSt)
                # print(f"qL after appending optSt:{qL}")
                # qL.append(combObj.__dict__)
        # dg = aggregLsts(qL)
        # sortchron(dg)
    
    ## can't figure out why i put it outside the outermost for loop
    sortchron(qL,pres=pres,refLng=refLng)
        # return qL
        # return dg
