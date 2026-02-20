import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

# 1. Page Configuration
st.set_page_config(
    page_title="Badger | Asset Matrix Creator", 
    page_icon="🦡", 
    layout="wide"
)

# 2. Robust Path Handling
# This finds the directory where this script lives, so it can find CSS/JS files
PARENT_DIR = Path(__file__).parent.absolute()
CSS_PATH = PARENT_DIR / "styles.css"
JS_PATH = PARENT_DIR / "script.js"

def load_file(file_path):
    try:
        return file_path.read_text()
    except FileNotFoundError:
        st.error(f"⚠️ Could not find {file_path.name}. Please ensure it is in the same folder.")
        return ""

css = load_file(CSS_PATH)
js = load_file(JS_PATH)

# 3. Define the HTML Structure
# We wrap the UI in a single HTML block to allow the custom JS to interact with it
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>{css}</style>
</head>
<body>
    <header>
        <h1 class="main-header">🦡 Badger</h1>
        <p class="sub-header">Asset Matrix Creator — Generate naming conventions in seconds</p>
    </header>

    <div class="container">
        <aside class="sidebar">
            <section class="card">
                <h3>🛠️ Step 1: Choose Matrix Type</h3>
                <p class="caption">Select the type of assets you're creating</p>
                
                <div class="radio-group">
                    <label class="radio-label">
                        <input type="radio" name="matrixType" value="Social" checked>
                        <span>Social</span>
                    </label>
                    <label class="radio-label">
                        <input type="radio" name="matrixType" value="Display">
                        <span>Display</span>
                    </label>
                </div>
                
                <div id="platformsContainer">
                    <label class="label">Platforms</label>
                    <div class="checkbox-group" id="platformCheckboxes">
                        </div>
                </div>
            </section>

            <section class="card">
                <h3>⚙️ Step 2: Campaign Details</h3>
                <label class="label">Line of Business (LOB)</label>
                <select id="lobSelect" class="input-small">
                    <option>Connected Home</option>
                    <option>Consumer Wireless</option>
                    <option>Rogers Business</option>
                    <option>Rogers Bank</option>
                    <option>Corporate Brand</option>
                    <option>Shaw Direct</option>
                </select>

                <div class="date-row" style="display: flex; gap: 10px; margin-top: 10px;">
                    <div>
                        <label class="label">Start Date</label>
                        <input type="date" id="startDate" class="input-small">
                    </div>
                    <div>
                        <label class="label">End Date</label>
                        <input type="date" id="endDate" class="input-small">
                    </div>
                </div>
            </section>
        </aside>

        <main class="content">
            <div id="welcomePanel" class="card" style="text-align: center; padding: 4rem 2rem;">
                <div style="font-size: 4rem; margin-bottom: 1rem;">📋</div>
                <h2>Ready to generate your matrix?</h2>
                <p>Configure your settings on the left and click the button below.</p>
                <button id="generateBtn" class="btn btn-primary" style="margin-top: 1.5rem;">🚀 Generate Matrix</button>
            </div>

            <div id="resultPanel" class="card" style="display: none;">
                <div class="metrics-row">
                    <div class="metric-card">
                        <span id="totalAssets" class="metric-card-value">0</span>
                        <span class="metric-card-label">Total Assets</span>
                    </div>
                    <div class="metric-card">
                        <span id="colCount" class="metric-card-value">0</span>
                        <span class="metric-card-label">Columns</span>
                    </div>
                </div>
                
                <div class="table-container">
                    <table id="matrixTable">
                        <thead></thead>
                        <tbody></tbody>
                    </table>
                </div>
                
                <div class="divider"></div>
                
                <div class="button-row">
                    <button id="copyBtn" class="btn btn-primary">📋 Copy to Clipboard</button>
                    <button id="downloadBtn" class="btn btn-primary">📥 Download CSV</button>
                    <button id="clearBtn" class="btn btn-secondary">🗑️ Reset</button>
                </div>
            </div>
        </main>
    </div>

    <script>{js}</script>
</body>
</html>
'''

# 4. Inject into Streamlit
# We use a custom style block to hide the default Streamlit padding/header
st.markdown("""
<style>
    .stApp > header { display: none; }
    .block-container { padding: 0 !important; max-width: 100% !important; }
    iframe { border: none !important; }
</style>
""", unsafe_allow_html=True)

# Render the HTML component
components.html(html_content, height=1200, scrolling=True)
