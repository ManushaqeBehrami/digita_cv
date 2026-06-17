import streamlit as st

from other_pages.home import show_home
from other_pages.about import show_about
from other_pages.projects import show_projects
from other_pages.lessons.lessons import show_lessons

PAGE_TITLE = "Digital CV | Manushaqe Behrami"
PAGE_ICON = ":wave:"

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON
)

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "About",
        "Projects",
        "Lessons",
    ]
)

if page == "Home":
    show_home()

elif page == "About":
    show_about()

elif page == "Projects":
    show_projects()

elif page == "Lessons":
    show_lessons()