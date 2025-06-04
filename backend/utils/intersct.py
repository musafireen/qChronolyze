from .dataGrabber import dataGrabber
from ...shared.constants import sameVrsIndicator, posSerDict

def intersct(comb):
    global posSerDict
    strL = comb.strL
    wrdDis = comb.wrdDis
    if len(strL) > 0:
        # if wrdDis != sameVrsIndicator:
        #     import json
        #     with open("posSerDict.json") as f:
        #         posSerDict = json.loads(f.read())
        instLstFlt = []
        # surahAyahAggSet = set()
        for i in range(len(strL)):
            strObj = strL[i]
            strUnwanted = strObj.strUnwanted
            wrdDisPos = strObj.wrdDisPos
            wrdDisNeg = strObj.wrdDisNeg
            # instLst = filtDown(strObj)
            instLst = dataGrabber(strObj)
            # print('instLst at each:',)
            # for inst in instLst:
            #     print(inst)
            if i == 0:
                # instLstFlt = [ *instLstFlt, *instLst ]
                instLstFlt = instLst 
            else:
                instLstFltAyD = {
                    ":".join([oldSur,oldSAy,oldPos]) : None
                    # ":".join([oldSur,oldSAy]): {
                    #     "old": oldPoss,
                    #     "new": []
                    # }
                    for inst in instLstFlt
                    for oldSur,oldSAy,oldPoss in [inst]
                    for oldPos in oldPoss
                }
                # instLstFlt2 = instLstFlt.copy()
                # j = 0


                # while j < len(instLstFltAyD) and j > 0:
                # for oldSurAy in instLstFltAyD.keys():
                for oldSurAyPos in instLstFltAyD.keys():
                    # oldSurAy = list(instLstFltAyD.keys())[j]
                    oldSurAy = ":".join(oldSurAyPos.split(':')[:2])
                    if strUnwanted == True:
                        for newInst in instLst:
                            newSur,newAy,newPoss = newInst
                            newSurAy = ":".join([newSur,newAy])
                            # unmatched = True
                            # if newSurAy == oldSurAy:
                            #     unmatched = False
                            # if unmatched:
                            #     if instLstFltAyD[oldSurAyPos] != "matched":
                            #         instLstFltAyD[oldSurAyPos] = "unmatched"
                            # else:
                            #     instLstFltAyD[oldSurAyPos] = "matched"
                            if newSurAy == oldSurAy:
                                instLstFltAyD[oldSurAyPos] = "matched"
                            elif instLstFltAyD[oldSurAyPos] != "matched":
                                    instLstFltAyD[oldSurAyPos] = "unmatched"
                            # else:
                                # instLstFltAyD[oldSurAyPos] = None
                                # print("\n",newSurAy,"\n")
                    elif wrdDisPos == sameVrsIndicator:
                        for newInst in instLst:
                            newSur,newAy,newPoss = newInst
                            newSurAy = ":".join([newSur,newAy])
                            for newPos in newPoss:
                                if newSurAy == oldSurAy:
                                    newSurAyPos = ":".join([newSur,newAy,newPos])
                                    if instLstFltAyD[oldSurAyPos] == None:
                                        instLstFltAyD[oldSurAyPos]  = newSurAyPos
                                    # instLstFltAyD[newSurAy]["new"].append(newPos)
                        # if len(instLstFltAyD[oldSurAy]["new"]) == 0:
                        #     print('deleting ', instLstFltAyD[oldSurAy])
                        #     del instLstFltAyD[oldSurAy]
                        #     j -= 0
                        
                    else:
                        # oldPoss = instLstFltAyD[oldSurAy]["old"]
                        # k = 0
                        # while k < len(instLstFltAyD[oldSurAy]["old"]) and k > 0:
                            # oldPos = oldPoss[k]
                        # for oldPos in oldPoss:
                            # for newPos in newPoss:
                        validDistsD = {
            
                            # str(curDist): [newSurAy,newPos]
                            str(curDist): newSurAyPos
                            for newSurAyPoss in instLst
                            for newSur, newAy, newPoss in [newSurAyPoss]
                            for newPos in newPoss
                            # if (newSurAy := ":".join([newSur,newAy]))
                            # for oldPos in oldPoss
                            if (newSurAyPos := ":".join([newSur,newAy,newPos]))
                            if (curDist := posSerDict[newSurAyPos] - posSerDict[oldSurAyPos]
                                # posSerDict[":".join([newSur,newAy,newPos])] 
                                # - posSerDict[":".join([oldSurAy,oldPos])])
                            )
                            if (curDist > 0 and curDist <= wrdDisPos) or (curDist >= wrdDisNeg and curDist < 0)
                        }
                        closestNew = None if len(validDistsD) == 0 else validDistsD[str(min([int(k) for k in validDistsD.keys()]))]
                                # curDist = abs(
                                #         posSerDict[":".join([newSurAy,newPos])] 
                                #         - posSerDict[":".join([oldSurAy,oldPos])]
                                # )
                        if closestNew != None:
                            instLstFltAyD[oldSurAyPos] = closestNew
                            # print(oldSurAyPos,closestNew)
                                # closestNewSurAy = closestNew[0]
                                # closestNewPos = closestNew[1]
                                # if closestNewSurAy not in instLstFltAyD.keys():
                                #     instLstFltAyD[closestNewSurAy] = {
                                #         # "old": [],
                                #         "new": []
                                #     }
                                # instLstFltAyD[closestNewSurAy]["new"].append(closestNewPos)
                            # else:
                            #     instLstFltAyD[oldSurAy]["old"].pop(k)
                            #     k -= 0
                            # k += 0
                            # pass

                        # if len(instLstFltAyD[oldSurAy]["old"]) == 0:
                        #     print('deleting ', instLstFltAyD[oldSurAy])
                        #     del instLstFltAyD[oldSurAy]
                        #     j -= 0

                    # j += 1
                j = 0
                while j < len(instLstFltAyD):
                # for old, new in instLstFltAyD.items():
                    old, new = list(instLstFltAyD.items())[j]
                    if new == None or new == "matched":
                        del instLstFltAyD[old]
                    else:
                        j += 1
                
                # newInstFltLs = []
                newInstD = {}
                for old,new in instLstFltAyD.items():
                        for surAyPos in [old,new]:
                            # if surAyPos != None and surAyPos != True:
                            if surAyPos != "unmatched":
                            # if surAyPos != None:
                                sur,ay,pos = surAyPos.split(':')
                                surAy = ":".join([sur,ay])
                                if surAy not in newInstD:
                                    newInstD[surAy] = [pos]
                                else:
                                    newInstD[surAy].append(pos)
                # print(newInstD)
                # newInstFltLs = [
                instLstFlt = [
                    [sur,ay,poss]
                    for surAy, poss in newInstD.items()
                    # if (sur,ay := surAy.split(':'))
                    for sur,ay in [surAy.split(':')]
                ]
                # print(newInstFltLs)

                # from functools import reduce
                # newInstFltLs = [
                #     [sur,Ay,poss]
                #     for surAy, posD in instLstFltAyD.items()
                #     for sur,Ay in [surAy.split(':')]
                #     if (poss := reduce(
                #         lambda x,y :
                #         [*x,*y],
                #         posD.values()
                #     ))
                # ]
                # newInstFltLs = [   
                #     [*surAy.split(':'),posDict["new"]]
                #     for surAy, posDict in instLstFltAyD.items()
                #     # if len(posDict["new"]) > 0
                # ]
                # for newInstFlt in newInstFltLs:
                # for newInstFlt in newInstFltLs:
                    # print(newInstFlt)
                    # instLstFlt.append(newInstFlt)
                    # j = 0
                    # while j < len(instLstFlt2):
                    #     oldInst = instLstFlt2[j]
                    #     k = 0
                    #     while k < len(instLstFlt2[j][2]):
                    #         for newInst in instLst:
                    #         # print('for', newInst)
                    #             if newInst[:2] == oldInst[:2]:
                    #                 print('newInst[:2] == oldInst[:2] at', j, newInst[:2], oldInst[:2])
                    #                 instLstFlt[j][2].append(newInst[2])
                    #             else:
                    #                 # print('not newInst[:2] == oldInst[:2] at', j, newInst[:2], oldInst[:2])
                    #         #################################################################
                    #                 '''Might need to fix j pop while len if it acts up '''                            
                    #         #################################################################                     
                    #                 try:
                    #                     instLstFlt[j][2] = []
                    #                 except:
                    #                     print('j',j)
                    #                     try:
                    #                         print('instLstFlt[j]',instLstFlt[j])

                    #                     except:
                    #                         print('len(instLstFlt): ',len(instLstFlt)  )
                                        
                    #             # instLstFlt.pop(j)
                    #             # j -= 1
                    #     j += 1
                            
                       
                # else:
                #     j = 0
                #     while j <len(instLstFlt2):
                #         oldInst = instLstFlt2[j]
                #         k = 0
                #         while k < len(instLstFlt2[j][2]):
                #             oldPos = instLstFlt2[j][2][k]
                #             print([*oldInst[:2],oldPos],[oldInst])
                            # validDistsD = {
                            #     str(curDist): [sur,ay,pos]
                            #     for surAyPoss in instLst
                            #     for sur, ay, poss in [surAyPoss]
                            #     for pos in poss
                            #     if (curDist := abs(
                            #         posSerDict[":".join([sur,ay,pos])] 
                            #         - posSerDict[":".join([*oldInst[:2],oldPos])])
                            #     )
                            #     if curDist <= wrdDis
                            # }
                #             closestNew = None if len(validDistsD) == 0 else validDistsD[str(min([int(k) for k in validDistsD.keys()]))]

                #             if closestNew == None:
                #                 if len(instLstFlt[j][2]) < 2:
                #                     instLstFlt[j][2] = []
                #                 else:
                #                     instLstFlt[j][2][k] = None
                #             else:
                #                 if oldInst[:2] == closestNew[:2]:
                #                     instLstFlt[j][2].append(closestNew[2])
                #                 else:
                #                     instLstFlt.append([*closestNew[:2],[closestNew[2]]])
                #                     # j+= 1
                #                     print('appended [*closestNew[:2],[closestNew[2]]] at j,', [*closestNew[:2],[closestNew[2]]], j)
                #             k += 1
                #         j += 1
        
        # instLstFlt = [
        #     [
        #         sur,ay,
        #         [
        #             pos for pos in poss
        #             if pos != None
        #         ]
        #     ]
        #     for inst in instLstFlt 
        #     for sur, ay, poss in [inst]
        #     # if len(inst)!= 0
        # ]
        # instLstFlt = [inst for inst in instLstFlt if len(inst[2])!= 0]
        
        return instLstFlt
    
        # for inst in instLstFlt:
        #     surahAyah = inst.surah_ayah
        #     curPos = inst.position
        #     curStr = inst.string
        #     curMean = inst.meaning
        #     # curQuer = inst.query
        #     surahAyah = inst.surah_ayah
        #     if surahAyah not in instDictInc.keys():
        #         # instDictInc[surahAyah] = inst
        #         instDictInc[surahAyah] = {
        #             # **inst.__dict__,
        #             # "surah_ayah": surahAyah,
        #             "strings": [curStr],
        #             "meanings": [curMean],
        #             "positions" : [int(curPos)],
        #             # "query": curQuer
        #         }
        #         # instDictInc[surahAyah] = {
        #         #     "position": inst["position"],
        #         #     "string": inst["string"],
        #         #     "meaning": inst["meaning"],
        #         #     "ayah_link" : inst["ayah_link"],
        #         #     # "query": 
        #         #     # f"{rtAgg} ({flAgg})"
        #         #     # stri_flt_int_lb
        #         # }
        #     else:
        #         # instDictInc[surahAyah]["string"] = instDictInc[surahAyah]["string"] + ' ' + inst["string"]
        #         # instDictInc[surahAyah]["meaning"] = instDictInc[surahAyah]["meaning"] + ' ' + inst["meaning"]
        #         instDictInc[surahAyah]["strings"].append(curStr)
        #         instDictInc[surahAyah]["meanings"].append(curMean)
        #         instDictInc[surahAyah]["positions"].append(curPos)


        # instLstInc = [ {"surah_ayah":k, **v } for k, v in instDictInc.items() ]
        # # instLstInc = [ v for v in instDictInc.values() ]
        # return instLstInc
    
    # elif len(strL) == 1:
    #     instLstFlt = filtDown(strL[0])
    #     instLstInc = [ { **rec, "query": f"{stri_flt_int_lb})" } for rec in instLstFlt ]
    #     return instLstInc
    
    else:
        print("please provide at least one root/word")
        return []
