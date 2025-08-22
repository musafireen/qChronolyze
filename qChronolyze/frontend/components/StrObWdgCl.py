from ...backend.database.schemas.strObjClass import StrObjClass

# from ..imports import widg
import ipywidgets as widg
from ipywidgets import Output

from ...shared.constants import sameVrsIndicator, lng2InpSchD, striD, inpLngSchD, lngD, lngL, strTypL, frmL, poSpL

class StrObWdgCl:
    # global fulWdgD
    # idx = 0
    # parentIdx = 1
    strngs = []
    # strTypSt = "root"
    strTypSt = StrObjClass.strTypSt
    frmSt = StrObjClass.frmSt
    poSpSt = StrObjClass.poSpSt
    inpLngSt = StrObjClass.inpLngSt
    inpSchSt = StrObjClass.inpSchSt
    inpSchArSt = StrObjClass.inpSchArSt
    wrdDisPosSt = StrObjClass.wrdDisPosSt
    wrdDisNegSt = StrObjClass.wrdDisNegSt
    strUnwantedSt = StrObjClass.strUnwantedSt

    def update_language_scheme_options(self,*args):
        # print(self.inpLngW.value)
        self.inpSchW.options=lng2InpSchD[self.inpLngW.value]
        self.inpSchW.value=lng2InpSchD[self.inpLngW.value][0]
    
    # def entStrObjM(self,*args):
    def entStrObjM(self,button,
                #    strngs,comb_container
                   ):
        StrObWdgCl.strTypSt=self.strTypeW.value
        StrObWdgCl.frmSt=self.frmW.value
        StrObWdgCl.poSpSt=self.poSpW.value
        StrObWdgCl.inpLngSt=self.inpLngW.value
        StrObWdgCl.inpSchSt=self.inpSchW.value
        StrObWdgCl.strUnwantedSt=self.strUnwantedW.value
        StrObWdgCl.wrdDisPosSt=self.wrdDisPosW.value
        StrObWdgCl.wrdDisNegSt=self.wrdDisNegW.value

        StrObWdgCl(
            self.parentComb
                                 )

    def delStrObjM(self,button,
                   ):
        if len(self.parentComb.strngs) > 1:
            if self.strContainer in self.parentComb.strngs:
                self.parentComb.strngs.remove(self.strContainer)
                self.parentComb.comb_container.children = [w for w in self.parentComb.comb_container.children if w != self.strContainer]

    def findM(self,button,
                   ):
        self.striW.value = striD[self.findW.value]["stri"][inpLngSchD[self.inpSchArSt]]
        self.strTypeW.value = striD[self.findW.value]["typ"]
        self.inpSchW.value = self.inpSchArSt

    def __init__(self,
                 parentComb,
                ):

        self.parentComb = parentComb
        
        self.findW = widg.Combobox(
            options=list(striD.keys()),
            description='Find',
            value=list(striD.keys())[0]
        )
        self.striW = widg.Text(description=f"String",value=striD[self.findW.value]["stri"][inpLngSchD[self.inpSchArSt]])
        self.fltW = widg.Text(description=f"Translation_filter")
        self.strTypeW = widg.Dropdown(options=strTypL, value=striD[self.findW.value]["typ"],description=f"String_type")
        self.poSpW = widg.Dropdown(options=poSpL, value=self.poSpSt,description=f"Part_of_speech")
        self.frmW = widg.Dropdown(options=frmL, value=self.frmSt,description=f"Form")
        self.inpLngW = widg.Dropdown(options=lngL[:-1], value=self.inpLngSt,description=f"Input_language")
        self.inpSchW = widg.Dropdown(description=f"Input_scheme")
        self.entStrObjB = widg.Button(description=f"Enter String Object")
        self.delStrObjB = widg.Button(description=f"Delete String Object")
        self.findB = widg.Button(description=f"Find")
        self.entStrObjB.on_click(self.entStrObjM)
        self.delStrObjB.on_click(self.delStrObjM)
        self.findB.on_click(self.findM)
        self.inpLngW.observe(self.update_language_scheme_options)
        self.update_language_scheme_options(self)
        self.out = Output()

        self.strUnwantedW = widg.ToggleButton(value=False,description='Exclude')
        self.wrdDisPosW = widg.IntText(min=0,max=sameVrsIndicator,value=self.wrdDisPosSt, description=f"Word Distance before")
        self.wrdDisNegW = widg.IntText(min=-sameVrsIndicator,max=0,value=self.wrdDisNegSt, description=f"Word Distance after")

        self.strContainer = widg.VBox(
            [
                self.striW,
                self.fltW,
                self.strTypeW,
                self.poSpW,
                self.frmW,
                self.inpLngW,
                self.inpSchW,
                self.wrdDisPosW,
                self.wrdDisNegW,
                self.strUnwantedW,
                self.entStrObjB,
                self.delStrObjB,
                self.findW,
                self.findB,
            ]
        )

        parentComb.strngs.append(self.strContainer)

        with self.out:
            parentComb.comb_container.children = [parentComb.comb_container.children[0], self.strContainer, *parentComb.comb_container.children[1:]]

            parentComb.comb_container.layout=widg.Layout(
                max_width="800px",       # Set the width to control the horizontal space
                # max_height="800px",       # Set the width to control the horizontal space
                # width="500px",       # Set the width to control the horizontal space
                # height="200px",       # Set the width to control the horizontal space
                # overflow="scroll",  # Enable horizontal scrolling if content overflows
                border="1px solid black",  # Optional: add a border to make the scroll area visible
                # display="flex",
                # flex_flow='row',
                overflow='scroll hidden'
            )
