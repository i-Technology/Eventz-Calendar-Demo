from datetime import datetime
import os

TUPLE_LOG_FILE = "calendar_space.tsv"

def load_events():
    if not os.path.exists(TUPLE_LOG_FILE):
        print("❌ No calendar data found.")
        return []

    events = []
    with open(TUPLE_LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) == 4:
                date, time, description, recorded_at = parts
                events.append({
                    "date": date,
                    "time": time,
                    "description": description,
                    "recorded_at": recorded_at
                })
    return events

def display_events(events):
    if not events:
        print("📭 No events in the calendar.")
        return

    def sort_key(event):
        return datetime.strptime(f"{event['date']} {event['time']}", "%Y-%m-%d %H:%M")

    sorted_events = sorted(events, key=sort_key)

    print("📅 Eventz Calendar - Upcoming Events")
    print("-" * 40)
    for event in sorted_events:
        print(f"🕒 {event['date']} {event['time']} - {event['description']}")
        print(f"    Recorded at: {event['recorded_at']}")
    print("-" * 40)

def main():
    events = load_events()
    display_events(events)

if __name__ == "__main__":
    main()
