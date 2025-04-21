from flask import Flask, render_template, request, redirect, jsonify
from datetime import datetime
import os

app = Flask(__name__)
TUPLE_LOG_FILE = "calendar_space.tsv"

@app.route("/")
def calendar_view():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        date = request.form.get("date")
        time = request.form.get("time")
        description = request.form.get("description")
        recorded_at = datetime.now().astimezone().isoformat()

        new_line = f"{date}\t{time}\t{description.strip()}\t{recorded_at}\n"
        with open(TUPLE_LOG_FILE, "a", encoding="utf-8") as f:
            f.write(new_line)

        return redirect("/")

    return render_template("add_event.html")

@app.route("/reschedule", methods=["POST"])
def reschedule_event():
    data = request.get_json()
    old_start = data.get("old_start")
    new_start = data.get("new_start")
    title = data.get("title")

    try:
        old_dt = datetime.fromisoformat(old_start)
        new_dt = datetime.fromisoformat(new_start)
    except ValueError:
        return "Invalid datetime format", 400

    new_date = new_dt.strftime("%Y-%m-%d")
    new_time = new_dt.strftime("%H:%M")
    recorded_at = datetime.now().astimezone().isoformat()

    new_description = title.strip()  # Don't add "(rescheduled)"

    new_line = f"{new_date}\t{new_time}\t{new_description}\t{recorded_at}\n"

    with open(TUPLE_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(new_line)

    return "Rescheduled", 200

@app.route("/events")
def get_events():
    all_tuples = []
    latest_by_title = {}
    history_map = {}

    # Step 1: Read all tuples
    if os.path.exists(TUPLE_LOG_FILE):
        with open(TUPLE_LOG_FILE, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) == 4:
                    date, time, description, recorded_at = parts
                    try:
                        dt = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
                        recorded_dt = datetime.fromisoformat(recorded_at)
                        iso_start = dt.isoformat()

                        base_title = description.lower().strip()

                        all_tuples.append({
                            "title": description,
                            "base_title": base_title,
                            "start": iso_start,
                            "recorded_at": recorded_at,
                            "recorded_dt": recorded_dt,
                            "date": date,
                            "time": time
                        })

                        # Track latest per base_title
                        if base_title not in latest_by_title or recorded_dt > latest_by_title[base_title]:
                            latest_by_title[base_title] = recorded_dt

                        # Build history
                        history_map.setdefault(base_title, []).append(f"{date} {time}")

                    except ValueError:
                        continue

    # Step 2: Classify and construct JSON output
    output = []
    for t in all_tuples:
        is_latest = t["recorded_dt"] == latest_by_title[t["base_title"]]
        css_class = "active" if is_latest else "obsolete"
        tooltip = None

        if is_latest:
            history_list = history_map.get(t["base_title"], [])
            tooltip = "🕓 History:\n" + "\n".join(f"- {h}" for h in sorted(history_list))

        event = {
            "title": t["title"],
            "start": t["start"],
            "className": css_class,
            "extendedProps": {
                "date": t["date"],
                "time": t["time"],
                "recorded_at": t["recorded_at"]
            }
        }

        if tooltip:
            event["extendedProps"]["tooltip"] = tooltip

        output.append(event)

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)





