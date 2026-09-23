import streamlit as st

# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 5%, rgba(255, 0, 80, .12), transparent 25%),
        radial-gradient(circle at 90% 10%, rgba(110, 0, 255, .12), transparent 25%),
        linear-gradient(135deg, #03050c 0%, #070b16 50%, #03050c 100%);
    color: #f5f7ff;
}

.block-container {
    max-width: 1450px;
    padding: 1.2rem 1.5rem 2rem;
}

/* ============================================================
   HERO
============================================================ */

.hero {
    position: relative;
    overflow: hidden;
    padding: 34px 25px 30px;
    margin-bottom: 22px;
    border: 1px solid rgba(255, 50, 120, .45);
    border-radius: 22px;
    text-align: center;

    background:
        radial-gradient(circle at 12% 50%, rgba(255, 0, 75, .20), transparent 28%),
        radial-gradient(circle at 88% 45%, rgba(100, 30, 255, .20), transparent 30%),
        rgba(5, 8, 20, .92);

    box-shadow: 0 0 45px rgba(255, 0, 80, .12);
}

.hero-badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;

    background: linear-gradient(90deg, #ff1744, #d500f9);

    color: white;
    font-size: 13px;
    font-weight: 800;
    letter-spacing: .5px;
}

.hero h1 {
    margin: 15px 0 8px;

    font-size: clamp(34px, 5vw, 58px);
    font-weight: 800;

    background: linear-gradient(
        90deg,
        #ffffff,
        #ff72a0,
        #c879ff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    max-width: 850px;
    margin: auto;

    color: #d8dced;
    font-size: 15px;
    line-height: 1.65;
}

/* ============================================================
   SECTION TITLE
============================================================ */

.section-title {
    display: flex;
    align-items: center;
    gap: 10px;

    margin: 22px 0 12px;
    padding-bottom: 7px;

    border-bottom: 1px solid rgba(255,255,255,.09);
}

.section-title span {
    font-size: 23px;
}

.section-title h2 {
    margin: 0;

    font-size: 23px;
    font-weight: 800;
}

/* ============================================================
   CARDS
============================================================ */

.card {
    min-height: 155px;

    padding: 18px;

    border: 1px solid rgba(115, 140, 255, .35);
    border-radius: 15px;

    background:
        linear-gradient(
            145deg,
            rgba(14, 21, 42, .95),
            rgba(5, 10, 23, .95)
        );

    box-shadow: 0 8px 28px rgba(0,0,0,.25);
}

.card:hover {
    border-color: rgba(255, 80, 160, .65);
    transform: translateY(-2px);
    transition: .2s ease;
}

.card h3 {
    margin: 0 0 8px;
    font-size: 17px;
}

.card p {
    margin: 0;

    color: #cbd1e4;
    line-height: 1.55;
    font-size: 13px;
}

.icon {
    font-size: 30px;
    margin-bottom: 8px;
}

/* ============================================================
   WORKFLOW
============================================================ */

.workflow {
    display: grid;

    grid-template-columns:
        repeat(8, minmax(130px, 1fr));

    gap: 10px;
}

.step {
    min-height: 155px;

    padding: 14px;

    border: 1px solid rgba(75, 150, 255, .35);
    border-radius: 13px;

    background: rgba(8, 16, 32, .9);
}

.step-number {
    display: inline-flex;

    width: 32px;
    height: 32px;

    align-items: center;
    justify-content: center;

    border-radius: 50%;

    background:
        linear-gradient(
            135deg,
            #ff1744,
            #7c4dff
        );

    font-weight: 800;
    font-size: 12px;

    margin-bottom: 10px;
}

.step h4 {
    margin: 0 0 7px;
    font-size: 14px;
}

.step p {
    margin: 0;

    color: #bfc7db;
    font-size: 11px;
    line-height: 1.5;
}

/* ============================================================
   TABLE
============================================================ */

.table-wrap {
    overflow-x: auto;

    border: 1px solid rgba(255, 50, 110, .35);
    border-radius: 14px;

    background: rgba(5, 10, 22, .9);
}

.project-table {
    width: 100%;
    min-width: 700px;

    border-collapse: collapse;
}

.project-table th {
    padding: 13px 12px;

    background:
        linear-gradient(
            90deg,
            rgba(255,0,70,.16),
            rgba(100,40,255,.15)
        );

    color: #fff;

    font-size: 13px;
    text-align: center;

    border-bottom:
        1px solid rgba(255,255,255,.12);
}

.project-table th:first-child,
.project-table td:first-child {
    text-align: left;
}

.project-table td {
    padding: 10px 12px;

    border-bottom:
        1px solid rgba(255,255,255,.07);

    color: #dce1ef;

    font-size: 12px;
    text-align: center;
}

.project-table tr:last-child td {
    border-bottom: none;
}

.project-table tr:hover td {
    background: rgba(255,255,255,.025);
}

/* ============================================================
   YES / NO
============================================================ */

.yes {
    display: inline-block;

    min-width: 58px;
    padding: 5px 9px;

    border-radius: 15px;

    background: rgba(0, 210, 120, .16);

    border:
        1px solid rgba(0, 240, 140, .4);

    color: #48f2a5;

    font-weight: 700;
}

.no {
    display: inline-block;

    min-width: 58px;
    padding: 5px 9px;

    border-radius: 15px;

    background: rgba(255, 30, 65, .14);

    border:
        1px solid rgba(255, 50, 80, .35);

    color: #ff7185;

    font-weight: 700;
}

/* ============================================================
   DETAIL TABLE
============================================================ */

.detail-table {
    width: 100%;
    border-collapse: collapse;
}

.detail-table th,
.detail-table td {
    padding: 11px 12px;

    border-bottom:
        1px solid rgba(255,255,255,.08);

    text-align: left;
}

.detail-table th {
    color: #ff78a2;
    font-size: 12px;
}

.detail-table td {
    color: #d7dced;
    font-size: 12px;
}

.detail-table tr:last-child td {
    border-bottom: none;
}

/* ============================================================
   OUTCOME
============================================================ */

.outcome {
    padding: 18px;

    border-radius: 15px;

    border:
        1px solid rgba(255, 30, 100, .45);

    background:
        linear-gradient(
            90deg,
            rgba(255,0,75,.10),
            rgba(110,30,255,.10)
        );
}

.outcome h3 {
    margin: 0 0 8px;
}

.outcome p {
    color: #cbd1e4;
    line-height: 1.6;
    font-size: 13px;
}

/* ============================================================
   FOOTER
============================================================ */

.footer {
    margin-top: 28px;

    padding: 22px;

    text-align: center;

    border-top:
        1px solid rgba(255,255,255,.08);

    color: #aeb5c9;

    font-size: 12px;
}

.footer strong {
    color: #ff6d9d;
}

/* ============================================================
   MOBILE
============================================================ */

@media (max-width: 1000px) {

    .workflow {
        grid-template-columns:
            repeat(2, 1fr);
    }
}

@media (max-width: 650px) {

    .block-container {
        padding: .8rem .7rem 1.5rem;
    }

    .hero {
        padding: 25px 15px;
    }

    .hero h1 {
        font-size: 32px;
    }

    .workflow {
        grid-template-columns: 1fr;
    }

    .card {
        min-height: auto;
    }
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">

    <div class="hero-badge">
        🎬 MACHINE LEARNING PROJECT
    </div>

    <h1>
        Movie Recommendation System
    </h1>

    <p>
        A Content-Based Movie Recommendation System that recommends movies
        according to the similarity between their features, genres,
        keywords, cast, crew and other important information.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

st.markdown("""
<div class="section-title">
    <span>🎬</span>
    <h2>Project Introduction</h2>
</div>
""", unsafe_allow_html=True)


col1, col2 = st.columns([1.35, 1])


with col1:

    st.markdown("""
    <div class="card">

        <div class="icon">
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


with col2:

    st.markdown("""
    <div class="card">

        <div class="icon">
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
    <span>⚙️</span>
    <h2>How Our System Works</h2>
</div>
""", unsafe_allow_html=True)


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


workflow_html = '<div class="workflow">'


for number, title, description in workflow:

    workflow_html += f"""

    <div class="step">

        <div class="step-number">
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


workflow_html += "</div>"


st.markdown(
    workflow_html,
    unsafe_allow_html=True
)


# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.markdown("""
<div class="section-title">
    <span>🌐</span>
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
        "🛒",
        "E-Commerce",
        "The same recommendation concept can be applied to recommend products similar to a product selected by a customer."
    ),

    (
        "📱",
        "Entertainment Apps",
        "Entertainment applications can personalize content discovery using recommendation algorithms."
    ),

    (
        "🎬",
        "Movie Websites",
        "Movie websites can recommend similar movies when a user opens the details of a particular movie."
    ),

    (
        "🍿",
        "Streaming Services",
        "Streaming platforms can help users discover relevant movies without searching through a large catalogue."
    ),

    (
        "🎵",
        "Music Recommendation",
        "A similar content-based approach can recommend songs or artists based on their features."
    )

]


app_cols = st.columns(3)


for i, (icon, title, description) in enumerate(applications):

    with app_cols[i % 3]:

        st.markdown(f"""

        <div class="card">

            <div class="icon">
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
    <span>💻</span>
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


tech_cols = st.columns(5)


for col, (icon, name) in zip(
    tech_cols,
    technologies
):

    with col:

        st.markdown(f"""

        <div
            class="card"
            style="text-align:center; min-height:100px;"
        >

            <div class="icon">
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
    <span>👥</span>
    <h2>Project Team</h2>
</div>
""", unsafe_allow_html=True)


team = [

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


team_cols = st.columns(3)


for col, (name, role) in zip(
    team_cols,
    team
):

    with col:

        st.markdown(f"""

        <div
            class="card"
            style="text-align:center;"
        >

            <div class="icon">
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
    <span>📊</span>
    <h2>Team Contribution</h2>
</div>
""", unsafe_allow_html=True)


st.markdown("""
<div
    class="card"
    style="min-height:auto; margin-bottom:12px;"
>

    <b>Note:</b>

    <span style="color:#48f2a5;">
        YES
    </span>
    = Member is involved in that particular part.

    &nbsp;&nbsp;&nbsp;

    <span style="color:#ff7185;">
        NO
    </span>
    = Member is not involved in that particular part.

</div>
""", unsafe_allow_html=True)


# EXACT TABLE FROM YOUR PROVIDED PHOTO

contributions = [

    (
        "To Make Recommendation System",
        "No",
        "No",
        "No"
    ),

    (
        "Data Collection",
        "No",
        "No",
        "No"
    ),

    (
        "Data Cleaning",
        "No",
        "Yes",
        "No"
    ),

    (
        "Bag of Words",
        "Yes",
        "Yes",
        "No"
    ),

    (
        "Similarity Matrix",
        "Yes",
        "Yes",
        "No"
    ),

    (
        "Vectorization",
        "Yes",
        "Yes",
        "No"
    ),

    (
        "Cosine Matrix",
        "Yes",
        "Yes",
        "No"
    ),

    (
        "Result",
        "No",
        "Yes",
        "Yes"
    ),

    (
        "Deployment",
        "No",
        "Yes",
        "No"
    ),

    (
        "UI / Web Development",
        "No",
        "No",
        "Yes"
    )

]


def status(value):

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


rows = ""


for work, anish, abhishek, vishal in contributions:

    rows += f"""

    <tr>

        <td>
            <b>
                {work}
            </b>
        </td>

        <td>
            {status(anish)}
        </td>

        <td>
            {status(abhishek)}
        </td>

        <td>
            {status(vishal)}
        </td>

    </tr>

    """


st.markdown(f"""

<div class="table-wrap">

<table class="project-table">

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

        {rows}

    </tbody>

</table>

</div>

""", unsafe_allow_html=True)


# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

st.markdown("""
<div class="section-title">
    <span>📝</span>
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

<div class="table-wrap">

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
    <span>🏆</span>
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

    <strong>
        Anish
    </strong>
    •
    <strong>
        Abhishek
    </strong>
    •
    <strong>
        Vishal
    </strong>

</div>
""", unsafe_allow_html=True)