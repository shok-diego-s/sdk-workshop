# Core python libraries
from os import getenv
from importlib.metadata import version
import datetime as dt

# Other libraries
from shimoku_api_python import Client

def tabs_example(shimoku: Client):
    """
    Show the placement of tabs
    """
    # Set tab order
    next_order=0

    data=[
        {"x": 1, "y": 1},
        {"x": 2, "y": 2},
        {"x": 3, "y": 3},
        {"x": 4, "y": 4}
    ]


    tab_group="my_group"
    menu_path="tabs_example"

    # First chart above tabs
    shimoku.plt.line(
        data=data,
        x="x",
        y=["y"],
        order=next_order,
        menu_path=menu_path,
    )
    next_order+=1

    shimoku.plt.update_tabs_group_metadata(
        order=next_order,
        menu_path=menu_path,
        group_name=tab_group,

        # Set styles
        just_labels=True,
        sticky=False,

    )

    # Charts go below tabs, increment order
    next_order+=1

    # First chart
    for i in range(1,3):
        shimoku.plt.bar(
            data=data,
            x="x",
            y=["y"],
            order=i,
            menu_path=menu_path,
            tabs_index=(tab_group, f"Tab {i}")
        )


    return next_order

if __name__ == "__main__":

    # Create the client
    shimoku = Client(
        universe_id=getenv('UNIVERSE_ID'),
        access_token=getenv('API_TOKEN'),
        business_id=getenv('BUSINESS_ID'),
        verbosity='INFO',
        async_execution=True,
    )

    menu_path="Info section"

    tabs_example(shimoku)

    # Execute all plots in asynchronous mode
    shimoku.activate_async_execution()
    shimoku.run()
