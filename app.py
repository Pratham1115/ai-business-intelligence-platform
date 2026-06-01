import streamlit as st

from utils.data_loader import load_file

from agents.dataset_agent import (
    generate_dataset_summary
)

from agents.feature_agent import (
    identify_business_features
)

from dashboard.charts import (
    create_column_type_chart
)

st.set_page_config(
    page_title="AI Business Intelligence Platform",
    page_icon="📊",
    layout="wide"
)

st.title(
    "📊 AI Business Intelligence Platform"
)

st.markdown(
    "Dynamic Business Intelligence using AI Agents"
)

uploaded_file = st.file_uploader(
    "Upload Dataset",
    type=["csv", "xlsx"]
)

if uploaded_file:

    df = load_file(uploaded_file)

    summary = generate_dataset_summary(df)

    features = identify_business_features(df)

    st.sidebar.header(
        "Dataset Overview"
    )

    st.sidebar.metric(
        "Rows",
        summary["rows"]
    )

    st.sidebar.metric(
        "Columns",
        summary["columns"]
    )

    st.sidebar.metric(
        "Completeness %",
        summary["completeness_score"]
    )

    tab1, tab2, tab3 = st.tabs([
        "Dataset",
        "Feature Agent",
        "Dashboard"
    ])

    with tab1:

        st.subheader(
            "Dataset Preview"
        )

        st.dataframe(
            df.head(20),
            use_container_width=True
        )

    with tab2:

        st.subheader(
            "Feature Selection Agent"
        )

        st.success(
            "Recommended Features for Analysis"
        )

        st.write(
            features["recommended_features"]
        )

        st.subheader(
            "Numerical Columns"
        )

        st.write(
            features["numerical_columns"]
        )

        st.subheader(
            "Categorical Columns"
        )

        st.write(
            features["categorical_columns"]
        )

    with tab3:

        st.subheader(
            "Dataset Dashboard"
        )

        fig = create_column_type_chart(
            len(features["numerical_columns"]),
            len(features["categorical_columns"])
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )