from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="喵格侦探",
    page_icon="🐈‍⬛",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).with_name("index.html")
html = html_path.read_text(encoding="utf-8")

st.markdown(
    """
    <style>
      #MainMenu, header, footer { display: none; }
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], .stDeployButton, .stActionButton, .viewerBadge_container__1QSob {
        display: none !important;
      }
      .block-container {
        max-width: 100%;
        padding: 0;
      }
      html, body, [data-testid="stAppViewContainer"], .main, .stApp {
        height: 100%;
        overflow: hidden;
        background: transparent;
      }
      [data-testid="stAppViewBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
      }
      section.main > div {
        padding: 0 !important;
      }
      [data-testid="stVerticalBlock"], [data-testid="stElementContainer"] {
        height: 100svh;
        overflow: hidden;
      }
      [data-testid="stElementContainer"] > div {
        height: 100svh !important;
        overflow: hidden !important;
      }
      iframe {
        display: block;
        width: 100% !important;
        height: 100svh !important;
        min-height: 100svh !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=900, scrolling=False)
