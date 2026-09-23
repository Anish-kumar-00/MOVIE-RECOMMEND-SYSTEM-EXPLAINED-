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
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #05070d;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero-box {
        padding: 45px;
        border-radius: 25px;
        background: linear-gradient(
            135deg,
            #180811,
            #11151f
        );
        border: 1px solid #343846;
        margin-bottom: 35px;
    }

    .badge {
        color: #ff4d6d;
        font-weight: 800;
        letter-spacing: 1px;
        font-size: 14px;
    }

    .hero-title {
        font-size: 46px;
        font-weight: 900;
        color: white;
        margin-top: 12px;
    }

    .hero-description {
        color: #c7cbd4;
        font-size: 17px;
        line-height: 1.8;
        max-width: 900px;
        margin-top: 15px;
    }

    .card {
        background-color: #11151f;
        border: 1px solid #303542;
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 18px;
        min-height: 150px;
    }

    .card-title {
        color: white;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .card-text {
        color: #c6cad3;
        line-height: 1.7;
        font-size: 15px;
    }

    .number {
        color: #ff3155;
        font-size: 28px;
        font-weight: 900;
    }

    .team-card {
        background-color: #11151f;
        border: 1px solid #303542;
        border-radius: 18px;
        padding: 25px;
        text-align: center;
        min-height: 150px;
    }

    .team-name {
        color: white;
        font-size: 19px;
        font-weight: 800;
    }

    .team-role {
        color: #aeb4c0;
        margin-top: 8px;
    }

    .footer {
        text-align: center;
        color: #8f95a3;
        padding-top: 35px;
        padding-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <div class="hero-box">

        <div class="badge">
            🎬 MACHINE LEARNING PROJECT
        </div>

        <div class="hero-title">
            Movie Recommendation System
        </div>

        <div class="hero-description">
            A Content-Based Movie Recommendation System that recommends
            movies according to the similarity between their features,
            genres, keywords, cast, crew and other important information.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)

# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.header("🎬 Project Introduction")

st.subheader("🎞️ What is a Movie Recommendation System?")

st.write(
    "A Movie Recommendation System is a Machine Learning based "
    "system that helps users discover movies according to their interests."
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
# PROJECT OBJECTIVES
# ============================================================

st.header("🎯 Project Objectives")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🔎 Easy Discovery
            </div>

            <div class="card-text">
                Help users discover movies without manually searching
                through a huge movie collection.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                🤖 Machine Learning
            </div>

            <div class="card-text">
                Use Machine Learning and Natural Language Processing
                techniques to generate movie recommendations.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div class="card">

            <div class="card-title">
                ⚡ Fast Recommendation
            </div>

            <div class="card-text">
                Provide relevant movie recommendations quickly after
                the user selects a movie.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# ============================================================
# HOW SYSTEM WORKS
# ============================================================

st.header("⚙️ How Our System Works")

workflow = [

    (
        "01",
        "Data Collection",
        "Movie information is collected from the movie dataset."
    ),

    (
        "02",
        "Data Cleaning",
        "Unnecessary information is removed and useful data is prepared."
    ),

    (
        "03",
        "Feature Selection",
        "Important features such as genres, keywords, cast and crew are selected."
    ),

    (
        "04",
        "Bag of Words",
        "Important textual features are combined to create a meaningful representation."
    ),

    (
        "05",
        "Vectorization",
        "Movie information is converted into numerical vectors."
    ),

    (
        "06",
        "Similarity Calculation",
        "Cosine similarity is used to calculate similarity between movies."
    ),

    (
        "07",
        "Recommendation",
        "Movies having the highest similarity are selected and displayed."
    ),

    (
        "08",
        "Deployment",
        "The final application is deployed as an interactive web application using Streamlit."
    )

]

for start in range(0, len(workflow), 4):

    cols = st.columns(4)

    for col, item in zip(
        cols,
        workflow[start:start + 4]
    ):

        number, title, description = item

        with col:

            st.markdown(
                f"""
                <div class="card">

                    <div class="number">
                        {number}
                    </div>

                    <div class="card-title">
                        {title}
                    </div>

                    <div class="card-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

st.divider()

# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.header("🌐 Real-Life Applications")

applications = [

    (
        "🎥 OTT Platforms",
        "Recommendation systems can help OTT platforms suggest movies "
        "and shows based on the content users are interested in."
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
        "A similar content-based approach can recommend songs or artists "
        "based on their features."
    )

]

for start in range(0, len(applications), 3):

    cols = st.columns(3)

    for col, (title, description) in zip(
        cols,
        applications[start:start + 3]
    ):

        with col:

            st.markdown(
                f"""
                <div class="card">

                    <div class="card-title">
                        {title}
                    </div>

                    <div class="card-text">
                        {description}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

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

for col, (icon, name) in zip(
    tech_cols,
    technologies
):

    with col:

        st.markdown(
            f"""
            <div class="team-card">

                <div style="font-size:35px;">
                    {icon}
                </div>

                <div class="team-name">
                    {name}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# ============================================================
# PROJECT TEAM
# ============================================================

st.header("👥 Project Team")

team = [

    (
        "Abar Ahmad",
        "Special Project Manager"
    ),

    (
        "Anish",
        "Team Leader & Coder"
    ),

    (
        "Abhishek",
        "Mathematical Logic"
    ),

    (
        "Vishal",
        "Frontend"
    )

]

team_cols = st.columns(4)

for col, (name, role) in zip(
    team_cols,
    team
):

    with col:

        st.markdown(
            f"""
            <div class="team-card">

                <div style="font-size:38px;">
                    👤
                </div>

                <div class="team-name">
                    {name}
                </div>

                <div class="team-role">
                    {role}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

st.divider()

# ============================================================
# TEAM CONTRIBUTION
# ============================================================

st.header("📊 Team Contribution")

st.write(
    "✓ YES = Member is involved in that particular work."
)

st.write(
    "✕ NO = Member is not involved in that particular work."
)

# ============================================================
# IMPORTANT:
# ALL REQUESTED YES VALUES ARE SET HERE
# ============================================================

contribution_data = [

    [
        "To Make Recommendation System",
        "YES",
        "YES",
        "YES",
        "YES"
    ],

    [
        "Data Collections",
        "YES",
        "YES",
        "YES",
        "YES"
    ],

    [
        "Data Cleaning",
        "YES",
        "YES",
        "YES",
        "YES"
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
        "YES",
        "YES",
        "YES",
        "YES"
    ],

    [
        "Deployment",
        "YES",
        "YES",
        "YES",
        "YES"
    ],

    [
        "UI / Web Development",
        "YES",
        "YES",
        "YES",
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

# Native Streamlit table
# No HTML table is used here.

st.table(contribution_df)

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
        "Data Collections",
        "Abar Ahmad, Anish, Abhishek & Vishal",
        "Collection of movie data and required project information."
    ],

    [
        "Data Cleaning",
        "Abar Ahmad, Anish, Abhishek & Vishal",
        "Cleaning and preparation of useful movie information."
    ],

    [
        "Bag of Words",
        "Anish & Abhishek",
        "Creation of textual feature representation used by the recommendation model."
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
        "Abar Ahmad, Anish, Abhishek & Vishal",
        "Displaying and presenting recommendation results through the application."
    ],

    [
        "Deployment",
        "Abar Ahmad, Anish, Abhishek & Vishal",
        "Deployment and configuration of the Streamlit web application."
    ],

    [
        "UI / Web Development",
        "Abar Ahmad, Anish, Abhishek & Vishal",
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

st.caption("🎬 Movie Recommendation System")
st.caption("Machine Learning Project")
st.caption(
    "Developed by Abar Ahmad • Anish • Abhishek • Vishal"
)