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
from ipywidgets import interactive, HBox, VBox
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

        - Switch to Light scheme by going to the drop down menu on the right > Settings > Theme > Light
        - Add disclaimer
        - Add instructions on how to navigate, extract data


        ### Contact
        - Please contact namesurname@transformua.com for more details
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
#French
    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/french_ukraine.csv"
    s=requests.get(url).content
    france_news=pd.read_csv(io.StringIO(s.decode('utf-8')))
#German
    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/germany_news.csv"
    s=requests.get(url).content
    germany_news=pd.read_csv(io.StringIO(s.decode('utf-8')))
#German
    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/italy_news.csv"
    s=requests.get(url).content
    italy_news=pd.read_csv(io.StringIO(s.decode('utf-8')))
    
    st.write("# TCA Data Lab 🧪")
    
    #IMPORTING DATASET
    twittertest_full = pd.read_csv(r'C:\Users\dbukhanevych\Downloads\french_ukraine.csv')
    germany_news = pd.read_csv(r'C:\Users\dbukhanevych\Downloads\germany_news.csv')
    italy_news = pd.read_csv(r'C:\Users\dbukhanevych\Downloads\italy_news.csv')

    global_news = pd.concat([france_news, germany_news, italy_news], keys=['France', 'Germany', 'Italy']).reset_index()



    global_news['Date'] = pd.to_datetime(global_news['Date']).dt.normalize()
    global_news.columns = global_news.columns.str.replace(' ', '')

    global_news_grouped = global_news.groupby(['level_0', 'Date']).size().to_frame('Count').reset_index()

    global_news_grouped = global_news_grouped[~(global_news_grouped['Date'] < '2022-04-22')]


    print(global_news)
    print(global_news['level_0'].unique())


    #OLD#

    twittertest_full['Date'] = pd.to_datetime(twittertest_full['Date']).dt.normalize()
    twittertest_full.columns = twittertest_full.columns.str.replace(' ', '')
    twittertest_full = twittertest_full[~(twittertest_full['Date'] < '2022-04-22')]
    counted = twittertest_full.groupby(['Date', 'Author', 'AuthorName', 'AuthorFollowersCount']).size().to_frame('Count').reset_index()
    newdate = counted.set_index('AuthorName', drop=False)

    counted = twittertest_full.groupby(['Date', 'Author', 'AuthorName', 'AuthorFollowersCount', 'Content', 'NumberofLikes', 'NumberofRetweets','pos', 'neg', 'neu', 'compound', 'Emotion']).size().to_frame('Count').reset_index()
    newdate2 = counted.set_index('AuthorName', drop=False)



    hover = alt.selection_single(
        fields=["Date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    #Example of data#
    highlight = alt.selection(type='single', on='mouseover', 
                            fields=['AuthorName'], nearest=True)

    selection = alt.selection_multi(on='click', fields=['level_0'], bind='legend', empty='all')
    tooltips2 = (
    alt.Chart(global_news_grouped)
    .mark_circle(size=60)
    .encode(
    x="yearmonthdate(Date)",
    y="Count",
    color="level_0", 
    opacity=alt.condition(hover, alt.value(0.5), alt.value(0)),
    tooltip=[
        alt.Tooltip("Date", title="Date"),
        alt.Tooltip("Count", title="Tweets"),
        alt.Tooltip("level_0", title="Country"),

    ],
    )
    .add_selection(hover)
    )

    st.write("#### Ukraine in the news")
    st.write("This graph shows mentions of 'Ukraine' in the French news media in their 1000 latest tweets.")


    chart = (
        alt.Chart(global_news_grouped, width=750,
        height=350)
        .mark_area(opacity=0.2)
        .encode(
            x=alt.X("yearmonthdate(Date)", title="Date"),
            y=alt.Y("Count:Q", stack=None),
            color="level_0:N",
            opacity=alt.condition(selection, alt.value(0.5), alt.value(0.1))
        ).add_selection(
    selection
    )
    ).interactive()
    st.altair_chart(chart +tooltips2, use_container_width=True)
    st.button("Reset")




    #INSERTINGTABLE AND SELECTIONS

    counted_global = global_news.groupby(['Date', 'level_0', 'Author', 'AuthorName', 'AuthorFollowersCount', 'Content', 'NumberofLikes', 'NumberofRetweets','pos', 'neg', 'neu', 'compound', 'Emotion']).size().to_frame('Count').reset_index()
    global_news = counted_global.set_index('level_0', drop=False)
    global_news = counted_global.set_index('level_0', drop=False)
    #global_news.style.set_precision(1)

    def showtable():
        return global_news.set_index("level_0")

    try:
        df = showtable()
        media2 = st.multiselect(
                "View by country", list(global_news.index.unique())
        )        
        if not media2:
            st.write()
        else:
            global_news = global_news.loc[media2]

            st.write("#### Tweets", global_news) #this creates the table

    #
            fig=px.scatter(global_news, x="NumberofLikes", y="NumberofRetweets", 
            size="NumberofLikes", color="AuthorName", color_discrete_sequence=px.colors.qualitative.Bold, 
            custom_data=["AuthorName", 'NumberofLikes', 'Date', 'Content'],
                log_x=True, size_max=20)
            fig.update_traces(
            hovertemplate="<br>".join([
            "Likes: %{customdata[1]}",
            "Date: %{customdata[2]}",
            "Content: %{customdata[3]}",

        ])
    )
            fig.update_layout(width = 800, height = 450,
            title = "Mentions of Ukraine <br><sup>Based on a thousand latest tweets from each outlet</sup>",         xaxis_title="Likes",
            yaxis_title="Retweets",
            legend_title="Media Source",)
            today = date.today()
            fig.add_annotation(
                text = (f"TCA | {today}<br>Source: TCA")
                , showarrow=False
                , x = 0
                , y = -0.15
                , xref='paper'
                , yref='paper' 
                , xanchor='left'
                , yanchor='bottom'
                , xshift=-1
                , yshift=-5
                , font=dict(size=10, color="lightgrey")
                , align="left"
                ,)
            st.plotly_chart(fig, use_container_width=False)


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
