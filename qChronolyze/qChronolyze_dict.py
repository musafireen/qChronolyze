import ipywidgets as widg
from ipywidgets import interactive as intct
from IPython.display import display, clear_output

# List to track widget groups

presD={'1':'table','2':'plot'}

refLngD={'1':'arabic','2':'bengali','3':'english'}

tafsDict={"arabic":"ar-tafsir-al-tabari","bengali":"bn-tafseer-ibn-e-kaseer","english":"en-tafisr-ibn-kathir"}

strTypD = {
    "root": "root",
    "stem": "stem",
    "lemma": "lem",
    "english": "eng",
    "All": "All"
}

strTypL = list(strTypD.keys())

frmL = ["All","i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii",]

poSpD = {
    'All': 'All',
    'Adjective': 'ADJ',
    'Noun': 'N',
    'Proper noun': 'PN',
    'Verb': 'V',
    'Imperative verbal noun': 'IMPN',
    'Personal pronoun': 'PRON',
    'Demonstrative pronoun': 'DEM',
}

poSpL = list(poSpD.keys())

lngD = {
    "arabic": "arb",
    "english": "eng",
    "bengali": "bng"
}

lngL = list(lngD.keys())

lng2InpSchD = {
    "arabic": [
        "buckwalter_Scheme",
        "arabic_Scheme"
    ],
    "bengali": [
        "bengali_Scheme"
    ],
    "english": [
        "english_Scheme"
    ]
}
inpLngSchD = {
    "buckwalter_Scheme": "bkwSch",
    "arabic_Scheme": "arbSch",
    "bengali_Scheme": "bngSch",
    "english_Scheme": "engSch",
}

def getSorter():
    
    
    """ to tweak the sorter tweak the "surOrd.tsv" file manually """

    import os
    import json
    import csv
    with open('qdict.json') as f:
        qStr = f.read()
    qDict = json.loads(qStr)

    loadedFromDict = False

    if os.path.isfile('sorter.json'):
        print("'sorter.json' found'")
        if os.path.getctime('sorter.json') > os.path.getctime('surOrd.tsv'):
            with open('sorter.json') as f:
                sortStr = f.read()
                # print(f"in 'sorter.json': \n\n{sortStr}")
            try:
                sorter = json.loads(sortStr)
                print('last item in sorter:', sorter[-1])
                if len(sorter) == 6236:
                    loadedFromDict = True
                    print(f"successfully loaded sorter of length {len(sorter)} from 'sorter.json'")
                else:
                    print(f"length of sorter is {len(sorter)} (not equal to 114)")
                    del sorter
            except:
                print("failed to load sorter from 'sorter.json'")
        else:
            print("'surOrd.tsv' was modified. \nCreating new sorter")

    if not loadedFromDict:
        print("creating sorter from 'surOrd.tsv'")
        with open('surOrd.tsv') as f:
            surOrd = [row for row in csv.DictReader(f, delimiter='\t') ]

        sorter = [''] * 6236
        bef = {}
        aft = {}
        befaft = []

        for v in surOrd:
            s=v["surah"]
            if "exception" in v.keys():
                exs = v["exception"]
                if type(exs) == type(''):
                    exs = json.loads(exs)
                if len(exs) > 0:
                    for ex in exs:
                        ar = ex["ayah_range"].split('-')
                        al = ar if len(ar) == 1 else list(range(int(ar[0]),int(ar[1])+1)) if len(ar) == 2 else []
                        if "before" in ex.keys():
                            if ex["before"] != '':
                                if ex["before"] not in bef.keys():
                                    bef[ex["before"]]=[]
                                for ay in al:
                                    bef[ex["before"]].append(f'{s}:{ay}')
                                    befaft.append(f'{s}:{ay}')
                        if "after" in ex.keys():
                            if ex["after"] != '':
                                if ex["after"] not in aft.keys():
                                    aft[ex["after"]]=[]
                                for ay in al:
                                    aft[ex["after"]].append(f'{s}:{ay}')
                                    befaft.append(f'{s}:{ay}')

        i = 0

        for v in surOrd:
            s=v["surah"]
            for a in range(1, qDict[s]["verse_count"]+1):
                s_a= f'{s}:{a}'
                if s_a in bef.keys():
                    for sa in bef[s_a]:
                        sorter[i] = sa
                        i += 1
                if s_a not in befaft:
                    sorter[i] = s_a
                    i += 1
                if s_a in aft.keys():
                    for sa in aft[s_a]:
                        sorter[i] = sa
                        i += 1

        with open(f'sorter.json', 'w') as f:
            f.write(json.dumps(sorter))
    
    return sorter

def getColMap(dicti):
    import numpy as np
    colMap = {}
    leng = len(dicti)
    lwrLmt = 100
    uprLmt = 250
    p = np.linspace(lwrLmt,uprLmt,num=leng)
    for idx in range(1,leng+1):
        # n1=rand.randn()
        # n2=rand.randn()
        # i1=rand.randint(0,50)
        # i2=rand.randint(0,50)
        # clr=f"rgb({50+(100/leng)*idx})"
        # colMap[df["query"].unique()[idx]] = f"rgb({clr},{clr},{clr})" 
        #   rd = int(p[idx-1])
        #   radialDist = (rd - lwrLmt) if (rd - lwrLmt) < (uprLmt - rd) else (uprLmt - rd)
        #   colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        #   pair = dicti[idx-1]
        #   colMap[f"{list(pair.keys())[0]} ({list(pair.values())[0]})"] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        quer = dicti[idx-1]
        colMap[quer] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        # colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({rd},{gn},{bl})' 
        # print(f'rgb({int(p[idx-1])},{int(p[-idx]-50)},25)' )
    return colMap

def rtTrns(rt,inpLng,inpLngSch):
    lngSts = {
        "arb": "arbSch",
        "eng": "engSch",
        "bng": "bngSch"
    }

    bkwSch2arbSch = {
        "'": "ء",
        ">": "أ",
        "&": "ؤ",
        "<": "إ",
        "}": "ئ",
        "A": "ا",
        "b": "ب",
        "p": "ة",
        "t": "ت",
        "v": "ث",
        "j": "ج",
        "H": "ح",
        "x": "خ",
        "d": "د",
        "*": "ذ",
        "r": "ر",
        "z": "ز",
        "s": "س",
        "$": "ش",
        "S": "ص",
        "D": "ض",
        "T": "ط",
        "Z": "ظ",
        "E": "ع",
        "g": "غ",
        "_": "ـ",
        "f": "ف",
        "q": "ق",
        "k": "ك",
        "l": "ل",
        "m": "م",
        "n": "ن",
        "h": "ه",
        "w": "و",
        "Y": "ى",
        "y": "ي",
        "F": "ي",
        "N": "ٌ",
        "K": "ٍ",
        "a": "َ",
        "u": "ُ",
        "i": "ِ",
        "~": "ّ",
        "o": "ْ",
        "^": "ٓ",
        "#": "ٔ",
        "`": "ٰ",
        "{": "ٱ",
        ":": "ۜ",
        "@": "۟",
        '"': "۠",
        "[": "ۢ",
        ";": "ۣ",
        ",": "ۥ",
        ".": "ۦ",
        "!": "ۨ",
        "-": "۪",
        "+": "۫",
        "%": "۬",
        "]": "ۭ",
    }
    iasSch2arbSch = {

    }

    chrOut = {
        "arb": {
            "bkwSch": bkwSch2arbSch,
            "iasSch": iasSch2arbSch,
        },
        "eng": {
            "engSch": None
        },
        "bng": {
            "bngSc": None
        },
    }

    chrTrnsTbl = chrOut[inpLng][inpLngSch]
    rtTrns = ''
    if chrTrnsTbl != None:
        for chr in rt:
            if chr in chrTrnsTbl.keys():
                chrTrns = chrTrnsTbl[chr]
            else:
                chrTrns = chr
            rtTrns += chrTrns
            # print("language schema is present\ncharacter transform: ", chrTrns)
    else:
        rtTrns = rt
    
    return rtTrns

def filecheck(filepath):
    import os
    BASE_DIR = os.getcwd()
    dirc = os.path.join(BASE_DIR,filepath)
    subdircL = filepath.split(os.sep)
    try:
        subdircL.remove('')
    except:
        pass
    doesPathExist = ''
    try:
        for supDirc in subdircL[:-1]:
            doesPathExist = os.path.join(doesPathExist,supDirc)
            if not os.path.exists(os.path.join(BASE_DIR,doesPathExist)):
                os.makedirs(os.path.join(BASE_DIR,doesPathExist))
                if os.path.exists(doesPathExist):
                    pass
        return os.path.isfile(os.path.join(BASE_DIR,filepath))
    except:
        pass

def tblUp(tblCumul,tblAgg,instDct,stri,lnk
            #   frm='',ptSp=''
                ):
        # for tbl in tbls:
        #     # print(tbl)
        #     tblAgg += tbl

        # print(len(tblAgg))
        
        print(f"number of instances of {stri} in {lnk} before Adam filter: {len(tblAgg)}")

        if len(tblAgg) > 0:
        # if len(tbls) > 0:
            # print(f"1st row of Table aggregate for {lnk} for {rt} is: {tblAgg[0].find_all('td')}")
            print(tblAgg[0].find_all('td')[1])
            if 'adam' in tblAgg[0].find_all('td')[1].get_text().lower():
            # if 'adam' in tbls[0].find_all('td')[1].get_text().lower():
                if stri.lower() != 'adam' and stri != 'A^dam':
                    # print("no results")
                    tblAgg = []
                    # tbls = []

        print(f"number of instances of {stri} in {lnk} after Adam filter: {len(tblAgg)}")
        # print(tblAgg)

        tblCumul += tblAgg
        # tblCumul += tbls

        print("length of tblCumul: ", len(tblCumul))
        # print(f"total number of instances so far of {rt} without removing duplicates: {len(tblCumul)}")

        for rw in tblCumul:
            row = [ fld.get_text() for fld in rw.find_all("td") ]
            # row = []
            # for fld in rw:
            #   row.append(fld.get_text())
        
            # print(row)
            pos = row[0].split(' ')[0].strip('()')
            # print(pos)
            if pos not in instDct:
                # print(posSplit)
                posSplit = pos.split(':')
                # print(posSplit)
                # instLst.append({
                instDct[pos] = {
                        "surah:ayah": f'{posSplit[0]}:{posSplit[1]}',
                        #   "position": int(posSplit[2]), 
                        "position": posSplit[2], 
                        "string": row[0].split(' ')[1], 
                        "meaning": row[1],
                        # "form": frm,
                        # "p-o-s": ptSp,
                        "ayah_link": row[2]
                    }
                # })
        
                # poss.add(pos)
            else:
                # if instDct[pos]["form"] == '' and frm != '':
                #     instDct[pos]["form"] = frm
                # if instDct[pos]["p-o-s"] == '' and ptSp != '':
                #     instDct[pos]["p-o-s"] = ptSp
                pass

            # print(f"number of unique instances upto {lnk}: {len(poss)} or {len(instLst)}")
            
        print(len(tblCumul), len(instDct))
        # print(tblAgg)

        return tblCumul, instDct

def fileGet(stri,filepath):
        import csv
        print(f"file found for {stri}")
        instDct = {}
        try:
            with open(filepath) as f:
                # print(f"loading {filepath}")
                instTbl = csv.DictReader(f, delimiter='\t')
                # instLst = [row for row in csv.DictReader(f, delimiter='\t') ]
                for row in instTbl:
                    surAyPos = f'{row["surah:ayah"]}:{row["position"]}'

                    instDct[surAyPos] = row

                print(f"Successfully loaded data from '{filepath}: lenght {len(instDct)}'")
                # propDat = True
        except:
            # propDat = False
            instDct = {}
            print(f"couldn't load data from '{filepath}': lenght {len(instDct)}")
        
        return instDct

def webGet(stri,lnks,filepath,poSp,frm):
    # import html2text
    # import json
    import requests
    from bs4 import BeautifulSoup
    import re

    def getTbl(grabhtmlPara):
        soup = BeautifulSoup(
            grabhtmlPara,
            'lxml' 
        )

        tblsRet = soup.find_all(
            "table",
            {"class":"taf"}
        )

        return tblsRet


    # poss = set()
    instDct={}
    tblCumul = []
    # tblAgg = []
    print(f"proper data not found for {stri}")


    for lnk in lnks:
        print('\ngetting for link: ', lnk, '\n')
        if lnk == f'https://corpus.quran.com/qurandictionary.jsp?q={stri}':
            grabhtml = requests.get(lnk).text
            # print(type(grabhtml))

            import re

            headTbls = re.findall('(<h4 class="dxe">.*?(?=<h4))',grabhtml,re.DOTALL)

            # print(len(headTbls))

            for headTbl in headTbls:
                tblAgg = []
                soup = BeautifulSoup(
                    headTbl,
                    'lxml',
                    # 'html.parser',
                )
                head4 = soup.find_all(
                    "h4",
                    {"class":"dxe"}
                )[0]

                # if len(tblsRet) > 0:
                    # print(len(tblsRet) > 0)
                    # print(len(tblsRet))
                    # if len(tblsRet) == len(head4s):
                    # print(len(tblsRet) == len(head4s))
                # for i in range(len(head4s)):
                    # print(head4s[i].text)

                tblGrm = head4.text.split('-')[0]
                tblForms = re.findall('\(form (.*?)\)', tblGrm)
                if len(tblForms) == 0:
                    tblForm = 'All'
                else:
                    # print(tempForms[0])
                    tblForm = tblForms[0]
                tblPoSps = re.findall(f'(^[^\(\)]*?(?=\s*$|\s*\())', tblGrm)
                if len(tblPoSps) == 0:
                    tblPoSp = 'All'
                else:
                    # print(tempPtSps[0])
                    tblPoSp = tblPoSps[0]

                if tblForm == 'All':
                    if tblPoSp != 'All':
                        tblForm = 'I'
                print(
                    # grm, 
                    tblForm, 
                    tblPoSp
                )

                tbls = soup.find_all(
                    "table",
                    {"class":"taf"}
                )

                # tblAgg = [ tbl for tbl in tbls ]

                # print(tblsRet)
                for tbl in tbls:
                    if tblPoSp == poSp and tblForm == frm:
                        tblAgg += tbl
                print("tblAgg length", len(tblAgg))
                tblCumul,instDct = tblUp(tblCumul,tblAgg,instDct,
                                        #  tempForm,tempPtSp
                                        stri,lnk
                                            )


        else:
            pgs = []
            tblAgg = []
            grabhtml = requests.get(f"{lnk}").text
            tbls = getTbl(grabhtml)
            if 'Results' in grabhtml:
                matches = re.findall(">[\n\s]*Results[\s\n]*<b>\d*</b>[\s\n]*to[\s\n]*<b>\d*</b>[\s\n]*of[\s\n]*<b>(\d*)</b>", grabhtml, re.DOTALL)
                print('\nmatches: ', matches)
                if len(matches) > 0:
                    pgFlt = int(matches[0])/50
                    pgCount = int(pgFlt) + 1 if int(matches[0]) % 50 != 0 else int(pgFlt)
                    # print(f"page count in {lnk} is: {pgCount}")
                    # print(type(pgCount), pgCount)
                    pgs = list(map(lambda x : f'&page={x}', list(range(2,pgCount+1))))

                for pg in pgs:
                    print(f'\nin pg {pg}')
                    grabhtml = requests.get(f"{lnk}{pg}").text
                    tbls += getTbl(grabhtml)
                    # print(f"length of grabhtml is: {len(grabhtmlNew)}")
                    # grabhtml += grabhtmlNew
                    # print(f"length of grabhtml after adding is: {len(grabhtml)}")
                
            for tbl in tbls:
                tblAgg += tbl
                
            print("length of tblAgg: ", len(tblAgg))
            
            tblCumul,instDct = tblUp(tblCumul,tblAgg,instDct,stri,lnk)

        # print(f"\nnumber of tables found in {lnk} for {rt} is: {len(tbls)}")
        # print(f"{tbls}\n")


    list_header = ['surah:ayah', 'position', 'string', 'meaning', 'ayah_link'
                #    'form', 'p-o-s', 
        ]
    print(f"writing {stri} to '{filepath}'")
    with open(f'{filepath}', 'x') as f:
        # print(f"writing {stri} to '{filepath}'")
        import csv
        writer = csv.DictWriter(f, delimiter='\t', fieldnames=list_header)
        writer.writeheader()
        # for datum in instLst:
        for k, datum in instDct.items():
            writer.writerow({
                list_header[0] : datum['surah:ayah'],
                list_header[1] : datum['position'],
                list_header[2] : datum['string'],
                list_header[3] : datum['meaning'],
                list_header[4] : datum['ayah_link'],
                # list_header[4] : datum['form'],
                # list_header[5] : datum['p-o-s'],
            })
    
    return instDct


def dataGrabber(
        strObj
    ):

    '''Grabs data from corpus.quran.com & formats them'''

    flt = str(strObj["flt"]).lower()
    strTyp = strTypD[strObj["strTyp"]]
    frm = strObj["frm"]
    poSp = strObj["poSp"] if strObj["poSp"] in poSpD.values() else poSpD[strObj["poSp"]]
    inpLng = lngD[strObj["inpLng"]]
    inpSch = inpLngSchD[strObj["inpSch"]]
    stri = strObj["stri"]
    filename = rtTrns(strObj["stri"],inpLng,inpSch)


    # if stri == "" or strTyp == "eng" "aeiou" not in stri and strTyp == "All":
    #     strTyp = "root"

    mainLnk = "https://corpus.quran.com/search.jsp?q="
    isArabic = strTyp != 'eng' and stri !='' and inpLng == 'arb'

    if not isArabic:
        if flt != '' and stri =='':
            stri = str(flt).lower()
            flt = ''
    lnks = []
    if isArabic:
        filepath = f'data/cache/arb/{filename}/{strTyp}/{frm}/{poSp}.tsv'
        if poSp != "All":
            mainLnk += f"pos:{stri} "
        if frm != "All":
            mainLnk += f"({frm}) "
        if strTyp !='All':
            mainLnk += f"{strTyp}:"
        if strTyp == 'All':
            for strTy in ['lem','stem','root']:
                lnks.append(
                    f"https://corpus.quran.com/search.jsp?q={strTy}:{stri}"
                )
            # lnks = [
            #     f"https://corpus.quran.com/search.jsp?q=lem:{stri}",
            #     f"https://corpus.quran.com/search.jsp?q=stem:{stri}",
            #     f"https://corpus.quran.com/search.jsp?q=root:{stri}",
            # ]
        # lnks = [mainLnk]
        mainLnk += stri
        lnks = [*lnks, f"https://corpus.quran.com/qurandictionary.jsp?q={stri}"]
    else:
        # lnks = [mainLnk]
        filepath = f'data/cache/nonarb/{stri}.tsv'
        mainLnk += stri
    lnks = [*lnks,mainLnk]
    
    # instLst=[]

    fileFound = filecheck(filepath)
    # if len(links) != 1:
    # import os
    # for k, direcLnk in direcLnkDic.items():
        # propDat, 
    instDct = fileGet(stri,filepath) if fileFound else webGet(stri,lnks,filepath,poSp,frm,)
        # for lnk in lnks:

    # posDic = {
    #     'ADJ': 'Adjective',
    #     'N': 'Noun',
    #     'PN': 'Proper noun',
    #     'V': 'Verb',
    #     'IMPN': 'Imperative verbal noun',
    #     'PRON': 'Personal pronoun',
    #     'DEM': 'Demonstrative pronoun',
    #     '': '',
    # }
    
    # print(frmReq, ptSpReq)
        # print(len(instLst))
    instLst = [datum for datum in instDct.values()]
    # if frmReq != None:
    #     # instLst = [datum if datum["form"] == frmReq.capitalize() else None for datum in instLst]
    #     instLst = list(filter(lambda datum: datum["form"] == frmReq.capitalize(), instLst))
    # if ptSpReq != None:
    #     # instLst = [datum if datum["p-o-s"] == posDic[ptSpReq] else for datum in instLst]
    #     instLst = list(filter(lambda datum: datum["p-o-s"] == posDic[ptSpReq], instLst))
        

    return instLst

def filtDown(strObj):
    stri = strObj["stri"]
    flt = strObj["flt"]
    import re
    instLst = dataGrabber(strObj)
    instLstFiltered =  list(filter( lambda row : len(re.compile(str(flt).lower()).findall(row["meaning"].lower())) > 0 or len(re.compile(str(stri)).findall(row["meaning"])), instLst))
    # instLstFiltered = [ { **row , "query" : f"{rt} ({flt})"} for row in instLstFiltered ]
    return instLstFiltered

def intersct(comb):
    strL = comb["strL"]
    if len(strL) > 0:
        instLstAgg = []
        surahAyahAggSet = set()
        for i in range(len(strL)):
            strObj = strL[i]
            instLst = filtDown(strObj)
            surahAyahList = [ inst["surah:ayah"] for inst in instLst ]
            if i == 0:
            # if surahAyahAggSet == set([]):
                surahAyahAggSet = set(surahAyahList)
            else:
                surahAyahAggSet = surahAyahAggSet.intersection(surahAyahList)
            instLstAgg += instLst
        
        instLstFlt = list(filter(
            lambda x: x["surah:ayah"] in surahAyahAggSet,
            instLstAgg
        ))
        instDictInc = {}
        for inst in instLstFlt:
            surahAyah = inst["surah:ayah"]
            if surahAyah not in instDictInc.keys():
                instDictInc[surahAyah] = {
                    "position": inst["position"],
                    "string": inst["string"],
                    "meaning": inst["meaning"],
                    "ayah_link" : inst["ayah_link"],
                    # "query": 
                    # f"{rtAgg} ({flAgg})"
                    # stri_flt_int_lb
                }
            else:
                instDictInc[surahAyah]["string"] = instDictInc[surahAyah]["string"] + ' ' + inst["string"]
                instDictInc[surahAyah]["meaning"] = instDictInc[surahAyah]["meaning"] + ' ' + inst["meaning"]

        instLstInc = [ {"surah:ayah":k, **v } for k, v in instDictInc.items() ]
        return instLstInc
    
    # elif len(strL) == 1:
    #     instLstFlt = filtDown(strL[0])
    #     instLstInc = [ { **rec, "query": f"{stri_flt_int_lb})" } for rec in instLstFlt ]
    #     return instLstInc
    
    else:
        print("please provide at least one root/word")


def aggregLsts(qL,tafs="ar-tafsir-al-tabari"):
    # lnkStyle = ' '
    fontSize = '18'
    fontCol = 'rgb(0,0,150)'
    shPx = str(int(fontSize)/100*0)
    shCol = '#000000'
    bgCol = 'rgb(220,220,250)'
    txtShad = ''
    # txtShad = f'text-shadow:{shPx}px {shPx}px 0 {shCol}, {shPx}px -{shPx}px 0 {shCol}, -{shPx}px -{shPx}px 0 {shCol}, -{shPx}px {shPx}px 0 {shCol};'
    # lnkStyle = "style='background-color:rgb(250,250,250);font-size:30px;color:rgb(0,0,150);-webkit-text-stroke-width:5px;-webkit-text-stroke-color:white' "
    lnkStyle = f"style='background-color:{bgCol};font-size:{fontSize}px;color:{fontCol};{txtShad}' "
    # lnkStyle = "style='color:rgb(250,250,250);-webkit-text-stroke-width:1px;-webkit-text-stroke-color:rgb(0,0,0);' "
    instLstAgg = []
    for optSt in qL:
        print(optSt)
        lblParts = []
        optStInsts = []
        for comb in optSt:
            print(comb)
            strL = comb["strL"]
            lblParts += [' + '.join([ 
                f'{strObj["stri"]} ({strObj["flt"]})' for 
                strObj 
                in strL
            ])]
            combInstLst = intersct(comb)
            optStInsts += combInstLst
        lbl = ' / '.join(lblParts)
        instLst = [ { **inst, "query": lbl } for inst in optStInsts  ]
        instLstAgg += instLst
    instLstAgg = [ { 
        **row, 
        "ayah_link": f"<a {lnkStyle}href='https://quran.com/{row['surah:ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
        # "ayah_link": f"<a href='https://quran.com/{row['surah:ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
        } for row in instLstAgg ]
    print(f"\ntotal {len(instLstAgg)} instances found")
    return instLstAgg

class strObjClass:
    # idx = 0
    # parentIdx = 1
    striSt = ''
    fltSt=''
    # strTypSt='root'
    strTypSt='All'
    frmSt='All'
    poSpSt='All'
    inpLngSt="arabic"
    inpSchSt="buckwalter_Scheme"


    def __init__(self,                
                stri = striSt,
                flt = fltSt,
                strTyp = strTypSt,
                frm = frmSt,
                poSp = poSpSt,
                inpLng = inpLngSt,
                inpSch = inpSchSt ,
                #  strSt=strObjStClass()
                #  **kwargs
                ):
        
        self.stri = stri
        self.flt = flt
        self.strTyp = strTyp
        self.frm = frm
        self.poSp = poSp
        self.inpLng = inpLng
        self.inpSch = inpSch
        self.strObj = {
            "stri": stri,
            "flt": flt,
            "strTyp": strTyp,
            "frm": frm,
            "poSp": poSp,
            "inpLng": inpLng,
            "inpSch": inpSch,
        }


class combClass:
    strLSt = []
    vrsDisSt = 0
    combObjSt = {
        "strL": [],
        "vrsDis": 0,
    }
    def __init__(self,strL=strLSt,vrsDis=vrsDisSt):
    #   global strObjClass
      # print(combsLsA)
      self.vrsDis = vrsDis
      # print(strL)
      # for strObj in [{"stri":"EiysaY"}]:
      #     print(strObjClass(strObj).strObj)
    #   print([strObjClass(**strObj).strObj for strObj in strL ])
      self.strL = [ strObjClass(**strObj).strObj for strObj in strL  ]
    #   print([strObjClass(**strObj).strObj for strObj in self.strL ])
      # for strObj in strL:
      #     self.strL.append(strObjClass(strObj))
      self.combObj = {
          "strL": self.strL,
          "vrsDis": self.vrsDis,
      }


class strObWdgCl:
    # global fulWdgD
    # idx = 0
    # parentIdx = 1
    strngs = []
    # strTypSt = "root"
    strTypSt = strObjClass.strTypSt
    frmSt = strObjClass.frmSt
    poSpSt = strObjClass.poSpSt
    inpLngSt = strObjClass.inpLngSt
    inpSchSt = strObjClass.inpSchSt

    def update_language_scheme_options(self,*args):
        # print(self.inpLngW.value)
        self.inpSchW.options=lng2InpSchD[self.inpLngW.value]
        self.inpSchW.value=lng2InpSchD[self.inpLngW.value][0]
    
    # def entStrObjM(self,*args):
    def entStrObjM(self,button,
                #    strngs,comb_container
                   ):
        strObWdgCl.strTypSt=self.strTypeW.value
        strObWdgCl.frmSt=self.frmW.value
        strObWdgCl.poSpSt=self.poSpW.value
        strObWdgCl.inpLngSt=self.inpLngW.value
        strObWdgCl.inpSchSt=self.inpSchW.value

        strObWdgCl(
            self.parentComb
                                 )

    def delStrObjM(self,button,
                   ):
        if len(self.parentComb.strngs) > 1:
            if self.strContainer in self.parentComb.strngs:
                self.parentComb.strngs.remove(self.strContainer)
                self.parentComb.comb_container.children = [w for w in self.parentComb.comb_container.children if w != self.strContainer]

    def __init__(self,
                 parentComb,
                ):

        self.parentComb = parentComb

        self.striW = widg.Text(description=f"String_Object")
        self.fltW = widg.Text(description=f"Translation_filter")
        self.strTypeW = widg.Dropdown(options=strTypL, value=self.strTypSt,description=f"String_type")
        self.poSpW = widg.Dropdown(options=poSpL, value=self.poSpSt,description=f"Part_of_speech")
        self.frmW = widg.Dropdown(options=frmL, value=self.frmSt,description=f"Form")
        self.inpLngW = widg.Dropdown(options=lngL, value=self.inpLngSt,description=f"Input_language")
        self.inpSchW = widg.Dropdown(description=f"Input_scheme")
        self.entStrObjB = widg.Button(description=f"Enter String Object")
        self.delStrObjB = widg.Button(description=f"Delete String Object")
        self.entStrObjB.on_click(self.entStrObjM)
        self.delStrObjB.on_click(self.delStrObjM)
        self.inpLngW.observe(self.update_language_scheme_options)
        self.update_language_scheme_options(self)

        self.strContainer = widg.VBox(
            [
                self.striW,
                self.fltW,
                self.strTypeW,
                self.poSpW,
                self.frmW,
                self.inpLngW,
                self.inpSchW,
                self.entStrObjB,
                self.delStrObjB
            ]
        )

        parentComb.strngs.append(self.strContainer)

        parentComb.comb_container.children = [parentComb.comb_container.children[0], self.strContainer, *parentComb.comb_container.children[1:]]

        parentComb.comb_container.layout=widg.Layout(
            max_width="800px",       # Set the width to control the horizontal space
            # max_height="800px",       # Set the width to control the horizontal space
            # width="500px",       # Set the width to control the horizontal space
            # height="200px",       # Set the width to control the horizontal space
            # overflow="scroll",  # Enable horizontal scrolling if content overflows
            border="1px solid black",  # Optional: add a border to make the scroll area visible
            # display="flex",
            # flex_flow='row',
            overflow='scroll hidden'
        )


class combWdgCl:
        # Function to add a new group of widgets
    vrsDisSt = combClass.vrsDisSt
    strLSt = combClass.strLSt
    def entCombM(self,button):
        # new_group_id = len(combs) + 1
        # new_group = 
        print(len(self.opt_container.children[1].children))
        combWdgCl(
            # new_group_id
            self.combs,
            self.opt_container
            )
        print(len(self.opt_container.children[1].children))
        
        # self.combs.append(new_group)
        # self.container.children = list(self.container.children) + [new_group]

    # Function to remove this specific group of widgets
    def delCombM(self,button):
        if len(self.combs) > 1:
            if self.comb_container in self.combs:
                self.combs.remove(self.comb_container)
                self.opt_container.children[1].children = [w for w in self.opt_container.children[1].children if w != self.comb_container]
    # Function to create a new group of widgets with its own Add and Remove buttons
    def __init__(self,
            # comb_id
                 combs,
                 opt_container
            ):
        # Widgets for the group (e.g., Text and Slider)

        self.combs = combs
        self.opt_container = opt_container
        # print(len(self.container.children))

        self.vrsDistW = widg.IntText(min=0,max=6236,value=0, description=f"Verse Distance")
        self.entCombB = widg.Button(description="Enter Combination of String Objects")
        self.entCombB.on_click(self.entCombM)
        self.delCombB = widg.Button(description="Delete Combination of String Objects")
        self.delCombB.on_click(self.delCombM)

        self.comb_container = widg.HBox(
            [
                widg.VBox(
                    [
                        self.vrsDistW,
                        widg.HBox([self.entCombB, self.delCombB]),
                    ],
                    # layout = widgets.Layout(
                    #     width="200px"
                    # )
                )
            ],
                # layout=widgets.Layout(
                #     width="500px",       # Set the width to control the horizontal space
                #     overflow_x="scroll",  # Enable horizontal scrolling if content overflows
                #     border="1px solid black"  # Optional: add a border to make the scroll area visible
                # )   
        )

        # strngs_container = widgets.HBox()

        self.strngs = []

        strObWdgCl(self)

        # strngs_container.children = [initial_strng]

        # strngs.append(initial_strng)

        self.combs.append(self.comb_container)
        self.opt_container.children[1].children = [self.comb_container,*self.opt_container.children[1].children,]

class optStWdgCl:
        # Function to add a new group of widgets
    def entOptStM(self,button):
        # new_group_id = len(combs) + 1
        # new_group = 
        print(len(self.container.children))
        optStWdgCl(
            # new_group_id
            self.optSts,
            self.container
            )
        print(len(self.container.children))
        

    # Function to remove this specific group of widgets
    def delOptStM(self,button):
        if len(self.optSts) > 1:
            if self.optSt_container in self.optSts:
                self.optSts.remove(self.optSt_container)
                self.container.children = [w for w in self.container.children if w != self.optSt_container]
    # Function to create a new group of widgets with its own Add and Remove buttons
    def __init__(self,
            # comb_id
                 optSts,
                 container
            ):
        # Widgets for the group (e.g., Text and Slider)

        self.optSts = optSts
        self.container = container
        # print(len(self.container.children))

        # self.vrsDistW = widg.IntText(min=0,max=6236,value=0, description=f"Verse Distance")
        self.entOptStB = widg.Button(description="Enter Option of String Objects")
        self.entOptStB.on_click(self.entOptStM)
        self.delOptStB = widg.Button(description="Delete Option of String Objects")
        self.delOptStB.on_click(self.delOptStM)

        self.optSt_container = widg.VBox(
            [
                widg.HBox(
                    
                        [self.entOptStB, self.delOptStB],
                    
                    # layout = widgets.Layout(
                    #     width="200px"
                    # )
                ),
                widg.HBox([])
            ],
                # layout=widgets.Layout(
                #     width="500px",       # Set the width to control the horizontal space
                #     overflow_x="scroll",  # Enable horizontal scrolling if content overflows
                #     border="1px solid black"  # Optional: add a border to make the scroll area visible
                # )
        )

        # strngs_container = widgets.HBox()

        self.combs = []

        combWdgCl(
            self.combs,
            self.optSt_container
        )

        self.optSts.append(self.optSt_container)
        self.container.children = [self.optSt_container,*self.container.children,]


def tabular(df,colMap,sorter):
    import pandas as pd
    # print(df)

    # for rt in dicti.keys():
    #     instLst = aggregLsts(rt,dicti[rt])
    #     dfNew = pd.DataFrame.from_records(instLst)
    #     df = pd.concat([df, dfNew], axis=0)

    print(f'dataframe length: {len(df)}')
    # df.drop(columns=[
    # #  "query",
    #     "index"
    #     ],
    #     inplace=True
    # )

    compareDict = {}
    for i in range(len(sorter)):
        compareDict[sorter[i]]=i

    df.insert( 0, 'verses_before',    list(
        map(
            lambda x: compareDict[x],
            # df["surah"]
            df["surah:ayah"]
            )
        )
    )

    from IPython.core.display import HTML

    def colo(s):
        # print(s)
        return [
            f'background-color: {colMap[s["query"]]};'
            + 'foreground-color: black;'
            + 'color: black;'
            + 'opacity: 1;' 
        ] * len(s)
    clear_output()
    display(
        HTML(df.style.apply(
                colo , axis=1
            ).to_html(render_links=True,escape=False,index=False)
        )

    )


def plotDf(df,colMap,sorter):
    import plotly.express as px
    # import plotly.graph_objects as go
    # from plotly.subplots import make_subplots
    # from plotly.offline import iplot, init_notebook_mode
    # init_notebook_mode()

    ay_ln = df.groupby(['surah:ayah', 'query'],observed=True).apply(lambda group: ' .. '.join(group['ayah_link'])).reset_index()
    pos = df.groupby(['surah:ayah', 'query'],observed=True).apply(lambda group: ','.join(group['position'])).reset_index()

    df = df.drop_duplicates(subset=['surah:ayah', 'query'], keep="first").reset_index(drop=True)

    df["position"] = pos[0]
    df["ayah_link"] = ay_ln[0]
    
    df["ayah_link"] = list(df["surah:ayah"]) + df["ayah_link"]
    df.reset_index(inplace=True)


    fig = px.scatter(
        df,
        # x='surah:ayah',
        x='query',
        y='surah:ayah',
        # y='ayah_link',
        # y='index',
        color='query',
        hover_data={
        'ayah_link':True,
        'query': False, 
        'surah:ayah': False,
        'index': False
        },
    #  color_continuous_scale=["green","yellow","orange","red"],
        # color_discrete_map=colMap,
        # height=((len(df))*7)+200,
        width=((len(df["query"].unique()))*20)+600,
        # height=1200,
        # width=(len(sorter))/8+500,
        height=(len(sorter))/8+500+8*max([len(s) for s in df["query"].unique()]),
    )

    # fig = make_subplots(
    #     specs=[[{"secondary_y": True}]]
    # )

    # # fig.layout=go.Layout(clickmode='event+select')
    
    fig.update_layout(
    #  hovermode=False,
        clickmode='event+select',
        hoverdistance=-1,
        # hovermode='y',
        hoverlabel=dict(
           font=dict(
              size=15,
              color='rgb(0,0,0)',              
           ),
            # font_size=15,
            # font_color='rgb(0,0,0)',
            bgcolor = 'rgb(220,220,250)'
        )
    #  itemclick='toggle'
    )

    # for rt in dicti:
    #     if rt != '' and rt != None:
    #       tbl = dataGrabber(tafs,rt,dicti[rt])
    #       fig.add_trace(
    #           go.Scatter(
    #               y=tbl.ayah_link,
    #               x=tbl['surah:ayah'],
    #               name=rt +  f' ({dicti[rt]})' if dicti[rt] != None or dicti[rt] != '' else '',
    #               mode='markers',
    #               # customdata=dataGrabber(tafs,rt,dicti[rt]).ayah_link,
    #               hoverinfo='y+x'
    #               # marker=dict(
    #               # color='rgb(34,163,192)'
    #               # )
    #           ),
    #           secondary_y=True
    #       )
    fig.update_yaxes(
        categoryorder='array',
        categoryarray=sorter,
        range=[0,len(sorter)],
        title=" (earlier)   -->  'Surah:Ayah' (Chronologically Ordered)  -->   (latter)"
    )
    fig.update_xaxes(
    #  showticklabels=False,
    #  range=[0,len(df)],
        title='query'
    )
    clear_output()
    fig.show()


def sortchron(
        # dicti={},
        # qL=[],
        qL,
        pres='plot',
        refLng='english',
    ):
    sorter = getSorter()
    # pres = confPres(pres=pres)
    # tafs = confLng(refLng=refLng)
    tafs = tafsDict[refLng]
    instLstAgg = aggregLsts(qL,tafs)
    import pandas as pd
    df = pd.DataFrame(instLstAgg,columns = ["surah:ayah","position","string","meaning","ayah_link","query"])
    df['position'] = df['position'].astype('int')
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    df['position'] = df['position'].astype('str')
    df.reset_index(drop=True,inplace=True)
    # df.reset_index(inplace=True)
    
    colMap = getColMap(df["query"].unique())
    # display()
    if pres == "table":
        return tabular(df,colMap,sorter)
    if pres == "plot":
        plotDf(df,colMap,sorter)
    # qL = []

    # from IPython import get_ipython 
    # get_ipython().magic('reset -sf')


def finish_query_f(button,container=widg.VBox([]),qL=[],pres='plot',refLng='english'):
    # global qL
    for k in range(len(container.children)-1,-1,-1):
        optStC = container.children[k].children[1]
        optSt = []
        for l in range(len(optStC.children)-1,-1,-1):
            combC = optStC.children[l]
            if not len(combC.children) < 2:
                vrsDisFld = combC.children[0].children[0]
                print(vrsDisFld.description, vrsDisFld.value)
                # combObj = combClass()
                combObj = {"strL":[],"vrsDis":vrsDisFld.value}
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
                    if strCFlds[0].value != '' or strCFlds[1].value != '':
                        for j in range(7):
                            fld = strCFlds[j]
                            # print(fld.description, fld.value)
                            # print(strD[strAtts[j]], fld.value)
                            # strD.strObj[strAtts[j]] = fld.value
                            strD[strAtts[j]] = fld.value
                        # print(strD)
                        # print(strD.strObj)
                        # combObj.strL.append(strD.strObj)
                        combObj["strL"].append(strD)
                # if len(combObj.strL) > 0:
                if len(combObj["strL"]) > 0:
                    optSt.append(combObj)
            if len(optSt) > 0:
                print(qL)
                qL.append(optSt)
                # qL.append(combObj.__dict__)
        # dg = aggregLsts(qL)
        # sortchron(dg)
        sortchron(qL,pres,refLng)
        
        # return dg


def intctv(
    qL=[],
    pres='',refLng=''
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
    finish_query_B.on_click(partial(finish_query_f,container=container,qL=qL,pres=pres,refLng=refLng))
    # Container to hold all groups of widgets
    # Initialize the first group of widgets
    optStWdgCl(
        # 1
        combs,
        container
        )
    clear_output()
    display(finish_query_B,container,)

def confFcheck(pres='plot',refLng='english'):
    if pres not in presD.values():
      if str(pres) in presD.keys():
        pres=presD[pres]
      else:
        presFound = False
        with open("./cnf.json") as f:
            import json
            confD = json.loads(f.read())
            print(confD)
            if 'pres' in confD.keys():
                print('pres found in cnf.txt', pres)
                if confD['pres'] in presD.values():
                    pres = confD['pres']
                    presFound = True
        if not presFound:
            print('pres not found in cnf.txt')
            pres = "plot"
    if refLng not in refLngD.values():
      if str(refLng) in refLng.keys():
        refLng=refLngD[refLng]
      else:
        refLngFound = False
        with open("./cnf.json") as f:
            import json
            confD = json.loads(f.read())
            print(confD)
            if 'refLng' in confD.keys():
                print('refLng found in cnf.txt', refLng)
                if confD['refLng'] in presD.values():
                    refLng = confD['refLng']
                    refLngFound = True
        if not refLngFound:
            refLng = "english"
    return pres, refLng

def querize(
        # qL
        qL=[],
        # qL=[],
        pres='plot',
        # tafs='ar-tafsir-al-tabari',
        refLng='english',
    ):
    global presD
    global refLngD
    pres, refLng = confFcheck(pres,refLng)
    presW = widg.Dropdown(description="Presentation style",options=presD.values(),value=pres)
    refLngW = widg.Dropdown(description="Tafsir Language",options=refLngD.values(),value=refLng)
    def submConf(button,qL=qL,pres=presW.value,refLng=refLngW.value):
        clear_output()
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
            intctv(qL,pres,refLng)
        else:
            qL = [
                [combClass(**comb).combObj for comb in optLs]
                for optLs in qL
            ]
            # colMap = getColMap(dicti)
            sortchron(qL,pres,refLng)
    confSetB = widg.Button(description='Enter configuration')
    from functools import partial
    confSetB.on_click(partial(submConf,qL=qL,pres=presW.value,refLng=refLngW.value))
    confCont = widg.VBox([presW,refLngW,confSetB])
    clear_output()
    display(confCont)