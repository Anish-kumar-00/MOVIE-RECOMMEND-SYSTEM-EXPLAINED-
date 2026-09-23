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
# HTML RENDER FUNCTION
# ============================================================

def html(content):
    st.html(content)


# ============================================================
# GLOBAL CSS
# ============================================================

html("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');

* {
    box-sizing: border-box;
}

html, body {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(
            circle at 5% 5%,
            rgba(229, 9, 20, 0.13),
            transparent 28%
        ),
        radial-gradient(
            circle at 95% 30%,
            rgba(100, 50, 180, 0.10),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #05060b 0%,
            #080a12 50%,
            #05060b 100%
        );

    color: white;
}

header {
    visibility: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

.block-container {
    max-width: 1250px;
    padding-top: 25px;
    padding-bottom: 60px;
}


/* ============================================================
   HERO
   ============================================================ */

.hero {
    width: 100%;

    padding: 65px 35px;

    margin-bottom: 55px;

    text-align: center;

    border-radius: 28px;

    background:
        linear-gradient(
            135deg,
            rgba(229, 9, 20, 0.20),
            rgba(15, 18, 30, 0.97)
        );

    border: 1px solid rgba(229, 9, 20, 0.40);

    box-shadow:
        0 0 45px rgba(229, 9, 20, 0.12),
        inset 0 0 35px rgba(255,255,255,0.015);
}

.badge {
    display: inline-block;

    padding: 9px 18px;

    margin-bottom: 20px;

    border-radius: 50px;

    background: rgba(229, 9, 20, 0.14);

    border: 1px solid rgba(229, 9, 20, 0.45);

    color: #ff6872;

    font-size: 13px;

    font-weight: 700;

    letter-spacing: 1px;
}

.hero h1 {
    margin: 0;

    color: #ffffff;

    font-size: clamp(34px, 5vw, 62px);

    font-weight: 800;

    line-height: 1.15;
}

.hero p {
    max-width: 850px;

    margin: 22px auto 0;

    color: #b9becb;

    font-size: 16px;

    line-height: 1.8;
}


/* ============================================================
   SECTION
   ============================================================ */

.section {
    margin-top: 55px;

    margin-bottom: 30px;
}

.section-title {
    margin: 0;

    color: #ffffff;

    font-size: 28px;

    font-weight: 800;
}

.section-line {
    width: 72px;

    height: 4px;

    margin-top: 13px;

    border-radius: 10px;

    background: #e50914;
}


/* ============================================================
   GENERAL CARD
   ============================================================ */

.card {
    width: 100%;

    min-height: 100%;

    padding: 28px;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(23, 26, 37, 0.98),
            rgba(11, 13, 21, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.20);

    box-shadow:
        0 12px 35px rgba(0,0,0,0.25),
        inset 0 0 20px rgba(255,255,255,0.012);
}

.card-icon {
    width: 56px;

    height: 56px;

    display: flex;

    align-items: center;

    justify-content: center;

    margin-bottom: 18px;

    border-radius: 16px;

    background: rgba(229, 9, 20, 0.12);

    border: 1px solid rgba(229, 9, 20, 0.28);

    font-size: 28px;
}

.card h3 {
    margin: 0 0 16px;

    color: #ffffff;

    font-size: 21px;

    font-weight: 700;
}

.card p {
    margin: 0;

    color: #aeb5c3;

    font-size: 14px;

    line-height: 1.85;
}


/* ============================================================
   WORKFLOW
   ============================================================ */

.workflow {
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

    transition: transform 0.25s ease;
}

.workflow:hover {
    transform: translateY(-4px);

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

    border: 1px solid rgba(229, 9, 20, 0.30);

    color: #ff5963;

    font-size: 15px;

    font-weight: 800;
}

.workflow h4 {
    margin: 0 0 12px;

    color: #ffffff;

    font-size: 18px;

    font-weight: 700;
}

.workflow p {
    margin: 0;

    color: #9fa6b5;

    font-size: 13px;

    line-height: 1.7;
}


/* ============================================================
   APPLICATION
   ============================================================ */

.application {
    min-height: 255px;

    padding: 27px;

    border-radius: 21px;

    background:
        linear-gradient(
            145deg,
            rgba(22, 25, 36, 0.98),
            rgba(11, 13, 21, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.18);
}

.application-icon {
    width: 55px;

    height: 55px;

    display: flex;

    align-items: center;

    justify-content: center;

    margin-bottom: 18px;

    border-radius: 16px;

    background: rgba(229, 9, 20, 0.12);

    font-size: 27px;
}

.application h3 {
    margin: 0 0 12px;

    color: white;

    font-size: 19px;
}

.application p {
    margin: 0;

    color: #aeb4c2;

    font-size: 13px;

    line-height: 1.75;
}


/* ============================================================
   TECHNOLOGIES
   ============================================================ */

.tech {
    padding: 25px;

    margin-bottom: 20px;

    text-align: center;

    border-radius: 20px;

    background: rgba(18, 21, 31, 0.96);

    border: 1px solid rgba(100, 120, 180, 0.18);
}

.tech-icon {
    font-size: 36px;

    margin-bottom: 12px;
}

.tech h3 {
    margin: 0;

    color: #ffffff;

    font-size: 17px;
}


/* ============================================================
   TEAM
   ============================================================ */

.team {
    padding: 28px 20px;

    margin-bottom: 20px;

    text-align: center;

    border-radius: 22px;

    background:
        linear-gradient(
            145deg,
            rgba(22, 25, 36, 0.98),
            rgba(11, 13, 21, 0.98)
        );

    border: 1px solid rgba(100, 120, 180, 0.18);

    min-height: 190px;
}

.team-icon {
    width: 68px;

    height: 68px;

    display: flex;

    align-items: center;

    justify-content: center;

    margin: 0 auto 17px;

    border-radius: 50%;

    background: rgba(229, 9, 20, 0.12);

    border: 1px solid rgba(229, 9, 20, 0.30);

    font-size: 29px;
}

.team h3 {
    margin: 0 0 8px;

    color: white;

    font-size: 17px;
}

.team p {
    margin: 0;

    color: #a7adba;

    font-size: 12px;

    line-height: 1.6;
}


/* ============================================================
   NOTE
   ============================================================ */

.note {
    padding: 16px 18px;

    margin-bottom: 20px;

    border-radius: 14px;

    background: rgba(255,255,255,0.035);

    border: 1px solid rgba(255,255,255,0.08);

    color: #aeb4c2;

    font-size: 13px;
}

.yes-text {
    color: #48f2a5;

    font-weight: 700;
}

.no-text {
    color: #ff7185;

    font-weight: 700;
}


/* ============================================================
   TABLE
   ============================================================ */

.table-box {
    width: 100%;

    overflow-x: auto;

    border-radius: 18px;

    background: #0c0f17;

    border: 1px solid rgba(100,120,180,0.18);
}

table {
    width: 100%;

    min-width: 900px;

    border-collapse: collapse;
}

th {
    padding: 17px 15px;

    background: rgba(229,9,20,0.12);

    color: #ffffff;

    font-size: 13px;

    font-weight: 700;

    text-align: left;

    border-bottom: 1px solid rgba(229,9,20,0.25);
}

td {
    padding: 16px 15px;

    color: #c3c8d2;

    font-size: 13px;

    border-bottom: 1px solid rgba(255,255,255,0.06);
}

tr:hover td {
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
   OUTCOME
   ============================================================ */

.outcome {
    padding: 32px;

    border-radius: 23px;

    background:
        linear-gradient(
            135deg,
            rgba(229,9,20,0.13),
            rgba(20,23,34,0.98)
        );

    border: 1px solid rgba(229,9,20,0.25);
}

.outcome h3 {
    margin: 0 0 16px;

    color: #ffffff;

    font-size: 23px;
}

.outcome p {
    margin: 0;

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

        padding-top: 15px;
    }

    .hero {
        padding: 42px 20px;

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
        padding: 23px;
    }

    .workflow {
        min-height: auto;
    }

}

</style>
""")


# ============================================================
# HERO
# ============================================================

html("""
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
""")


# ============================================================
# PROJECT INTRODUCTION
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        🎬 Project Introduction
    </div>

    <div class="section-line"></div>

</div>
""")


col1, col2 = st.columns(2)


with col1:

    html("""
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
    """)


with col2:

    html("""
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
    """)


# ============================================================
# WORKFLOW
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        ⚙️ How Our System Works
    </div>

    <div class="section-line"></div>

</div>
""")


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


for start in range(0, 8, 4):

    cols = st.columns(4)

    for col, item in zip(cols, workflow[start:start + 4]):

        number, title, description = item

        with col:

            html(f"""
            <div class="workflow">

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
            """)


# ============================================================
# REAL-LIFE APPLICATIONS
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        🌐 Real-Life Applications
    </div>

    <div class="section-line"></div>

</div>
""")


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


for start in range(0, 6, 3):

    cols = st.columns(3)

    for col, item in zip(cols, applications[start:start + 3]):

        icon, title, description = item

        with col:

            html(f"""
            <div class="application">

                <div class="application-icon">
                    {icon}
                </div>

                <h3>
                    {title}
                </h3>

                <p>
                    {description}
                </p>

            </div>
            """)


# ============================================================
# TECHNOLOGIES
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        💻 Technologies Used
    </div>

    <div class="section-line"></div>

</div>
""")


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

        html(f"""
        <div class="tech">

            <div class="tech-icon">
                {icon}
            </div>

            <h3>
                {name}
            </h3>

        </div>
        """)


# ============================================================
# PROJECT TEAM
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        👥 Project Team
    </div>

    <div class="section-line"></div>

</div>
""")


# CORRECT 4 MEMBERS

team = [

    (
        "👔",
        "Abar Ahmad",
        "Special Project Manager"
    ),

    (
        "👨‍💻",
        "Anish",
        "Team Leader & Coder"
    ),

    (
        "🧮",
        "Abhishek",
        "Mathematical Logic"
    ),

    (
        "🎨",
        "Vishal",
        "Frontend"
    )

]


cols = st.columns(4)


for col, member in zip(cols, team):

    icon, name, role = member

    with col:

        html(f"""
        <div class="team">

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
        """)


# ============================================================
# TEAM CONTRIBUTION
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        📊 Team Contribution
    </div>

    <div class="section-line"></div>

</div>
""")


html("""
<div class="note">

    <b>Note:</b>

    <span class="yes-text">YES</span>
    = Member is involved in that particular part.

    &nbsp;&nbsp;&nbsp;&nbsp;

    <span class="no-text">NO</span>
    = Member is not involved in that particular part.

</div>
""")


# ============================================================
# CONTRIBUTION TABLE
# ============================================================

html("""
<div class="table-box">

<table>

<thead>

<tr>
    <th>Project Work</th>
    <th>Abar Ahmad</th>
    <th>Anish</th>
    <th>Abhishek</th>
    <th>Vishal</th>
</tr>

</thead>

<tbody>

<tr>

    <td>
        <b>To Make Recommendation System</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Data Collection</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Data Cleaning</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Bag of Words</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Similarity Matrix</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Vectorization</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Cosine Matrix</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>Result</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

</tr>


<tr>

    <td>
        <b>Deployment</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

</tr>


<tr>

    <td>
        <b>UI / Web Development</b>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="no">✕ NO</span>
    </td>

    <td>
        <span class="yes">✓ YES</span>
    </td>

</tr>

</tbody>

</table>

</div>
""")


# ============================================================
# DETAILED CONTRIBUTION
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        📝 Detailed Contribution
    </div>

    <div class="section-line"></div>

</div>
""")


html("""
<div class="table-box">

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

    <td>
        <b>Data Cleaning</b>
    </td>

    <td>
        Abhishek
    </td>

    <td>
        Data cleaning and preparation of useful movie information.
    </td>

</tr>


<tr>

    <td>
        <b>Bag of Words</b>
    </td>

    <td>
        Anish &amp; Abhishek
    </td>

    <td>
        Creation of the textual feature representation used by
        the recommendation model.
    </td>

</tr>


<tr>

    <td>
        <b>Similarity Matrix</b>
    </td>

    <td>
        Anish &amp; Abhishek
    </td>

    <td>
        Calculation and preparation of movie similarity information.
    </td>

</tr>


<tr>

    <td>
        <b>Vectorization</b>
    </td>

    <td>
        Anish &amp; Abhishek
    </td>

    <td>
        Conversion of selected textual features into numerical vectors.
    </td>

</tr>


<tr>

    <td>
        <b>Cosine Matrix</b>
    </td>

    <td>
        Anish &amp; Abhishek
    </td>

    <td>
        Calculation of cosine similarity between movie vectors.
    </td>

</tr>


<tr>

    <td>
        <b>Result</b>
    </td>

    <td>
        Abhishek &amp; Vishal
    </td>

    <td>
        Displaying recommendation results through the application interface.
    </td>

</tr>


<tr>

    <td>
        <b>Deployment</b>
    </td>

    <td>
        Abhishek
    </td>

    <td>
        Deployment and configuration of the Streamlit web application.
    </td>

</tr>


<tr>

    <td>
        <b>UI / Web Development</b>
    </td>

    <td>
        Vishal
    </td>

    <td>
        Frontend design and user-interface development.
    </td>

</tr>


<tr>

    <td>
        <b>Project Management</b>
    </td>

    <td>
        Abar Ahmad
    </td>

    <td>
        Special project management and overall project coordination.
    </td>

</tr>


</tbody>

</table>

</div>
""")


# ============================================================
# PROJECT OUTCOME
# ============================================================

html("""
<div class="section">

    <div class="section-title">
        🏆 Project Outcome
    </div>

    <div class="section-line"></div>

</div>
""")


html("""
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
""")


# ============================================================
# FOOTER
# ============================================================

html("""
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

    <strong>Abar Ahmad</strong>
    •
    <strong>Anish</strong>
    •
    <strong>Abhishek</strong>
    •
    <strong>Vishal</strong>

</div>
""")