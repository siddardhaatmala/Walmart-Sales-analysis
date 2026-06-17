from sqlalchemy import create_engine
import pandas as pd

SQLALCHEMY_DATABASE_URL = f"postgresql://{input('Enter Username:')}:{input('Enter Password:')}@localhost:5432/Project1"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

features_df = pd.read_csv("data/features.csv")
test_df = pd.read_csv("data/test.csv")
stores_df = pd.read_csv("data/stores.csv")
train_df = pd.read_csv('data/train.csv')

features_df.to_sql('raw_features', engine, if_exists='replace', index=False)
test_df.to_sql('test_data', engine, if_exists='replace', index=False)
stores_df.to_sql('stores', engine, if_exists='replace', index=False)
train_df.to_sql('train_data', engine, if_exists='replace', index=False)