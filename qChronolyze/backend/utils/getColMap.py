

def getColMap(dicti):
    import numpy as np
    colMap = {}
    leng = len(dicti)
    lwrLmt = 100
    uprLmt = 250
    p = np.linspace(lwrLmt,uprLmt,num=leng)
    for idx in range(1,leng+1):
        # n1=rand.randn()
        # n2=rand.randn()
        # i1=rand.randint(0,50)
        # i2=rand.randint(0,50)
        # clr=f"rgb({50+(100/leng)*idx})"
        # colMap[df["query"].unique()[idx]] = f"rgb({clr},{clr},{clr})" 
        #   rd = int(p[idx-1])
        #   radialDist = (rd - lwrLmt) if (rd - lwrLmt) < (uprLmt - rd) else (uprLmt - rd)
        #   colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        #   pair = dicti[idx-1]
        #   colMap[f"{list(pair.keys())[0]} ({list(pair.values())[0]})"] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        quer = dicti[idx-1]
        colMap[quer] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
        # colMap[f"{list(dicti.keys())[idx-1]} ({list(dicti.values())[idx-1]})"] = f'rgb({rd},{gn},{bl})' 
        # print(f'rgb({int(p[idx-1])},{int(p[-idx]-50)},25)' )
    return colMap
