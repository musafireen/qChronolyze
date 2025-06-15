from ...shared.constants import presD, refLngD, USR_CONF_FILE

def confFcheck(pres='plot',refLng='english'):
    
    if pres not in presD.values():
      if str(pres) in presD.keys():
        pres=presD[pres]
      else:
        presFound = False
        with open(USR_CONF_FILE) as f:
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
        with open(USR_CONF_FILE) as f:
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
