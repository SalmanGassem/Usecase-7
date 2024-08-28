import streamlit as st
from PIL import Image

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.title('Do you need clustering? I know I do!')

st.image('clusters.png', caption='', use_column_width=True)

st.markdown("""
### :ringed_planet: Welcome! Glad you are here :dizzy:
            
#### This is a Clustering K-Means model to predict players category. 

            
#### :point_left: Please check the other pages on the side for either predicting with new data, or to see the model's visualization.
            """)
            
with st.sidebar:
      st.caption("By Salman Gassem © 2024")