from .intersct import intersct
from ...data.repository.row2DictCL import row2DictCl

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
