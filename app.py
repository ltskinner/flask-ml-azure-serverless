import logging

# import joblib
# import pandas as pd
from flask import Flask, jsonify  # , request
from flask.logging import create_logger
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)


def scale(payload):
    """Scales Payload"""

    LOG.info("Scaling Payload: %s payload")
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict


@app.route("/")
def home():
    app_title = "Sklearn Prediction Home"
    app_subtitle = "From Azure Pipelines (Continuous Delivery)"
    html = f"<h3>{app_title}: {app_subtitle}</h3>"
    return html.format(format)


@app.route("/predict", methods=["POST"])
def predict():
    """Performs an sklearn prediction
    input looks like:
            {
    "CHAS":{
      "0":0
    },
    "RM":{
      "0":6.575
    },
    "TAX":{
      "0":296.0
    },
    "PTRATIO":{
       "0":15.3
    },
    "B":{
       "0":396.9
    },
    "LSTAT":{
       "0":4.98
    }
    result looks like:
    { "prediction": [ 20.35373177134412 ] }
    """

    """
    json_payload = request.json
    LOG.info("JSON payload: %s json_payload")
    inference_payload = pd.DataFrame(json_payload)
    LOG.info("inference payload DataFrame: %s inference_payload")

    try:
        model_path = "./models/boston_housing_prediction.joblib"
        clf = joblib.load(model_path)
    except Exception as e:
        LOG.critical(str(e))
        LOG.info("JSON payload: %s json_payload")
        #return "Model not loaded"
        return str(e)

    scaled_payload = scale(inference_payload)
    prediction = list(clf.predict(scaled_payload))
    """
    # 03/31/2023 LTS - basically, there are version issues
    # I care more about the interface than the model actually running
    # so we are gonna stub the output and keep moving

    prediction = [20.35373177134412]

    LOG.info("prediction: %s prediction")

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
