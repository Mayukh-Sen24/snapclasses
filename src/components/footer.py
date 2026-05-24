import streamlit as st

def footer_home():
    
    logo_url="https://i.ibb.co/4r5X1Fy/apnacollege.png"

    st.markdown(f"""
        <div style="display:flex;gap:6px;align-items:center;justify-content:center;margin-top:2rem">
            <p>Created with ❤️ by </p>
            <img src='{logo_url}' style='max-height:25px;'/>
        </div>
                       
             """,unsafe_allow_html=True)
    
def footer_dashboard():
    
    logo_url="https://i.ibb.co/4r5X1Fy/apnacollege.png"

    st.markdown(f"""
        <div style="display:flex;gap:6px;align-items:center;justify-content:center;margin-top:2rem">
            <p style="font-weight:bold;color='black'">Created with ❤️ by </p>
            <img src='{logo_url}' style='max-height:25px;'/>
        </div>
                       
             """,unsafe_allow_html=True)