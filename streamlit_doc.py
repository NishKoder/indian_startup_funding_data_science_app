import time

import streamlit as st
import pandas as pd

st.title('Startup dashboard')

st.header('I am learning stream lit')

st.subheader('Love it')

st.write('Hello i am like paragraph')

st.markdown("""
### My fav movies
- Race 3
- Hum
- Houseful
""")

st.code("""
def fo():
    return fo*2
x = fo(2)
""")

st.latex('x^2 + y^2 + 4 =0')

df = pd.DataFrame({
    'name':['Niti','Anki','Nik'],
    'marks': [40,34,54],
    'package': [10,20,30]
})
st.dataframe(df, width=1000)

st.metric('Revenue','Rs 3L', '3%')

st.json({
    'name':['Nit','Anki','Nik'],
    'marks': [40,34,54],
    'package': [10,20,30]
})

st.image('un.png')


st.sidebar.title('Sidebar')
col1,col2,col3 = st.columns(3)
with col1:
    st.image('un.png')
with col2:
    st.image('un.png')
with col3:
    st.image('un.png')



st.error('Login failed')
st.success('Login success')
st.warning('Login warning')
st.info('Login info')

bar = st.progress(0)

for i in range(1,101):
    # time.sleep(0.1)
    bar.progress(i)


email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['Male','Female','others'])
file = st.file_uploader('Upload  a csv file')
btn = st.button('Login')

# if the button is click
if btn:
   if email == 'nish' and password == '1234':
       st.success('Login Successful')
       st.balloons()
       if file is not None:
           df = pd.read_csv(file)
           st.dataframe(df.describe())
   else:
       st.error('Login Error')



import streamlit as st
import pandas as pd

email = st.text_input('Enter email')
password = st.text_input('Enter password')
gender = st.selectbox('Select gender',['Male','Female','others'])
file = st.file_uploader('Upload  a csv file',)
btn = st.button('Login')

# if the button is click
if btn:
   if email == 'nish' and password == '1234':
       st.success('Login Successful')
       st.balloons()
       if file is not None:
           df = pd.read_csv(file)
           st.dataframe(df.describe())
   else:
       st.error('Login Error')






