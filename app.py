from sqlite3 import Date
import streamlit as st
import pandas as pd
import altair as alt
import numpy as np
import plotly.express as px
import plotly.graph_objs as go
from ipywidgets import widgets
import json # library to handle JSON files
from geopy.geocoders import Nominatim 
# convert an address into latitude and longitude values
import requests # library to handle requests
import folium # map rendering library
from streamlit_folium import folium_static
from folium.features import GeoJsonPopup, GeoJsonTooltip
import geopandas as gpd
import branca.colormap as cm
import tweepy
import time
from datetime import date, datetime
from ipywidgets import interactive
import inspect
import textwrap
from collections import OrderedDict
import io
from IPython.display import display
import matplotlib.pyplot as plt
from vega_datasets import data

import streamlit as st
from streamlit.logger import get_logger


import sys
sys.path.insert(1, r'C:\Users\dbukhanevych\Anaconda3\envs\TCA\hello')


import demos
st.set_page_config(
        page_title="TCA Data Lab",
        page_icon=":running:",

    )


LOGGER = get_logger(__name__)

# Dictionary of
# demo_name -> (demo_function, demo_description)
DEMOS = OrderedDict(
    [
        ("—", (demos.intro, None)),
        (
            "Animation Demo",
            (
                demos.fractal_demo,
                """
This app provides insight into - to be added
""",
            ),
        ),
        (
            "Mapping Demo",
            (
                demos.mapping_demo,
                """
This demo shows how to use
[`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
to display geospatial data.
""",
            ),
        ),
        (
            "News Analysis",
            (
                demos.data_frame_demo,
                """
The graph and table below show the distribution of tweets mentioning Ukraine in the main official news accounts of a selected number of countries.
""",
            ),
        ),
    ]
)



def run():
    demo_name = st.sidebar.selectbox("Select project", list(DEMOS.keys()), 0)
    demo = DEMOS[demo_name][0]




    if demo_name == "—":
    
        show_code = False
        st.write("# TCA Data Lab 🧪")
        
        
    else:
        show_code = False
        st.markdown("# %s" % demo_name)
        description = DEMOS[demo_name][1]
        if description:
            st.write(description)
        # Clear everything from the intro page.
        # We only have 4 elements in the page so this is intentional overkill.
        for i in range(10):
            st.empty()

    demo()

    if show_code:
        st.markdown("## Code")
        sourcelines, _ = inspect.getsourcelines(demo)
        st.code(textwrap.dedent("".join(sourcelines[1:])))


if __name__ == "__main__":
    run()
