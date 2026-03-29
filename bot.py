import json
import datetime
import os

today = str(datetime.date.today())
log_file = f"logs/{today}.md"

# Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# Load activity data
with open("activity.json") as f:
    data = json.load(f)

dsa = data.get("dsa", [])
projects = data.get("projects", [])
learning = data.get("learning", [])

# Write structured log
with open(log_file, "w") as f:
    f.write(f"# 📅 Learning Log - {today}\n\n")

    if not (dsa or projects or learning):
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

    # Optional summary (very impressive)
    total_tasks = len(dsa) + len(projects) + len(learning)
    f.write("---\n")
    f.write(f"✅ Total productive tasks: {total_tasks}\n")

# 🔥 Reset activity after logging (IMPORTANT)
reset_data = {
    "dsa": [],
    "projects": [],
    "learning": []
}

with open("activity.json", "w") as f:
    json.dump(reset_data, f, indent=2)
