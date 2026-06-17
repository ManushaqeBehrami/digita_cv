import streamlit as st

def show():
    st.title("Lecture 12: SQL, DBMS & Data Warehousing")

    st.write("")

    st.header("📌 DBMS vs RDBMS")
    st.write("""
- DBMS stores data in files and is more basic  
- RDBMS stores data in tables (rows and columns)  
- RDBMS supports relationships using keys  
- Examples: MySQL, PostgreSQL
""")

    st.header("📌 SQL Relationships")
    st.write("""
- One-to-One: one record maps to one record  
- One-to-Many: one record maps to many records  
- Many-to-Many: many records map to many records (uses a junction table)
""")

    st.header("📌 Database Normalization")
    st.write("""
- Organizes data to reduce duplication  
- Improves consistency  
- Makes databases more efficient and clean
""")

    st.header("📌 Star Schema vs Snowflake Schema")
    st.write("""
- Star Schema: simple structure, faster queries  
- Snowflake Schema: more structured, less redundancy, more complex
""")

    st.header("📌 Slowly Changing Dimensions (SCD)")
    st.write("""
- Used to track changes in data over time  
- Type 1: overwrite old data  
- Type 2: keep full history (new row added)  
- Type 3: keep limited history
""")

    st.header("📌 OLTP vs OLAP")
    st.write("""
- OLTP: real-time transactions (banking, apps)  
- OLAP: data analysis and reporting (BI systems)
""")

    st.header("📌 Spark & Iceberg (Basics)")
    st.write("""
- Spark SQL: query data using SQL  
- DataFrames: programmatic data processing  
- Iceberg: improves big data storage, performance, and versioning
""")

    st.header("📌 Key Takeaway")
    st.write("""
- SQL is used for structured data  
- DBMS manages data storage  
- Data warehouses support analytics  
- Big data tools help scale systems
""")