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

from typing import Any


def intro():
    import streamlit as st

    st.sidebar.success("Select a project above.")

    st.markdown(
        """
        TCA Data Lab is a web app, which provides a repository of research materials created by TCA.

        **👈 Select a project from the dropdown on the left**

        ### FAQ

        - Add disclaimer
        - Add instructions on how to navigate, extract data


        ### Contact
        - Please contact dbukhanevych@transformua.com for more details
    """
    )


# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def mapping_demo():
    import streamlit as st
    import pandas as pd
    import pydeck as pdk

    from urllib.error import URLError

    @st.cache
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename)
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown('### Map Layers')
        selected_layers = [
            layer for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)]
        if selected_layers:
            st.pydeck_chart(pdk.Deck(
                map_style="mapbox://styles/mapbox/light-v9",
                initial_view_state={"latitude": 37.76,
                                    "longitude": -122.4, "zoom": 11, "pitch": 50},
                layers=selected_layers,
            ))
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error("""
            **This demo requires internet access.**

            Connection error: %s
        """ % e.reason)
# fmt: on

# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off


def fractal_demo():
    import streamlit as st
    import numpy as np

    df = px.data.gapminder()
    fig=px.scatter(df, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",
           size="pop", color="continent", hover_name="country",
           log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
    st.plotly_chart(fig)

    progress_bar = st.sidebar.progress(0)
    # We clear elements by calling empty on them.
    progress_bar.empty()
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")





def data_frame_demo():
    #from sqlite3 import Date
    from matplotlib.colors import Normalize
    import streamlit as st
    import pandas as pd
    import altair as alt
    import numpy as np
    import plotly.express as px
    import plotly.graph_objs as go
    from ipywidgets import widgets
    import json # library to handle JSON files
    from geopy.geocoders import Nominatim 
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
    import streamlit as st
    from streamlit.logger import get_logger
    
    #NAME OF THE PAGE
    import sys
    sys.path.insert(1, r'C:\Users\dbukhanevych\Anaconda3\envs\TCA\hello')


    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()


    #IMPORTING DATASET

    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/french_ukraine.csv"
    s=requests.get(url).content
    twittertest_full=pd.read_csv(io.StringIO(s.decode('utf-8')))


    #twittertest_full = pd.read_csv(r'C:\Users\dbukhanevych\Downloads\french_ukraine.csv')


    #NORMALIZING
    twittertest_full['Date'] = pd.to_datetime(twittertest_full['Date']).dt.normalize()

    twittertest_full.columns = twittertest_full.columns.str.replace(' ', '')

    #edit date

    twittertest_full = twittertest_full[~(twittertest_full['Date'] < '2022-04-22')]



    #GROUPING#
    counted = twittertest_full.groupby(['Date', 'Author', 'AuthorName', 'AuthorFollowersCount']).size().to_frame('Count').reset_index()
    newdate = counted.set_index('AuthorName', drop=False)




    expander = st.expander("How it's done")
    expander.write("""
        The news analysis is operationalized through the outlets' respective Twitter accounts' activity. 
        The media lists are based on open-source data on the largest official news outlets by country. 
        The data comes from a selection of 1000 latest tweets from each news account. 
        Further, the data is processed to exclude retweets and a subset 
        of tweets containing the word 'Ukraine' is selected.
    """)



    hover = alt.selection_single(
        fields=["Date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    #Example of data#
    highlight = alt.selection(type='single', on='mouseover', 
                            fields=['AuthorName'], nearest=True)


    twittertest_full = pd.read_csv(r'C:\Users\dbukhanevych\Downloads\french_ukraine.csv')
    twittertest_full['Date'] = pd.to_datetime(twittertest_full['Date']).dt.normalize()
    twittertest_full.columns = twittertest_full.columns.str.replace(' ', '')
    twittertest_full = twittertest_full[~(twittertest_full['Date'] < '2022-04-22')]


    from urllib.error import URLError

    counted = twittertest_full.groupby(['Date', 'Author', 'AuthorName', 'AuthorFollowersCount', 'Content', 'NumberofLikes', 'NumberofRetweets','pos', 'neg', 'neu', 'compound', 'Emotion']).size().to_frame('Count').reset_index()
    newdate2 = counted.set_index('AuthorName', drop=False)

    print(newdate2)

    selection = alt.selection_multi(on='click', fields=['AuthorName'], bind='legend', empty='all')
    tooltips2 = (
    alt.Chart(newdate)
    .mark_circle(size=60)
    .encode(
    x="yearmonthdate(Date)",
    y="Count",
    color="AuthorName",
    opacity=alt.condition(hover, alt.value(0.5), alt.value(0)),
    tooltip=[
        alt.Tooltip("Date", title="Date"),
        alt.Tooltip("Count", title="Tweets"),
        alt.Tooltip("AuthorName", title="Media"),
        alt.Tooltip("AuthorFollowersCount", title="Followers"),

    ],
    )
    .add_selection(hover)
    )
#- Title goes here

    chart = (
        alt.Chart(newdate, width=750,
        height=350)
        .mark_area(opacity=0.3)
        .encode(
            x=alt.X("yearmonthdate(Date)", title="Date"),
            y=alt.Y("Count:Q", stack=None),
            color="AuthorName:N",
            opacity=alt.condition(selection, alt.value(0.5), alt.value(0.1))
        ).add_selection(
    selection
    )
    ).interactive()

    st.altair_chart(chart + tooltips2, use_container_width=False)
    st.button("Reset")




    #INSERTINGTABLE AND SELECTIONS

    def showtable():
        newdate2.drop(columns=['Author'], axis=1, inplace=True)
        return newdate2.set_index("AuthorName")

    try:
        df = showtable()
        media2 = st.multiselect(
                "View in table", list(newdate2.index.unique())
        )        
        if not media2:
            st.write()
        else:
            newdate2 = newdate2.loc[media2]

            st.write("#### Tweets", newdate2) #this creates the table

            b=alt.Chart(newdate2).mark_bar(size=3).encode(
        x = 'Date',
        y = 'Count',
        color = 'AuthorName'
    )
            

            #st.altair_chart(b, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )





# fmt: on
