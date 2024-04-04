# configs and utilities
if 'logger' not in globals():
    try:
        from loguru import logger
    except ImportError:
        from logging import getLogger
        logger = getLogger(__name__)

logger.info('configuring ipython')

# pylab inline + other magic
from IPython import get_ipython
ipython = get_ipython()
ipython.magic('config InlineBackend.figure_format="retina"')
ipython.magic('load_ext autoreload')
ipython.magic('autoreload 2')

# cells can have multiple outputs
from IPython.core.interactiveshell import InteractiveShell
from IPython.display import display, HTML, display_html
InteractiveShell.ast_node_interactivity = "all"

import pandas as pd
pd.set_option('display.precision', 4)
pd.options.display.float_format = '{:.4f}'.format
pd.plotting.register_matplotlib_converters()
from pandas import DataFrame, Series, Timestamp
D, S, T = DataFrame, Series, Timestamp

import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt
import seaborn as sns
from copy import copy
from pprint import pprint
from pathlib import Path
from tqdm.auto import auto

sns.set(rc={'figure.figsize': (9, 5)})

sns_grid_light_theme = {
    'rc': {
        'figure.figsize': (9, 5), 
        'grid.color': '#dddddd',
        'axes.edgecolor': '#dddddd',
        'legend.frameon': True,
        'patch.force_edgecolor': True,
    },
    'style': 'whitegrid',
    'font_scale' : 1.25,
    'color_codes': True,
    'context': 'notebook'
}
sns_ticks_light_theme = {
    'rc': {
        'figure.figsize': (9, 5), 
        'axes.spines.top': False, 
        'axes.spines.right': False,
        'legend.frameon': False,
        'patch.force_edgecolor': True,
        'axes.titlepad': 30
    },
    'style': 'ticks',
    'font_scale' : 1.25,
    'color_codes': True,
    'context': 'notebook'
}
sns_dark_theme_updates = {
    'rc': {
        'axes.facecolor': '#111111',
        'figure.facecolor': '#111111',
        'grid.color': '#6f6f6f',
        'text.color': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'axes.edgecolor': '#6f6f6f',
        'axes.labelcolor': 'white'
    }
}
sns_grid_dark_theme = copy(sns_grid_light_theme).update(sns_dark_theme_updates)
sns_ticks_datk_theme = copy(sns_ticks_light_theme).update(sns_dark_theme_updates)

# sns.set_theme(**grid_light_theme)

# setup hvplot and plotly
try:
    import hvplot.pandas
    import holoviews as hv
    hvkw = dict(height=500, width=700, grid=True, legend='top')
except ImportError:
    pass

try:
    import plotly.express as px
    import plotly.io as pio

    pio.renderers.default = 'notebook'
    pio.templates.default = 'plotly_dark'

    pd.options.plotting.backend = 'plotly'
except ImportError:
    pass

try:
    from ipydatagrid import DataGrid
except ImportError:
    pass

# reset any bultin we may have overidden
import builtins
for var in dir(builtins):
    globals()[var] = getattr(builtins, var)
    
logger.info('done configuring ipython')