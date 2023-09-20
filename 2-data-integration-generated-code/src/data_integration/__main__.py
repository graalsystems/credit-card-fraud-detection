import pandas as pd
import s3fs
import pyarrow as pa
import pyarrow.parquet as pq

df_6a9f672a = pd.read_csv(
    "s3a://graal-demo-data-integration/input/geo.csv",
    sep=",",
    header=0,
    names=[
        "ip_range",
        "country_name",
        "geoname_id",
        "locale_code",
        "continent_code",
        "continent_name",
        "country_iso_code",
        "is_in_european_union",
    ],
    dtype={
        "ip_range": "str",
        "country_name": "str",
        "geoname_id": "str",
        "locale_code": "str",
        "continent_code": "str",
        "continent_name": "str",
        "country_iso_code": "str",
        "is_in_european_union": "Int32",
    },
    storage_options={
        "key": "SCWESH97SYBFJBS6JT64",
        "secret": "REPLACE SECRET KEY HERE",
        "client_kwargs": {
            "endpoint_url": "https://s3.fr-par.scw.cloud",
            "region_name": "fr-par",
        },
    },
)
df_818ed030 = pd.read_csv(
    "s3a://graal-demo-data-integration/input/provider.csv",
    sep=",",
    header=0,
    names=["ip_range", "provider"],
    dtype={
        "ip_range": "str",
        "provider": "str",
    },
    storage_options={
        "key": "SCWESH97SYBFJBS6JT64",
        "secret": "REPLACE SECRET KEY HERE",
        "client_kwargs": {
            "endpoint_url": "https://s3.fr-par.scw.cloud",
            "region_name": "fr-par",
        },
    },
)
df_b2402fae = pd.read_csv(
    "s3a://graal-demo-data-integration/input/transaction.csv",
    sep=";",
    header=0,
    names=["CN", "date", "montant", "ip", "ip_range", "is_valid"],
    dtype={
        "CN": "Int64",
        "date": "str",
        "montant": "Int64",
        "ip": "str",
        "ip_range": "str",
        "is_valid": "bool",
    },
    storage_options={
        "key": "SCWESH97SYBFJBS6JT64",
        "secret": "REPLACE SECRET KEY HERE",
        "client_kwargs": {
            "endpoint_url": "https://s3.fr-par.scw.cloud",
            "region_name": "fr-par",
        },
    },
)
df_fa3ea7ea = df_6a9f672a.drop(
    columns=["geoname_id", "locale_code", "country_iso_code"]
).reset_index(drop=True)
df_095cd80b = df_b2402fae.rename(columns={"montant": "amount"}).reset_index(drop=True)
df_5d66525d = df_818ed030.merge(
    right=df_095cd80b, left_on=["ip_range"], right_on=["ip_range"], how="right",
).reset_index(drop=True)
df_10ff6720 = df_fa3ea7ea.merge(
    right=df_5d66525d, left_on=["ip_range"], right_on=["ip_range"], how="right",
).reset_index(drop=True)
fs_408118d6 = s3fs.S3FileSystem(
    key="SCWESH97SYBFJBS6JT64",
    secret="REPLACE SECRET KEY HERE",
    client_kwargs={
        "endpoint_url": "https://s3.fr-par.scw.cloud",
        "region_name": "fr-par",
    },
)
table_10ff6720 = pa.Table.from_pandas(df_10ff6720, preserve_index=False)
pq.write_table(
    table=table_10ff6720,
    where="s3a://graal-demo-data-integration/output/fraud.parquet",
    filesystem=fs_408118d6,
)
