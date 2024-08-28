import streamlit as st

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
 
with st.sidebar:
      st.caption("By Salman Gassem © 2024")

with st.container():
    
    

    st.header("Clusters")
    st.write("The clusters are split into 4 clusters. The categories represent the values of the players from low to high.")

    st.image("2D.png", use_column_width=True)

    st.divider()


    st.subheader("The Three Main Features")
    st.write("- How many times the player appeared in the field\n- How long they played.\n- Their highest value.")

    st.image("3D.png", use_column_width=True)

    st.subheader("Insight")
    st.write("We can see that the highest valued category include players that have high participation in the field.")

