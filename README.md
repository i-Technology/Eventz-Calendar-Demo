
# 📅 Eventz Calendar Demo

A fully functional calendar application built using **Python** and **Flask**, backed by an **immutable tuple archive**.  
This project demonstrates the **Eventz Law**:  
> `y = F(Y, e)`  
Where:
- `Y` = the archive of all past tuples (a tab-separated `.tsv` file)
- `e` = a new event
- `F` = a pure function that appends `e` to `Y`
- `y` = the enriched new state (the updated archive)

No database. No ORM. No backend complexity.  
Just truth — preserved through time.

---

## 🚀 Features

- 📆 Month-view calendar powered by [FullCalendar](https://fullcalendar.io/)
- ✍️ Add events via a clean HTML form
- 🕹️ Drag & drop to reschedule events
- 📜 Each change adds a new tuple — no data is ever overwritten
- 🧠 Hover tooltips show full historical schedule
- 🌓 Toggle: show only current (latest) events or full history

---

## 🧰 Tech Stack

- **Language**: Python 3
- **Framework**: Flask
- **Storage**: Plain text (`calendar_space.tsv`)
- **UI**: FullCalendar.js + native HTML/CSS
- **Architecture**: [Eventz](https://github.com/i-Technology) tuple-space model

---

## 📦 Installation

```bash
git clone https://github.com/i-Technology/Eventz-Calendar-Demo.git
cd Eventz-Calendar-Demo
python3 -m venv .venv
source .venv/bin/activate
pip install flask
python app.py
```

Then visit: [http://localhost:5000](http://localhost:5000)

---

## 📂 Project Structure

```
.
├── app.py                  # Core Python app (F)
├── calendar_space.tsv      # Tuple archive (Y)
├── templates/
│   ├── index.html          # Calendar view
│   └── add_event.html      # Event entry form
└── static/                 # (optional, unused unless styles/scripts are added)
```

---

## 🧠 Why Eventz?

Most software systems are too complex.  
**Eventz is a new software law** that keeps logic pure, data immutable, and history preserved.  
Every new input is an event. Every rule is a function. Every result is a tuple.

This calendar proves you can build modern, interactive tools with:
- Zero databases
- Zero coupling
- Zero accidental complexity

---

## 📜 License

MIT — Use it, fork it, improve it, share it.

---

## 👋 Contributions Welcome

If you're inspired to extend this (tagging, notifications, history viewer), open a PR!

```
