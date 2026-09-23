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
# GLOBAL CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(229, 9, 20, 0.12), transparent 25%),
        radial-gradient(circle at 90% 30%, rgba(90, 30, 180, 0.10), transparent 25%),
        linear-gradient(135deg, #05060b 0%, #080a12 50%, #05060b 100%);
    color: white;
}

/* Hide Streamlit default elements */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

/* Main container */
.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* ============================================================
   HERO
   ============================================================ */

.hero {
    padding: 65px 35px;
    margin-bottom: 45px;
    border-radius: 28px;
    text-align: center;

    background:
        linear-gradient(
            135deg,
            rgba(229, 9, 20, 0.18),
            rgba(15, 18, 30, 0.96)
        );

    border: 1px solid rgba(229, 9, 20, 0.35);

    box-shadow:
        0 0 40px rgba(229, 9, 20, 0.12),
        inset 0 0 40px rgba(255,255,255,0.015);
}

.badge {
    display: inline-block;
    padding: 9px 18px;
    margin-bottom: 20px;

    border-radius: 50px;

    background: rgba(229, 9, 20, 0.14);
    border: 1px solid rgba(229, 9, 20, 0.45);

    color: #ff6670;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
}

.hero h1 {
    margin: 0;
    color: #ffffff;
    font-size: clamp(32px, 5vw, 62px);
    font-weight: 800;
    line-height: 1.15;
}

.hero p {
    max-width: 850px;
    margin: 22px auto 0 auto;

    color: #b9becb;
    font-size: 16px;
    line-height: 1.8;
}


/* ============================================================
   SECTION TITLE
   ============================================================ */

.section-title {
    margin-top: 55px;
    margin-bottom: 25px;

    color: #ffffff;
    font-size: 28px;
    font-weight: 800;
}

.section-line {
    width: 70px;
    height: 4px;
    margin-top: -15px;
    margin-bottom: 30px;

    border-radius: 10px;
    background: #e50914;
}


/* ============================================================
   GENERAL CARD
   ============================================================ */

.card {
    height: 100%;
    padding: 28px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(22, 25, 36, 0.98),
            rgba(12, 14, 22, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.20);

    box-shadow:
        0 10px 35px rgba(0,0,0,0.25),
        inset 0 0 20px rgba(255,255,255,0.015);
}

.card:hover {
    border-color: rgba(229, 9, 20, 0.45);
    box-shadow:
        0 10px 40px rgba(229, 9, 20, 0.10),
        inset 0 0 20px rgba(255,255,255,0.02);
}

.card-icon {
    width: 55px;
    height: 55px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 18px;

    border-radius: 16px;

    background: rgba(229, 9, 20, 0.12);
    border: 1px solid rgba(229, 9, 20, 0.25);

    font-size: 27px;
}

.card h3 {
    margin: 0 0 15px 0;

    color: #ffffff;
    font-size: 21px;
    font-weight: 700;
}

.card p {
    margin: 0;

    color: #aeb4c2;
    font-size: 14px;
    line-height: 1.85;
}


/* ============================================================
   OBJECTIVE CARDS
   ============================================================ */

.objective {
    height: 100%;
    padding: 25px;

    border-radius: 20px;

    background: rgba(18, 21, 31, 0.96);

    border: 1px solid rgba(100, 120, 180, 0.18);
}

.objective h3 {
    color: white;
    font-size: 20px;
    margin: 0 0 10px 0;
}

.objective p {
    color: #aeb4c2;
    font-size: 14px;
    line-height: 1.75;
    margin: 0;
}


/* ============================================================
   WORKFLOW
   ============================================================ */

.workflow-card {
    min-height: 245px;
    padding: 25px;

    border-radius: 20px;

    background:
        linear-gradient(
            145deg,
            rgba(20, 23, 34, 0.98),
            rgba(10, 12, 20, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.18);

    transition: 0.25s ease;
}

.workflow-card:hover {
    transform: translateY(-3px);
    border-color: rgba(229, 9, 20, 0.45);
}

.number {
    width: 48px;
    height: 48px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin-bottom: 18px;

    border-radius: 14px;

    background: rgba(229, 9, 20, 0.13);
    border: 1px solid rgba(229, 9, 20, 0.3);

    color: #ff5963;
    font-size: 15px;
    font-weight: 800;
}

.workflow-card h4 {
    margin: 0 0 12px 0;

    color: #ffffff;
    font-size: 18px;
    font-weight: 700;
}

.workflow-card p {
    margin: 0;

    color: #9fa6b5;
    font-size: 13px;
    line-height: 1.7;
}


/* ============================================================
   TECHNOLOGY
   ============================================================ */

.tech-card {
    padding: 25px;
    text-align: center;

    border-radius: 20px;

    background: rgba(18, 21, 31, 0.96);

    border: 1px solid rgba(100, 120, 180, 0.18);
}

.tech-icon {
    font-size: 35px;
    margin-bottom: 12px;
}

.tech-card h3 {
    margin: 0;

    color: white;
    font-size: 17px;
}


/* ============================================================
   TEAM
   ============================================================ */

.team-card {
    padding: 28px;
    text-align: center;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(22, 25, 36, 0.98),
            rgba(11, 13, 21, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.18);
}

.team-icon {
    width: 70px;
    height: 70px;

    display: flex;
    align-items: center;
    justify-content: center;

    margin: 0 auto 18px auto;

    border-radius: 50%;

    background: rgba(229, 9, 20, 0.12);
    border: 1px solid rgba(229, 9, 20, 0.30);

    font-size: 30px;
}

.team-card h3 {
    color: white;
    font-size: 18px;
    margin: 0 0 8px 0;
}

.team-card p {
    color: #a7adba;
    font-size: 13px;
    margin: 0;
}


/* ============================================================
   TABLE
   ============================================================ */

.table-wrapper {
    width: 100%;
    overflow-x: auto;

    border-radius: 18px;
    border: 1px solid rgba(100, 120, 180, 0.18);

    background: rgba(12, 15, 23, 0.98);
}

table {
    width: 100%;
    min-width: 750px;

    border-collapse: collapse;
}

thead th {
    padding: 17px 15px;

    background: rgba(229, 9, 20, 0.12);

    color: #ffffff;

    font-size: 13px;
    font-weight: 700;

    border-bottom: 1px solid rgba(229, 9, 20, 0.25);
}

tbody td {
    padding: 16px 15px;

    color: #c2c7d2;

    font-size: 13px;

    border-bottom: 1px solid rgba(255,255,255,0.06);
}

tbody tr:hover {
    background: rgba(255,255,255,0.025);
}

.yes {
    color: #48f2a5;
    font-weight: 700;
    white-space: nowrap;
}

.no {
    color: #ff7185;
    font-weight: 700;
    white-space: nowrap;
}


/* ============================================================
   NOTE
   ============================================================ */

.note {
    margin-bottom: 20px;
    padding: 15px 18px;

    border-radius: 14px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.07);

    color: #aeb4c2;
    font-size: 13px;
}

.note .yes-text {
    color: #48f2a5;
    font-weight: 700;
}

.note .no-text {
    color: #ff7185;
    font-weight: 700;
}


/* ============================================================
   OUTCOME
   ============================================================ */

.outcome {
    padding: 32px;

    border-radius: 22px;

    background:
        linear-gradient(
            135deg,
            rgba(229, 9, 20, 0.12),
            rgba(20, 23, 34, 0.98)
        );

    border: 1px solid rgba(229, 9, 20, 0.25);
}

.outcome h3 {
    color: white;
    font-size: 22px;
    margin-top: 0;
}

.outcome p {
    color: #b3bac7;
    font-size: 14px;
    line-height: 1.9;
}


/* ============================================================
   FOOTER
   ============================================================ */

.custom-footer {
    margin-top: 65px;
    padding: 30px;

    text-align: center;

    border-top: 1px solid rgba(255,255,255,0.08);

    color: #8d94a3;

    font-size: 13px;
    line-height: 1.8;
}

.custom-footer strong {
    color: #ffffff;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 768px) {

    .block-container {
        padding-left: 12px;
        padding-right: 12px;
        padding-top: 1rem;
    }

    .hero {
        padding: 40px 20px;
        border-radius: 22px;
    }

    .hero h1 {
        font-size: 34px;
    }

    .hero p {
        font-size: 13px;
    }

    .section-title {
        font-size: 23px;
    }

    .card {
        padding: 22px;
    }

    .workflow-card {
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
    🎬 Project Introduction
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:

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


with col2:

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
    ⚙️ How Our System Works
</div>

<div class="section-line"></div>
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


for i in range(0, len(workflow), 4):

    cols = st.columns(4)

    for col, item in zip(cols, workflow[i:i+4]):

        number, title, description = item

        with col:

            st.markdown(f"""
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
            """, unsafe_allow_html=True)


# ============================================================
# REAL LIFE APPLICATIONS
# ============================================================

st.markdown("""
<div class="section-title">
    🌐 Real-Life Applications
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


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

    for col, item in zip(cols, applications[i:i+3]):

        icon, title, description = item

        with col:

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
    💻 Technologies Used
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


technologies = [

    ("🐍", "Python"),
    ("🤖", "Machine Learning"),
    ("📊", "Pandas"),
    ("🔢", "NumPy"),
    ("🌐", "Streamlit")

]


cols = st.columns(5)

for col, item in zip(cols, technologies):

    icon, name = item

    with col:

        st.markdown(f"""
        <div class="tech-card">

            <div class="tech-icon">
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
    👥 Project Team
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


team = [

    (
        "👤",
        "Anish (Abrar) Ahmad",
        "Mathematics / ML Logic"
    ),

    (
        "👤",
        "Abhishek Anish",
        "Coding / ML Implementation"
    ),

    (
        "👤",
        "Vishal",
        "Frontend / UI Development"
    )

]


cols = st.columns(3)

for col, member in zip(cols, team):

    icon, name, role = member

    with col:

        st.markdown(f"""
        <div class="team-card">

            <div class="team-icon">
                {icon}
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
    📊 Team Contribution
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="note">

    <b>Note:</b>

    <span class="yes-text">
        YES
    </span>
    = Member is involved in that particular part.

    &nbsp;&nbsp;&nbsp;&nbsp;

    <span class="no-text">
        NO
    </span>
    = Member is not involved in that particular part.

</div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="table-wrapper">

<table>

<thead>

<tr>

    <th>Project Work</th>
    <th>Anish</th>
    <th>Abhishek</th>
    <th>Vishal</th>

</tr>

</thead>

<tbody>


<tr>

    <td><b>To Make Recommendation System</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Data Collection</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Data Cleaning</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Bag of Words</b></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Similarity Matrix</b></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Vectorization</b></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Cosine Matrix</b></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>Result</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="yes">✓ YES</span></td>

</tr>


<tr>

    <td><b>Deployment</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="yes">✓ YES</span></td>

    <td><span class="no">✕ NO</span></td>

</tr>


<tr>

    <td><b>UI / Web Development</b></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="no">✕ NO</span></td>

    <td><span class="yes">✓ YES</span></td>

</tr>


</tbody>

</table>

</div>
""", unsafe_allow_html=True)


# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

st.markdown("""
<div class="section-title">
    📝 Detailed Contribution
</div>

<div class="section-line"></div>
""", unsafe_allow_html=True)


st.markdown("""
<div class="table-wrapper">

<table>

<thead>

<tr>

    <th>Project Work</th>
    <th>Member</th>
    <th>Contribution</th>

</tr>

</thead>

<tbody>


<tr>

    <td><b>Data Cleaning</b></td>

    <td>Abhishek</td>

    <td>
        Data cleaning and preparation of useful movie information.
    </td>

</tr>


<tr>

    <td><b>Bag of Words</b></td>

    <td>Anish &amp; Abhishek</td>

    <td>
        Creation of the textual feature representation used by the recommendation model.
    </td>

</tr>


<tr>

    <td><b>Similarity Matrix</b></td>

    <td>Anish &amp; Abhishek</td>

    <td>
        Calculation and preparation of movie similarity information.
    </td>

</tr>


<tr>

    <td><b>Vectorization</b></td>

    <td>Anish &amp; Abhishek</td>

    <td>
        Conversion of selected textual features into numerical vectors.
    </td>

</tr>


<tr>

    <td><b>Cosine Matrix</b></td>

    <td>Anish &amp; Abhishek</td>

    <td>
        Calculation of cosine similarity between movie vectors.
    </td>

</tr>


<tr>

    <td><b>Result</b></td>

    <td>Abhishek &amp; Vishal</td>

    <td>
        Displaying recommendation results through the application interface.
    </td>

</tr>


<tr>

    <td><b>Deployment</b></td>

    <td>Abhishek</td>

    <td>
        Deployment and configuration of the Streamlit web application.
    </td>

</tr>


<tr>

    <td><b>UI / Web Development</b></td>

    <td>Vishal</td>

    <td>
        Frontend design and user-interface development.
    </td>

</tr>


</tbody>

</table>

</div>
""", unsafe_allow_html=True)


# ============================================================
# PROJECT OUTCOME
# ============================================================

st.markdown("""
<div class="section-title">
    🏆 Project Outcome
</div>

<div class="section-line"></div>
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
<div class="custom-footer">

    🎬
    <br>

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