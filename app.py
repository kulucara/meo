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
      :root { --streamlit-strip-fix: 64px; }
      #MainMenu, header, footer { display: none !important; }
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"],
      [data-testid="stStatusWidget"], [data-testid="stToolbarActions"], [data-testid="collapsedControl"],
      [data-testid="stBaseButton-header"], [data-testid="manage-app-button"], [data-testid="stMainMenu"],
      .stDeployButton, .stActionButton, .viewerBadge_container__1QSob, .viewerBadge_link__1S137,
      .viewerBadge_container__r5tak, .viewerBadge_link__qRIco {
        display: none !important;
        visibility: hidden !important;
        pointer-events: none !important;
        position: fixed !important;
        inset: auto auto 100% auto !important;
        height: 0 !important;
        min-height: 0 !important;
        max-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
        border: 0 !important;
        overflow: hidden !important;
      }
      body {
        margin: 0 !important;
        padding: 0 !important;
        background:
          radial-gradient(circle at 12% 10%, rgba(255, 255, 255, 0.92) 0 12rem, transparent 12rem),
          linear-gradient(135deg, #f8ede8 0%, #eef7f4 54%, #fff6e3 100%) !important;
      }
      .block-container {
        max-width: 100%;
        padding: 0 !important;
      }
      html, body, [data-testid="stAppViewContainer"], .main, .stApp, [data-testid="stMain"] {
        height: 100svh;
        overflow: hidden;
        background:
          radial-gradient(circle at 12% 10%, rgba(255, 255, 255, 0.92) 0 12rem, transparent 12rem),
          linear-gradient(135deg, #f8ede8 0%, #eef7f4 54%, #fff6e3 100%) !important;
      }
      .stApp {
        margin-top: calc(var(--streamlit-strip-fix) * -1) !important;
        height: calc(100svh + var(--streamlit-strip-fix)) !important;
      }
      [data-testid="stAppViewContainer"] {
        top: calc(var(--streamlit-strip-fix) * -1) !important;
        transform: translateY(calc(var(--streamlit-strip-fix) * -1));
        height: calc(100svh + var(--streamlit-strip-fix) * 2) !important;
      }
      .stApp > div:first-child,
      [data-testid="stAppViewContainer"] > section:first-child,
      section[data-testid="stMain"], section.main {
        top: calc(var(--streamlit-strip-fix) * -1) !important;
        padding-top: 0 !important;
        margin-top: calc(var(--streamlit-strip-fix) * -1) !important;
      }
      [data-testid="stAppViewBlockContainer"] {
        padding: 0 !important;
        max-width: 100% !important;
        margin-top: 0 !important;
      }
      section.main > div {
        padding: 0 !important;
      }
      [data-testid="stVerticalBlock"], [data-testid="stElementContainer"] {
        height: calc(100svh + var(--streamlit-strip-fix) * 2);
        overflow: hidden;
      }
      [data-testid="stElementContainer"] > div {
        height: calc(100svh + var(--streamlit-strip-fix) * 2) !important;
        overflow: hidden !important;
      }
      iframe {
        display: block;
        width: 100% !important;
        height: calc(100svh + var(--streamlit-strip-fix) * 2) !important;
        min-height: calc(100svh + var(--streamlit-strip-fix) * 2) !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

components.html(html, height=1200, scrolling=False)
