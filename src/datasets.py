import pandas as pd
from sklearn.model_selection import train_test_split


def get_train_test_datasets():
    df = pd.read_csv("./data/european_soccer_player.csv")

    x = df[df.columns[1:]]
    y = df[df.columns[0]]

    # - split datasets into train and test
    xtrain, xtest, ytrain, ytest = train_test_split(x, y.values, test_size=0.2, random_state=42)

    return xtrain, xtest, ytrain, ytest
