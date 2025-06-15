from ...shared.constants import arbVwlsDict

def remVwls(stri,schm="bkwSch"):

    if schm == "arbSch":
        for chr in arbVwlsDict.values():
            stri = stri.replace(chr,'')
    if schm == "bkwSch":
        for chr in arbVwlsDict.keys():
            stri = stri.replace(chr,'')
    return stri
