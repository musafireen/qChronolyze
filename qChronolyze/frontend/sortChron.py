
from ..shared.constants import tafsDict

from ..backend.utils import getSorter, aggregLsts, getColMap

from .views.plotDf import plotDf

from .views.tabular import tabular

def sortchron(
        # dicti={},
        # qL=[],
        qL,
        pres='plot',
        refLng='english',
        # qyArLegSch=lng2InpSchD["arabic"][-1]
    ):
    sorter = getSorter()
    # pres = confPres(pres=pres)
    # tafs = confLng(refLng=refLng)
    tafs = tafsDict[refLng]
    print(f"qL in sortchron: {qL}")
    instLstAgg = aggregLsts(qL,tafs)
    import pandas as pd
    # clear_output()
    # print([obj.__dict__ for obj in instLstAgg])
    df = pd.DataFrame([obj.__dict__ for obj in instLstAgg],columns = ["surah_ayah","positions","strings","meanings","ayah_link","query"])
    # df = pd.DataFrame(instLstAgg,columns = ["surahayah","position","string","meaning","ayah_link","query"])
    # df['positions'] = df['positions'].astype('int')
    # df['surah_ayah'] = pd.Categorical(df['surah_ayah'], categories=sorter, ordered=True)
    # df.sort_values(["surah_ayah","position"],inplace=True)
    df['surah_ayah'] = pd.Categorical(df['surah_ayah'], categories=sorter, ordered=True)
    df.sort_values(
        ["surah_ayah","positions"],
        key=lambda x: x.map(min) if x.name=='positions' else x,
        inplace=True
    )
    # df.sort_values(["surah_ayah","position"],inplace=True)
    # df['position'] = df['position'].astype('str')
    df.reset_index(drop=True,inplace=True)
    # df.reset_index(inplace=True)
    
    colMap = getColMap(df["query"].unique())
    # display()
    if pres == "table":
        return tabular(df,colMap,sorter)
    if pres == "plot":
        plotDf(df,colMap,sorter)
    # qL = []

    # from IPython import get_ipython 
    # get_ipython().magic('reset -sf')
