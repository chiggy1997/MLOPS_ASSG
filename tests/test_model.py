import pytest
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@pytest.fixture
def sample_data():
    data = load_iris()
    return data.data, data.target

def test_model_training(sample_data):
    X, y = sample_data
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, y)
    assert len(model.predict(X)) == len(y)

def test_prediction_shape(sample_data):
    X, _ = sample_data
    model = RandomForestClassifier(n_estimators=10)
    model.fit(X, X[:, 0])  # Using the first feature as the target for simplicity
    predictions = model.predict(X)
    assert predictions.shape[0] == X.shape[0]