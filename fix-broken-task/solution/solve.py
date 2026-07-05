import json
import re
from collections import Counter
from pathlib import Path

paths, ips, total = Counter(), set(), 0


BASE_DIR = Path(__file__).resolve().parent.parent
LOG_FILE = BASE_DIR / "environment" / "access.log"
OUTPUT_FILE = BASE_DIR / "report.json"

with open(LOG_FILE) as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

with open(OUTPUT_FILE, "w") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": paths.most_common(1)[0][0],
        },
        out,
    )
print("wrote /app/report.json")

