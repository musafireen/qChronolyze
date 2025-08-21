
from ..backend.utils import qLModder

from ..frontend.components.intctv import intctv

from ..frontend.sortChron import sortchron

def intOrNot(qL,pres,refLng,qyArLegSch):
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
    # return