def set_custom_theme():
    import streamlit as st
    custom_css = """
    <style>
    .stButton > button {
        background-color: #e91e63;
        color: white;
        border: none;
        padding: 0.5em 1.5em;
        border-radius: 8px;
    }
    .stButton > button:hover {
        background-color: #ff8a80;
    }
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #e91e63;
    }
    .stMetric label {
        color: #e91e63;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
