import streamlit as st
name =st.text_input("Enter your name: ")
fname =st.text_input("Enter your Father Name: ")
adr =st.text_area("Enter your address: ")
classdata =st.selectbox("Enter your class:",(1,2,3,4,5,6))

button =st.button("Done")

if button :
    st.markdown(f"""
                Name:{name}
                Father Name:{fname}
                address:{adr}
                class:{classdata}
                
                """)