import streamlit as st
import pandas as pd
import numpy as np


with st.sidebar:
    # Paragon Autonomous logo
    st.image("https://avatars.githubusercontent.com/u/151069538?s=200&v=4")
    st.caption("Streamlit App by Max Neville")
    st.caption("Contact: menevill@asu.edu")

# main container element
with st.container():
    st.title('Autonomous Delivery Drones')
    st.write("In the race to modernize first response teams, fire and medical teams have been largely left behind, leaving them vulnerable in crisis situations.")
    st.write("Our company seeks to help equip first response teams with autonomous capabilities that would help overcome challenges through delivery and sensory applications.")
