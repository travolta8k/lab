import requests
import re
import time
import os

# لیست کانال‌ها
channels = [
    "NETMelliAnti",
    "Proxy_v2ry",
    "V2RootConfigPilot"
]

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
all_links = []

print("Searching for links...")

for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)
        # استخراج هوشمند لینک‌ها
        links = re.findall(r'(vless|vmess|trojan|ss)://[^\s"<]+', r.text, re.I)
        all_links.extend(links)
        print(f"Done: {ch} | Found: {len(links)}")
        time.sleep(1)
    except Exception as e:
        print(f"Error on {ch}: {e}")

# حذف تکراری‌ها
all_links = list(dict.fromkeys(all_links))

# خواندن لینک‌های دستی (چون فایل در صفحه‌ی اصلی است)
manual_links = []
if os.path.exists("server_manual.txt"):
    with open("server_manual.txt", "r") as f:
        manual_links = [line.strip() for line in f if line.strip()]

final_links = manual_links + all_links

# ذخیره در فایل servers.txt در صفحه‌ی اصلی
with open("servers.txt", "w") as f:
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#King_{i}\n")

print(f"Finished! Total servers: {len(final_links)}")
