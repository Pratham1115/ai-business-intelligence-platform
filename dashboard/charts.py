import plotly.express as px
import pandas as pd


def create_column_type_chart(
    numerical_count,
    categorical_count
):

    data = pd.DataFrame({
        "Type": [
            "Numerical",
            "Categorical"
        ],
        "Count": [
            numerical_count,
            categorical_count
        ]
    })

    fig = px.pie(
        data,
        names="Type",
        values="Count",
        title="Column Type Distribution"
    )

    return fig