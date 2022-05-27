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
import requests
from typing import Any
from urllib.request import urlopen

def intro():
    import streamlit as st

    st.sidebar.success("Select a project above.")

    st.markdown(
        """
        TCA Data Lab is a web app, which provides a repository of research materials created by TCA.

        **👈 Select a project from the dropdown on the left**

        ### FAQ

        - This TCA Data Lab demo currently hosts two complete projects.
        - The complete projects are News Analysis and Mapping.
            - News Analysis visualizes Twitter data from official news sources in three select countries (France, Germany, Italy).
            - Mapping showcases geospatial data on the number of internally displaced persons in Ukraine.
            - Animation Demo is a placeholder for potential visualizations of TCA's research. 
        - Data (table contents, snapshots of graphs) can be extracted as images. 


        ### Contact
        - Please contact namesurname@transformua.com for more details
    """
    )


# Turn off black formatting for this function to present the user with more
# compact code.
# fmt: off
def mapping_demo():
    st.write("Currently, one data layer is present in the project, which represents the preliminary number (as of 25.03.2022) of internally displaced persons in Ukraine")
    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/IDP/IDP_data.csv"
    s=requests.get(url).content
    data_all=pd.read_csv(io.StringIO(s.decode('utf-8')))

    with urlopen(r'https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/IDP/stanford-gg870xt4706-geojson.json') as f:
        data_geo = json.load(f)

    #with urlopen('https://raw.githubusercontent.com/org-scn-design-studio-community/sdkcommunitymaps/master/geojson/Europe/Ukraine-regions.json') as response:
    #    data_geo = json.load(response)

    #data_geo = json.load(open('Kecamatan_Surabaya.geojson'))
    #data_all["IDPs"] = pd.to_numeric(data_all['IDPs'], errors='coerce')
    #data_all["IDPs"]  = data_all["IDPs"] .astype(int)

    data_all["IDPs"] = data_all["IDPs"].apply(pd.to_numeric)


    #data_all['IDPs'] = data_all['IDPs'].astype('Int64')


    def center():
        address = 'Ukraine'
        geolocator = Nominatim(user_agent="id_explorer")
        location = geolocator.geocode(address)
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude

    def threshold(data):

        threshold_scale = np.linspace(data_all[dicts[data]].min(),
                                data_all[dicts[data]].max(),
                                5, dtype=float)
        threshold_scale = threshold_scale.tolist() # change the numpy array to a list
        threshold_scale[-1] = threshold_scale[-1]
        return threshold_scale


    def show_maps(data, threshold_scale):
        maps= folium.Choropleth(
            geo_data = data_geo,
            data = data_all,
            columns=['Region', dicts[data]],
            key_on='feature.properties.name_1',
            #threshold_scale=threshold_scale,
            fill_color='YlGnBu', 
            fill_opacity=0.7, 
            line_opacity=0.2,
            legend_name=dicts[data],
            highlight=True,
            smooth_factor=0,
            overlay=True,
            nan_fill_color='black', nan_fill_opacity=None, 
            bins = [0, 20000, 50000, 100000, 200000, 300000],
            reset=True).add_to(map_sby)


        folium.LayerControl().add_to(map_sby)
        maps.geojson.add_child(folium.features.GeoJsonTooltip(fields=['name_1',data],
                                                            aliases=['name_1: ', dicts[data]],
                                                            labels=True))                                                       
        folium_static(map_sby)

    centers = center()


    select_maps = st.sidebar.selectbox(
        "What data do you want to see?",
        ("cartodbpositron","OpenStreetMap", "Stamen Toner")
    )
    select_data = st.sidebar.radio(
        "What data do you want to see?",
        ("Total_IDPs", "LastUpdated")
    )

    map_sby = folium.Map(tiles=select_maps,  location=[centers[0], centers[1]], zoom_start=5)

    data_all['Region'] = data_all['Region'].str.title()
    #data_all = data_all.replace({'Region':'Pabean Cantikan'},'Pabean Cantian')
    #data_all = data_all.replace({'Region':'Karangpilang'},'Karang Pilang')

    dicts = {"Total_IDPs":'IDPs',
    "LastUpdated": 'LastUpdated',  
            }

    for idx in range(27):
        data_geo['features'][idx]['properties']['Total_IDPs'] = int(data_all['IDPs'][idx])
        data_geo['features'][idx]['properties']['LastUpdated'] = int(data_all['LastUpdated'][idx])

    show_maps(select_data, threshold(select_data))

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
    url="https://raw.githubusercontent.com/dmytro-buhanevyc/twitteranalysis/main/france_news.csv"
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
        
    #IMPORTING DATASET

    global_news = pd.concat([france_news, germany_news, italy_news], keys=['France', 'Germany', 'Italy']).reset_index()



    global_news['Date'] = pd.to_datetime(global_news['Date']).dt.normalize()

    global_news.columns = global_news.columns.str.replace(' ', '')

    global_news_grouped = global_news.groupby(['level_0', 'Date']).size().to_frame('Count').reset_index()

    global_news_grouped = global_news_grouped[~(global_news_grouped['Date'] < '2022-05-01')]


    #OLD#



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
    expander = st.expander("How it's done")
    expander.write("""
     The news sources are selected based on two criteria: 1) They are in top-10 nation-wide media in their countries based on open-source audience estimates;  2) They have an 
     official Twitter account that is active. Tweets from each news source are extracted via Twitter's Developers API, pre-processed
     to include only those relating to Ukraine. First graph aggregates the tweets on a country-level, while the table and graph below delve deeper into 
     specific countries and their news outlets, as well as visualizes engagements that these outlets garner.""")

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



    counted_global = global_news.groupby(['Date', 'level_0', 'Author', 'AuthorName', 'AuthorFollowersCount', 'Content', 'NumberofLikes', 'NumberofRetweets']).size().to_frame('Count').reset_index()
    global_news = counted_global.set_index('level_0', drop=False)
    global_news = counted_global.set_index('level_0', drop=False)
    global_news.Content = global_news.Content.str.wrap(60)
    global_news.Content = global_news.Content.apply(lambda x: x.replace('\n', '<br>'))



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
            global_news_short = global_news.drop(columns = [ 'Count', 'level_0', 'Author'])
            st.write("####  ", global_news_short) #this creates the table
            fig=px.scatter(global_news, x="NumberofLikes", y="NumberofRetweets", 
            size="NumberofLikes", color="AuthorName", color_discrete_sequence=px.colors.qualitative.Bold, 
            custom_data=["AuthorName", 'NumberofLikes', 'Date', 'Content'],
                log_x=False, size_max=30)
            fig.update_traces(
            hovertemplate="<br>".join([
            "Name: %{customdata[0]}",
            "Likes: %{customdata[1]}",
            "Date: %{customdata[2]}",
            "Content: %{customdata[3]}",
            
        ])
    )
            fig.update_layout(width = 900, height = 550,
            title = "Ukraine in the news <br><sup>Based on latest tweets from each outlet</sup>",         xaxis_title="Likes",
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
