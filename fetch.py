import requests
import re
import time
import os

channels = [
    "NETMelliAnti",
    "Proxy_v2ry",
    "V2RootConfigPilot"
]

headers = {"User-Agent": "Mozilla/5.0"}
all_links = []

# پیدا کردن مسیر دقیق پوشه lab
base_path = os.path.dirname(os.path.abspath(__file__))

print("Searching for links...")

for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)
        # استخراج لینک‌ها
        links = re.findall(r'(vless|vmess|trojan|ss)://[^\s"<]+', r.text, re.I)
        all_links.extend(links)
        print(f"Done: {ch}")
        time.sleep(1)
    except Exception as e:
        print(f"Error on {ch}: {e}")

all_links = list(dict.fromkeys(all_links))

# خواندن فایل دستی از داخل پوشه lab
manual_file = os.path.join(base_path, "server_manual.txt")
manual_links = []
if os.path.exists(manual_file):
    with open(manual_file, "r") as f:
        manual_links = [line.strip() for line in f if line.strip()]

final_links = manual_links + all_links

# ذخیره در servers.txt داخل پوشه lab
output_file = os.path.join(base_path, "servers.txt")
with open(output_file, "w") as f:
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#King_{i}\n")

print(f"OK! Saved to {output_file}")
