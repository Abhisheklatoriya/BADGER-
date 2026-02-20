import os
import streamlit as st

# 1. Find the folder where THIS file lives
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Build the full path to your assets
css_path = os.path.join(current_dir, 'styles.css')
js_path = os.path.join(current_dir, 'script.js')

# 3. Open them with the full path
try:
    with open(css_path, 'r', encoding='utf-8') as f:
        css = f.read()
    with open(js_path, 'r', encoding='utf-8') as f:
        js = f.read()
except FileNotFoundError:
    st.error(f"Could not find assets in {current_dir}. Check your file names!")

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
