# SDK Workshop

In this repository you can find the code examples that were presented in the Shimoku SDK Workshop.

Find the slides [here](https://www.canva.com/design/DAFltylHSMA/0LnBdQmjEIisDXnUXw6BRg/edit?utm_content=DAFltylHSMA&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton).

# New changes SDK v1

Installation, with pip

```bash
pip install git+https://github.com/shimoku-tech/shimoku-api-python.git@release/1.1.0#egg=shimoku-api-python
```
I
Installation, with poetry

```bash
# New poetry project
poetry new sdk_test

# Add from github
poetry add git+https://github.com/shimoku-tech/shimoku-api-python.git#release/1.1.0
```

Client creation

```python
from os import getenv
from shimoku_api_python import Client

api_key: str = getenv('API_TOKEN')
config = {
    'access_token': api_key,
}
shimoku = Client(
    config=config,
    universe_id=getenv('UNIVERSE_ID'),
    verbosity="INFO",
    async_execution=True
)
shimoku.set_workspace(getenv('BUSINESS_ID'))
```

Menu paths
```python
shimoku.set_menu_path("path", "subpath")
```

```
shimoku.plt.horizontal_bar(
    x='Name', y=['y', 'z'],
    data=data_,
    order=self.order,
    x_axis_name="X data",
)

```

Charts that change parameter names
```python
# Before
shimoku.plt.funnel(
    data=data_,
    name='name',
    value='value',
    order=order,
    rows_size=2, cols_size=12,
)

# After
shimoku.plt.funnel(
    data=data_,
    names='name',
    values='value',
    order=order,
    rows_size=2, cols_size=12,
)
```

Some charts change their name
```python
# v.0.20
shimoku.plt.stacked_area_chart()

# v1.1.0
shimoku.plt.stacked_area()
```

```
# v.0.20
shimoku.plt.zero_centered_barchart()

# v1.1.0
shimoku.plt.zero_centered_bar()
```

Tabs
```python
# Iniciar ploteo de charts en el grupo 
# de tabs "group"
shimoku.plt.set_tabs_index(
    tabs_index=("group", "tab1"),
    order=0,
)

shimoku.plt.bar(...)

# Cambiar a una nueva tab
shimoku.plt.change_current_tab(
    tab="tab2"
)

shimoku.plt.bar(...)

# Dejar de plotear los charts en el grupo
# "group"
shimoku.plt.pop_out_of_tabs_group()
```

Bentobox

```
# Iniciar ploteo en bentobox
shimoku.plt.set_bentobox(cols_size=8, rows_size=3)

# Dejar de plotear en la bentobox
shimoku.plt.pop_out_of_bentobox()
```
