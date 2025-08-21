from ...shared.constants import surAyPosStrAdvWrdMD
from ...shared.constants import USR_SORTER_PATH, USR_SURORD_PATH, USR_POSSER_PATH
from ...shared.constants import qDict_path

def getSorter():
    
    """ to tweak the sorter tweak the "surOrd.tsv" file manually """

    import os
    import json
    import csv

    with open(qDict_path) as f:
        qStr = f.read()
    qDict = json.loads(qStr)

    loadedFromDict = False


    if USR_SORTER_PATH.is_file():
        print("'sorter.json' found'")
        if os.path.getctime(USR_SORTER_PATH) > os.path.getctime(USR_SURORD_PATH):
            with open( USR_SORTER_PATH ) as f:
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
        with open(USR_SURORD_PATH) as f:
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

        with open( USR_SORTER_PATH, 'w+') as f:
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
        with open( USR_POSSER_PATH, 'w+') as f:
            f.write(json.dumps(posSerDict))

    return sorter
