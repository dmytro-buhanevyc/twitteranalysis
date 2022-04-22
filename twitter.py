#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import streamlit as st


# In[8]:



st.set_page_config(layout = "wide")
twitter = pd.read_csv(r'C:\Users\dbukhanevych\Downloads/Twitter3.csv')


st.header("TCA Data Library")
page = st.sidebar.selectbox('Select project',
  ['Twitter Analysis','IDP'])
if page == 'Twitter Analysis':
    
  ## Twitter
  clist = twitter['Author Verified'].unique()
  country = st.selectbox("Blue Check Mark:",clist)
  col1, = st.columns(1)
  fig = px.scatter(twitter[twitter['Author Verified'] == country], 
    x = "Number of Likes", y = "Number of Retweets", size="Author Followers Count",  title = "Analysis of 2500 latest tweets containing hashtag #moskva <br><sup>Tweets between April 14-15</sup>", 
                log_x=True, size_max=80, color="Author Followers Count",  color_continuous_scale="sunset_r", hover_name="Author",
                height=600)

  col1.plotly_chart(fig,use_container_width = True)
  fig = px.scatter(twitter[twitter['Author Verified'] == country], 
    x = "Number of Likes", y = "Number of Retweets",title = "Unverified Accounts")
  
  

else:
  ## IDP
  contlist = df['continent'].unique()
 
  continent = st.selectbox("Select a continent:",contlist)
  col1,col2 = st.columns(2)
  fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "gdpPercap",
    title = "GDP per Capita",color = 'country')
  
  col1.plotly_chart(fig)
  fig = px.line(df[df['continent'] == continent], 
    x = "year", y = "pop",
    title = "Population",color = 'country')
  
  col2.plotly_chart(fig, use_container_width = True)

