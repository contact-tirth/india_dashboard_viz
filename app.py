import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.set_page_config(layout='wide',page_title='India Analysis')

st.title('India Analysis Dashboard')

st.sidebar.title('Select Your Choice')

final_df = pd.read_csv('D:\Learning\DSMP 2.0\india_dashboard_viz\Datasets\india.csv')
state_name = list(final_df['State'].unique())
state_name.insert(0,'All Over India')
first_Para = list(final_df[['Population','Households_with_Internet','sex_ratio','Lat_Rate']])

state_selected = st.sidebar.selectbox('State',state_name)
pri_para = st.sidebar.selectbox('Select 1st Parameter',first_Para)
second_para = st.sidebar.selectbox('Select 2nd Parameter',first_Para)

plot = st.sidebar.button('Plot Graph')

st.write('Size Represent 1st Parameter')
st.write('Color Represent 2nd Parameter')

if plot:
    if state_selected=='All Over India':
        fig=px.scatter_mapbox(final_df,lat='Latitude',lon='Longitude',zoom=3,mapbox_style='carto-positron',color=second_para,size=pri_para,
                              width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = final_df[final_df['State']==state_selected]
        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', zoom=6, mapbox_style='carto-positron',
                                color=second_para, size=pri_para,
                                width=1200, height=700, hover_name='District')
        st.plotly_chart(fig, use_container_width=True)







