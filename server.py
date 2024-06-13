from flask import Flask,render_template,request
from weather import get_weather
from waitress import serve 

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template(
        'index.html'
    )

@app.route("/weather")
def get_new_weather():
    city = request.args.get('city')
    data = get_weather(city)
    return render_template(
        "weather.html",
        title = data["name"],
        status = data["weather"][0]["description"].capitalize(),
        temp =f"{data['main']['temp']}",
        feels_like =f"{data['main']['feels_like']:.1f}"
    )


if(__name__ == "__main__"):
    serve(app,host="0.0.0.0",port=800)