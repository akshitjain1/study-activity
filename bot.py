import json
import datetime
import os

today = str(datetime.date.today())
log_file = f"logs/{today}.md"

os.makedirs("logs", exist_ok=True)

with open("activity.json") as f:
    data = json.load(f)

activities = data["dsa"] + data["projects"] + data["learning"]

with open(log_file, "w") as f:
    f.write(f"# Learning Log - {today}\n\n")

    if activities:
        for act in activities:
            f.write(f"- {act}\n")
    else:
        f.write("No coding today. Reviewed previous notes and planned upcoming tasks.\n")

os.system("git add .")
os.system(f'git commit -m "Learning log update {today}"')
os.system("git push")