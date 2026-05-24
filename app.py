import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# -----------------------
# PAGE CONFIG
# -----------------------
st.set_page_config(
    page_title="TwinAI 3D",
    page_icon="🧠",
    layout="wide"
)

# -----------------------
# LOAD CSS (safe)
# -----------------------
try:
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except:
    pass

# -----------------------
# SIDEBAR NAV
# -----------------------
st.sidebar.title("🧠 TwinAI")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "My Twin", "3D Twin", "Future Simulator", "Achievements"]
)

# -----------------------
# SESSION DEFAULTS
# -----------------------
if "study" not in st.session_state:
    st.session_state.study = 5
if "sleep" not in st.session_state:
    st.session_state.sleep = 8
if "exercise" not in st.session_state:
    st.session_state.exercise = 1
if "screen" not in st.session_state:
    st.session_state.screen = 5
if "name" not in st.session_state:
    st.session_state.name = "User"

# -----------------------
# HOME
# -----------------------
if page == "Home":

    hero = Image.open("assets/hero.jpg")

    st.image(hero, use_container_width=True)

    st.markdown("""
    <div style='text-align:center; padding:20px'>
        <h1 style='font-size:50px'>Meet Your Future Self</h1>
        <p style='font-size:18px; color:gray'>
        TwinAI simulates your digital future based on your daily habits.
        </p>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    c1.metric("Active Twins", "12,548")
    c2.metric("Predictions", "84,291")
    c3.metric("Growth", "+18%")

# -----------------------
# MY TWIN
# -----------------------
elif page == "My Twin":

    st.header("Create Your Twin")

    st.session_state.name = st.text_input("Name", st.session_state.name)

    st.session_state.study = st.slider("Study Hours", 0, 12, st.session_state.study)
    st.session_state.sleep = st.slider("Sleep Hours", 0, 12, st.session_state.sleep)
    st.session_state.exercise = st.slider("Exercise Hours", 0, 5, st.session_state.exercise)
    st.session_state.screen = st.slider("Screen Time", 0, 15, st.session_state.screen)

    if st.button("Generate Twin"):

        score = (
            st.session_state.study * 5 +
            st.session_state.sleep * 4 +
            st.session_state.exercise * 8 -
            st.session_state.screen
        )

        score = max(0, min(100, score))

        st.session_state.score = score

        st.success(f"{st.session_state.name}'s Twin Generated")

        st.progress(score / 100)

        if score >= 80:
            st.info("Elite Potential 🚀")
        elif score >= 60:
            st.info("Strong Growth 📈")
        else:
            st.warning("Needs Improvement ⚠️")

# -----------------------
# 3D TWIN
# -----------------------
elif page == "3D Twin":

    study = st.session_state.study
    sleep = st.session_state.sleep
    exercise = st.session_state.exercise
    screen = st.session_state.screen
    name = st.session_state.name

    focus = max(0, min(100, study * 10 - screen * 2))
    energy = max(0, min(100, sleep * 12))
    discipline = max(0, min(100, study * 6 + exercise * 12))

    overall = (focus + energy + discipline) / 300

    st.title(f"🧠 {name}'s Digital Twin")

    col1, col2 = st.columns([2, 1])

    with col1:
        components.html(
            """
            <iframe
            src="https://sketchfab.com/models/27f75fa94c384000bb6a79a3000f8e80/embed?autostart=1&ui_infos=0&ui_controls=1"
            width="100%"
            height="600"
            frameborder="0">
            </iframe>
            """,
            height=620
        )

    with col2:
        st.metric("Focus", f"{focus}%")
        st.metric("Energy", f"{energy}%")
        st.metric("Discipline", f"{discipline}%")

        st.progress(overall)

        if overall > 0.75:
            st.success("Elite Twin 🚀")
        elif overall > 0.5:
            st.info("Developing Twin 📈")
        else:
            st.warning("Early Stage Twin 🌱")

# -----------------------
# FUTURE SIMULATOR
# -----------------------
elif page == "Future Simulator":

    st.header("Future Simulator")

    current = st.slider("Current Performance", 0, 100, 70)
    improvement = st.slider("Potential Growth", 0, 50, 10)

    future = min(100, current + improvement)

    st.metric("Future Score", future)
    st.progress(future / 100)

    st.divider()

    focus = max(0, min(100, st.session_state.study * 10 - st.session_state.screen * 2))
    energy = max(0, min(100, st.session_state.sleep * 12))
    discipline = max(0, min(100, st.session_state.study * 6 + st.session_state.exercise * 12))

    if focus > 80 and discipline > 70:
        career = "AI Researcher 🤖"
    elif focus > 70:
        career = "Software Engineer 💻"
    elif energy > 80:
        career = "Entrepreneur 🚀"
    else:
        career = "Explorer 🌱"

    st.success(f"Predicted Career: {career}")

# -----------------------
# ACHIEVEMENTS
# -----------------------
elif page == "Achievements":

    st.header("Achievements")

    st.success("🏆 Focus Master")
    st.success("🔥 Study Beast")
    st.success("😴 Sleep Champion")
    st.success("🚀 Elite Twin")
