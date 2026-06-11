import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Manushaqe Behrami"
PAGE_ICON = ":wave:"
NAME = "Manushaqe Behrami"
DESCRIPTION = """
Software Engineer specializing in full stack web development and scalable applications.
"""

EMAIL = "manushaqe@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com"

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/Lorem_ipsum_CV.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV.pdf",
            mime="application/octet-stream",
        )

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications")
    st.write(
        """
- ✔️ Experience in full stack software development across web applications.
- ✔️ Strong background in backend and frontend development using modern technologies.
- ✔️ Experience collaborating in agile teams, code reviews and production environments.
- ✔️ Focus on clean code, debugging, performance optimization and scalable systems.
"""
    )

    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills")
    st.write(
        """
- 👩‍💻 Programming: C#, JavaScript, TypeScript, Java, SQL
- ⚛️ Frontend: ReactJS, VueJS, HTML, CSS
- 🔧 Backend: ASP.NET Core, NodeJS
- 🗄️ Databases: MySQL, MongoDB
- ☁️ Tools & Platforms: Docker, Azure, Git
"""
    )

    # --- WORK HISTORY ---
    st.write("\n")
    st.subheader("Work History")
    st.write("---")

    # --- JOB 1
    st.write("🚧", "**Software Engineer | Isa Consulting**")
    st.write("09/2024 – 11/2025")
    st.write(
        """
- ► Developed and maintained backend application features under senior guidance.
- ► Participated in debugging, testing and improving system reliability and performance.
- ► Collaborated with cross functional teams in an agile environment.
"""
    )

    # --- JOB 2
    st.write("\n")
    st.write("🚧", "**Full Stack Developer Apprentice | LIFE from Gjirafa**")
    st.write("11/2023 – 09/2024")
    st.write(
        """
- ► Gained hands on experience in full stack development using modern web technologies.
- ► Worked on frontend and backend features in real world projects
- ► Contributed to deployment workflows and cloud based applications.
"""
    )

    # --- JOB 3
    st.write("\n")
    st.write("🚧", "**Software Development Lecturer | jCoders Academy**")
    st.write("10/2021 – 09/2024")
    st.write(
        """
- ► Taught web development fundamentals including JavaScript, HTML, CSS and databases.
- ► Mentored students through hands on projects and coding exercises.
- ► Updated and improved learning materials based on industry practices.
"""
    )

    # --- JOB 4
    st.write("\n")
    st.write("🚧", "**Full Stack Developer | Freelance**")
    st.write("09/2022 – Current")
    st.write(
        """
- ► Built full stack web applications using modern frontend and backend technologies.
- ► Designed and maintained APIs and database driven applications.
- ► Delivered end to end solutions from planning to deployment.
"""
    )

elif page == "About":
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
