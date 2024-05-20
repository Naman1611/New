import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(
    page_title="Floqer",
    page_icon="🧊",
    layout="wide"

)

@st.cache_data
def load_data():
    # Load your DataFrame here
    df = pd.read_csv('salaries.csv')
    return df
 
df = load_data()

a=df[['work_year']].value_counts()
b=df.groupby('work_year')['salary_in_usd'].mean()
main_table = a.reset_index().set_index('work_year').combine_first(b.reset_index().set_index('work_year'))

col1,col2 = st.columns([0.2,0.7])
with col1:
    st.markdown('')
    st.title('Main Table')
    st.markdown('')
    st.dataframe(main_table)

with col2:
    st.bar_chart(main_table,y='count')
    st.bar_chart(main_table,y='salary_in_usd')
