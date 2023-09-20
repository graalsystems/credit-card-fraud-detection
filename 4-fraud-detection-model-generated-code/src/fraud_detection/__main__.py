import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import accuracy_score
import s3fs
import joblib

df_e8c0e4da = pd.read_parquet(
    "s3a://graal-demo-data-integration/output/fraud.parquet",
    storage_options={
        "key": "SCWESH97SYBFJBS6JT64",
        "secret": "REPLACE SECRET KEY HERE",
        "client_kwargs": {
            "endpoint_url": "https://s3.fr-par.scw.cloud",
            "region_name": "fr-par",
        },
    },
)
# Implementing a RandomForestRegressor model
x_columns = df_e8c0e4da[["amount", "is_in_european_union"]]
y_column = df_e8c0e4da["is_valid"]
X_train, X_test, y_train, y_test = train_test_split(
    x_columns, y_column, test_size=0.2, random_state=42
)
# Random forest regressor
model_83ea8978 = RandomForestClassifier(n_estimators=1000, max_depth=3, random_state=42)
model_83ea8978.fit(X_train, y_train)
# Model prediction
y_pred_test = model_83ea8978.predict(X_test)
# Metrics
print(
    f"accuracy_score: {accuracy_score(y_test, y_pred_test)}"
)  # accurracy is automatically printed
s3 = s3fs.S3FileSystem(
    key="SCWESH97SYBFJBS6JT64",
    secret="REPLACE SECRET KEY HERE",
    client_kwargs={
        "endpoint_url": "https://s3.fr-par.scw.cloud",
        "region_name": "fr-par",
    },
)
joblib.dump(
    model_83ea8978,
    s3.open("s3a://graal-demo-data-integration/output/models/fraud/model.joblib", "wb"),
)
