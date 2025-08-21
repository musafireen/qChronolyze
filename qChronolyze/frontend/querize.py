
from ..backend.utils import confFcheck
from . import submConf

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

    confSetB = widg.Button(description='Enter configuration')
    from functools import partial
    confSetB.on_click(partial(submConf,presW=presW,refLngW=refLngW,qL=qL,qyArLegSchW=qyArLegSchW))
    confCont = widg.VBox([presW,refLngW,qyArLegSchW,confSetB])
    clear_output()
    display(confCont)


