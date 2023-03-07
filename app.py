import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('startup_cleaned.csv')


def load_investor_details(investor):
    st.title(investor)
    last5_df = df[df['investors'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    big_df = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
    st.subheader('Biggest Investments')
    st.dataframe(big_df)

st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    startup_btn = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')

else:
    selected_investor = st.sidebar.selectbox('Select StartUp', sorted(set(df['investors'].str.split(',').sum())))
    investor_btn = st.sidebar.button('Find Investor Details')
    if investor_btn:
        load_investor_details(selected_investor)
