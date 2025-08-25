import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.button('Why hello there')
else:
    st.write('Goodbye')