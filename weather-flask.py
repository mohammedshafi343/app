from flask import Flask, render_template, request
import requests

app = Flask(__name__)
API_KEY = 'your_api_key_here'  # Replace with your OpenWeatherMap API key

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    if request.method == "POST":
        city = request.form.get("city")
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric")
        if response.status_code == 200:
            weather = response.json()
        else:
            weather = "City not found."
    return render_template("index.html", weather=weather)

if __name__ == "__main__":
    app.run(debug=True)
