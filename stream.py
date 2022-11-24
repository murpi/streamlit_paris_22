import streamlit as st
import requests 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title('Hello Wilders, welcome to my application!')
st.write('coucou coucou')

df = pd.read_csv("velib.csv")


fig, ax = plt.subplots()

option_velo = st.selectbox(
    'Quel type de vélo ?',
    ('mechanical', 'ebike'))
ax = sns.boxplot(df[option_velo])
st.pyplot(fig)