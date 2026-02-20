import streamlit as st
import pandas as pd

# --- Reset Logic ---
def reset_app():
    st.session_state["file_uploader_key"] += 1
    st.session_state["data_editor_key"] += 1

if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0
if "data_editor_key" not in st.session_state:
    st.session_state["data_editor_key"] = 100

top_col1, top_col2, top_col3 = st.columns([3, 2, 1])

with top_col1:
    st.title("📁 Dynamic File Matcher")

with top_col2:
    num_cols = st.number_input("Number of Columns to Paste", min_value=1, max_value=20, value=4)

with top_col3:
    st.write(" ") 
    if st.button("🔄 Reset All", use_container_width=True, on_click=reset_app):
        st.rerun()

# ... (Paste the rest of your original Matcher processing logic here) ...
