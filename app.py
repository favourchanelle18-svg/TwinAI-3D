import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Load CSS
with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# Page Config
st.set_page_config(
    page_title="TwinAI 3D",
    page_icon="🧠",
    layout="wide"
)

# Sidebar
st.sidebar.title("🧠 TwinAI")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "My Twin",
        "3D Twin",
        "Future Simulator",
        "Achievements"
    ]
)

# =========================
# HOME
# =========================

if page == "Home":

    hero = Image.open("assets/hero.jpg")

    st.image(
        hero,
        use_container_width=True
    )

    st.markdown(
        """
        <div class="hero-title">
        Meet Your Future Self
        </div>

        <div class="hero-subtitle">
        Build a realistic digital twin and explore how today's habits shape tomorrow's outcomes.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Active Twins", "12,548")

    with c2:
        st.metric("Predictions Generated", "84,291")

    with c3:
        st.metric("Average Growth", "+18%")

# =========================
# MY TWIN
# =========================

elif page == "My Twin":

    st.header("Create Your Twin")

    name = st.text_input("Name")

    age = st.slider("Age", 13, 30, 17)

    study = st.slider("Study Hours", 0, 12, 5)

    sleep = st.slider("Sleep Hours", 0, 12, 8)

    exercise = st.slider("Exercise Hours", 0, 5, 1)

    screen = st.slider("Screen Time", 0, 15, 5)

    # Save data for other pages
    st.session_state["study"] = study
    st.session_state["sleep"] = sleep
    st.session_state["exercise"] = exercise
    st.session_state["screen"] = screen
    st.session_state["name"] = name

    if st.button("Generate Twin"):

        score = (
            study * 5
            + sleep * 4
            + exercise * 8
            - screen
        )

        score = max(0, min(100, score))

        st.subheader(f"{name}'s Twin")

        st.progress(score / 100)

        st.metric(
            "Twin Score",
            f"{score}/100"
        )

        if score >= 80:
            st.success("Elite Potential 🚀")

        elif score >= 60:
            st.info("Strong Growth 📈")

        else:
            st.warning("Needs Improvement ⚠️")

# =========================
# 3D TWIN
# =========================

elif page == "3D Twin":

    study = st.session_state.get("study", 5)
    sleep = st.session_state.get("sleep", 8)
    exercise = st.session_state.get("exercise", 1)
    screen = st.session_state.get("screen", 5)
    name = st.session_state.get("name", "Your")

    focus = max(0, min(100, study * 10 - screen * 2))
    energy = max(0, min(100, sleep * 12))
    discipline = max(0, min(100, study * 6 + exercise * 12))

    overall = (focus + energy + discipline) / 300

    st.title(f"🧠 {name}'s Digital Twin")

    left, right = st.columns([2, 1])

    with left:

        components.html(
            """
            <iframe
            title="Angelica"
            frameborder="0"
            allowfullscreen
            mozallowfullscreen="true"
            webkitallowfullscreen="true"
            allow="autoplay; fullscreen; xr-spatial-tracking"
            width="100%"
            height="650"
            src="https://sketchfab.com/models/27f75fa94c384000bb6a79a3000f8e80/embed?autostart=1&ui_infos=0&ui_controls=1">
            </iframe>
            """,
            height=700
        )

    with right:

        st.metric("Level", "12")

        st.metric("XP", "845")

        st.metric(
            "Focus",
            f"{focus}%"
        )

        st.metric(
            "Energy",
            f"{energy}%"
        )

        st.metric(
            "Discipline",
            f"{discipline}%"
        )

        st.progress(overall)

        if overall >= 0.8:
            st.success("Twin Status: Elite Growth 🚀")

        elif overall >= 0.6:
            st.info("Twin Status: Strong Progress 📈")

        else:
            st.warning("Twin Status: Needs Improvement ⚠️")

# =========================
# FUTURE SIMULATOR
# =========================

elif page == "Future Simulator":

    st.header("Future Simulator")

    current = st.slider(
        "Current Performance",
        0,
        100,
        75
    )

    improvement = st.slider(
        "Future Improvement",
        0,
        50,
        15
    )

    future = min(
        100,
        current + improvement
    )

    st.metric(
        "Predicted Future Score",
        future
    )

    st.progress(
        future / 100
    )
study = st.session_state.get("study", 5)
sleep = st.session_state.get("sleep", 8)
exercise = st.session_state.get("exercise", 1)
screen = st.session_state.get("screen", 5)

focus = max(0, min(100, study * 10 - screen * 2))
energy = max(0, min(100, sleep * 12))
discipline = max(0, min(100, study * 6 + exercise * 12))

st.divider()

st.subheader("🔮 Career Prediction")

if focus > 80 and discipline > 70:
    career = "AI Researcher 🤖"

elif focus > 70:
    career = "Software Engineer 💻"

elif energy > 80 and discipline > 60:
    career = "Entrepreneur 🚀"

elif discipline > 60:
    career = "Project Leader 📈"

else:
    career = "Potential Untapped 🌱"

st.success(f"Predicted Future Career: {career}")
# =========================
# ACHIEVEMENTS
# =========================

elif page == "Achievements":

    st.header("Achievements")

    st.success("🏆 Focus Master")

    st.success("🔥 Study Beast")

    st.success("😴 Sleep Champion")

    st.success("🚀 Elite Twin")
