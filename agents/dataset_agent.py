import pandas as pd


def generate_dataset_summary(df):

    numerical_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    total_missing = df.isnull().sum().sum()

    total_cells = df.shape[0] * df.shape[1]

    completeness = (
        ((total_cells - total_missing) / total_cells)
        * 100
    )

    summary = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols,
        "missing_values": df.isnull().sum(),
        "completeness_score": round(
            completeness,
            2
        )
    }

    return summary