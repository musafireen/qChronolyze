def confPres(pres):
    '''Sets configuration'''
    presDict={'1':'table','2':'plot'}
    if pres not in presDict.values():
      if pres in presDict.keys():
        pres=presDict[pres]
      else:
        if pres=='' or pres=='None':
            print('No presentation style provided')
        else:
            print('Invalid presentation style:', pres)
        pres=''

        import os
        import re

        if not os.path.isfile('./cnf.txt'):
          with open('./cnf.txt', 'w') as f:
              f.write(f, '')
        with open('./cnf.txt') as f:
            txt = f.read()
        for m in re.compile('(?<=presentation\=).*?(?=$|\n)').findall(txt):
            pres+=m
        if len(pres) > 1:
            print(pres, 'found in cnf.txt')
        while pres not in presDict.values():
            print(f'{pres} not valid presentation style')
            pres = str(input(
               'Please provide presentation style:\n1 for table \n2 for plot (default)'+ 
               '\n\n(You can change later from \'cnf.txt\')'
               )).lower() or 'plot'
            if pres == '' or pres == 'None':
               pres = '2'
            if pres in presDict.keys() or pres in presDict.values():
              if pres in presDict.keys():
                pres = presDict[pres]
              import re
              import functools
              newTxt = re.compile(r'(?=^|\n)presentation\=.*(?=\n|$)').sub('',txt) + f'presentation={pres}\n'
              with open('./cnf.txt','w') as f:
                    f.write(newTxt)
    print(f'{pres} style choosen for presentation.')
    return pres

def confLng(refLng):
    lngDict={'1':'arabic','2':'bengali','3':'english'}
    if refLng not in lngDict.values():
      if refLng in lngDict.keys():
          refLng=lngDict[refLng]
      else:
        if refLng=='' or refLng=='None':
            print('No tafsir language provided')
        else:
            print('Invalid tafsir language:', refLng)
        refLng=''
        import re
        with open('./cnf.txt') as f:
            txt = f.read()
        for m in re.compile('(?<=refLng\=).*(?=$|\n)').findall(txt):
            refLng+=m
        if len(refLng) > 0:
            print(refLng, 'found in cnf.txt')
        while refLng not in lngDict.values():
            print('no valid tafsir language!')
            refLng = str(input(
               'Please choose tafsir language:\n1 for Arabic \n2 for Bengali \n3 for English (default) '+
               '\n\n(You can change later from \'cnf.txt\')'
               )).lower()
            if refLng == '' or refLng == 'None':
               refLng = '3'
            if refLng in lngDict.values() or refLng in lngDict.keys():
              if refLng in lngDict.keys():
                refLng=lngDict[refLng]
              import re
              newTxt = re.compile(r'(?=^|\n)refLng\=.*(?=\n|$)').sub('',txt) + f'refLng={refLng}\n'
              with open('./cnf.txt','w') as f:
                  f.write(newTxt)
    print(f'{refLng} language choosen for reference.')

    tafsDict={"arabic":"ar-tafsir-al-tabari","bengali":"bn-tafseer-ibn-e-kaseer","english":"en-tafisr-ibn-kathir"}
    return tafsDict[refLng]



def dataGrabber(tafs,rt,flt=''):
    '''Grabs data from corpus.quran.com & formats them'''

    flt=str(flt).lower()

    import requests
    import re
    import html2text
    import json

    links = [
        "https://corpus.quran.com/qurandictionary.jsp?q=",
        "https://corpus.quran.com/search.jsp?q=root%3A",
        "https://corpus.quran.com/search.jsp?q=lem%3A",
        "https://corpus.quran.com/search.jsp?q=stem%3A",
        "https://corpus.quran.com/search.jsp?q=",
        ]

    data=[]



    propDat = False
    import os
    if os.path.isfile(f'data/roots/{rt}'):
      try:
        with open(f'data/roots/{rt}') as f:
          tmpDat = json.loads(f.read())
        if type(tmpDat) == type([]):
          data = tmpDat
          propDat = True
      except:
        propDat = False
    if not propDat:
      for lnk in links:
          txt = requests.get(f"{lnk}{rt}").text

          txt_ex_list = re.findall('<table class="taf".*?</table>', txt)

          txt_ex=''
          for i in txt_ex_list:
              txt_ex += i

          txt_ex=re.sub(
              '<\/*span[^>]*>',
              '',
              txt_ex
          )
          txt_ex

          str2 = html2text.html2text(txt_ex)

          strng_prepare = re.sub(
              "###[^\n]*\n",
              "",
              str2
              )

          strng_prepare = strng_prepare.replace(',','').replace('"', '`').replace('\'','`')

          strng_sub =re.sub(
              r'\((\d*):(\d*):(\d*)\)\s*_([^\d+\t]+?)_\|\s*\[([^\d\t]+?)\]\(.*\)\|([^\()]+)\n',
              # '{ "surah:ayah": "\\1:\\2", "position": \\3, "word": "\\4", "meaning": "\\5", "ayah_link": "<a style=\'color:rgb(150,200,255)\' href=\'https://quran.com/\\1:\\2/tafsirs/'+tafs+'\'>\\6</a>" }, \n',
              '{ "surah:ayah": "\\1:\\2", "position": \\3, "word": "\\4", "meaning": "\\5", "ayah_link": "<a style=\'color:#95C7FF\' href=\'https://quran.com/\\1:\\2/tafsirs/'+tafs+'\'>\\6</a>" }, \n',
              # '{ "surah:ayah": "\\1:\\2", "position": \\3, "word": "\\4", "meaning": "\\5", "ayah_link": "<a href=\'https://quran.com/\\1:\\2/tafsirs/'+tafs+'\'>\\6</a>" }, \n',
              strng_prepare
          )

          strng_sub = '[' + strng_sub.replace('\n',' ')[:-3] + ']'

          dat = json.loads(strng_sub)


          if type(dat) != type([]):
            dat = []
          elif len(dat) == 0:
            dat = []
          elif type(dat[0]) != type({"a":"b"}):
            dat = []
          elif 'word' not in dat[0].keys():
            dat = []
          else:
            misMatch = False
            if 'adam' in dat[0]['meaning'].lower():
              if rt.lower() != 'adam' and rt != 'A^Edam':
                misMatch = True
            if misMatch:
              dat = []
          data += dat

    with open(f'data/roots/{rt}', 'w') as f:
      f.write(json.dumps(data))



    import pandas as pd

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_colwidth', None)

    df = pd.DataFrame(columns = ["surah:ayah","position","word","meaning","ayah_link"])
    df = pd.concat([df,pd.DataFrame.from_records(data)],
                   axis=0
                   )
    df = df.drop_duplicates(['surah:ayah','position'])
    # df = df.drop(['position'], axis=1)
    df = df[df['meaning'].str.contains(flt, case=False)]
    df["query"] = f'{rt} ({flt})'

    return df.sort_values(["surah:ayah","position"])



def getSorter():
    
    
    """ to tweak the sorter tweak the "surOrd.tsv" file manually """

    import os
    import json
    import csv
    with open('qdict.json') as f:
        qStr = f.read()
    qDict = json.loads(qStr)

    loadedFromDict = False

    if os.path.isfile('sorter.json'):
        print("'sorter.json' found")
        if os.path.getctime('sorter.json') > os.path.getctime('surOrd.tsv'):
            print("'sorter.json' is newer than 'surOrd.tsv")
            with open('sorter.json') as f:
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
        with open('surOrd.tsv') as f:
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

        with open(f'sorter.json', 'w') as f:
            f.write(json.dumps(sorter))
    
    return sorter



def sortchron(dicti={},refLng='',pres=''):
    ''' Sorts ayahs chronologically '''

    pres = confPres(pres=pres)
    tafs = confLng(refLng=refLng)

    sorter = getSorter()
    
    # print(sorter[-1], len(sorter))

    if type(dicti) != type({}):
        print("Invalid root-filter key value pairs")
        dicti={}
    if dicti=={}:
        finished=False
        while finished==False:
            inpLs=str(input(
                """
                Enter comma-separated list of
                '::' double colon-separated pairs of
                word/root and meaning-filter regex like:

                \'$Tn::devil,rwH::(?:spirit|soul)\'

                or \'sHr,jnn::jinn\n\'
                """
                )
            ).split(',')
            if type(inpLs) == type([]) and len(inpLs) >= 1:
              for obj in inpLs:
                pair = obj.strip().split('::')
                if len(pair) == 2:
                  dicti[pair[0]]=pair[1]
                  finished=True
                if len(pair) == 1:
                  dicti[pair[0]]=''
                  finished=True

    import pandas as pd
    df = pd.DataFrame()
    for rt in dicti.keys():
      df = pd.concat([
         df,
         dataGrabber(tafs,rt,dicti[rt])
        ],
        axis=0
      )
    
    df['surah:ayah'] = pd.Categorical(df['surah:ayah'], categories=sorter, ordered=True)
    df.sort_values(["surah:ayah","position"],inplace=True)
    df.reset_index(drop=True,inplace=True)
    df.reset_index(inplace=True)

    # import numpy.random as rand
    import numpy as np
    colMap = {}
    leng = len(df["query"].unique())
    p = np.linspace(50,180,num=leng)
    for idx in range(1,leng+1):
      # n1=rand.randn()
      # n2=rand.randn()
      # i1=rand.randint(0,50)
      # i2=rand.randint(0,50)
      # clr=f"rgb({50+(100/leng)*idx})"
      # colMap[df["query"].unique()[idx]] = f"rgb({clr},{clr},{clr})" 
      colMap[df["query"].unique()[idx-1]] = f'rgb({int(p[idx-1])},{int(p[-idx]-30)},20)' 
      print(f'rgb({int(p[idx-1])},{int(p[-idx]-50)},25)' )

    if pres=='table':
      df.drop(columns=[
        #  "query",
         "index"],inplace=True)
      compareDict = {}
      for i in range(len(sorter)):
          compareDict[sorter[i]]=i

      df.insert( 0, 'verses_before',    list(
              map(
                lambda x: compareDict[x],
                # df["surah"]
                df["surah:ayah"]
              )
          )
      )

      from IPython.core.display import HTML

      def colo(s):
        return [
           f'background-color: {colMap[s["query"]]};' + 
           'foreground-color: black;' +
           'color: blue'
           'opacity: 1' 
        ] * len(s)
      
      return HTML(df.style.apply(
         colo , axis=1
        ).to_html(render_links=True,escape=False,index=False)
      )


    if pres=='plot':
      import plotly.express as px
      # import plotly.graph_objects as go
      # from plotly.subplots import make_subplots
      # from plotly.offline import iplot, init_notebook_mode

      # init_notebook_mode()
      df["ayah_link"] = list(df["surah:ayah"]) + df["ayah_link"]
      fig = px.scatter(
         df,
         x='surah:ayah',
        #  y='ayah_link',
         y='index',
         hover_data={
            'ayah_link':True,
            'query': False, 
            'surah:ayah': False,
            'index': False
          },
         color='query',
        #  color_continuous_scale=["green","yellow","orange","red"],
        color_discrete_map=colMap,
         height=(len(df))*10,
         width=(len(sorter))/5,
      )

      # fig = make_subplots(
      #     specs=[[{"secondary_y": True}]]
      # )

      # # fig.layout=go.Layout(clickmode='event+select')
      
      fig.update_layout(
        #  hovermode=False,
         clickmode='event+select',
         hoverdistance=-1,
         hoverlabel=dict(
            font_size=16
         )
        #  itemclick='toggle'
      )

      # for rt in dicti:
      #     if rt != '' and rt != None:
      #       tbl = dataGrabber(tafs,rt,dicti[rt])
      #       fig.add_trace(
      #           go.Scatter(
      #               y=tbl.ayah_link,
      #               x=tbl['surah:ayah'],
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
      fig.update_xaxes(
         categoryorder='array',
         categoryarray=sorter,
         range=[0,len(sorter)],
         title=" (earlier)   -->  'Surah:Ayah' (Chronologically Ordered)  -->   (latter)"
      )
      fig.update_yaxes(
        #  showticklabels=False,
        #  range=[0,len(df)],
         title=''
      )
      fig.show()
      # iplot(fig)
      # import matplotlib.pyplot as plt
      # plt.show()

  