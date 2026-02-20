import streamlit as st
import streamlit.components.v1 as components
import os

# --- 1. PAGE CONFIG SAFETY ---
# This prevents the "set_page_config() can only be called once" error
try:
    st.set_page_config(page_title="Badger | Asset Matrix Creator", page_icon="🦡", layout="wide")
except st.errors.StreamlitAPIException:
    pass

# --- 2. LOAD ASSETS ---
# Using encoding='utf-8' is vital for the emojis in your CSS/JS
with open('styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    js = f.read()

# --- 3. THE REST OF YOUR CODE ---
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <style>{css}</style>
</head>
<body>
    <header>
        <h1 class="main-header">🦡 Badger</h1>
        <p class="sub-header">Asset Matrix Creator</p>
    </header>
    <script>{js}</script>
</body>
</html>
'''

st.markdown("""
<style>
    .stApp > header { display: none; }
    .block-container { padding: 0 !important; }
</style>
""", unsafe_allow_html=True)

components.html(html_content, height=1200, scrolling=True)
