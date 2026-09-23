import streamlit as st

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
# CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 5% 5%, rgba(255, 0, 70, .15), transparent 25%),
        radial-gradient(circle at 95% 5%, rgba(100, 30, 255, .15), transparent 25%),
        linear-gradient(135deg, #02040a, #070b17, #02040a);
    color: white;
}

.block-container {
    max-width: 1450px;
    padding: 25px 25px 40px;
}

/* ============================================================
   HERO
============================================================ */

.hero {
    text-align: center;
    padding: 42px 25px;
    margin-bottom: 25px;

    border: 1px solid rgba(255, 50, 120, .45);
    border-radius: 25px;

    background:
        radial-gradient(
            circle at 10% 50%,
            rgba(255, 0, 70, .20),
            transparent 30%
        ),
        radial-gradient(
            circle at 90% 50%,
            rgba(100, 30, 255, .20),
            transparent 30%
        ),
        rgba(5, 8, 20, .92);

    box-shadow:
        0 0 50px rgba(255, 0, 80, .10);
}

.badge {
    display: inline-block;

    padding: 9px 20px;

    border-radius: 30px;

    background:
        linear-gradient(
            90deg,
            #ff1744,
            #d500f9
        );

    color: white;

    font-size: 13px;
    font-weight: 800;
}

.hero h1 {
    margin: 15px 0 10px;

    font-size: clamp(35px, 5vw, 60px);
    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #ff719f,
            #bd7cff
        );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    max-width: 850px;

    margin: auto;

    color: #cdd3e5;

    font-size: 15px;

    line-height: 1.7;
}

/* ============================================================
   SECTION TITLE
============================================================ */

.section-title {
    display: flex;

    align-items: center;

    gap: 10px;

    margin-top: 28px;
    margin-bottom: 15px;

    padding-bottom: 8px;

    border-bottom:
        1px solid rgba(255,255,255,.10);
}

.section-title .emoji {
    font-size: 25px;
}

.section-title h2 {
    margin: 0;

    font-size: 23px;
    font-weight: 800;
}

/* ============================================================
   CARD
============================================================ */

.card {
    padding: 20px;

    border:
        1px solid rgba(100,130,255,.35);

    border-radius: 16px;

    background:
        linear-gradient(
            145deg,
            rgba(15,22,45,.95),
            rgba(5,9,22,.95)
        );

    box-shadow:
        0 8px 25px rgba(0,0,0,.25);

    margin-bottom: 12px;
}

.card:hover {
    border-color:
        rgba(255,70,150,.65);

    transform: translateY(-2px);

    transition: .2s;
}

.card-icon {
    font-size: 32px;

    margin-bottom: 8px;
}

.card h3 {
    margin: 0 0 10px;

    font-size: 17px;
}

.card p {
    margin: 0;

    color: #c9d0e2;

    font-size: 13px;

    line-height: 1.65;
}

/* ============================================================
   WORKFLOW
============================================================ */

.workflow {
    display: grid;

    grid-template-columns:
        repeat(8, minmax(120px, 1fr));

    gap: 10px;
}

.workflow-card {
    min-height: 170px;

    padding: 14px;

    border:
        1px solid rgba(80,150,255,.35);

    border-radius: 14px;

    background:
        rgba(8,15,31,.95);
}

.number {
    display: flex;

    width: 34px;
    height: 34px;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #ff1744,
            #7c4dff
        );

    font-size: 12px;

    font-weight: 800;

    margin-bottom: 10px;
}

.workflow-card h4 {
    margin: 0 0 8px;

    font-size: 14px;
}

.workflow-card p {
    margin: 0;

    color: #b9c2d8;

    font-size: 11px;

    line-height: 1.5;
}

/* ============================================================
   TABLE
============================================================ */

.table-box {
    width: 100%;

    overflow-x: auto;

    border:
        1px solid rgba(255,50,110,.40);

    border-radius: 16px;

    background:
        rgba(4,9,20,.95);
}

.contribution-table {
    width: 100%;

    min-width: 720px;

    border-collapse: collapse;
}

.contribution-table th {
    padding: 14px 12px;

    background:
        linear-gradient(
            90deg,
            rgba(255,0,70,.18),
            rgba(100,30,255,.18)
        );

    color: white;

    font-size: 13px;

    text-align: center;

    border-bottom:
        1px solid rgba(255,255,255,.12);
}

.contribution-table th:first-child {
    text-align: left;
}

.contribution-table td {
    padding: 11px 12px;

    color: #d8ddec;

    font-size: 12px;

    text-align: center;

    border-bottom:
        1px solid rgba(255,255,255,.07);
}

.contribution-table td:first-child {
    text-align: left;
}

.contribution-table tr:hover td {
    background:
        rgba(255,255,255,.035);
}

.yes {
    display: inline-block;

    padding: 5px 11px;

    border-radius: 20px;

    color: #45f3a2;

    background:
        rgba(0,220,120,.13);

    border:
        1px solid rgba(0,240,140,.40);

    font-weight: 700;
}

.no {
    display: inline-block;

    padding: 5px 11px;

    border-radius: 20px;

    color: #ff7185;

    background:
        rgba(255,30,60,.12);

    border:
        1px solid rgba(255,50,80,.35);

    font-weight: 700;
}

/* ============================================================
   DETAIL TABLE
============================================================ */

.detail-table {
    width: 100%;

    min-width: 700px;

    border-collapse: collapse;
}

.detail-table th {
    padding: 13px;

    color: #ff7ca7;

    text-align: left;

    background:
        rgba(255,0,80,.10);
}

.detail-table td {
    padding: 12px;

    color: #d5dbea;

    font-size: 12px;

    border-bottom:
        1px solid rgba(255,255,255,.07);
}

.detail-table tr:hover td {
    background:
        rgba(255,255,255,.03);
}

/* ============================================================
   OUTCOME
============================================================ */

.outcome {
    padding: 22px;

    border:
        1px solid rgba(255,40,110,.45);

    border-radius: 17px;

    background:
        linear-gradient(
            90deg,
            rgba(255,0,70,.10),
            rgba(100,30,255,.10)
        );
}

.outcome h3 {
    margin-top: 0;
}

.outcome p {
    color: #cbd2e3;

    font-size: 13px;

    line-height: 1.7;
}

/* ============================================================
   FOOTER
============================================================ */

.footer {
    margin-top: 30px;

    padding: 25px;

    text-align: center;

    color: #9fa8bd;

    font-size: 12px;

    border-top:
        1px solid rgba(255,255,255,.08);
}

.footer strong {
    color: #ff719e;
}

/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 1100px) {

    .workflow {
        grid-template-columns:
            repeat(4, 1fr);
    }
}

@media (max-width: 700px) {

    .block-container {
        padding: 15px 10px 30px;
    }

    .hero {
        padding: 30px 15px;
    }

    .hero h1 {
        font-size: 34px;
    }

    .workflow {
        grid-template-columns:
            repeat(2, 1fr);
    }
}

@media (max-width: 450px) {

    .workflow {
        grid-template-columns: 1fr;
    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="badge">
        🎬 MACHINE LEARNING PROJECT
    </div>

    <h1>
        Movie Recommendation System
    </h1>

    <p>
        A Content-Based Movie Recommendation System that recommends
        movies according to the similarity between their features,
        genres, keywords, cast, crew and other important information.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">🎬</div>
    <h2>Project Introduction</h2>
</div>
""", unsafe_allow_html=True)

intro_col, objective_col = st.columns([1.4, 1])


with intro_col:

    st.markdown("""
    <div class="card">

        <div class="card-icon">
            🎞️
        </div>

        <h3>
            What is a Movie Recommendation System?
        </h3>

        <p>
            A Movie Recommendation System is a Machine Learning based
            system that helps users discover movies according to their
            interests.

            <br><br>

            Instead of manually searching through thousands of movies,
            the system analyzes movie information and recommends movies
            that are similar to the movie selected by the user.

            <br><br>

            Our project uses a
            <b>Content-Based Filtering</b>
            approach.

            The system analyzes different features of movies such as
            genres, keywords, cast, crew and other textual information.

            <br><br>

            These features are converted into numerical vectors and
            their similarity is calculated using mathematical techniques.

            <br><br>

            When a user selects a movie, the system compares that movie
            with other movies and displays the most similar movies.
        </p>

    </div>
    """, unsafe_allow_html=True)


with objective_col:

    st.markdown("""
    <div class="card">

        <div class="card-icon">
            🎯
        </div>

        <h3>
            Project Objectives
        </h3>

        <p>

            <b>🔎 Easy Discovery</b>

            <br>

            Help users discover movies without manually searching through
            a huge movie collection.

            <br><br>

            <b>🤖 Machine Learning</b>

            <br>

            Use Machine Learning and Natural Language Processing techniques
            to generate movie recommendations.

            <br><br>

            <b>⚡ Fast Recommendation</b>

            <br>

            Provide relevant movie recommendations quickly after the user
            selects a movie.

        </p>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# WORKFLOW
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">⚙️</div>
    <h2>How Our System Works</h2>
</div>
""", unsafe_allow_html=True)


workflow_data = [

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


workflow_html = """
<div class="workflow">
"""


for number, title, description in workflow_data:

    workflow_html += f"""
    <div class="workflow-card">

        <div class="number">
            {number}
        </div>

        <h4>
            {title}
        </h4>

        <p>
            {description}
        </p>

    </div>
    """


workflow_html += """
</div>
"""


st.markdown(
    workflow_html,
    unsafe_allow_html=True
)


# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">🌐</div>
    <h2>Real-Life Applications</h2>
</div>
""", unsafe_allow_html=True)


applications = [

    (
        "🎥",
        "OTT Platforms",
        "Recommendation systems can help OTT platforms suggest movies and shows based on the content users are interested in."
    ),

    (
        "🎬",
        "Movie Websites",
        "Movie websites can recommend similar movies when a user opens the details of a particular movie."
    ),

    (
        "🛒",
        "E-Commerce",
        "The same recommendation concept can be applied to recommend products similar to a product selected by a customer."
    ),

    (
        "🍿",
        "Streaming Services",
        "Streaming platforms can help users discover relevant movies without searching through a large catalogue."
    ),

    (
        "📱",
        "Entertainment Apps",
        "Entertainment applications can personalize content discovery using recommendation algorithms."
    ),

    (
        "🎵",
        "Music Recommendation",
        "A similar content-based approach can recommend songs or artists based on their features."
    )

]


application_columns = st.columns(3)


for index, (icon, title, description) in enumerate(applications):

    with application_columns[index % 3]:

        st.markdown(f"""
        <div class="card">

            <div class="card-icon">
                {icon}
            </div>

            <h3>
                {title}
            </h3>

            <p>
                {description}
            </p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# TECHNOLOGIES
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">💻</div>
    <h2>Technologies Used</h2>
</div>
""", unsafe_allow_html=True)


technologies = [

    ("🐍", "Python"),
    ("🤖", "Machine Learning"),
    ("📊", "Pandas"),
    ("🔢", "NumPy"),
    ("🌐", "Streamlit")

]


technology_columns = st.columns(5)


for column, (icon, name) in zip(
    technology_columns,
    technologies
):

    with column:

        st.markdown(f"""
        <div
            class="card"
            style="text-align:center; min-height:110px;"
        >

            <div class="card-icon">
                {icon}
            </div>

            <h3>
                {name}
            </h3>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# PROJECT TEAM
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">👥</div>
    <h2>Project Team</h2>
</div>
""", unsafe_allow_html=True)


team_members = [

    (
        "Anish (Abrar) Ahmad",
        "Mathematics / ML Logic"
    ),

    (
        "Abhishek Anish",
        "Coding / ML Implementation"
    ),

    (
        "Vishal",
        "Frontend / UI Development"
    )

]


team_columns = st.columns(3)


for column, (name, role) in zip(
    team_columns,
    team_members
):

    with column:

        st.markdown(f"""
        <div
            class="card"
            style="text-align:center;"
        >

            <div class="card-icon">
                👤
            </div>

            <h3>
                {name}
            </h3>

            <p>
                {role}
            </p>

        </div>
        """, unsafe_allow_html=True)


# ============================================================
# TEAM CONTRIBUTION
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">📊</div>
    <h2>Team Contribution</h2>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="card">

    <b>Note:</b>

    <span style="color:#48f2a5;">
        YES
    </span>
    = Member is involved in that particular part.

    &nbsp;&nbsp;&nbsp;&nbsp;

    <span style="color:#ff7185;">
        NO
    </span>
    = Member is not involved in that particular part.

</div>
""", unsafe_allow_html=True)


# ============================================================
# CONTRIBUTION DATA
# ============================================================

contributions = [

    ("To Make Recommendation System", "No", "No", "No"),

    ("Data Collection", "No", "No", "No"),

    ("Data Cleaning", "No", "Yes", "No"),

    ("Bag of Words", "Yes", "Yes", "No"),

    ("Similarity Matrix", "Yes", "Yes", "No"),

    ("Vectorization", "Yes", "Yes", "No"),

    ("Cosine Matrix", "Yes", "Yes", "No"),

    ("Result", "No", "Yes", "Yes"),

    ("Deployment", "No", "Yes", "No"),

    ("UI / Web Development", "No", "No", "Yes")

]


def make_status(value):

    if value.lower() == "yes":

        return """
        <span class="yes">
            ✓ YES
        </span>
        """

    return """
    <span class="no">
        ✕ NO
    </span>
    """


table_rows = ""


for work, anish, abhishek, vishal in contributions:

    table_rows += f"""
    <tr>

        <td>
            <b>
                {work}
            </b>
        </td>

        <td>
            {make_status(anish)}
        </td>

        <td>
            {make_status(abhishek)}
        </td>

        <td>
            {make_status(vishal)}
        </td>

    </tr>
    """


# ============================================================
# ACTUAL TABLE
# ============================================================

st.markdown(f"""
<div class="table-box">

<table class="contribution-table">

    <thead>

        <tr>

            <th>
                Project Work
            </th>

            <th>
                Anish
            </th>

            <th>
                Abhishek
            </th>

            <th>
                Vishal
            </th>

        </tr>

    </thead>

    <tbody>

        {table_rows}

    </tbody>

</table>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">📝</div>
    <h2>Detailed Contribution</h2>
</div>
""", unsafe_allow_html=True)


details = [

    (
        "Data Cleaning",
        "Abhishek",
        "Data cleaning and preparation of useful movie information."
    ),

    (
        "Bag of Words",
        "Anish & Abhishek",
        "Creation of the textual feature representation used by the recommendation model."
    ),

    (
        "Similarity Matrix",
        "Anish & Abhishek",
        "Calculation and preparation of movie similarity information."
    ),

    (
        "Vectorization",
        "Anish & Abhishek",
        "Conversion of selected textual features into numerical vectors."
    ),

    (
        "Cosine Matrix",
        "Anish & Abhishek",
        "Calculation of cosine similarity between movie vectors."
    ),

    (
        "Result",
        "Abhishek & Vishal",
        "Displaying recommendation results through the application interface."
    ),

    (
        "Deployment",
        "Abhishek",
        "Deployment and configuration of the Streamlit web application."
    ),

    (
        "UI / Web Development",
        "Vishal",
        "Frontend design and user-interface development."
    )

]


detail_rows = ""


for work, member, contribution in details:

    detail_rows += f"""
    <tr>

        <td>
            <b>
                {work}
            </b>
        </td>

        <td>
            {member}
        </td>

        <td>
            {contribution}
        </td>

    </tr>
    """


st.markdown(f"""
<div class="table-box">

<table class="detail-table">

    <thead>

        <tr>

            <th>
                Project Work
            </th>

            <th>
                Member
            </th>

            <th>
                Contribution
            </th>

        </tr>

    </thead>

    <tbody>

        {detail_rows}

    </tbody>

</table>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT OUTCOME
# ============================================================

st.markdown("""
<div class="section-title">
    <div class="emoji">🏆</div>
    <h2>Project Outcome</h2>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="outcome">

    <h3>
        🎬 Final Result
    </h3>

    <p>

        The final result is an interactive web-based
        <b>Movie Recommendation System</b>
        where users can select a movie and receive recommendations
        for similar movies.

        <br><br>

        The project combines
        <b>
            Machine Learning,
            Natural Language Processing,
            Mathematics,
            Python Programming
        </b>
        and
        <b>
            Web Development
        </b>
        into a single practical application.

        <br><br>

        The system demonstrates how Machine Learning techniques can
        be used to solve a real-world content recommendation problem.

    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    🎬
    <strong>
        Movie Recommendation System
    </strong>

    <br>

    Machine Learning Project

    <br><br>

    Developed by

    <strong>Anish</strong>
    •
    <strong>Abhishek</strong>
    •
    <strong>Vishal</strong>

</div>
""", unsafe_allow_html=True)