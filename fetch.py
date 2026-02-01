import requests
import re
import os
import time
from datetime import datetime

channels = [
    "NETMelliAnti",
    "Proxy_v2ry",
    "V2RootConfigPilot"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

servers_file = "servers.txt"
auto_file = "server_manual.txt"

print("GOD MODE Fetch Started...")

auto_links = []

# --- گرفتن لینک از تلگرام وب ---
for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)

        links = re.findall(
            r'(vless|vmess|trojan|ss)://[^\s"\'<>]+',
            r.text,
            re.IGNORECASE
        )

        auto_links.extend(links)
        print(f"{ch}: {len(links)} found")

        time.sleep(1)

    except Exception as e:
        print(f"Channel error {ch}: {e}")

# حذف تکراری
auto_links = list(dict.fromkeys(auto_links))

# پاکسازی لینک خراب
auto_links = [
    link for link in auto_links
    if len(link) > 20 and "://" in link
]

# --- خواندن لینک‌های دستی (اولویت بالا) ---
manual_links = []
if os.path.exists(servers_file):
    with open(servers_file, "r", encoding="utf-8") as f:
        manual_links = [
            line.strip() for line in f
            if line.strip() and not line.startswith("#")
        ]

# --- ذخیره لینک‌های تلگرام جدا ---
with open(auto_file, "w", encoding="utf-8") as f:
    for link in auto_links:
        f.write(link + "\n")

# --- ترکیب نهایی: دستی اول ---
final_links = manual_links + auto_links

# حذف تکراری بین دستی و اتومات
final_links = list(dict.fromkeys(final_links))

# --- زمان ---
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

# --- نوشتن خروجی ---
with open(servers_file, "w", encoding="utf-8") as f:
    f.write(f"# KING GOD MODE — Updated: {now}\n")
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#King_{i}\n")

print(f"GOD MODE DONE ✅ Total: {len(final_links)}")