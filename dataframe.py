import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder

def clean_and_preprocess(df):
    # Handle missing values
    df = df.fillna(df.mean(numeric_only=True))

    # Normalize numerical columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    # Encode categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    encoder = OneHotEncoder(sparse=False)
    encoded = encoder.fit_transform(df[categorical_cols])
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(categorical_cols))
    df = df.drop(categorical_cols, axis=1)
    df = pd.concat([df, encoded_df], axis=1)

    return df
