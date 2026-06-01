import streamlit as st
import pandas as pd

from utils.data_loader import load_file
from agents.dataset_agent import generate_dataset_summary

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Business Intelligence Platform")

st.markdown(
    "Upload business datasets and generate insights."
)

uploaded_file = st.file_uploader(
    "Upload CSV or Excel File",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    st.success("Dataset Loaded Successfully")

    tab1, tab2, tab3 = st.tabs(
        [
            "Preview",
            "Statistics",
            "Dataset Agent"
        ]
    )

    with tab1:

        st.subheader("Dataset Preview")

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

    with tab2:

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Rows",
                df.shape[0]
            )

        with col2:
            st.metric(
                "Columns",
                df.shape[1]
            )

        st.subheader("Column Names")

        st.write(
            list(df.columns)
        )

    with tab3:

        summary = generate_dataset_summary(df)

        st.subheader(
            "Dataset Understanding Agent"
        )

        st.write(
            f"Rows: {summary['rows']}"
        )

        st.write(
            f"Columns: {summary['columns']}"
        )

        st.subheader(
            "Numerical Columns"
        )

        st.write(
            summary["numerical_columns"]
        )

        st.subheader(
            "Categorical Columns"
        )

        st.write(
            summary["categorical_columns"]
        )

        st.subheader(
            "Missing Values"
        )

        st.dataframe(
            summary["missing_values"]
        )