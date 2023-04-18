# Machine Learning Model Training With MLFLOW MLproject.

This is a tutorial on training a machine learning model using MLFLOW MLproject concept.

## 0 - Setup environment
```bash
python3 -m venv venv
source venv/bib/activate
python -m pip install --upgrade pip
pip install -U setuptools
pip install mlflow
pip install virtualenv
pip install kubernetes
```
## 1- Run with local env (optional)
Test the setup with your local environment.
```bash
mlflow run . --env-manager local
```

Open a new terminal and start the mlflow ui.

```bash
mlflow server
```
You should be able to see the MLproject run under the default experiment label.

## 2 - Run with defined Conda or Python env
In the MLproject file, docker_env and conda_env are currently commented so the default env is python_env.

```bash
mlflow run .
```
To run the project with a conda environment, uncomment conda_env and comment python_env in the MLproject.

## 3 - Run with docker env
Before running with docker_env, you need to build the image first.

If you have docker compose installed you can build the images using
```bash
docker-compose build
```
esle use
```bash
docker build -t european-soccer-player-rating .
```

Uncomment the docker_env and comment out conda_env and python_env in the MLproject. Now you can run the project with

```bash
mlflow run . --build-image
```

## 4 - Modify the parameters

```bash
mlflow run . \
    -P alpha=1.0 \
    -P l1_ratio=0.5
```


## 5 - Define experiment_name and run_name.

```bash
mlflow run . \
    -P alpha=1.0 \
    -P l1_ratio=0.5 \
    --experiment-name European-Soccer-Player \
    --run-name efficient-net-european-soccer-player
```

## 6 - Run project on Kubernetes
```bash
mlflow run . --build-image --backend kubernetes --backend-config kubernetes/kubernetes_config.json
```
