# from ..imports import widg
import ipywidgets as widg
from ipywidgets import Output
from IPython.display import display, clear_output

from .CombWdgCl import CombWdgCl

class OptStWdgCl:
        # Function to add a new group of widgets
    def entOptStM(self,button):
        # new_group_id = len(combs) + 1
        # new_group = 
        print(len(self.container.children))
        OptStWdgCl(
            # new_group_id
            self.optSts,
            self.container
            )
        print(len(self.container.children))
        

    # Function to remove this specific group of widgets
    def delOptStM(self,button):
        if len(self.optSts) > 1:
            if self.optSt_container in self.optSts:
                self.optSts.remove(self.optSt_container)
                self.container.children = [w for w in self.container.children if w != self.optSt_container]
    # Function to create a new group of widgets with its own Add and Remove buttons
    def __init__(self,
            # comb_id
                 optSts,
                 container
            ):
        # Widgets for the group (e.g., Text and Slider)

        self.optSts = optSts
        self.container = container

        print("Container ID in OptStWdgCl:", id(container))
        print("Self.container ID:", id(self.container))

        # print(len(self.container.children))

        # self.wrdDisW = widg.IntText(min=0,max=6236,value=0, description=f"Verse Distance")
        self.entOptStB = widg.Button(description="Enter Option of String Objects")
        self.entOptStB.on_click(self.entOptStM)
        self.delOptStB = widg.Button(description="Delete Option of String Objects")
        self.delOptStB.on_click(self.delOptStM)
        self.out = Output()

        self.optSt_container = widg.VBox(
            [
                widg.HBox(
                    
                        [self.entOptStB, self.delOptStB],
                    
                    # layout = widgets.Layout(
                    #     width="200px"
                    # )
                ),
                widg.HBox([])
            ],
                # layout=widgets.Layout(
                #     width="500px",       # Set the width to control the horizontal space
                #     overflow_x="scroll",  # Enable horizontal scrolling if content overflows
                #     border="1px solid black"  # Optional: add a border to make the scroll area visible
                # )
        )

        # strngs_container = widgets.HBox()

        self.combs = []

        CombWdgCl(
            self.combs,
            self.optSt_container
        )

        self.optSts.append(self.optSt_container)
        self.container.children = [self.optSt_container,*self.container.children,]

        clear_output()
        display(self.container)
