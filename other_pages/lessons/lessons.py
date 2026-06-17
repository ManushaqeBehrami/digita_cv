import streamlit as st

from other_pages.lessons import lecture_12
from other_pages.lessons import lecture_13


def show_lessons():
    st.title("Lessons")

    lectures = {
        "Lecture 12": lecture_12.show,
        "Lecture 13": lecture_13.show,
    }

    choice = st.selectbox(
        "Choose a lecture",
        ["Select a lecture"] + list(lectures.keys())
    )

    if choice == "Select a lecture":
        st.info("Please select a lecture to view its content.")
        return

    lectures[choice]()