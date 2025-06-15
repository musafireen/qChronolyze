
from ..imports import clear_output

from ...shared.constants import bkwSch2arbSch

def plotDf(df,colMap,sorter):
    import plotly.express as px
    # import plotly.graph_objects as go
    # from plotly.subplots import make_subplots
    # from plotly.offline import iplot, init_notebook_mode
    # init_notebook_mode()

    # ay_ln = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ' .. '.join(group['ayah_link'])).reset_index()
    # pos = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ','.join(group['position'])).reset_index()

    # df = df.drop_duplicates(subset=['surah_ayah', 'query'], keep="first").reset_index(drop=True)
    # ay_ln = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ' .. '.join(group['ayah_link'])).reset_index()
    # pos = df.groupby(['surah_ayah', 'query'],observed=True).apply(lambda group: ','.join(group['positions'])).reset_index()

    df = df.drop_duplicates(subset=['surah_ayah', 'query'], keep="first").reset_index(drop=True)

    # df["positions"] = pos[0]
    # df["ayah_link"] = ay_ln[0]
    
    # df["ayah_link"] = list(df["surah_ayah"]) + df["ayah_link"]
    # df["ayah_link"] = list(df["surah_ayah"]) + df["ayah_link"]
    df.reset_index(inplace=True)

    # width=((len(df["query"].unique()))*20)+600
    # print(width,len(df["query"].unique()), df["query"].unique())
    
    isArabic=False if len(df) == 0 else df.loc[0,"query"][0] in bkwSch2arbSch.values()
    max_leg_width=False if len(df) == 0 else len(max(df["query"].unique(),key=len))
    legend_size=12 if not isArabic else 14
    xtick_size=12 if not isArabic else 14
    datapoint_width=20
    datapoint_height=8
    tick_angle=45
    import math
    fig = px.scatter(
        df,
        # x='surah_ayah',
        x='query',
        # y='surah_ayah',
        y='surah_ayah',
        # y='ayah_link',
        # y='index',
        color='query',
        hover_data={
        'ayah_link':True,
        'query': False, 
        'surah_ayah': False,
        # 'surah_ayah': False,
        'index': False
        },
    #  color_continuous_scale=["green","yellow","orange","red"],
        # color_discrete_map=colMap,
        # height=((len(df))*7)+200,
        width=((len(df["query"].unique()))*datapoint_width) + 
            max_leg_width*legend_size + 
            300,
        # height=1200,
        # width=(len(sorter))/8+500,
        height=(len(sorter))/datapoint_height+max_leg_width*xtick_size*math.sin(tick_angle)+500,
    )

    # fig = make_subplots(
    #     specs=[[{"secondary_y": True}]]
    # )

    # # fig.layout=go.Layout(clickmode='event+select')
    fig.update_layout(
    #  hovermode=False,
        legend=dict(font=dict(size=legend_size)),
        clickmode='event+select',
        hoverdistance=-1,
        # hovermode='y',
        hoverlabel=dict(
           font=dict(
              size=15,
              color='rgb(0,0,0)',              
           ),
            # font_size=15,
            # font_color='rgb(0,0,0)',
            bgcolor = 'rgb(220,220,250)'
        ),
        # xaxis=dict(dtick=1),
    #  itemclick='toggle'
    )

    # for rt in dicti:
    #     if rt != '' and rt != None:
    #       tbl = dataGrabber(tafs,rt,dicti[rt])
    #       fig.add_trace(
    #           go.Scatter(
    #               y=tbl.ayah_link,
    #               x=tbl['surah_ayah'],
    #               name=rt +  f' ({dicti[rt]})' if dicti[rt] != None or dicti[rt] != '' else '',
    #               mode='markers',
    #               # customdata=dataGrabber(tafs,rt,dicti[rt]).ayah_link,
    #               hoverinfo='y+x'
    #               # marker=dict(
    #               # color='rgb(34,163,192)'
    #               # )
    #           ),
    #           secondary_y=True
    #       )
    
    fig.update_traces(
        hovertemplate=
        "query: %{x}<br>"
        "surah_ayah: %{y}<br>"
        "%{customdata[0]}"
        "<extra></extra>"
    )

    fig.update_yaxes(
        categoryorder='array',
        categoryarray=sorter,
        range=[0,len(sorter)],
        title=" (earlier)   -->  'Surah_Ayah' (Chronologically Ordered)  -->   (later)"
        # title=" (earlier)   -->  'Surah:Ayah' (Chronologically Ordered)  -->   (later)"
    )
    fig.update_xaxes(
    #  showticklabels=False,
    #  range=[0,len(df)],
        title='(earlier)  -->  queries  -->  (later)',
        dtick=1,
        tickangle=tick_angle,
        tickfont=dict(size=xtick_size)
    )

    clear_output()
    fig.show()
