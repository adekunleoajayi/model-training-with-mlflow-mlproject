import sqlite3

import pandas as pd
from sklearn.model_selection import train_test_split


def get_train_test_datasets():
    # Create your connection.
    database = sqlite3.connect("./data/database.sqlite")

    # - get player_Attributes from the database
    df = pd.read_sql_query("SELECT * FROM Player_Attributes", database)

    # Remove player_fifa_api_id, player_api_id, date and other columns with integer values
    df = df.select_dtypes(include=["float"])

    # - remove missing values
    df = df.dropna()

    x = df[df.columns[1:]]
    y = df[df.columns[0]]

    # - split datasets into train and test
    xtrain, xtest, ytrain, ytest = train_test_split(x, y.values, test_size=0.2, random_state=42)

    return xtrain, xtest, ytrain, ytest
