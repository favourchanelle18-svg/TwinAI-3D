import streamlit as st
from PIL import Image
import streamlit.components.v1 as components
with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="TwinAI 3D",
    page_icon="🧠",
    layout="wide"
)

# -----------------------
# SIDEBAR
# -----------------------

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

# -----------------------
# HOME
# -----------------------

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
        st.metric(
            "Active Twins",
            "12,548"
        )

    with c2:
        st.metric(
            "Predictions Generated",
            "84,291"
        )

    with c3:
        st.metric(
            "Average Growth",
            "+18%"
        )

# -----------------------
# MY TWIN
# -----------------------

elif page == "My Twin":

    st.header("Create Your Twin")

    name = st.text_input("Name")

    age = st.slider("Age", 13, 30, 17)

    study = st.slider("Study Hours", 0, 12, 5)

    sleep = st.slider("Sleep Hours", 0, 12, 8)

    exercise = st.slider("Exercise Hours", 0, 5, 1)

    screen = st.slider("Screen Time", 0, 15, 5)

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

# -----------------------
# FUTURE SIMULATOR
# -----------------------

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

# -----------------------
# ACHIEVEMENTS
# -----------------------

elif page == "Achievements":

    st.header("Achievements")

    st.success("🏆 Focus Master")

    st.success("🔥 Study Beast")

    st.success("😴 Sleep Champion")

    st.success("🚀 Elite Twin")
    elif page == "3D Twin":

    st.header("Your Digital Twin")

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

    st.success("Twin Connected")
