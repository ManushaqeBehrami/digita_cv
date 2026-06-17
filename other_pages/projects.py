import streamlit as st


def show_projects():
    st.title("My Projects")

    st.write(
        """
**WorkFlow - HR Management System (01/2026 – 02/2026)**  
Technologies: C# ASP.NET, ReactJS, MySQL, MongoDB

Developed a full stack HR management platform using ASP.NET, REST API and ReactJS for managing
employees, payroll, contracts and user roles. Implemented JWT authentication with role based
access control for Employees, HR personnel and Managers. Built a complete PTO workflow for
submitting, approving and rejecting leave requests. Utilized MySQL and MongoDB for data
management and documented APIs using Swagger.

**Ditari Im (02/2025 – 04/2025)**  
Technologies: ASP.NET (C#), ReactJS, TypeScript, MySQL

Built a full stack web application using ASP.NET REST API, ReactJS, TypeScript and MySQL.
Implemented authentication and role based authorization, along with full CRUD functionality
for managing structured data. Designed a responsive and maintainable frontend and documented
backend APIs using Swagger.

**Event Ticketing System (04/2024 – 05/2024)**  
Technologies: C# ASP.NET MVC, ReactJS, MySQL, Entity Framework, Elasticsearch

Developed a full stack event management platform enabling event creation, ticket booking and
role based access for organizers and users. Integrated Elasticsearch for fast event search and
filtering, utilized Entity Framework for data access, implemented unit testing for backend
functionality and documented APIs with Swagger.
"""
    )