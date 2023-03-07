import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout='wide', page_title='StartUp Analysis')
df = pd.read_csv('startup_cleaned.csv')
df['date'] = pd.to_datetime(df['date'], errors='coerce')


def load_investor_details(investor):
    st.title(investor)
    last5_df = df[df['investors'].str.contains(investor)].head()[
        ['date', 'startup', 'vertical', 'city', 'round', 'amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    col1, col2 = st.columns(2)
    with col1:
        big_series = df[df['investors'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(
            ascending=False).head()
        fig, ax = plt.subplots()
        st.subheader('Biggest Investments (Top 5)')
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col2:
        verti_series = df[df['investors'].str.contains(investor)].groupby('vertical')['amount'].sum().head()
        fig1, ax1 = plt.subplots()
        st.subheader('Sector invest in (Top 5)')
        ax1.pie(verti_series, labels=verti_series.index, autopct="%0.0f%%")
        st.pyplot(fig1)

    col3, col4 = st.columns(2)
    with col3:
        big_series = df[df['investors'].str.contains(investor)].groupby('round')['amount'].sum().sort_values(
            ascending=False).head()
        fig, ax = plt.subplots()
        st.subheader('Stage Investments (Top 5)')
        ax.bar(big_series.index, big_series.values)
        st.pyplot(fig)
    with col4:
        verti_series = df[df['investors'].str.contains(investor)].groupby('city')['amount'].sum().head()
        fig1, ax1 = plt.subplots()
        st.subheader('City invest in (Top 5)')
        ax1.pie(verti_series, labels=verti_series.index, autopct="%0.0f%%")
        st.pyplot(fig1)

    df['year'] = df['date'].dt.year
    yoy_series = df[df['investors'].str.contains(investor)].groupby('year')['amount'].sum()
    fig2, ax2 = plt.subplots()
    st.subheader('YoY Investments')
    ax2.plot(yoy_series.index, yoy_series.values)
    st.pyplot(fig2)


def load_overall_analysis():
    st.title('Overall Analysis')
    st.metric('Total Investments', round(df['amount'].sum()))


st.sidebar.title('Startup Funding Analysis')

option = st.sidebar.selectbox('Select One', ['Overall Analysis', 'StartUp', 'Investor'])

if option == 'Overall Analysis':
    oa_btn = st.sidebar.button('Show overall analysis')
    if oa_btn:
        load_overall_analysis()
elif option == 'StartUp':
    st.sidebar.selectbox('Select StartUp', sorted(df['startup'].unique().tolist()))
    startup_btn = st.sidebar.button('Find StartUp Details')
    st.title('StartUp Analysis')

else:
    selected_investor = st.sidebar.selectbox('Select StartUp', sorted(set(df['investors'].str.split(',').sum())))
    investor_btn = st.sidebar.button('Find Investor Details')
    if investor_btn:
        load_investor_details(selected_investor)
