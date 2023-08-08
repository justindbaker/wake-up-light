from flask import Flask, render_template, request
import datetime
import lights_on
import lights_off

app = Flask(__name__)

@app.route("/")
def main():
    now = datetime.datetime.now()
    time_string = now.strftime("%Y-%m-%d %H:%M")
    template_data = {
        'title' : 'Wake Up Light',
        'time' : time_string
    }
    return render_template('main.html', **template_data)

@app.route("/on")
def turn_lights_on():
    lights_on.main()
    return render_template('main.html')

@app.route("/off")
def turn_lights_off():
    lights_off.main()
    return render_template('main.html')


if __name__ == '__main__':
    
    app.run(debug=True, port=80, host='0.0.0.0')