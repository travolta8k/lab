from telethon import TelegramClient
import re
import os

api_id = int(os.environ.get("TG_API_ID"))
api_hash = os.environ.get("TG_API_HASH")

channels = ['NETMelliAnti', 'Proxy_v2ry', 'V2RootConfigPilot']

client = TelegramClient('session', api_id, api_hash)

async def main():
    all_links = []

    for ch in channels:
        try:
            async for msg in client.iter_messages(ch, limit=50):
                if msg.text:
                    links = re.findall(r'(vmess://\S+|vless://\S+|trojan://\S+)', msg.text, re.I)
                    all_links.extend(links)
        except:
            continue

    all_links = list(dict.fromkeys(all_links))

    with open('server_auto.txt', 'w', encoding='utf-8') as f:
        for i, link in enumerate(all_links, 1):
            f.write(f"{link}#king{i}\n")

with client:
    client.loop.run_until_complete(main())
