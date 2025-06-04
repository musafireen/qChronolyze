
from backend.utils import qLModder, confFcheck

from .components.intctv import intctv

from .sortChron import sortchron

from ..shared.constants import lng2InpSchD, presD, refLngD

from .imports import widg, clear_output, display


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


