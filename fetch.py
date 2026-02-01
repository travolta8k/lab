import requests
import re
import time

channels = [
    "NETMelliAnti",
    "Proxy_v2ry",
    "V2RootConfigPilot"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

all_links = []

for ch in channels:
    try:
        url = f"https://t.me/s/{ch}"
        r = requests.get(url, headers=headers, timeout=20)
        html = r.text
        links = re.findall(r'(vmess://\S+|vless://\S+|trojan://\S+)', html, re.I)
        all_links.extend(links)
        time.sleep(2)
    except Exception as e:
        print("Error on", ch, e)

all_links = list(dict.fromkeys(all_links))

manual_links = []
try:
    with open("server_manual.txt") as f:
        manual_links = [line.strip() for line in f if line.strip()]
except:
    pass

final_links = manual_links + all_links

with open("servers.txt", "w") as f:
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#king{i}\n")

print("OK — servers.txt updated")
