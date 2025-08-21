
from pathlib import Path
import json

# from ...backend.utils import get_usr_conf_dir, get_usr_posser_path, get_usr_sorter_path, get_usr_surord_path
from ..tools.get_path import get_usr_conf_dir, get_usr_conf_file, get_usr_posser_path, get_usr_sorter_path, get_usr_surord_path

DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
# FIXED_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
FIXED_DATA_DIR = Path(__file__).resolve().parent.parent.parent / "config"
# INIT_CONF_DIR = Path(__file__).resolve().parent.parent.parent / "config"
# INIT_SORTER_PATH = INIT_CONF_DIR / "sorter.json"
# INIT_POSSER_PATH = INIT_CONF_DIR / 'posSerDict.json'
# INIT_SURORD_PATH = INIT_CONF_DIR / "surOrd.tsv"

qDict_path = FIXED_DATA_DIR / "qdict.json"

USR_CONF_DIR = get_usr_conf_dir()

USR_CONF_FILE = get_usr_conf_file()

USR_SORTER_PATH = get_usr_sorter_path()

USR_SURORD_PATH = get_usr_surord_path()

USR_POSSER_PATH = get_usr_posser_path()

USR_CONF_PATH = USR_CONF_DIR / "cnf.json"

# BASE_DIR = Path(__file__).resolve().parent
with open( DATA_DIR / 'striD.json' ) as f:
    striD = json.loads(f.read())

with open( DATA_DIR / 'surAyPosStrAdvWrdMD.json' ) as f:
    surAyPosStrAdvWrdMD = json.loads(f.read())

# with open("data/striSuAyPosWMD.json") as f:
#     striSuAyPosWMD = json.loads(f.read())

with open( USR_POSSER_PATH ) as f:
    posSerDict = json.loads(f.read())

qL=[]

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

#####__________________________________________________________#########
#### to be populated ####
bkw2Ben = {

}

#####__________________________________________________________#########
#### to be populated ####
bkw2SimpBen = {

}

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



wrdCount = len(posSerDict)

sameVrsIndicator = wrdCount