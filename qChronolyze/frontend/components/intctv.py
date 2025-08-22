
from ...shared.constants import lng2InpSchD
# from ..imports import widg, display
# from ..imports import display
from IPython.display import display, clear_output
import ipywidgets as widg
from ..finish_query_F import finish_query_f
from .OptStWdgCl import OptStWdgCl

def intctv(
    qL=[],
    pres='',refLng='',qyArLegSch=lng2InpSchD["arabic"][-1]
    ):
    container = widg.VBox(
        # layout=widgets.Layout(
        #             width="600px",       # Set the width to control the horizontal space
        #             overflow_x="scroll",  # Enable horizontal scrolling if content overflows
        #             border="1px solid black"  # Optional: add a border to make the scroll area visible
        #         )   
    )
    combs = []
    from functools import partial
    finish_query_B = widg.Button(description="Finish Query", layout=widg.Layout(width="auto"))
    finish_query_B.on_click(partial(finish_query_f,container=container,qL=qL,pres=pres,refLng=refLng,qyArLegSch=qyArLegSch))
    # Container to hold all groups of widgets
    # Initialize the first group of widgets
    print("Container ID in intctv:", id(container))
    OptStWdgCl(
        # 1
        combs,
        container
        )
    
    print("Container ID in intctv:", id(container))
    # clear_output()
    print("reached button")
    display(finish_query_B,)
    print("reached container")
    # display(container,)
