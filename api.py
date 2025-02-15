from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
df = pd.read_csv("data.csv")

@app.route("/", methods=["GET"])
def get_data():
    return jsonify(df.to_dict())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
