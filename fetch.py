import os
import re
import asyncio
from telethon import TelegramClient

# Telegram API (تو فرستادی)
api_id = 37255161
api_hash = "9417c668138b16b5f1e90265096ac073"

# کانال‌ها
channels = ["NETMelliAnti", "Proxy_v2ry", "V2RootConfigPilot"]

# مسیر فایل‌ها
current_dir = os.path.dirname(os.path.abspath(__file__))
servers_file = os.path.join(current_dir, "servers.txt")
manual_file = os.path.join(current_dir, "server_manual.txt")

# خواندن سرورهای خودت (اولویت بالا)
existing_links = []
existing_numbers = {}  # نگه داشتن شماره هر لینک
if os.path.exists(servers_file):
    with open(servers_file, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                existing_links.append(line)
                # جدا کردن شماره King
                if "#King_" in line:
                    parts = line.rsplit("#King_", 1)
                    existing_numbers[parts[0]] = int(parts[1])

# خواندن لینک‌های دستی
manual_links = []
if os.path.exists(manual_file):
    with open(manual_file, "r") as f:
        manual_links = [line.strip() for line in f if line.strip()]

# تابع گرفتن لینک‌ها از کانال‌ها
async def fetch_channel_links():
    auto_links = []
    client = TelegramClient("session", api_id, api_hash)
    async with client:
        for ch in channels:
            try:
                async for msg in client.iter_messages(ch, limit=300):
                    if msg.text:
                        found = re.findall(r'(vless|vmess|trojan|ss)://[^\s]+', msg.text, re.I)
                        auto_links.extend(found)
                print(f"Fetched {len(auto_links)} from {ch}")
            except Exception as e:
                print(f"Error {ch}: {e}")
    return list(dict.fromkeys(auto_links))

# اجرای اصلی
async def main():
    auto_links = await fetch_channel_links()

    # ترکیب نهایی
    combined_links = existing_links.copy()

    # اضافه کردن لینک‌های دستی اگر نبودند
    for link in manual_links:
        if link not in [l.rsplit("#King_", 1)[0] for l in combined_links]:
            combined_links.append(link)

    # اضافه کردن لینک‌های کانال اگر نبودند
    for link in auto_links:
        if link not in [l.rsplit("#King_", 1)[0] for l in combined_links]:
            combined_links.append(link)

    # شماره‌گذاری
    final_list = []
    current_number = 1
    for line in combined_links:
        base_link = line.rsplit("#King_", 1)[0]
        if base_link in existing_numbers:
            number = existing_numbers[base_link]
        else:
            number = current_number
        final_list.append(f"{base_link}#King_{number}")
        current_number = max(current_number, number + 1)

    # ذخیره
    with open(servers_file, "w") as f:
        for line in final_list:
            f.write(line + "\n")

    print(f"Done! Total links: {len(final_list)}")

asyncio.run(main())
