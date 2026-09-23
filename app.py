import streamlit as st
import pandas as pd

# ============================================================
# PAGE CONFIGURATION
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

    /* Main background */
    .stApp {
        background:
            radial-gradient(
                circle at 15% 10%,
                rgba(255, 0, 55, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 85% 40%,
                rgba(90, 0, 255, 0.10),
                transparent 30%
            ),
            #05070d;
        color: white;
    }

    /* Main container */
    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Text */
    h1, h2, h3, h4 {
        color: white !important;
    }

    p {
        color: #d4d7df;
        line-height: 1.8;
    }

    /* Hero */
    .hero {
        padding: 55px 45px;
        border-radius: 28px;
        background:
            linear-gradient(
                135deg,
                rgba(80, 0, 20, 0.65),
                rgba(18, 20, 30, 0.95)
            );
        border: 1px solid rgba(255, 35, 75, 0.35);
        box-shadow:
            0 20px 60px rgba(255, 0, 50, 0.10),
            inset 0 0 50px rgba(255, 0, 50, 0.04);
        margin-bottom: 50px;
    }

    .badge {
        display: inline-block;
        padding: 8px 16px;
        border-radius: 50px;
        background: rgba(255, 30, 60, 0.15);
        border: 1px solid rgba(255, 50, 80, 0.45);
        color: #ff6b82;
        font-weight: 700;
        font-size: 14px;
        letter-spacing: 1px;
        margin-bottom: 18px;
    }

    .hero-title {
        font-size: 48px;
        font-weight: 800;
        margin: 0;
        color: white;
    }

    .hero-text {
        font-size: 18px;
        max-width: 850px;
        margin-top: 18px;
        color: #cfd2da;
    }

    /* Section heading */
    .section-title {
        font-size: 32px;
        font-weight: 800;
        margin-top: 45px;
        margin-bottom: 8px;
        color: white;
    }

    .section-line {
        width: 110px;
        height: 5px;
        border-radius: 20px;
        background: #ff173f;
        margin-bottom: 30px;
    }

    /* Cards */
    .info-card {
        background: rgba(24, 27, 36, 0.95);
        border: 1px solid rgba(90, 100, 140, 0.30);
        border-radius: 20px;
        padding: 28px;
        margin-bottom: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.25);
    }

    .info-icon {
        font-size: 32px;
        margin-bottom: 8px;
    }

    .info-title {
        color: white;
        font-size: 21px;
        font-weight: 750;
        margin-bottom: 8px;
    }

    .info-text {
        color: #cdd1db;
        font-size: 15px;
        line-height: 1.75;
    }

    /* Workflow */
    .workflow-card {
        background: rgba(20, 23, 31, 0.95);
        border: 1px solid rgba(80, 90, 120, 0.30);
        border-radius: 18px;
        padding: 25px;
        min-height: 190px;
        margin-bottom: 20px;
    }

    .workflow-number {
        font-size: 30px;
        font-weight: 900;
        color: #ff3155;
    }

    .workflow-title {
        font-size: 19px;
        font-weight: 750;
        color: white;
        margin-top: 8px;
    }

    .workflow-text {
        color: #c7cbd4;
        font-size: 14px;
        line-height: 1.7;
    }

    /* Team */
    .team-card {
        background: rgba(22, 25, 34, 0.96);
        border: 1px solid rgba(90, 100, 140, 0.30);
        border-radius: 20px;
        padding: 28px;
        text-align: center;
        min-height: 180px;
        margin-bottom: 20px;
    }

    .team-icon {
        font-size: 42px;
    }

    .team-name {
        font-size: 20px;
        font-weight: 800;
        color: white;
        margin-top: 10px;
    }

    .team-role {
        color: #aeb4c2;
        margin-top: 8px;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 45px 10px 15px 10px;
        color: #969baa;
    }

    .footer-title {
        color: white;
        font-size: 20px;
        font-weight: 800;
    }

    /* Mobile */
    @media (max-width: 700px) {

        .block-container {
            padding-left: 12px;
            padding-right: 12px;
        }

        .hero {
            padding: 32px 22px;
        }

        .hero-title {
            font-size: 34px;
        }

        .hero-text {
            font-size: 15px;
        }

        .section-title {
            font-size: 27px;
        }
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
    <div class="hero">
        <div class="badge">🎬 MACHINE LEARNING PROJECT</div>

        <div class="hero-title">
            Movie Recommendation System
        </div>

        <div class="hero-text">
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

st.markdown(
    '<div class="section-title">🎬 Project Introduction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-card">

    <div class="info-icon">🎞️</div>

    <div class="info-title">
        What is a Movie Recommendation System?
    </div>

    <div class="info-text">

    A Movie Recommendation System is a Machine Learning based
    system that helps users discover movies according to their
    interests.

    <br><br>

    Instead of manually searching through thousands of movies,
    the system analyzes movie information and recommends movies
    that are similar to the movie selected by the user.

    <br><br>

    Our project uses a <b>Content-Based Filtering</b> approach.

    The system analyzes different features of movies such as
    genres, keywords, cast, crew and other textual information.

    <br><br>

    These features are converted into numerical vectors and
    their similarity is calculated using mathematical techniques.

    <br><br>

    When a user selects a movie, the system compares that movie
    with other movies and displays the most similar movies.

    </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# OBJECTIVES
# ============================================================

st.markdown(
    '<div class="section-title">🎯 Project Objectives</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

objective_columns = st.columns(3)

objectives = [
    (
        "🔎",
        "Easy Discovery",
        "Help users discover movies without manually searching through a huge movie collection."
    ),
    (
        "🤖",
        "Machine Learning",
        "Use Machine Learning and Natural Language Processing techniques to generate movie recommendations."
    ),
    (
        "⚡",
        "Fast Recommendation",
        "Provide relevant movie recommendations quickly after the user selects a movie."
    )
]

for col, (icon, title, text) in zip(objective_columns, objectives):

    with col:
        st.markdown(
            f"""
            <div class="info-card">
                <div class="info-icon">{icon}</div>
                <div class="info-title">{title}</div>
                <div class="info-text">{text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# WORKFLOW
# ============================================================

st.markdown(
    '<div class="section-title">⚙️ How Our System Works</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

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

for i in range(0, len(workflow), 4):

    cols = st.columns(4)

    for col, item in zip(cols, workflow[i:i + 4]):

        number, title, text = item

        with col:

            st.markdown(
                f"""
                <div class="workflow-card">

                    <div class="workflow-number">
                        {number}
                    </div>

                    <div class="workflow-title">
                        {title}
                    </div>

                    <div class="workflow-text">
                        {text}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.markdown(
    '<div class="section-title">🌐 Real-Life Applications</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

applications = [
    (
        "🎥",
        "OTT Platforms",
        "Recommendation systems can help OTT platforms suggest movies and shows based on the content users are interested in."
    ),
    (
        "🍿",
        "Streaming Services",
        "Streaming platforms can help users discover relevant movies without searching through a large catalogue."
    ),
    (
        "🎬",
        "Movie Websites",
        "Movie websites can recommend similar movies when a user opens the details of a particular movie."
    ),
    (
        "📱",
        "Entertainment Apps",
        "Entertainment applications can personalize content discovery using recommendation algorithms."
    ),
    (
        "🛒",
        "E-Commerce",
        "The same recommendation concept can be applied to recommend products similar to a product selected by a customer."
    ),
    (
        "🎵",
        "Music Recommendation",
        "A similar content-based approach can recommend songs or artists based on their features."
    )
]

for i in range(0, len(applications), 3):

    cols = st.columns(3)

    for col, item in zip(cols, applications[i:i + 3]):

        icon, title, text = item

        with col:

            st.markdown(
                f"""
                <div class="info-card">

                    <div class="info-icon">
                        {icon}
                    </div>

                    <div class="info-title">
                        {title}
                    </div>

                    <div class="info-text">
                        {text}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )


# ============================================================
# TECHNOLOGIES
# ============================================================

st.markdown(
    '<div class="section-title">💻 Technologies Used</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

technologies = [
    ("🐍", "Python"),
    ("🤖", "Machine Learning"),
    ("📊", "Pandas"),
    ("🔢", "NumPy"),
    ("🌐", "Streamlit")
]

cols = st.columns(5)

for col, (icon, name) in zip(cols, technologies):

    with col:

        st.markdown(
            f"""
            <div class="team-card">

                <div class="team-icon">
                    {icon}
                </div>

                <div class="team-name">
                    {name}
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# PROJECT TEAM
# ============================================================

st.markdown(
    '<div class="section-title">👥 Project Team</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

team = [
    (
        "👤",
        "Abar Ahmad",
        "Special Project Manager"
    ),
    (
        "👤",
        "Anish",
        "Team Leader & Coder"
    ),
    (
        "👤",
        "Abhishek",
        "Mathematical Logic"
    ),
    (
        "👤",
        "Vishal",
        "Frontend"
    )
]

cols = st.columns(4)

for col, (icon, name, role) in zip(cols, team):

    with col:

        st.markdown(
            f"""
            <div class="team-card">

                <div class="team-icon">
                    {icon}
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


# ============================================================
# TEAM CONTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">📊 Team Contribution</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.info(
    "✓ YES = Member is involved in that particular part    |    "
    "✕ NO = Member is not involved in that particular part"
)


# ------------------------------------------------------------
# CONTRIBUTION DATA
# ------------------------------------------------------------

contribution_data = [
    ["To Make Recommendation System", "NO", "NO", "NO", "NO"],
    ["Data Collection", "NO", "NO", "NO", "NO"],
    ["Data Cleaning", "NO", "NO", "YES", "NO"],
    ["Bag of Words", "NO", "YES", "YES", "NO"],
    ["Similarity Matrix", "NO", "YES", "YES", "NO"],
    ["Vectorization", "NO", "YES", "YES", "NO"],
    ["Cosine Matrix", "NO", "YES", "YES", "NO"],
    ["Result", "NO", "YES", "YES", "YES"],
    ["Deployment", "NO", "YES", "NO", "NO"],
    ["UI / Web Development", "NO", "NO", "NO", "YES"],
    ["Project Management", "YES", "NO", "NO", "NO"]
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


# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

st.markdown(
    '<div class="section-title">📝 Detailed Contribution</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

detailed_data = [
    [
        "Project Management",
        "Abar Ahmad",
        "Special project management and overall project coordination."
    ],
    [
        "Bag of Words",
        "Anish & Abhishek",
        "Creation of the textual feature representation used by the recommendation model."
    ],
    [
        "Data Cleaning",
        "Abhishek",
        "Data cleaning and preparation of useful movie information."
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
        "Anish, Abhishek & Vishal",
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


# ============================================================
# PROJECT OUTCOME
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Project Outcome</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-line"></div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-card">

    <div class="info-icon">🎬</div>

    <div class="info-title">
        Final Result
    </div>

    <div class="info-text">

    The final result is an interactive web-based
    <b>Movie Recommendation System</b>
    where users can select a movie and receive recommendations
    for similar movies.

    <br><br>

    The project combines
    <b>Machine Learning, Natural Language Processing,
    Mathematics, Python Programming</b>
    and <b>Web Development</b>
    into a single practical application.

    <br><br>

    The system demonstrates how Machine Learning techniques can
    be used to solve a real-world content recommendation problem.

    </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-title">
            🎬 Movie Recommendation System
        </div>

        <div>
            Machine Learning Project
        </div>

        <br>

        <div>
            Developed by
            <b>Abar Ahmad</b> •
            <b>Anish</b> •
            <b>Abhishek</b> •
            <b>Vishal</b>
        </div>

    </div>
    """,
    unsafe_allow_html=True
)