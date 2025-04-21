from datetime import datetime, UTC
import os

TUPLE_LOG_FILE = "calendar_space.tsv"

def get_event_input():
    date = input("Enter the date (YYYY-MM-DD): ")
    time = input("Enter the time (HH:MM): ")
    description = input("Enter the event description: ")
    recorded_at = datetime.now(UTC).isoformat()
    return f"{date}\t{time}\t{description}\t{recorded_at}"

def append_to_tuple_space(tuple_line):
    with open(TUPLE_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(tuple_line + "\n")

def main():
    print("📅 Eventz Calendar - Add an Event")
    tuple_line = get_event_input()
    append_to_tuple_space(tuple_line)
    print("✅ Event added to tuple space.")

if __name__ == "__main__":
    main()




