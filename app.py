import streamlit as st
from PIL import Image
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
        "Future Simulator",
        "Achievements"
    ]
)

# -----------------------
# HOME
# -----------------------

if page == "Home":

    hero = Image.open("assets/hero.jpg")

    st.image(hero, use_container_width=True)

    st.title("Meet Your Future Self")

    st.write(
        "TwinAI creates a digital version of you and predicts future outcomes based on your habits."
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
