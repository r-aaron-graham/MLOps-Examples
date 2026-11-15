# MLOps Examples

An experiment-tracking demo and companion templates for CI, data versioning, and serving. Start with the MLflow script to see how training results can be recorded and inspected.

## Run the experiment

From the repository root, using an activated Python virtual environment:

```sh
python -m pip install mlflow scikit-learn
MLFLOW_TRACKING_URI=sqlite:///mlflow.db python "Experiment Tracking with MLflow.py"
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

In PowerShell, set `$env:MLFLOW_TRACKING_URI = "sqlite:///mlflow.db"` before running the Python command. Open the local MLflow UI at `http://127.0.0.1:5000` and select **Diabetes_Regression_Experiment**.

The script uses scikit-learn's bundled diabetes dataset, a fixed train/test split, and linear regression. It logs mean squared error, R², the model type, and the fitted model.

## Companion templates

| Example | What to supply when adapting it |
| --- | --- |
| [GitHub Actions YAML](CICD%20Pipeline%20with%20GitHub%20Actions.yaml) | A target repository with a dependency manifest and tests. The sample lives at the repository root and is not an active workflow. |
| [DVC command sketch](Data%20Versioning%20with%20DVC.txt) | A dataset, training script, and commands compatible with your DVC version. |
| [Dockerfile sketch](Dockerfile%20for%20Model%20Containerization.txt) | A FastAPI application and dependency manifest. |
| [Deployment call](mlops_example.py) | A deployment script. The Python file illustrates calling it with `subprocess`. |
