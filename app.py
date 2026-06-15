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
      .block-container {
        max-width: 100%;
        padding: 0;
      }
      html, body, [data-testid="stAppViewContainer"], .main {
        height: 100%;
        overflow: hidden;
        background: transparent;
      }
      [data-testid="stVerticalBlock"], [data-testid="stElementContainer"] {
        height: 100svh;
      }
      iframe {
        display: block;
        width: 100% !important;
        height: 100svh !important;
        min-height: 100svh !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=1200, scrolling=True)
