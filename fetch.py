import requests
import re
import os

# لیست کانال‌ها
channels = ["NETMelliAnti", "Proxy_v2ry", "V2RootConfigPilot"]
headers = {"User-Agent": "Mozilla/5.0"}
all_links = []

print("Searching for links...")

for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)
        # استخراج لینک‌ها
        links = re.findall(r'(vless|vmess|trojan|ss)://[^\s"<]+', r.text, re.I)
        all_links.extend(links)
        print(f"Done: {ch}")
    except Exception as e:
        print(f"Error on {ch}: {e}")

# حذف تکراری‌ها و ذخیره
all_links = list(dict.fromkeys(all_links))

with open("servers.txt", "w") as f:
    for i, link in enumerate(all_links, 1):
        f.write(f"{link}#King_{i}\n")

print(f"Finished! Total: {len(all_links)}")
