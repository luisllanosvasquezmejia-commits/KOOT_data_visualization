#This program displays our findings

import streamlit as st
# Hide Streamlit menu and footer
st.markdown( """<style> #MainMenu {visibility: hidden;}  footer {visibility: hidden;}  header {visibility: hidden;}  </style>  """, unsafe_allow_html=True)

# Set  GIF as background
st.markdown("<style>.stApp {background-image: url(\"https://www.nasa.gov/wp-content/uploads/2023/03/452banimated_1280x720_360degrees.gif\"); background-size: cover; background-position: center; background-repeat: no-repeat;}</style>", unsafe_allow_html=True)

# Center title and buttons using columns
st.write("\n"*100)  # Add vertical spacing
col1, col2, col3 = st.columns([25,2,1])  # Center column
with col1:
    st.markdown(
        '<h1 style="color:#ffffff ; font-size:70px; font-weight:500; background-color:rgba(2,2,2,0.7); padding:2px 10px; display:inline-block; border-radius:10px;">KIND OF ON THAT</h1>',
        unsafe_allow_html=True
    )
    st.text('')
    st.image("https://media.licdn.com/dms/image/v2/C4E03AQEy_DD4xzEuaw/profile-displayphoto-shrink_800_800/profile-displayphoto-shrink_800_800/0/1560606428735?e=1759363200&v=beta&t=76DS27F8RXmfZAO-pVDiope_odYW5z3KuVQ9Xg61zjg", width=300)
    st.markdown('<h1 style="color:#ffffff ; font-size:20px; font-weight:500">"kind on on that" -- Dr-William Stoll',  unsafe_allow_html=True)
   # if st.button("Go to Planet Explorer"):
      #  Redirigir a otra wbd
  #  if st.button("Info / About us"):
    #   Redirigir al readme.txt
