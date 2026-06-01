def generate_dataset_summary(df):

    numerical_cols = df.select_dtypes(include=["number"]).columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    missing_values = (
        df.isnull()
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols,
        "missing_values": missing_values
    }