import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# TITLE
# ============================================================

st.title("🎬 Movie Recommendation System")

st.write(
    "A Content-Based Movie Recommendation System that recommends "
    "movies according to the similarity between their features, "
    "genres, keywords, cast, crew and other important information."
)

st.divider()

# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.header("🎬 Project Introduction")

st.subheader("🎞️ What is a Movie Recommendation System?")

st.write(
    "A Movie Recommendation System is a Machine Learning based "
    "system that helps users discover movies according to their "
    "interests."
)

st.write(
    "Instead of manually searching through thousands of movies, "
    "the system analyzes movie information and recommends movies "
    "that are similar to the movie selected by the user."
)

st.write(
    "Our project uses a Content-Based Filtering approach. "
    "The system analyzes different features of movies such as "
    "genres, keywords, cast, crew and other textual information."
)

st.write(
    "These features are converted into numerical vectors and "
    "their similarity is calculated using mathematical techniques."
)

st.write(
    "When a user selects a movie, the system compares that movie "
    "with other movies and displays the most similar movies."
)

st.divider()

# ============================================================
# OBJECTIVES
# ============================================================

st.header("🎯 Project Objectives")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("🔎 Easy Discovery")
    st.write(
        "Help users discover movies without manually searching "
        "through a huge movie collection."
    )

with col2:
    st.subheader("🤖 Machine Learning")
    st.write(
        "Use Machine Learning and Natural Language Processing "
        "techniques to generate movie recommendations."
    )

with col3:
    st.subheader("⚡ Fast Recommendation")
    st.write(
        "Provide relevant movie recommendations quickly after "
        "the user selects a movie."
    )

st.divider()

# ============================================================
# WORKFLOW
# ============================================================

st.header("⚙️ How Our System Works")

workflow = [
    ("01", "Data Collection",
     "Movie information is collected from the movie dataset."),

    ("02", "Data Cleaning",
     "Unnecessary information is removed and useful data is prepared."),

    ("03", "Feature Selection",
     "Important features such as genres, keywords, cast and crew are selected."),

    ("04", "Bag of Words",
     "Important textual features are combined to create a meaningful representation."),

    ("05", "Vectorization",
     "Movie information is converted into numerical vectors."),

    ("06", "Similarity Calculation",
     "Cosine similarity is used to calculate similarity between movies."),

    ("07", "Recommendation",
     "Movies having the highest similarity are selected and displayed."),

    ("08", "Deployment",
     "The final application is deployed as an interactive web application using Streamlit.")
]

for i in range(0, len(workflow), 4):

    cols = st.columns(4)

    for col, item in zip(cols, workflow[i:i + 4]):

        number, title, description = item

        with col:

            st.subheader(f"{number} — {title}")
            st.write(description)

st.divider()

# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.header("🌐 Real-Life Applications")

applications = [
    (
        "🎥 OTT Platforms",
        "Recommendation systems can help OTT platforms suggest "
        "movies and shows based on the content users are interested in."
    ),

    (
        "🍿 Streaming Services",
        "Streaming platforms can help users discover relevant movies "
        "without searching through a large catalogue."
    ),

    (
        "🎬 Movie Websites",
        "Movie websites can recommend similar movies when a user "
        "opens the details of a particular movie."
    ),

    (
        "📱 Entertainment Apps",
        "Entertainment applications can personalize content discovery "
        "using recommendation algorithms."
    ),

    (
        "🛒 E-Commerce",
        "The same recommendation concept can be applied to recommend "
        "products similar to a product selected by a customer."
    ),

    (
        "🎵 Music Recommendation",
        "A similar content-based approach can recommend songs or "
        "artists based on their features."
    )
]

for i in range(0, len(applications), 3):

    cols = st.columns(3)

    for col, (title, description) in zip(
        cols,
        applications[i:i + 3]
    ):

        with col:
            st.subheader(title)
            st.write(description)

st.divider()

# ============================================================
# TECHNOLOGIES
# ============================================================

st.header("💻 Technologies Used")

tech_cols = st.columns(5)

technologies = [
    ("🐍", "Python"),
    ("🤖", "Machine Learning"),
    ("📊", "Pandas"),
    ("🔢", "NumPy"),
    ("🌐", "Streamlit")
]

for col, (icon, name) in zip(tech_cols, technologies):

    with col:
        st.subheader(f"{icon} {name}")

st.divider()

# ============================================================
# PROJECT TEAM
# ============================================================

st.header("👥 Project Team")

team = [
    ("Abar Ahmad", "Special Project Manager"),
    ("Anish", "Team Leader & Coder"),
    ("Abhishek", "Mathematical Logic"),
    ("Vishal", "Frontend")
]

team_cols = st.columns(4)

for col, (name, role) in zip(team_cols, team):

    with col:

        st.subheader(f"👤 {name}")
        st.write(role)

st.divider()

# ============================================================
# TEAM CONTRIBUTION
# ============================================================

st.header("📊 Team Contribution")

st.info(
    "YES = Member is involved in that particular work\n\n"
    "NO = Member is not involved in that particular work"
)

# ------------------------------------------------------------
# IMPORTANT:
# Abar Ahmad = Special Project Manager
# Anish = Team Leader & Coding
# Abhishek = Mathematical Logic
# Vishal = Frontend
#
# Technical contribution values are taken from the uploaded
# handwritten table.
# ------------------------------------------------------------

contribution_data = [

    [
        "To Make Recommendation System",
        "NO",
        "NO",
        "NO",
        "NO"
    ],

    [
        "Data Collection",
        "NO",
        "NO",
        "NO",
        "NO"
    ],

    [
        "Data Cleaning",
        "NO",
        "YES",
        "NO",
        "NO"
    ],

    [
        "Bag of Words",
        "NO",
        "YES",
        "YES",
        "NO"
    ],

    [
        "Similarity Matrix",
        "NO",
        "YES",
        "YES",
        "NO"
    ],

    [
        "Vectorization",
        "NO",
        "YES",
        "YES",
        "NO"
    ],

    [
        "Cosine Matrix",
        "NO",
        "YES",
        "YES",
        "NO"
    ],

    [
        "Result",
        "NO",
        "YES",
        "NO",
        "YES"
    ],

    [
        "Deployment",
        "NO",
        "YES",
        "NO",
        "NO"
    ],

    [
        "UI / Web Development",
        "NO",
        "NO",
        "NO",
        "YES"
    ],

    [
        "Project Management",
        "YES",
        "NO",
        "NO",
        "NO"
    ]
]

contribution_df = pd.DataFrame(
    contribution_data,
    columns=[
        "Project Work",
        "Abar Ahmad",
        "Anish",
        "Abhishek",
        "Vishal"
    ]
)

st.dataframe(
    contribution_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

st.header("📝 Detailed Contribution")

detailed_data = [

    [
        "Project Management",
        "Abar Ahmad",
        "Special project management and overall project coordination."
    ],

    [
        "Data Cleaning",
        "Anish",
        "Data cleaning and preparation of useful movie information."
    ],

    [
        "Bag of Words",
        "Anish & Abhishek",
        "Creation of the textual feature representation used by the recommendation model."
    ],

    [
        "Similarity Matrix",
        "Anish & Abhishek",
        "Calculation and preparation of movie similarity information."
    ],

    [
        "Vectorization",
        "Anish & Abhishek",
        "Conversion of selected textual features into numerical vectors."
    ],

    [
        "Cosine Matrix",
        "Anish & Abhishek",
        "Calculation of cosine similarity between movie vectors."
    ],

    [
        "Result",
        "Anish & Vishal",
        "Displaying recommendation results through the application interface."
    ],

    [
        "Deployment",
        "Anish",
        "Deployment and configuration of the Streamlit web application."
    ],

    [
        "UI / Web Development",
        "Vishal",
        "Frontend design and user-interface development."
    ]
]

detailed_df = pd.DataFrame(
    detailed_data,
    columns=[
        "Project Work",
        "Member",
        "Contribution"
    ]
)

st.dataframe(
    detailed_df,
    use_container_width=True,
    hide_index=True
)

st.divider()

# ============================================================
# PROJECT OUTCOME
# ============================================================

st.header("🏆 Project Outcome")

st.subheader("🎬 Final Result")

st.write(
    "The final result is an interactive web-based "
    "Movie Recommendation System where users can select "
    "a movie and receive recommendations for similar movies."
)

st.write(
    "The project combines Machine Learning, Natural Language "
    "Processing, Mathematics, Python Programming and Web "
    "Development into a single practical application."
)

st.write(
    "The system demonstrates how Machine Learning techniques "
    "can be used to solve a real-world content recommendation problem."
)

st.divider()

# ============================================================
# FOOTER
# ============================================================

st.caption(
    "🎬 Movie Recommendation System"
)

st.caption(
    "Machine Learning Project"
)

st.caption(
    "Developed by Abar Ahmad • Anish • Abhishek • Vishal"
)