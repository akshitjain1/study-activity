import json
import datetime
import os

today = str(datetime.date.today())
log_file = f"logs/{today}.md"

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Load activity data
with open("activity.json", encoding="utf-8") as f:
    data = json.load(f)

dsa = data.get("dsa", [])
projects = data.get("projects", [])
learning = data.get("learning", [])
# Written by Engineering OS when a session is closed: what I learned, where I
# got stuck, what I do first tomorrow. .get with a default so an activity.json
# from before this section existed still runs.
journal = data.get("journal", [])

# Write structured log. Explicit encoding: the entries carry em dashes now, and
# a runner defaulting to ascii would fail on them mid-write.
with open(log_file, "w", encoding="utf-8") as f:
    f.write(f"# 📅 Learning Log - {today}\n\n")

    if not (dsa or projects or learning or journal):
        f.write("⚠️ No significant activity today.\n")
        f.write("Reviewed previous concepts and notes and planned upcoming tasks.\n")
    else:
        if dsa:
            f.write("## 🧠 DSA Practice\n")
            for item in dsa:
                f.write(f"- {item}\n")
            f.write("\n")

        if projects:
            f.write("## 🚀 Projects\n")
            for item in projects:
                f.write(f"- {item}\n")
            f.write("\n")

        if learning:
            f.write("## 📚 Learning\n")
            for item in learning:
                f.write(f"- {item}\n")
            f.write("\n")

        if journal:
            f.write("## 📝 Reflection\n")
            for item in journal:
                f.write(f"- {item}\n")
            f.write("\n")

    # Optional summary (very impressive)
    # The reflection is a record of the day rather than a task, so it is not
    # counted -- otherwise writing three sentences would read as three tasks.
    total_tasks = len(dsa) + len(projects) + len(learning)
    f.write("---\n")
    f.write(f"✅ Total productive tasks: {total_tasks}\n")

# 🔥 Reset activity after logging (IMPORTANT)
reset_data = {
    "dsa": [],
    "projects": [],
    "learning": [],
    "journal": []
}

with open("activity.json", "w", encoding="utf-8") as f:
    json.dump(reset_data, f, indent=2)
