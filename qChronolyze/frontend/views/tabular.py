from ...shared.constants import posSerDict
from ..imports import clear_output, display


def tabular(df,colMap,sorter):
    # import pandas as pd
    # print(df)

    # for rt in dicti.keys():
    #     instLst = aggregLsts(rt,dicti[rt])
    #     dfNew = pd.DataFrame.from_records(instLst)
    #     df = pd.concat([df, dfNew], axis=0)

    print(f'dataframe length: {len(df)}')
    # df.drop(columns=[
    # #  "query",
    #     "index"
    #     ],
    #     inplace=True
    # )

    # compareDict = {}
    # for i in range(len(sorter)):
    #     compareDict[sorter[i]]=i

    def words_before_f(row):
        return posSerDict[row['surah_ayah'] +':'+ str( min([int(pos) for pos in row['positions']]) )]

    # df['words_before'] = df.apply(words_before_f,axis=1)
    if len(df) > 0:
        df.insert( 
            0, 
            'words_before', 
            value=df.apply(lambda row: words_before_f(row), axis=1 )
            # list(
            #     map(
            #         lambda x: words_before_f(x),
            #         # df["surah"]
            #         df,
            #         # df["surah_ayah"]
            #         axis = 1
            #         )
            # )
    )
    # df.insert( 0, 'verses_before',    list(
    #     map(
    #         lambda x: compareDict[x],
    #         # df["surah"]
    #         df["surah_ayah"]
    #         # df["surah_ayah"]
    #         )
    #     )
    # )

    from IPython.core.display import HTML

    def colo(s):
        # print(s)
        return [
            f'background-color: {colMap[s["query"]]};'
            + 'foreground-color: black;'
            + 'color: black;'
            + 'opacity: 1;' 
        ] * len(s)
    clear_output()
    display(
        HTML(df.style.apply(
                colo , axis=1
            ).to_html(render_links=True,escape=False,index=False)
        )

    )
