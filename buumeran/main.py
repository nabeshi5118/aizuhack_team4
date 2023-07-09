from flask import Flask
from flask import render_template
import threading,webbrowser
from ics import Calendar
from datetime import datetime, timezone, timedelta

app = Flask(__name__)
filename = 'test3.ics'
tz_jst = timezone(timedelta(hours=9))

@app.route("/")
def main():
    with open(filename,'r', encoding='utf-8') as f:
        ics_str = f.read()

    gcal = Calendar(ics_str)
    new_gcal = Calendar()
    dt_now = datetime.now()
    task = []
    
    for event in gcal.events:
        if event.begin.datetime.month == dt_now.month and event.begin.datetime.year == dt_now.year:
            task.append(event.name)
            #print(event.name)
    return render_template("main.html", task=task)

if __name__ == '__main__':
    threading.Timer(0.1, lambda: webbrowser.open_new_tab('http://localhost:5000') ).start()
    app.run(debug=False)