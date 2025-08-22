
from ...backend.database.schemas.combClass import CombClass
# from ..imports import widg
import ipywidgets as widg
# from ipywidgets import Output
from IPython.display import display, clear_output
from ...shared.constants import sameVrsIndicator
from .StrObWdgCl import StrObWdgCl

class CombWdgCl:
        # Function to add a new group of widgets
    wrdDisSt = CombClass.wrdDisSt
    strLSt = CombClass.strLSt
    def entCombM(self,button):
        # new_group_id = len(combs) + 1
        # new_group = 
        print(len(self.opt_container.children[1].children))
        CombWdgCl(
            # new_group_id
            self.combs,
            self.opt_container
            )
        print(len(self.opt_container.children[1].children))
        
        # self.combs.append(new_group)
        # self.container.children = list(self.container.children) + [new_group]

    # Function to remove this specific group of widgets
    def delCombM(self,button):
        if len(self.combs) > 1:
            if self.comb_container in self.combs:
                self.combs.remove(self.comb_container)
                self.opt_container.children[1].children = [w for w in self.opt_container.children[1].children if w != self.comb_container]
    # Function to create a new group of widgets with its own Add and Remove buttons
    def __init__(self,
            # comb_id
                 combs,
                 opt_container
            ):
        # Widgets for the group (e.g., Text and Slider)

        self.combs = combs
        self.opt_container = opt_container
        # print(len(self.container.children))

        self.wrdDisW = widg.IntText(min=-1,max=sameVrsIndicator,value=self.wrdDisSt, description=f"Word Distance")
        self.qyLblW = widg.Text(value='', description=f"Query Label")
        self.entCombB = widg.Button(description="Enter Combination of String Objects")
        self.entCombB.on_click(self.entCombM)
        self.delCombB = widg.Button(description="Delete Combination of String Objects")
        self.delCombB.on_click(self.delCombM)
        # self.out = Output()

        self.comb_container = widg.HBox(
            [
                widg.VBox(
                    [
                        self.wrdDisW,
                        self.qyLblW,
                        widg.HBox([self.entCombB, self.delCombB]),
                    ],
                    # layout = widgets.Layout(
                    #     width="200px"
                    # )
                )
            ],
                # layout=widgets.Layout(
                #     width="500px",       # Set the width to control the horizontal space
                #     overflow_x="scroll",  # Enable horizontal scrolling if content overflows
                #     border="1px solid black"  # Optional: add a border to make the scroll area visible
                # )   
        )

        # strngs_container = widgets.HBox()

        self.strngs = []

        StrObWdgCl(self)

        # strngs_container.children = [initial_strng]

        # strngs.append(initial_strng)

        self.combs.append(self.comb_container)
        # with self.out:
        self.opt_container.children[1].children = [self.comb_container,*self.opt_container.children[1].children,]

        # clear_output()
        # display(self.opt_container)
