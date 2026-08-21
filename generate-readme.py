#!/usr/bin/env python3
from datetime import date
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BIRTH_DATE = date(1974, 12, 17)


def calc_uptime():
    today = date.today()
    y = today.year - BIRTH_DATE.year
    m = today.month - BIRTH_DATE.month
    d = today.day - BIRTH_DATE.day
    if d < 0:
        m -= 1
        pm = 12 if today.month == 1 else today.month - 1
        py = today.year - 1 if today.month == 1 else today.year
        dim = (date(py, pm + 1, 1) - date(py, pm, 1)).days
        d += dim
    if m < 0:
        y -= 1
        m += 12
    return y, m, d


y, m, d = calc_uptime()
uptime_str = f"{y} years, {m} months, {d} days"

info_panel = [
    "  vincent@dupain",
    "  " + "\u2500" * 12,
    "  Job:      DevOps/SRE/Platform Engineer",
    "  Location: Trosly Breuil, France",
    f"  Uptime:   {uptime_str}",
    "  Blog:     blog.vincentdupain.com",
    "  GitHub:   @vdupain",
    "  Contact:  vince9p+contact@pm.me",
    "  Tech:     IaC, Proxmox, k8s, Observability,",
    "            Gitops, Cloud",
    "  Hobbies:  Cycling (gravel and mountain",
    "            biking), sport shooting, ham",
    "            radio, homelab",
    "",
    '  "It\'s a UNIX system! I know this!"',
]

with open(os.path.join(HERE, "ascii.txt")) as f:
    art_lines = [line.rstrip("\n") for line in f.readlines()]

art_width = max(len(l) for l in art_lines)

output = []
for i, art_line in enumerate(art_lines):
    pad = " " * max(0, art_width - len(art_line))
    if i < len(info_panel):
        output.append(art_line + pad + "  " + info_panel[i])
    else:
        output.append(art_line)

readme = "```text\n" + "\n".join(output) + "\n```\n"

with open(os.path.join(HERE, "README.md"), "w") as f:
    f.write(readme)

print("README.md generated")