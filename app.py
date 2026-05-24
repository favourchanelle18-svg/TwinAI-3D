import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="TwinAI 3D",
    page_icon="🧠",
    layout="wide"
)

hero = Image.open("assets/hero.jpg")

st.image(hero, use_container_width=True)

st.markdown("""
# Meet Your Future Self

TwinAI creates a digital version of you and predicts how your habits today shape your future.

""")

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Focus", "88%")

with col2:
    st.metric("Energy", "91%")

with col3:
    st.metric("Discipline", "84%")

st.divider()

st.subheader("Create Your Twin")

name = st.text_input("Name")

age = st.slider(
    "Age",
    13,
    30,
    17
)

career = st.selectbox(
    "Dream Career",
    [
        "Software Engineer",
        "Doctor",
        "Entrepreneur",
        "AI Researcher",
        "Designer",
        "Other"
    ]
)

study = st.slider(
    "Study Hours",
    0,
    12,
    5
)

sleep = st.slider(
    "Sleep Hours",
    0,
    12,
    8
)

exercise = st.slider(
    "Exercise Hours",
    0,
    5,
    1
)

screen = st.slider(
    "Screen Time",
    0,
    15,
    5
)

if st.button("Generate My Twin"):

    score = (
        study * 5
        + sleep * 4
        + exercise * 8
        - screen
    )

    score = max(0, min(100, score))

    st.success("Twin Generated Successfully")

    st.subheader(f"{name}'s Digital Twin")

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
