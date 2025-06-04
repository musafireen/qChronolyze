from ...shared.constants import surAyPosStrAdvWrdMD

class row2DictCl:
        # lnkStyle = ' '
    fontSize = '18'
    fontCol = 'rgb(0,0,150)'
    shPx = str(int(fontSize)/100*0)
    shCol = '#000000'
    bgCol = 'rgb(220,220,250)'
    txtShad = ''
    # txtShad = f'text-shadow:{shPx}px {shPx}px 0 {shCol}, {shPx}px -{shPx}px 0 {shCol}, -{shPx}px -{shPx}px 0 {shCol}, -{shPx}px {shPx}px 0 {shCol};'
    # lnkStyle = "style='background-color:rgb(250,250,250);font-size:30px;color:rgb(0,0,150);-webkit-text-stroke-width:5px;-webkit-text-stroke-color:white' "
    lnkStyle = f" style='background-color:{bgCol};font-size:{fontSize}px;color:{fontCol};{txtShad}'"
    # lnkStyle = ''
    # lnkStyle = "style='color:rgb(250,250,250);-webkit-text-stroke-width:1px;-webkit-text-stroke-color:rgb(0,0,0);' "
    def __init__(self,surah='',ayah='',positions=[],query='',tafs="ar-tafsir-al-tabari"):
        # print(surah, ayah, positions)
        ayWrds = [
            # posD["wrd"] 
            posD["wrd"] 
            for posD in surAyPosStrAdvWrdMD[surah][ayah].values()
                  
        ]
        positions = [int(pos) for pos in positions]
        ayWrdsHgh = [
            f"<b><i>{ayWrds[i]}</i></b>"
            if i+1 in positions
            else ayWrds[i]
            for i in range(len(ayWrds))
        ]
        txtLwLmt = max(0,min(positions)-4)
        txtUpLmt = min(len(ayWrds),max(positions)+5)
        ayTxt = " ".join( ayWrdsHgh[txtLwLmt:txtUpLmt] )

        # surAy = ":".join([surah,ayah])
        self.surah_ayah = ":".join([surah,ayah])
        # self.surah = surah
        # self.ayah = ayah
        self.positions = positions
        # self.position_lowest = min([int(pos) for pos in positions])
        self.strings = [ surAyPosStrAdvWrdMD[surah][ayah][str(pos)]["wrd"] for pos in positions ]
        self.meanings = [ surAyPosStrAdvWrdMD[surah][ayah][str(pos)]["mean"] for pos in positions]
        self.ayah_link = f"<a{self.lnkStyle} href='https://quran.com/{self.surah_ayah}/tafsirs/{tafs}'>{ayTxt}</a>"
        # self.ayah_link = f"<a{self.lnkStyle}>{ayTxt}</a> <a href='https://quran.com/{self.surah_ayah}/tafsirs/{tafs}'>Tafs</a>"
        self.query = query