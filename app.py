from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load timetable from JSON
with open("timetable.json", "r") as file:
    timetable = json.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    teacher_name = None
    day_selected = None
    schedule = None

    if request.method == "POST":
        teacher_name = request.form["teacher_name"]
        day_selected = request.form["day"]
        if teacher_name in timetable and day_selected in timetable[teacher_name]:
            schedule = timetable[teacher_name][day_selected]

    return render_template("index.html", schedule=schedule, teacher_name=teacher_name, day_selected=day_selected)

if __name__ == "__main__":
    app.run(debug=True)
