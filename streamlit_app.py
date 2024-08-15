import streamlit as st


# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="Acerca de",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    "views/dashboard.py",
    title="Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="ChatBot",
    icon=":material/smart_toy:",
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
#pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)


# --- SHARED ON ALL PAGES ---
st.logo("assets/escudo_ing.png")
st.sidebar.markdown("Made with ❤️ by [Daniel]()")


# --- RUN NAVIGATION ---
pg.run()
