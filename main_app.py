import streamlit as st

# --- GLOBAL CONFIGURATION ---
# Must be called only once in the entry point file
st.set_page_config(
    page_title="Asset Management Suite",
    page_icon="🛠️",
    layout="wide"
)

# --- DEFINE PAGES ---
# Each page points to your existing scripts
pg_matrix = st.Page(
    "matrix_creator.py", 
    title="Asset Matrix Creator", 
    icon="🦡"
)
pg_matcher = st.Page(
    "file_matcher.py", 
    title="Dynamic File Matcher", 
    icon="📁"
)
pg_checker = st.Page(
    "asset_checker.py", 
    title="Smartly Asset Checker", 
    icon="📦"
)

# --- NAVIGATION ---
pg = st.navigation({
    "Creation": [pg_matrix],
    "Verification": [pg_matcher, pg_checker]
})

# --- RUN THE SELECTED PAGE ---
pg.run()
