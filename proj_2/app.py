import streamlit as st
st.title(":red[Data Science] Internship :smile:")
st.header("steamlit-python")
st.subheader("feb 2023")
code='''print(hello, i am lakshmi)'''
st.code(code,language="python")
btn_click = st.button("Click Me!")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()

