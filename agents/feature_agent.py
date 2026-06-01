import pandas as pd


def identify_business_features(df):
    """
    Automatically identify useful business columns.
    """

    numerical_cols = df.select_dtypes(include=["number"]).columns.tolist()

    categorical_cols = df.select_dtypes(
        exclude=["number"]
    ).columns.tolist()

    feature_scores = {}

    for col in numerical_cols:

        unique_ratio = df[col].nunique() / len(df)

        feature_scores[col] = round(unique_ratio, 3)

    sorted_features = sorted(
        feature_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    recommended_features = [
        feature[0]
        for feature in sorted_features[:5]
    ]

    return {
        "recommended_features": recommended_features,
        "numerical_columns": numerical_cols,
        "categorical_columns": categorical_cols
    }