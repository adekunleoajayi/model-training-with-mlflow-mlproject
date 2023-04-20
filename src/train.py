import argparse

import mlflow
import mlflow.sklearn
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import datasets as datasets


def eval_metrics(actual, pred):
    rmse = (mean_squared_error(actual, pred)) ** 0.5
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_model(alpha, l1_ratio, xtrain, xtest, ytrain, ytest):
    with mlflow.start_run():
        lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)

        lr.fit(xtrain, ytrain)

        predicted_qualities = lr.predict(xtest)

        (rmse, mae, r2) = eval_metrics(ytest, predicted_qualities)

        print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
        print("  RMSE: %s" % rmse)
        print("  MAE: %s" % mae)
        print("  R2: %s" % r2)

        mlflow.log_param("alpha", alpha)
        mlflow.log_param("l1_ratio", l1_ratio)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)
        mlflow.log_metric("mae", mae)

        mlflow.sklearn.log_model(lr, "model")

        mlflow.end_run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--alpha")
    parser.add_argument("--l1-ratio")
    args = parser.parse_args()

    alpha = float(args.alpha)
    l1_ratio = float(args.l1_ratio)

    mlflow.set_tracking_uri("")
    # this is just a hack to ensure the pipeline runs on kubernetes.
    # there is currently a bug and without it the pipeline will fail.

    xtrain, xtest, ytrain, ytest = datasets.get_train_test_datasets()

    train_model(alpha, l1_ratio, xtrain, xtest, ytrain, ytest)
