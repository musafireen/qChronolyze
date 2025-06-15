# from ..utils import qLModder

# from ...frontend.components.intctv import intctv

# from ...frontend.sortChron import sortchron

from ...shared.constants import lng2InpSchD, presD, refLngD, qL, USR_CONF_FILE

from ...frontend.imports import clear_output

from .intOrNot import intOrNot

def submConf(button,presW=None,refLngW=None,qL=qL,qyArLegSchW=lng2InpSchD["arabic"][-1]):
    pres = presW.value if presW != None else presD[-1]
    refLng = refLngW.value if refLngW != None else refLngD[-1]
    qyArLegSch = qyArLegSchW.value
    clear_output()
    with open(USR_CONF_FILE, 'w+') as f:
        import json
        f.write(json.dumps({"pres":pres,"refLng":refLng}))
    if type(qL) != type([]):
        print("Invalid root-filter key value pairs")
        # dicti={}
        qL=[]
    
    intOrNot(qL,pres,refLng,qyArLegSch)
    # if dicti=={}:
    # if qL==[]:
    # #     finished=False
    # #     # while finished==False:
    # # if finished==False:
    #     print("interactive")
    #     intctv(qL,pres,refLng,qyArLegSch)
    # else:
    #     print("not interactive")
    #     qL = qLModder(qL,qyArLegSch)
    #     # colMap = getColMap(dicti)
    #     sortchron(qL,pres,refLng)

