import streamlit as st
import pandas as pd
from matplotlib import image
import os
import plotly.express as px

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")


st.title("Dashboard - Tianic data")
img=image.imread(IMAGE_PATH)
st.image(img)
df=pd.read_csv(DATA_PATH)
st.dataframe(df)
col1, col2 = st.columns(2)
alone = st.selectbox("Select the town:", df['alone'].unique())
fig_1 = px.histogram(df[df['adult_male'] == alone], x="adult_male")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['adult_male'] == alone], y="alone")
col2.plotly_chart(fig_2, use_container_width=True)