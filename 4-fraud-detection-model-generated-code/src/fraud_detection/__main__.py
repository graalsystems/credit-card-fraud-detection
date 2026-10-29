import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import model_selection
from sklearn.metrics import accuracy_score
import s3fs
import joblib

import os

# Object storage settings come from the environment (for example project
# secrets), never from the code.
BUCKET = os.environ.get("GRAAL_BUCKET", "graal-demo-data-integration")
S3_OPTIONS = {
    "key": os.environ.get("AWS_ACCESS_KEY_ID"),
    "secret": os.environ.get("AWS_SECRET_ACCESS_KEY"),
    "client_kwargs": {
        "endpoint_url": os.environ.get("AWS_ENDPOINT_URL"),
        "region_name": os.environ.get("AWS_REGION"),
    },
}

df_e8c0e4da = pd.read_parquet(
    f"s3a://{BUCKET}/output/fraud.parquet",
    storage_options=S3_OPTIONS,
)
# Implementing a RandomForestClassifier model
x_columns = df_e8c0e4da[["amount", "is_in_european_union"]]
y_column = df_e8c0e4da["is_valid"]
X_train, X_test, y_train, y_test = train_test_split(
    x_columns, y_column, test_size=0.2, random_state=42
)
# Random forest classifier
model_83ea8978 = RandomForestClassifier(n_estimators=1000, max_depth=3, random_state=42)
model_83ea8978.fit(X_train, y_train)
# Model prediction
y_pred_test = model_83ea8978.predict(X_test)
# Metrics
print(
    f"accuracy_score: {accuracy_score(y_test, y_pred_test)}"
)  # accuracy is automatically printed
s3 = s3fs.S3FileSystem(
    key=S3_OPTIONS["key"],
    secret=S3_OPTIONS["secret"],
    client_kwargs=S3_OPTIONS["client_kwargs"],
)
joblib.dump(
    model_83ea8978,
    s3.open(f"s3a://{BUCKET}/output/models/fraud/model.joblib", "wb"),
)
