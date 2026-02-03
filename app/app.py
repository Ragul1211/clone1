from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)

# starting train location
train = {
    "lat": 12.9716,
    "lng": 77.5946,
    "time": ""   # initialize to avoid editor warning
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/location")
def location():
    # simulate train moving
    train["lat"] += 0.0001
    train["lng"] += 0.0001
    train["time"] = time.strftime("%H:%M:%S")

    return jsonify(train)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
