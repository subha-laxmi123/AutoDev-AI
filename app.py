import streamlit as st
from dotenv import load_dotenv
from agents.analyzer import analyze_code

# Load API key
load_dotenv()

st.set_page_config(
    page_title="AutoDev AI",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AutoDev AI")
st.subheader("Multi-Agent Code Review Assistant")

st.write("Upload a Python (.py) file and let AI analyze it.")

uploaded_file = st.file_uploader(
    "Choose a Python file",
    type=["py"]
)

if uploaded_file is not None:
    code = uploaded_file.read().decode("utf-8")

    st.success("File Uploaded Successfully!")

    st.subheader("Uploaded Code")
    st.code(code, language="python")

    if st.button("Analyze Code"):

        with st.spinner("AI Agent is reviewing your code..."):
            result = analyze_code(code)

        st.success("Analysis Complete!")

        st.markdown(result)