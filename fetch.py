import requests
import re
import os

# لیست کانال‌ها
channels = ["NETMelliAnti", "Proxy_v2ry", "V2RootConfigPilot"]
headers = {"User-Agent": "Mozilla/5.0"}
all_links = []

# مسیر فایل‌ها همان مسیر فعلی باقی می‌ماند
servers_file = "servers.txt"        # لینک‌های خودتونی
manual_file = "server_manual.txt"   # لینک‌های اتوماتیک

# خواندن لینک‌های خودتونی
custom_links = []
if os.path.exists(servers_file):
    with open(servers_file, "r") as f:
        custom_links = [line.strip() for line in f if line.strip()]

print("Searching for links from channels...")

for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)
        links = re.findall(r'(vless|vmess|trojan|ss)://[^\s"<]+', r.text, re.I)
        all_links.extend(links)
        print(f"Done: {ch}, found {len(links)} links")
    except Exception as e:
        print(f"Error on {ch}: {e}")

# خواندن لینک‌های اتوماتیک قبلی
manual_links = []
if os.path.exists(manual_file):
    with open(manual_file, "r") as f:
        manual_links = [line.strip() for line in f if line.strip()]

# ترکیب لینک‌ها و حذف تکراری‌ها
new_links = list(dict.fromkeys(all_links + manual_links))
new_links = [l for l in new_links if l not in custom_links]

# ترکیب نهایی: خودتونی + اتوماتیک
final_links = custom_links + new_links

# ذخیره در servers.txt
with open(servers_file, "w") as f:
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#King_{i}\n")

print(f"Update Finished. Total links: {len(final_links)}")
