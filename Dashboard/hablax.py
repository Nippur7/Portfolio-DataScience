import streamlit as st
import os
st.set_page_config(
    page_title="HABLAX.INC Dashboard - Home",
    layout="wide"
)


st.title('HABLAX Interactive Monthly Report Dashboard')

st.markdown("""
            <div style="text-align: justify;">
            The data displayed here is owned by Hablax.INC


            </div>
            """, unsafe_allow_html=True)
@st.experimental_memo
def load_dashboard():
    return st.secrets["powerbi_dash"]
# print(type(st.secrets["powerbi_dash"]))
st.components.v1.iframe(load_dashboard(), height=900)

