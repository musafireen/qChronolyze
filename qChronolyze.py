import ipywidgets as widg
from ipywidgets import interactive as intct
from IPython.display import display, clear_output

# List to track widget groups

arbVwlsDict = {
        "a": "َ",
        "u": "ُ",
        "i": "ِ",
        "~": "ّ",
        "o": "ْ",
        "^": "ٓ",
        "#": "ٔ",
        "`": "ٰ",
        "F": "ً",
        "N": "ٌ",
        "K": "ٍ",
        "_": "ـ",
}

arbConsD = {
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
        "{": "ٱ",
    }

arbSemiD = {
        # ":": "ۜ",
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

bkwSch2arbSch = {
    **arbVwlsDict,
    **arbConsD,
    **arbSemiD,
}

bkw2Simpl = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","i"),
    ("uw(?![aiu])","u"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","a"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]",""),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","t"),
    ("!","n"),
    ("D","d"),
    ("Z","z"),
    ("S","s"),
    (r"\$","sh"),
    ("x","kh"),
    ("H","h"),
    ("g","gh"),
    ("E",""),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

bkw2Ala = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","ī"),
    ("uw(?![aiu])","ū"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","ā"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]","'"),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","ṭ"),
    ("!","n"),
    ("D","ḍ"),
    ("Z","ẓ"),
    ("S","ṣ"),
    (r"\$","ś"),
    ("x","kh"),
    ("H","ḥ"),
    ("g","gh"),
    ("E","‘"),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

arbSch2bkwSch = {
    v : k for k,v in bkwSch2arbSch.items()
}

iasSch2arbSch = {

}
bkwSch2iasSch = {

}

arbBen2arbSch = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","i"),
    ("uw(?![aiu])","u"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","a"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]",""),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","t"),
    ("!","n"),
    ("D","d"),
    ("Z","z"),
    ("S","s"),
    (r"\$","sh"),
    ("x","kh"),
    ("H","h"),
    ("g","gh"),
    ("E",""),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

arbBen2bkwSch = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","i"),
    ("uw(?![aiu])","u"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","a"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]",""),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","t"),
    ("!","n"),
    ("D","d"),
    ("Z","z"),
    ("S","s"),
    (r"\$","sh"),
    ("x","kh"),
    ("H","h"),
    ("g","gh"),
    ("E",""),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

arbBenSimp2arbSch = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","i"),
    ("uw(?![aiu])","u"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","a"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]",""),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","t"),
    ("!","n"),
    ("D","d"),
    ("Z","z"),
    ("S","s"),
    (r"\$","sh"),
    ("x","kh"),
    ("H","h"),
    ("g","gh"),
    ("E",""),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

arbBenSimp2bkwSch = [
    (r"(?<!^)(.)(\1)\~","\\1\\1"),
    (r"(?<!^)(.)\~","\\1\\1"),
    (r"(?<=^)(.)\~","\\1"),
    ("(?:iy|iY)(?![aiu])","i"),
    ("uw(?![aiu])","u"),
    (r"(?:ay`|aw`|aY\`|a\,\`|a\.\`|a\`|\`|aY|a\,|a\.|aA|A\^|\^)+","a"),
    ("o",""),
    ("F","an"),
    ("N","un"),
    ("K","in"),
    (r"(?<=^)\{(?!l)","i"),
    (r"(?<=^)\{(?=l)","a"),
    (r"(?<=^)A(?!l)","i"),
    (r"(?<=^)A(?=l)","a"),
    (r"[\%\+\-\_]",""),
    (r"(?<!^)[\>\<\&\}\#]",""),
    (r"(?<=^)[\>\<\&\}\#]",""),
    (r"\[","m"),
    ("v","th"),
    (r"\*","dh"),
    ("T","t"),
    ("!","n"),
    ("D","d"),
    ("Z","z"),
    ("S","s"),
    (r"\$","sh"),
    ("x","kh"),
    ("H","h"),
    ("g","gh"),
    ("E",""),
    ("p","h"),
    # ("A",""),
    # ("[0-9]",""),
]

presD={'1':'table','2':'plot'}

refLngD={'1':'arabic','2':'bengali','3':'english'}

tafsDict={"arabic":"ar-tafsir-al-tabari","bengali":"bn-tafseer-ibn-e-kaseer","english":"en-tafisr-ibn-kathir"}

arStrTypD = {
    "root": "root",
    "stem": "stem",
    "lemma": "lem",
    # "english": "eng",
    # "All": "All"
}
strTypD = {
    # "root": "root",
    # "stem": "stem",
    # "lemma": "lem",
    **arStrTypD,
    "english": "eng",
    "All": "All"
}

strTypL = list(strTypD.keys())

arFrmL = [
    # "All",
    "i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii",
]

frmL = [
    "All",
    *arFrmL,
]

arPoSpD = {
    'All': 'All',
    # '': 'All',
    'Noun': 'N',
    'Proper noun': 'PN',
    'Adjective': 'ADJ',
    'Imperative verbal noun': 'IMPN',
    'Verb': 'V',
    'Personal pronoun': 'PRON',
    'Demonstrative pronoun': 'DEM',
    'Relative pronoun': 'REL',
    'Time adverb': 'T',
    'Location adverb': 'LOC',
    "Preposition": "P", 
    "Emphatic lām prefix": "EMPH", 
    "Imperative lām prefix": "IMPV", 
    "Purpose lām prefix": "PRP", 
    "Coordinating conjunction": "CONJ", 
    "Subordinating conjunction": "SUB", 
    "Accusative particle": "ACC", 
    "Amendment particle": "AMD", 
    "Answer particle": "ANS", 
    "Aversion particle": "AVR", 
    "Particle of cause": "CAUS", 
    "Particle of certainty": "CERT", 
    "Circumstantial particle": "CIRC", 
    "Comitative particle": "COM", 
    "Conditional particle": "COND", 
    "Equalization particle": "EQ", 
    "Exhortation particle": "EXH", 
    "Explanation particle": "EXL", 
    "Exceptive particle": "EXP", 
    "Future particle": "FUT", 
    "Inceptive particle": "INC", 
    "Particle of interpretation": "INT", 
    "Interogative particle": "INTG", 
    "Negative particle": "NEG", 
    "Preventive particle": "PREV", 
    "Prohibition particle": "PRO", 
    "Resumption particle": "REM", 
    "Restriction particle": "RES", 
    "Retraction particle": "RET", 
    "Result particle": "RSLT", 
    "Supplemental particle": "SUP", 
    "Surprise particle": "SUR", 
    "Vocative particle": "VOC", 
    "Quranic initials": "INL", 
}


poSpD = {
    "All": "All",
    **arPoSpD,
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
        "arabic_Scheme",
        "simplified_Scheme",
        "ALA_Scheme",
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
    "ALA_Scheme": "alaSch",
    "simplified_Scheme": "simplSch",
    "arabic_Scheme": "arbSch",
    "bengali_Scheme": "bngSch",
    "english_Scheme": "engSch",
}

import json
with open('data/striD.json') as f:
    striD = json.loads(f.read())

with open('data/surAyPosStrAdvWrdMD.json') as f:
    surAyPosStrAdvWrdMD = json.loads(f.read())

# with open("data/striSuAyPosWMD.json") as f:
#     striSuAyPosWMD = json.loads(f.read())

with open("posSerDict.json") as f:
    posSerDict = json.loads(f.read())

wrdCount = len(posSerDict)

sameVrsIndicator = wrdCount

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

        with open(f'sorter.json', 'w+') as f:
            f.write(json.dumps(sorter))

        # with open(f'posDict.json') as f:
        #     posDict = json.loads(f.read())

        posSerDict = {

        }

        ser = 0
        for i in range(len(sorter)):
            surAy = sorter[i]
            sur,ay = surAy.split(":")
            posLs = list(surAyPosStrAdvWrdMD[sur][ay].keys())
            for j in range(len(posLs)):
                ser += 1
                surAyPos = ":".join([sur,ay,posLs[j]])
                posSerDict[surAyPos] = ser
        with open(f'posSerDict.json', 'w+') as f:
            f.write(json.dumps(posSerDict))

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

def remVwls(stri,schm="bkwSch"):

    if schm == "arbSch":
        for chr in arbVwlsDict.values():
            stri = stri.replace(chr,'')
    if schm == "bkwSch":
        for chr in arbVwlsDict.keys():
            stri = stri.replace(chr,'')
    return stri

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


class row2DictCl:
        # lnkStyle = ' '
    fontSize = '18'
    fontCol = 'rgb(0,0,150)'
    shPx = str(int(fontSize)/100*0)
    shCol = '#000000'
    bgCol = 'rgb(220,220,250)'
    txtShad = ''
    # txtShad = f'text-shadow:{shPx}px {shPx}px 0 {shCol}, {shPx}px -{shPx}px 0 {shCol}, -{shPx}px -{shPx}px 0 {shCol}, -{shPx}px {shPx}px 0 {shCol};'
    # lnkStyle = "style='background-color:rgb(250,250,250);font-size:30px;color:rgb(0,0,150);-webkit-text-stroke-width:5px;-webkit-text-stroke-color:white' "
    lnkStyle = f" style='background-color:{bgCol};font-size:{fontSize}px;color:{fontCol};{txtShad}'"
    # lnkStyle = ''
    # lnkStyle = "style='color:rgb(250,250,250);-webkit-text-stroke-width:1px;-webkit-text-stroke-color:rgb(0,0,0);' "
    def __init__(self,surah='',ayah='',positions=[],query='',tafs="ar-tafsir-al-tabari"):
        # print(surah, ayah, positions)
        ayWrds = [
            # posD["wrd"] 
            posD["wrd"] 
            for posD in surAyPosStrAdvWrdMD[surah][ayah].values()
                  
        ]
        positions = [int(pos) for pos in positions]
        ayWrdsHgh = [
            f"<b><i>{ayWrds[i]}</i></b>"
            if i+1 in positions
            else ayWrds[i]
            for i in range(len(ayWrds))
        ]
        txtLwLmt = max(0,min(positions)-4)
        txtUpLmt = min(len(ayWrds),max(positions)+5)
        ayTxt = " ".join( ayWrdsHgh[txtLwLmt:txtUpLmt] )

        # surAy = ":".join([surah,ayah])
        self.surah_ayah = ":".join([surah,ayah])
        # self.surah = surah
        # self.ayah = ayah
        self.positions = positions
        # self.position_lowest = min([int(pos) for pos in positions])
        self.strings = [ surAyPosStrAdvWrdMD[surah][ayah][str(pos)]["wrd"] for pos in positions ]
        self.meanings = [ surAyPosStrAdvWrdMD[surah][ayah][str(pos)]["mean"] for pos in positions]
        self.ayah_link = f"<a{self.lnkStyle} href='https://quran.com/{self.surah_ayah}/tafsirs/{tafs}'>{ayTxt}</a>"
        # self.ayah_link = f"<a{self.lnkStyle}>{ayTxt}</a> <a href='https://quran.com/{self.surah_ayah}/tafsirs/{tafs}'>Tafs</a>"
        self.query = query
    

def qLModder(qL,qyArLegSch=lng2InpSchD["arabic"][-1]):
    qLMod = [
                # [combClass(**comb).combObj for comb in optLs]
                [combClass(**comb,qyArLegSch=qyArLegSch) for comb in optLs]
                for optLs in qL
            ]
    return qLMod


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


def filtDown(strObj):
    stri = strObj.stri
    flt = strObj.flt
    print(f"for string: {stri}")
    # stri = strObj["stri"]
    # flt = strObj["flt"]
    import re
    # instLst = dataGrabber(strObj)
    instD = dataGrabber(strObj)
    instLstFiltered =  list(
        filter( 
            lambda row : 
            len(re.compile(str(flt).lower()).findall(
                surAyPosStrAdvWrdMD[row[0][1][2]]["mean"].lower())
            ) > 0 
            or len(re.compile(str(stri)).findall(
                surAyPosStrAdvWrdMD[row[0]][row[1]][row[2]]["mean"])
            ), 
            instD
        )
    )
    # instLstFiltered =  list(
    #     filter( 
    #         lambda row : 
    #         len(re.compile(str(flt).lower()).findall(
    #             surAyPosStrAdvWrdMD[row[0][1][2]]["mean"].lower())
    #         ) > 0 
    #         or len(re.compile(str(stri)).findall(
    #             surAyPosStrAdvWrdMD[row[0]][row[1]][row[2]]["mean"])
    #         ), 
    #         instLst
    #     )
    # )
    # instLstFiltered =  list(filter( lambda row : len(re.compile(str(flt).lower()).findall(row.meaning.lower())) > 0 or len(re.compile(str(stri)).findall(row.meaning)), instLst))
    # instLstFiltered =  list(filter( lambda row : len(re.compile(str(flt).lower()).findall(row["meaning"].lower())) > 0 or len(re.compile(str(stri)).findall(row["meaning"])), instLst))
    # instLstFiltered = [ { **row , "query" : f"{rt} ({flt})"} for row in instLstFiltered ]
    return instLstFiltered

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

def aggregLsts(
        qL,
        tafs="ar-tafsir-al-tabari",
        # qyArLegSch=lng2InpSchD["arabic"][-1]
    ):
    instLstAgg = []
    for optSt in qL:
        # print(optSt)
        lblParts = []
        optStInsts = []
        # print(f"optStInsts before comb: {optStInsts}")
        for comb in optSt:
            # print(comb)
            strL = comb.strL
            # strL = comb["strL"]
            lblParts += [comb.lbl]
            # lblParts += [' + '.join([ 
            #     f'{rtTrns(strObj.stri,lngD[strObj.inpLng],inpLngSchD[strObj.inpSch],inpLngSchD[qyArLegSch])} ({strObj.flt})' for 
            #     # f'{strObj["stri"]} ({strObj["flt"]})' for 
            #     strObj 
            #     in strL
            # ])]
            # print(f"optStInsts after comb: {optStInsts}")
            combInstLst = intersct(comb)
            # optStInsts += combInstLst
            optStInsts = [*optStInsts,*combInstLst]
        lbl = ' / '.join(lblParts)
        # instLst = [ { **inst, "query": lbl } for inst in optStInsts  ]
        
        # print("optStInsts",optStInsts)
        # for inst in optStInsts:
        for i in range(len(optStInsts)):
            optStInsts[i] = [*optStInsts[i], lbl, tafs ]
            # inst["query"] = lbl
            # inst["query"] = lbl
        # instLstAgg += optStInsts
        instLstAgg = [*instLstAgg,*[row2DictCl(*optStInst) for optStInst in optStInsts ]]
        # instLstAgg = [*instLstAgg,*optStInsts]
        # instLstAgg += instLst
    # for row in instLstAgg:
    #     row["ayah_link"]= f"<a {lnkStyle}href='https://quran.com/{row.surah_ayah}/tafsirs/{tafs}'>{row.ayah_link}</a>"
        # "ayah_link": f"<a href='https://quran.com/{row['surah_ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
    # instLstAgg = [ { 
    #     **row, 
    #     "ayah_link": f"<a {lnkStyle}href='https://quran.com/{row['surah_ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
    #     # "ayah_link": f"<a href='https://quran.com/{row['surah_ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
    #     } for row in instLstAgg ]
    # instLstAgg = [ { 
    #     **row.__dict__, 
    #     "ayah_link": f"<a {lnkStyle}href='https://quran.com/{row.surah_ayah}/tafsirs/{tafs}'>{row.ayah_link}</a>"
    #     # "ayah_link": f"<a href='https://quran.com/{row['surah_ayah']}/tafsirs/{tafs}'>{row['ayah_link']}</a>"
    #     } for row in instLstAgg ]
    
    print(f"\ntotal {len(instLstAgg)} instances found")
    return instLstAgg


class strObjClass:
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


class combClass:
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
            strObjClass(**strObj,qyArLegSch=qyArLegSch) if strObj==strL[0]  
            else strObjClass(wrdDisPos=wrdDis,**strObj,qyArLegSch=qyArLegSch) if ("wrdDisPos" not in strObj.keys()) 
            else strObjClass(**strObj,qyArLegSch=qyArLegSch)
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
    inpSchArSt = strObjClass.inpSchArSt
    wrdDisPosSt = strObjClass.wrdDisPosSt
    wrdDisNegSt = strObjClass.wrdDisNegSt
    strUnwantedSt = strObjClass.strUnwantedSt

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
        strObWdgCl.strUnwantedSt=self.strUnwantedW.value
        strObWdgCl.wrdDisPosSt=self.wrdDisPosW.value
        strObWdgCl.wrdDisNegSt=self.wrdDisNegW.value

        strObWdgCl(
            self.parentComb
                                 )

    def delStrObjM(self,button,
                   ):
        if len(self.parentComb.strngs) > 1:
            if self.strContainer in self.parentComb.strngs:
                self.parentComb.strngs.remove(self.strContainer)
                self.parentComb.comb_container.children = [w for w in self.parentComb.comb_container.children if w != self.strContainer]

    def findM(self,button,
                   ):
        self.striW.value = striD[self.findW.value]["stri"][inpLngSchD[self.inpSchArSt]]
        self.strTypeW.value = striD[self.findW.value]["typ"]
        self.inpSchW.value = self.inpSchArSt

    def __init__(self,
                 parentComb,
                ):

        self.parentComb = parentComb
        
        self.findW = widg.Combobox(
            options=list(striD.keys()),
            description='Find',
            value=list(striD.keys())[0]
        )
        self.striW = widg.Text(description=f"String",value=striD[self.findW.value]["stri"][inpLngSchD[self.inpSchArSt]])
        self.fltW = widg.Text(description=f"Translation_filter")
        self.strTypeW = widg.Dropdown(options=strTypL, value=striD[self.findW.value]["typ"],description=f"String_type")
        self.poSpW = widg.Dropdown(options=poSpL, value=self.poSpSt,description=f"Part_of_speech")
        self.frmW = widg.Dropdown(options=frmL, value=self.frmSt,description=f"Form")
        self.inpLngW = widg.Dropdown(options=lngL[:-1], value=self.inpLngSt,description=f"Input_language")
        self.inpSchW = widg.Dropdown(description=f"Input_scheme")
        self.entStrObjB = widg.Button(description=f"Enter String Object")
        self.delStrObjB = widg.Button(description=f"Delete String Object")
        self.findB = widg.Button(description=f"Find")
        self.entStrObjB.on_click(self.entStrObjM)
        self.delStrObjB.on_click(self.delStrObjM)
        self.findB.on_click(self.findM)
        self.inpLngW.observe(self.update_language_scheme_options)
        self.update_language_scheme_options(self)

        self.strUnwantedW = widg.ToggleButton(value=False,description='Exclude')
        self.wrdDisPosW = widg.IntText(min=0,max=sameVrsIndicator,value=self.wrdDisPosSt, description=f"Word Distance before")
        self.wrdDisNegW = widg.IntText(min=-sameVrsIndicator,max=0,value=self.wrdDisNegSt, description=f"Word Distance after")

        self.strContainer = widg.VBox(
            [
                self.striW,
                self.fltW,
                self.strTypeW,
                self.poSpW,
                self.frmW,
                self.inpLngW,
                self.inpSchW,
                self.wrdDisPosW,
                self.wrdDisNegW,
                self.strUnwantedW,
                self.entStrObjB,
                self.delStrObjB,
                self.findW,
                self.findB,
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
    wrdDisSt = combClass.wrdDisSt
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

        self.wrdDisW = widg.IntText(min=-1,max=sameVrsIndicator,value=self.wrdDisSt, description=f"Word Distance")
        self.qyLblW = widg.Text(value='', description=f"Query Label")
        self.entCombB = widg.Button(description="Enter Combination of String Objects")
        self.entCombB.on_click(self.entCombM)
        self.delCombB = widg.Button(description="Delete Combination of String Objects")
        self.delCombB.on_click(self.delCombM)

        self.comb_container = widg.HBox(
            [
                widg.VBox(
                    [
                        self.wrdDisW,
                        self.qyLblW,
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

        # self.wrdDisW = widg.IntText(min=0,max=6236,value=0, description=f"Verse Distance")
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

    # compareDict = {}
    # for i in range(len(sorter)):
    #     compareDict[sorter[i]]=i

    def words_before_f(row):
        return posSerDict[row['surah_ayah'] +':'+ str( min([int(pos) for pos in row['positions']]) )]

    # df['words_before'] = df.apply(words_before_f,axis=1)
    if len(df) > 0:
        df.insert( 
            0, 
            'words_before', 
            value=df.apply(lambda row: words_before_f(row), axis=1 )
            # list(
            #     map(
            #         lambda x: words_before_f(x),
            #         # df["surah"]
            #         df,
            #         # df["surah_ayah"]
            #         axis = 1
            #         )
            # )
    )
    # df.insert( 0, 'verses_before',    list(
    #     map(
    #         lambda x: compareDict[x],
    #         # df["surah"]
    #         df["surah_ayah"]
    #         # df["surah_ayah"]
    #         )
    #     )
    # )

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

    # ay_ln = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ' .. '.join(group['ayah_link'])).reset_index()
    # pos = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ','.join(group['position'])).reset_index()

    # df = df.drop_duplicates(subset=['surah_ayah', 'query'], keep="first").reset_index(drop=True)
    # ay_ln = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ' .. '.join(group['ayah_link'])).reset_index()
    # pos = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ','.join(group['positions'])).reset_index()

    df = df.drop_duplicates(subset=['surah_ayah', 'query'], keep="first").reset_index(drop=True)

    # df["positions"] = pos[0]
    # df["ayah_link"] = ay_ln[0]
    
    # df["ayah_link"] = list(df["surah_ayah"]) + df["ayah_link"]
    # df["ayah_link"] = list(df["surah_ayah"]) + df["ayah_link"]
    df.reset_index(inplace=True)

    # width=((len(df["query"].unique()))*20)+600
    # print(width,len(df["query"].unique()), df["query"].unique())
    
    isArabic=False if len(df) == 0 else df.loc[0,"query"][0] in bkwSch2arbSch.values()
    max_leg_width=False if len(df) == 0 else len(max(df["query"].unique(),key=len))
    legend_size=12 if not isArabic else 14
    xtick_size=12 if not isArabic else 14
    datapoint_width=20
    datapoint_height=8
    tick_angle=45
    import math
    fig = px.scatter(
        df,
        # x='surah_ayah',
        x='query',
        # y='surah_ayah',
        y='surah_ayah',
        # y='ayah_link',
        # y='index',
        color='query',
        hover_data={
        'ayah_link':True,
        'query': False, 
        'surah_ayah': False,
        # 'surah_ayah': False,
        'index': False
        },
    #  color_continuous_scale=["green","yellow","orange","red"],
        # color_discrete_map=colMap,
        # height=((len(df))*7)+200,
        width=((len(df["query"].unique()))*datapoint_width) + 
            max_leg_width*legend_size + 
            300,
        # height=1200,
        # width=(len(sorter))/8+500,
        height=(len(sorter))/datapoint_height+max_leg_width*xtick_size*math.sin(tick_angle)+500,
    )

    # fig = make_subplots(
    #     specs=[[{"secondary_y": True}]]
    # )

    # # fig.layout=go.Layout(clickmode='event+select')
    fig.update_layout(
    #  hovermode=False,
        legend=dict(font=dict(size=legend_size)),
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
        ),
        # xaxis=dict(dtick=1),
    #  itemclick='toggle'
    )

    # for rt in dicti:
    #     if rt != '' and rt != None:
    #       tbl = dataGrabber(tafs,rt,dicti[rt])
    #       fig.add_trace(
    #           go.Scatter(
    #               y=tbl.ayah_link,
    #               x=tbl['surah_ayah'],
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
    
    fig.update_traces(
        hovertemplate=
        "query: %{x}<br>"
        "surah_ayah: %{y}<br>"
        "%{customdata[0]}"
        "<extra></extra>"
    )

    fig.update_yaxes(
        categoryorder='array',
        categoryarray=sorter,
        range=[0,len(sorter)],
        title=" (earlier)   -->  'Surah_Ayah' (Chronologically Ordered)  -->   (later)"
        # title=" (earlier)   -->  'Surah:Ayah' (Chronologically Ordered)  -->   (later)"
    )
    fig.update_xaxes(
    #  showticklabels=False,
    #  range=[0,len(df)],
        title='(earlier)  -->  queries  -->  (later)',
        dtick=1,
        tickangle=tick_angle,
        tickfont=dict(size=xtick_size)
    )

    clear_output()
    fig.show()


def sortchron(
        # dicti={},
        # qL=[],
        qL,
        pres='plot',
        refLng='english',
        # qyArLegSch=lng2InpSchD["arabic"][-1]
    ):
    sorter = getSorter()
    # pres = confPres(pres=pres)
    # tafs = confLng(refLng=refLng)
    tafs = tafsDict[refLng]
    print(f"qL in sortchron: {qL}")
    instLstAgg = aggregLsts(qL,tafs)
    import pandas as pd
    # clear_output()
    # print([obj.__dict__ for obj in instLstAgg])
    df = pd.DataFrame([obj.__dict__ for obj in instLstAgg],columns = ["surah_ayah","positions","strings","meanings","ayah_link","query"])
    # df = pd.DataFrame(instLstAgg,columns = ["surahayah","position","string","meaning","ayah_link","query"])
    # df['positions'] = df['positions'].astype('int')
    # df['surah_ayah'] = pd.Categorical(df['surah_ayah'], categories=sorter, ordered=True)
    # df.sort_values(["surah_ayah","position"],inplace=True)
    df['surah_ayah'] = pd.Categorical(df['surah_ayah'], categories=sorter, ordered=True)
    df.sort_values(
        ["surah_ayah","positions"],
        key=lambda x: x.map(min) if x.name=='positions' else x,
        inplace=True
    )
    # df.sort_values(["surah_ayah","position"],inplace=True)
    # df['position'] = df['position'].astype('str')
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


def finish_query_f(button,container=widg.VBox([]),qL=[],pres='plot',refLng='english',qyArLegSch=lng2InpSchD["arabic"][-1]):
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
                combClass.wrdDisSt = wrdDisFld.value
                combClass.strLSt = []
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
                                "wrdDisPos":strCFlds[7].value,
                                "wrdDisNeg":strCFlds[8].value,
                                "strUnwanted":strCFlds[9].value,
                            }
                        )
                        # print(f"combClass.strLSt: {combClass.strLSt}")
                # if len(combObj["strL"]) > 0:
                if len(combClass.strLSt) > 0:
                    # print(f"combClass.strL while appending to optSt: {combClass.strLSt}")
                    # print(f"optSt before appending comb:{optSt}")
                    optSt.append(combClass(lbl=qyLblFld.value,qyArLegSch=qyArLegSch))
                    # print(f"comb.strL appended to optSt: {optSt[-1].strL}")
                    # print(f"optSt after appending comb:{optSt}")
            if len(optSt) > 0:
                # print(f"qL before appending optSt:{qL}")
                qL.append(optSt)
                # print(f"qL after appending optSt:{qL}")
                # qL.append(combObj.__dict__)
        # dg = aggregLsts(qL)
        # sortchron(dg)
        sortchron(qL,pres=pres,refLng=refLng)
        # return qL
        # return dg


def intctv(
    qL=[],
    pres='',refLng='',qyArLegSch=lng2InpSchD["arabic"][-1]
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
    finish_query_B = widg.Button(description="Finish Query", layout=widg.Layout(width="auto"))
    finish_query_B.on_click(partial(finish_query_f,container=container,qL=qL,pres=pres,refLng=refLng,qyArLegSch=qyArLegSch))
    # Container to hold all groups of widgets
    # Initialize the first group of widgets
    optStWdgCl(
        # 1
        combs,
        container
        )
    # clear_output()
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
      if str(refLng) in refLngD.keys():
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
        qyArLegSch=lng2InpSchD["arabic"][-1],
    ):
    global presD
    global refLngD
    pres, refLng = confFcheck(pres,refLng)
    presW = widg.Dropdown(description="Presentation style",options=presD.values(),value=pres)
    refLngW = widg.Dropdown(description="Tafsir Language",options=refLngD.values(),value=refLng)
    qyArLegSchW = widg.Dropdown(description="Arabic Legend Scheme",options=lng2InpSchD["arabic"],value=qyArLegSch)
    def submConf(button,qL=qL,presW=presW,refLngW=refLngW,qyArLegSchW=qyArLegSchW):
        pres = presW.value
        refLng = refLngW.value
        qyArLegSch = qyArLegSchW.value
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
            print("interactive")
            intctv(qL,pres,refLng,qyArLegSch)
        else:
            print("not interactive")
            qL = qLModder(qL,qyArLegSch)
            # colMap = getColMap(dicti)
            sortchron(qL,pres,refLng)
    confSetB = widg.Button(description='Enter configuration')
    from functools import partial
    confSetB.on_click(partial(submConf,qL=qL,presW=presW,refLngW=refLngW,qyArLegSchW=qyArLegSchW))
    confCont = widg.VBox([presW,refLngW,qyArLegSchW,confSetB])
    clear_output()
    display(confCont)


def sAPFin(qL):
    if isinstance(qL,list):
        if len(qL) > 0:
            if isinstance(qL[0],list):
                if len(qL[0]) > 0:
                    if not isinstance(qL[0][0], combClass):
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
