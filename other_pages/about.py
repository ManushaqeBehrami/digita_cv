import streamlit as st

EMAIL = "manushaqe@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com"

def show_about():
    st.title("About Me")

    st.write("""
    I am a Full Stack Software Developer with experience in building modern web applications
    across frontend and backend systems. I enjoy working with technologies such as ReactJS,
    VueJS, C#, JavaScript, Java and ASP.NET Core to create scalable and efficient solutions.

    I have worked in both development and teaching environments, which strengthened my ability
    to communicate technical concepts clearly and collaborate effectively in teams. My focus is
    on building reliable software, improving performance and continuously learning new technologies.
    """)

    # Show LinkedIn and Email only on the About page
    st.write("📫", EMAIL)
    st.write(f"Feel free to connect with me on [LinkedIn]({LINKEDIN_URL}).")