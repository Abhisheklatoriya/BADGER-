import streamlit as st
import streamlit.components.v1 as components

# Note: st.set_page_config removed to avoid conflicts

with open('styles.css', 'r') as f:
    css = f.read()

with open('script.js', 'r') as f:
    js = f.read()

# ... (Paste the entire html_content string from your original Badger app here) ...

st.markdown("""
<style>
    .stApp > header { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

components.html(html_content, height=1200, scrolling=True)
