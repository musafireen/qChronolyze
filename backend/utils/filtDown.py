from ...shared.constants import surAyPosStrAdvWrdMD
from .dataGrabber import dataGrabber

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
