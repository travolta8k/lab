cat > fetch.py << 'EOF'
import requests
import re

channels = [
    "NETMelliAnti",
    "Proxy_v2ry",
    "V2RootConfigPilot"
]

all_links = []

for ch in channels:
    url = f"https://t.me/s/{ch}"
    html = requests.get(url, timeout=15).text
    
    links = re.findall(r'(vmess://\S+|vless://\S+|trojan://\S+)', html, re.I)
    all_links.extend(links)

# حذف تکراری
all_links = list(dict.fromkeys(all_links))

# خواندن دستی
manual_links = []
try:
    with open("server_manual.txt") as f:
        manual_links = [line.strip() for line in f if line.strip()]
except:
    pass

final_links = manual_links + all_links

# ذخیره خروجی
with open("servers.txt", "w") as f:
    for i, link in enumerate(final_links, 1):
        f.write(f"{link}#king{i}\n")

print("Done. servers.txt updated.")
EOF
