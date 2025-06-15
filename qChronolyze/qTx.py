# from qChronolyze import filtDown, getSorter
import ipywidgets as widg
from ipywidgets import interactive as intct
import re
from IPython.display import display, clear_output
from qChronolyze import refLngD, lng2InpSchD, tafsDict, surAyPosStrAdvWrdMD
from qChronolyze import aggregLsts, getSorter, combClass, optStWdgCl, confFcheck

def qChronoTx(dicti,flnm,refLng,qyArLegSch=lng2InpSchD["arabic"][1]):
    # instLstAgg = []   
    # tafsDict={"arabic":"tfTb","bengali":"tfKthB","english":"tfKthE"}
    tafs = tafsDict[refLng]
    alreadyRefed = []
    dicti = [
        [combClass(**comb,qyArLegSch=qyArLegSch) for comb in optLs]
        for optLs in dicti
    ]
    instLstAgg = aggregLsts(dicti,tafs)

    import pandas as pd

    df = pd.DataFrame(instLstAgg)
    sorter = getSorter()
    df = pd.DataFrame([obj.__dict__ for obj in instLstAgg],columns = ["surah_ayah","positions","strings","meanings","ayah_link","query"])
    # df['position'] = df['position'].astype('int')
    df['surah_ayah'] = pd.Categorical(df['surah_ayah'], categories=sorter, ordered=True)
    # df.sort_values(["surah_ayah","position"],inplace=True)
    df.sort_values(
        ["surah_ayah","positions"],
        key=lambda x: x.map(min) if x.name=='positions' else x,
        inplace=True
    )
    # df.reset_index(drop=True,inplace=True)
    sortedRecs = df.to_dict(orient='records')


    newDic = {}

    frstAys = {}

    with open(f"data/ref/Qrsi.md") as f:
        qTxt = f.read()

    import re

    vrSs = re.findall(
        "\n### (\d*:\d*)\s*\n{1,}"
        # +"(\[Q\.\d*\:\d*\]\(\[^\n]*\))\n{1,}"
        +"([^#a-zA-Z]{1,})\n{1,}"
        +"([^#]*(?=\n#|$))", 
        qTxt, 
        re.DOTALL
    )

    vrsDict = { 
        ser: {
            # "lnk": Lnk,
            "arb": vrsArb,
            "eng": vrsEng,
        }
        for ser, 
        # Lnk, 
        vrsArb, vrsEng in vrSs 
    }

    for rec in sortedRecs:
        surAy = rec["surah_ayah"]
        sur,ay = surAy.split(":")
        poss = rec["positions"]
        # pos = int(rec["position"])
        vrsRec = vrsDict[surAy]
        # vrsLnk = vrsRec["lnk"]
        # vrsArb = vrsRec["arb"].strip("\n").strip(" ")
        vrsEng = vrsRec["eng"]
        # vrsWrds = vrsArb.split(" ")
        vrsArbMod = " ".join([
            posD["wrd"] if int(pos) not in poss else f'***{posD["wrd"]}***'
            for pos, posD in surAyPosStrAdvWrdMD[sur][ay].items()
        ])
        # vrsArbMod = " ".join(vrsWrds[:pos-1]) + "***" + vrsWrds[pos-1] + "***" + " ".join(vrsWrds[pos:])
        if surAy not in newDic.keys():
            newDic[rec["surah_ayah"]] = {
                'string': f'\n[Q.{rec["surah_ayah"]}](https://quran.com/{surAy}/tafsirs/{tafs})\n'
                            + f'\n{vrsArbMod}\n{vrsEng}\n',
                # 'queries': [
                #     {
                #         'query': rec["query"],
                #         'postquery': ''
                #     }
                # ]
                'queries': {
                    rec["query"]: '\n\n'
                }
            }
        else:
            # newDic[rec["surah_ayah"]]["queries"].append(
            #     {
            #         'query': rec["query"], 
            #         'postquery': '',
            #     }
            # )
            newDic[surAy]["queries"][rec["query"]] = '\n\n'



    # print('\nnewDic before checking md: ', newDic, '\n')

    mdFile = f'data/compare/{flnm}.md'
    import os

    if os.path.isfile(mdFile):
        # import re

        with open(mdFile) as f:
            strn = f.read()

        olds = re.compile(
                '\n#\s*'
                +'(?:Q\:){0,1}'
                +'(\d{1,}\:\d{1,})'
                +'(.*?(?=\n#|$))'
                # +'(?:'
                +'(\n##\s{1,}.'
                +'*?'
                +'(?=\n#\s{1,}|$)'
                # +')'
                +'){0,1}'
                ,
                re.DOTALL
            ).findall(

            strn
        )


        # print(len(rep))

        oldSurAyLs = [x[0] for x in olds]

        # print(f'\nold surAy list: {oldSurAyLs}\n\nnew surAy list: {newDic.keys()}\n')

        j = 0
        for nk in newDic.keys():
            if nk not in oldSurAyLs:
                j+=1
                print(f'new not in old {j}: {nk}')
        
        i = 0

        def findSec(queriesOld):
            secondaries = re.findall(
                # '((?<=\n)##\s{1,}[^\n]*\n*)'
                '(?<=\n)##\s{1,}([^\n]*(?=\n))\n*'
                +'((?:\n*1st inst\: \[\[[^\n]*\]\]\n*){0,1})'
                +'((?:(?!1st inst:|(?<=\n)## ).)*?'
                # +'(^(?!1st inst\:)[^#]'
                # +'(.*'
                +'(?=\n## |$)*$'
                +')',
                queriesOld,
                re.DOTALL,
            )

            return secondaries
        

        for old in olds:
            surAyOld = old[0]
            primaryOld = old[1]
            queriesOld = old[2]
            if surAyOld not in newDic.keys():
                secondaries = findSec(queriesOld)
                
                queryContents = "".join([queryCont[2].replace('\n','').replace('\s','') for queryCont in secondaries])

                isQueryContent = len(queryContents) > 0 
                
                if isQueryContent:
                    print(f"for {surAyOld} secondaries: ", secondaries)
                    newDic[surAyOld] = { 
                        'string' : primaryOld , 
                        'queries': {
                            secondary[0]: secondary[2]
                            for secondary in secondaries
                            # quer[0]: quer[1]
                            
                            
                            # quer
                            # for quer in re.compile(
                            #     '\n##\s{1,}'
                            #     +'([^\n]{1,}(?=\n))'
                            #     +'(.*?(?=\n#|$))'
                            #     ,    
                            #     re.DOTALL,
                            # ).findall(
                            #     queriesOld 
                            # )
                        }
                            # how many queries
                            # if isQueryContent 
                            # else {}
                        # 'queries': [
                        #     {
                        #         'query': quer[0],
                        #         'postquery': quer[1],
                            
                        #     }
                        #     # quer
                        #     for quer in re.compile(
                        #         '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n))',    
                        #         re.DOTALL,
                        #     ).findall(
                        #         old[2] 
                        #     )
                        # ]
                        #     if len(old) > 2 else None 
                    }

                    i+=1
                    print(f'\nold not in new {i}: {surAyOld}')

            else:
                if newDic[surAyOld]['string'].strip('\n') != primaryOld.strip():
                    print('\n',surAyOld)
                    print('new', newDic[surAyOld]['string'])
                    print('old', primaryOld)

                newDic[surAyOld]['string'] = primaryOld
                # # bef = dict(newDic[surAyOld])
                secondaries = findSec(queriesOld)
                # for quer in re.compile(
                #             '\n##\s{1,}([^\n]{1,}(?=\n))(.*?(?=\n#|$))',    
                #             re.DOTALL,
                #         ).findall(
                #             queriesOld 
                #         ):
                for secondary in secondaries:
                    sK = secondary[0] if '~~~ ' not in secondary[0] else secondary[0].replace('~~~ ','')
                #     newDic[surAyOld]['queries'][quer[0]] = quer[1]
                    # newDic[old[0]]['queries'].append({
                    #         'query': quer[0],
                    #         'postquery': quer[1],
                        
                    #     })
                    kDels = []
                    for nK in newDic[surAyOld]['queries'].keys():
                        sKSt = re.sub(
                            '^(?:\s*~~~\s*|)(.*?)\s*\d*$',
                            '\\1',
                            sK
                        )
                        if newDic[surAyOld]['queries'][nK].strip('\n') != secondary[2].strip():
                            print('\n',surAyOld)
                            print('new', newDic[surAyOld]['queries'][nK])
                            print('old', secondary[2])

                        if nK == sKSt:
                            kDels.append(nK)
                    for kDel in kDels:
                        del newDic[surAyOld]['queries'][kDel]
                    newDic[surAyOld]['queries'][secondary[0]] = secondary[2]
                    
                # if bef != newDic[surAyOld]:
                #     print(f'\nVerse string before reading: {bef}')
                #     print(f'\nVerse string after reading: {newDic[surAyOld]}')
        

    # print('\nnewDic after checking md: ', newDic, '\n')
    # print(newDic)

    sorterIdxs = [sorter.index(suray) for suray in newDic.keys()]

    sorterIdxs.sort()

    surAyOrdered = [sorter[idx] for idx in sorterIdxs]

    
    newStr = ''

    print(f"\nNumber of ayahs: {len(surAyOrdered)}")

    queriesLeft = set()
    for surAy in surAyOrdered:
        for q in newDic[surAy]['queries'].keys():
            qReal = re.sub(
                "s*\d*\s*$",
                "",
                q,
            )
            qStrp = qReal.strip('~~~ ')
            queriesLeft.add(qStrp)

    for surAy in surAyOrdered:
        # if surAy == '68:2':
        #     print(f'\nnew string: {newDic[surAy]}\n')
        # newStrUp =   f'\n# Q:{surAy}\n' + f'\n[Q.{surAy}](https://quran.com/{surAy}/tafsirs/{tafs})\n' + f'\n![[Qrsi#{surAy}]]\n'
        # qpq = newDic[surAy]['queries'].items()

        addStr = f'\n# Q:{surAy}' + newDic[surAy]['string']

        newStr += addStr

        # newStr += newStrUp

        # alreadyRefed.append(rec["surah_ayah"])
        alreadyRefed.append(surAy)
        # for query in newDic[surAy]['queries']:
        #     if query['query'] in queriesLeft:
        #         print(f'\nquery left at {surAy} : {query["query"]}')
        #         newStrUp = f'\n## {query["query"]}\n' + query['postquery']
        #         newStr += newStrUp
        #         queriesLeft.remove(query["query"])

        

        for q, pq in newDic[surAy]['queries'].items():
            qStrp = q.strip('~~~ ')
            qReal = re.sub(
                "s*\d*\s*$",
                "",
                q,
            )

            qRlStrp = qReal.strip('~~~ ')
            # qReal = q.replace("~~~ ","")
            if qRlStrp in queriesLeft:
                # print(f'\nquery left at {surAy} : {qReal}')
                newStrUp = f'\n## {qStrp}'
                frstAys[qRlStrp] = surAy
                queriesLeft.remove(qRlStrp)
            else:
                qHd = f'\n## ~~~ {qStrp}' 
                qRef ='\n' + f"1st inst: [[#Q:{frstAys[qRlStrp]}]]"
                newStrUp = ''
                if qHd not in q:
                   newStrUp  += qHd
                if qRef not in pq:
                    newStrUp += qRef
            # print("\nnewStrUp =", newStrUp)
            newStrUp += '\n' + pq.strip('\n') + '\n'
            newStr += newStrUp
        
        # print('\n')
                

    with open(mdFile, 'w+') as f:
        f.write(newStr)


def finish_query_f(button,container=widg.VBox([]),qL=[],refLng='english',flnm='md',qyArLegSch=lng2InpSchD["arabic"][1]):
    # global qL
    for k in range(len(container.children)-1,-1,-1):
        optStC = container.children[k].children[1]
        optSt = []
        for l in range(len(optStC.children)-1,-1,-1):
            combC = optStC.children[l]
            if not len(combC.children) < 2:
                vrsDisFld = combC.children[0].children[0]
                qyLblFld = combC.children[0].children[1]
                # print(vrsDisFld.description, vrsDisFld.value)
                # combObj = combClass()
                combClass.vrsDisSt = vrsDisFld
                combClass.strLSt = []
                # combObj = {"strL":[],"vrsDis":vrsDisFld.value}
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
                        combClass.strLSt.append(
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
                            }
                        )
                        print(f"combClass.strLSt: {combClass.strLSt}")
                # if len(combObj["strL"]) > 0:
                if len(combClass.strLSt) > 0:
                    print(f"combClass.strL while appending to optSt: {combClass.strLSt}")
                    print(f"optSt before appending comb:{optSt}")
                    optSt.append(combClass(lbl=qyLblFld.value,qyArLegSch=qyArLegSch))
                    print(f"comb.strL appended to optSt: {optSt[-1].strL}")
                    print(f"optSt after appending comb:{optSt}")
            if len(optSt) > 0:
                print(f"qL before appending optSt:{qL}")
                qL.append(optSt)
                print(f"qL after appending optSt:{qL}")
                # qL.append(combObj.__dict__)
        # dg = aggregLsts(qL)
        # sortchron(dg)
        qChronoMd(qL,refLng=refLng,flnm=flnm)
        # return qL
        # return dg


def intctv(
    qL=[],
    pres='',refLng='',flnm='md',qyArLegSch=lng2InpSchD["arabic"][1]
    ):
    container = widg.VBox(
        # layout=widgets.Layout(
        #             width="600px",       # Set the width to control the horizontal space
        #             overflow_x="scroll",  # Enable horizontal scrolling if content overflows
        #             border="1px solid black"  # Optional: add a border to make the scroll area visible
        #         )   
    )
    combs = []
    from functools import partial
    finish_query_B = widg.Button(description="Add Combination", layout=widg.Layout(width="auto"))
    finish_query_B.on_click(partial(finish_query_f,container=container,qL=qL,flnm=flnm,refLng=refLng,qyArLegSch=qyArLegSch))
    # Container to hold all groups of widgets
    # Initialize the first group of widgets
    optStWdgCl(
        # 1
        combs,
        container
        )
    # clear_output()
    display(finish_query_B,container,)


def querizeMd(
        # qL
        qL=[],
        # qL=[],
        # tafs='ar-tafsir-al-tabari',
        flnm='md',
        refLng='english',
        qyArLegSch=lng2InpSchD["arabic"][1]
    ):
    global tafsDict
    global refLngD
    pres, refLng = confFcheck("None",refLng)
    flNmW = widg.Text(description="Output file name",value=flnm)
    refLngW = widg.Dropdown(description="Tafsir Language",options=refLngD.values(),value=refLng)
    qyArLegSchW = widg.Dropdown(description="Arabic Legend Scheme",options=lng2InpSchD["arabic"],value=qyArLegSch)
    def submConf(button,qL=qL,flNmW=flNmW,refLngW=refLngW,qyArLegSchW=qyArLegSchW):
        clear_output()
        flnm = flNmW.value
        refLng=refLngW.value
        qyArLegSch = qyArLegSchW.value
        with open('./cnf.txt', 'w+') as f:
            import json
            f.write(json.dumps({"pres":pres,"refLng":refLng}))
        if type(qL) != type([]):
            print("Invalid root-filter key value pairs")
            # dicti={}
            qL=[]
        # if dicti=={}:
        if qL==[]:
        #     finished=False
        #     # while finished==False:
        # if finished==False:
            print("interactive")
            intctv(qL,flnm,refLng,qyArLegSch=qyArLegSch)
        else:
            print("not interactive")
            qL = [
                # [combClass(**comb).combObj for comb in optLs]
                [combClass(**comb,qyArLegSch=qyArLegSch) for comb in optLs]
                for optLs in qL
            ]
            # colMap = getColMap(dicti)
            qChronoMd(qL,flnm,refLng)
    confSetB = widg.Button(description='Enter configuration')
    from functools import partial
    confSetB.on_click(partial(submConf,qL=qL,flnmW=flNmW,refLngW=refLngW,qyArLegSchW=qyArLegSchW))
    confCont = widg.VBox([refLngW,flNmW,qyArLegSchW,confSetB])
    clear_output()
    display(confCont)