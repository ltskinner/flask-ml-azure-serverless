import json

import numpy as np
import pandas as pd
import pytest
from numpy.testing import assert_array_equal

from app import app, scale


@pytest.fixture(name="client")
def client_fixture():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client


@pytest.fixture(name="payload")
def payload_fixture():
    payload = {
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98},
    }
    return payload


def test_scale(payload):
    expected = np.array([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0]])

    inference_payload = pd.DataFrame(payload)
    result = scale(inference_payload)
    assert_array_equal(result, expected)


def test_home(client):
    resp = client.get("/")
    expected_content = "Sklearn Prediction"
    assert expected_content in resp.text


def test_predict(client, payload):
    resp = client.post("/predict", data=payload)

    expected = {"prediction": [20.35373177134412]}

    result = resp.data.decode("utf-8")
    result = json.loads(result)

    assert result == expected
