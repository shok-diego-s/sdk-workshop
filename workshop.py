# Core python libraries
from os import getenv
from importlib.metadata import version

# Other libraries
from shimoku_api_python import Client
import pandas as pd
import datetime as dt

def read_csv(name: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(f"data/{name}.csv", **kwargs)

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

def bentbox_example(shimoku: Client):
    """
    Place two indicators horizontally using bentobox
    """

    next_order=0


    common_params = dict(
        value='value',
        header='title',
        color='color',
        variant='variant',
    )

    common_data = {
        "title": "Estado",
        "variant": "contained",
    }

    data = [
        {
            **common_data,
            "color": "success",
            "value": "Abierto",
        },
        {

            **common_data,
            "color": "error",
            "value": "Cerrado",
        }
    ]

    menu_path="bentobox"

    bentobox_data = {
        'bentoboxOrder': next_order,
        'bentoboxSizeColumns': 6,
        'bentoboxSizeRows': 1,
    }

    bentobox_id = {'bentoboxId': f"indi"}

        # for i in range(1,3):

    bentobox_data.update(bentobox_id)

    shimoku.plt.indicator(
        **common_params,
        data=data[0],
        menu_path=menu_path,
        order=0, rows_size=8, cols_size=12,
        bentobox_data=bentobox_data,
    )

    shimoku.plt.indicator(
        **common_params,
        data=data[1],
        menu_path=menu_path,
        order=1, rows_size=8, cols_size=12,
        bentobox_data=bentobox_id,
    )

def options_mod_ex(shimoku: Client):
    """
    Examples for line and bar chart
    """

    next_order=0

    line_data=read_csv("prod_rec_pordia")

    menu_path="options mod"

    shimoku.plt.line(
        title="Uso de app ReciclaYa",
        subtitle="Productos reciclados por día",
        data=line_data,
        x="dia",
        y=["Prod Reciclados"],
        order=next_order,
        menu_path=menu_path,
        cols_size=6,
        rows_size=2,
        option_modifications={
            # Quitar leyenda y zoom
            'dataZoom': False,
            'legend': False,
            'optionModifications': {
                'xAxis': {
                    'axisLabel': {
                        'formatter': '{value}',
                        # Inclinar las labels del ejeX
                        'rotate': 45,
                        # Distanciar labels del ejeX
                        'margin': 30,
                    },
                }
            },
        }
    )
    next_order+=1

    bar_data = pd.DataFrame(data={
        'days_avg': ['1','3','5','7','9+',],
        'Número de clientes': [1, 100, 47, 20, 3],
    })

    shimoku.plt.bar(
        data=bar_data,
        x="days_avg",
        y=["Número de clientes"],
        title="""Promedio de días para reciclar
        todos los productos de una compra""",
        x_axis_name="Días",
        y_axis_name="Clientes",
        menu_path=menu_path,
        order=next_order,
        cols_size=6,
        rows_size=2,
        option_modifications={
            # Aumentar espacio al nombre del eje Y
            'optionModifications': {
                'yAxis': {
                    'nameGap': 50,
                }
            }
        },
    )
    next_order+=1

def custom_predictive_line(shimoku: Client):
    """
    Cómo pintar la parte de predicción en LINE chart agregado por semanas o meses?
    """

    menu_path = 'predictive-line'
    data = [
        {'date': dt.date(2021, 1, 1), 'gas': 4, 'oil': 5},
        {'date': dt.date(2021, 1, 2), 'gas': 7, 'oil': 6},
        {'date': dt.date(2021, 1, 3), 'gas': 4, 'oil': 7},
        {'date': dt.date(2021, 1, 4), 'gas': 9, 'oil': 5},
        {'date': dt.date(2021, 1, 5), 'gas': 3, 'oil': 9},
        {'date': dt.date(2021, 1, 6), 'gas': 6, 'oil': 5},
        {'date': dt.date(2021, 1, 7), 'gas': 8, 'oil': 6},
    ]

    shimoku.plt.predictive_line(
        data=data,
        x='date', y=['gas', 'oil'],
        min_value_mark=dt.date(2021, 1, 5).isoformat(),
        max_value_mark=dt.date(2021, 1, 7).isoformat(),
        menu_path=menu_path,
        order=0,
        rows_size=2, cols_size=12,
        padding='0,0,0,1',
        title='Fossil price evolution - first days 2021.',
        color_mark='rgba(59, 255, 157, 0.4)',
    )

def custom_chart_ex(shimoku: Client):
    """
    Create a custom chart with free_echarts
    """

    menu_path="free echarts"
    df=read_csv("scatter_punchcard")

    option = {
        'title': {
            'text': 'Punch Card of Github'
        },
        'legend': {
            'data': ['Punch Card'],
            'left': 'right'
        },
        'tooltip': {
            'position': 'top',
        },
        'grid': {
            'left': 2,
            'bottom': 10,
            'right': 10,
            'containLabel': True
        },
        'xAxis': {
            'type': 'category',
            'boundaryGap': False,
            'splitLine': {
                'show': True
            },
            'axisLine': {
                'show': False
            }
        },
        'yAxis': {
            'type': 'category',
            'axisLine': {
                'show': False
            }
        },
        'series': [
            {
                'name': 'Punch Card',
                'type': 'scatter',
                'data': [
                    {
                        'value': [ row["hour"], row["day"] ],
                        'symbolSize': row["ncommits"] * 2,
                    } for idx, row in df.iterrows()
                ],
            },
        ]
    }

    shimoku.plt.free_echarts(
        data=df[:1], #dummy
        options=option,
        menu_path=menu_path,
        order=0,
    )

def ordernar_subpaths(shimoku: Client):
    """
    """
    # Plot dummy stuff
    next_order=0
    shimoku.plt.html(
        html=shimoku.html_components.create_h1_title(
            title="",
            subtitle="title 1"
        ),
        menu_path="subpath/path1",
        order=next_order,
    )
    next_order+=1

    shimoku.plt.html(
        html=shimoku.html_components.create_h1_title(
            title="",
            subtitle="title 2"
        ),
        menu_path="subpath/path2",
        order=next_order,
    )
    next_order+=1

    dash_name="Path ordering"

    shimoku.plt.set_sub_path_orders(
        paths_order={
            "subpath/path2": 1,
            "subpath/path1": 2,
        }
    )

def theme_example(shimoku: Client):
    """
    Change logo of the dashboard
    """

    shimoku.business.update_business_theme(
        business_id=shimoku.app.business_id,
        theme={
            "custom": {
                "logo": "https://www.vectorlogo.zone/logos/linux/linux-ar21.png",
            },
        },
    )

def format_pandas_date():
    """
    """
    df = pd.DataFrame({'date': {0: '26/1/2016', 1: '26/1/2016'}})
    # Convert date strings to 
    df['date'] = pd.to_datetime(df['date'])
    print(df.loc[0]['date'])
    # this is the line that you should use
    # Convert pandas dates to string with the desired format
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')
    print(df.loc[0]['date'])

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

    # tabs_example(shimoku)
    # bentbox_example(shimoku)
    # options_mod_ex(shimoku)
    # custom_chart_ex(shimoku)
    # theme_example(shimoku)
    # custom_predictive_line(shimoku)
    # ordernar_subpaths(shimoku)
    format_pandas_date()

    # Execute all plots in asynchronous mode
    shimoku.activate_async_execution()
    shimoku.run()
