import datetime
import re

current_time = datetime.datetime.now(datetime.UTC).strftime("%Y-%m-%d %H:%M:%S UTC")
new_content = f"**Last updated:** {current_time}\n"

with open("README.md", "r", encoding="utf-8") as file:
    readme_text = file.read()

cc = "<!-- C -->"
tm = "<!-- TM -->"

if 2 == readme_text.count(cc):
    split = readme_text.split(cc)
    before = split[0]
    n = 0
    after = split[2]
    try:
        n = int(split[1]) + 1
    except :
        print("probably NaN too lazy and dont care")
    readme_text = f"{before}{cc}\n{n}{cc}{after}"
    print("README.md successfully updated!")
else:
    print("Error: Could not find placeholder tags in README.md cc")


if 2 == readme_text.count(tm):
    split = readme_text.split(tm)
    before = split[0]
    after = split[2]
    readme_text = f"{before}{tm}\n{new_content}{tm}{after}"
    with open("README.md", "w", encoding="utf-8") as file:
        file.write(readme_text)
    print("README.md successfully updated!")
else:
    print("Error: Could not find placeholder tags in README.md tm")

