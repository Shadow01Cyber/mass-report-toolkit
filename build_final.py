#!/usr/bin/env python3
import json

with open("/data/telegram_abuse_reports/reports.json") as f:
    reports = json.load(f)

def js_esc(s):
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

rjs = []
for r in reports:
    rjs.append('{"s":`' + js_esc(r["s"]) + '`,"b":`' + js_esc(r["b"]) + '`}')
rstr = "[" + ",".join(rjs) + "]"

with open("/data/telegram_abuse_reports/template.html") as f:
    html = f.read()

html = html.replace("REPORTS_PLACEHOLDER", rstr)

with open("/data/telegram_abuse_reports/index.html", "w") as f:
    f.write(html)

print(f"Done: {len(html)} bytes")
