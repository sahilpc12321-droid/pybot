#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import httpx
import time
import random
import sys
import json
import uuid
import hashlib

# Ensure UTF-8 encoding for Windows console output
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

from urllib.parse import urlparse, parse_qs, urljoin, quote
from colorama import Fore, Style, init
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# ================= DUMMY HTTP HEALTH SERVER FOR FREE CLOUD HOSTING (RENDER/KOYEB) =================
class HealthCheckHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Bot is running 24/7!")
    def log_message(self, format, *args):
        return

def start_health_server():
    port = int(os.environ.get("PORT", 8080))
    server = HTTPServer(('0.0.0.0', port), HealthCheckHandler)
    server.serve_forever()

threading.Thread(target=start_health_server, daemon=True).start()

# Initialize colorama
init(autoreset=True)


# ================= TELEGRAM CONFIG =================
TELEGRAM_BOT_TOKEN = "8992964241:AAH_f6mvARIVioMt-Eox-SaWircDudDiZvQ"  # Apna Telegram Bot Token yahan daalein
TELEGRAM_CHAT_ID = "8392287620"      # Apni Telegram Chat ID yahan daalein

def send_telegram_msg(message):
    """Telegram bot par message bhejne ke liye helper function."""
    if TELEGRAM_BOT_TOKEN == "YOUR_BOT_TOKEN_HERE" or not TELEGRAM_BOT_TOKEN:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        httpx.post(url, json=payload, timeout=10.0)
    except Exception as e:
        print(f"Telegram Alert Failed: {e}", flush=True)

print(f"{Fore.MAGENTA}[BOOT] Initializing Automation Engine Matrix...", flush=True)
send_telegram_msg("🚀 *Automation Engine Matrix Initialized & Running 24/7!*")

# ================= CONFIG =================
WALLETS = {"8739984895": "XM4R"}
FIXED_IP = "45.92.116.221"
PB_BASE = "https://conv.adosiz.net/tracking/postback?event_type=install"
CAMPAIGN_NAME = "Roamiyo2"

# 🌐 SOCKS5 PROXY POOL
SOCKS5_PROXIES = [
   "socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_09416666:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_24469677:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_15612606:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_86964821:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_61039047:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_91073112:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_54527863:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_32784581:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_12238985:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_84812256:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_57199841:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_24827283:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_47123403:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_33536516:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_66625853:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_41499092:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_02809422:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_03669632:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_81887413:5534542@change4.owlproxy.com:7778",
"socks5://2ikqcLmo0m20_custom_zone_IN_st__city_sid_74179526:5534542@change4.owlproxy.com:7778"
]

UA_STRING = "Mozilla/5.0 (Linux; Android 14; 22101320I Build/UKQ1.240624.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/154.0.8037.0 Mobile Safari/537.36"

# ================= IP CHECKER HELPER =================
def get_current_socks_ip(proxy_string):
    if not proxy_string:
        return "Direct", False
    try:
        with httpx.Client(proxy=proxy_string, timeout=12.0) as client:
            res = client.get("https://httpbin.org/ip")
            if res.status_code == 200:
                return res.json().get("origin", "Unknown IP"), True
    except Exception as e:
        return f"Connection Failed ({type(e).__name__})", False
    return "Unknown IP", False

def realtime_countdown(seconds, label_text, text_color=Fore.YELLOW):
    for remaining in range(seconds, 0, -1):
        print(f"⌛ [{label_text}] Time Remaining: {remaining:03d}s", flush=True)
        time.sleep(1)

# ================= GENERATE FINGERPRINT =================
def generate_fingerprint_data(socks_ip=None):
    fp_data = {
        "ua": UA_STRING,
        "uaData": {
            "brands": [
                {"brand": "Chromium", "version": "154"},
                {"brand": "Android WebView", "version": "154"},
                {"brand": "Not A(Brand", "version": "99"}
            ],
            "mobile": True,
            "platform": "Android"
        },
        "platform": "Linux aarch64",
        "vendor": "Google Inc.",
        "language": "en-IN",
        "languages": ["en-IN", "en-US"],
        "cookieEnabled": True,
        "doNotTrack": None,
        "hardwareConcurrency": 8,
        "deviceMemory": 8,
        "maxTouchPoints": 5,
        "pdfViewerEnabled": False,
        "webdriver": False,
        "plugins": [],
        "mimeTypes": [],
        "screen": {
            "w": random.choice([393, 360, 412]),
            "h": random.choice([873, 800, 915]),
            "aw": random.choice([393, 360, 412]),
            "ah": random.choice([873, 800, 915]),
            "depth": 24,
            "pixelDepth": 24,
            "dpr": random.choice([2.75, 3.0, 2.625]),
            "orientation": "portrait-primary"
        },
        "viewport": {
            "w": 392,
            "h": 701,
            "outerW": 393,
            "outerH": 702
        },
        "timezone": "Asia/Calcutta",
        "timezoneOffset": -330,
        "dateLocale": "en-IN",
        "connection": {
            "effectiveType": "4g",
            "downlink": round(random.uniform(5.0, 15.0), 1),
            "rtt": random.choice([0, 50, 100]),
            "saveData": False,
            "type": "cellular"
        },
        "storageQuota": {
            "usage": 0,
            "quota": 10737418240
        },
        "webgl": {
            "vendor": "Qualcomm",
            "renderer": "Adreno (TM) 642L",
            "version": "WebGL 1.0 (OpenGL ES 2.0 Chromium)",
            "shading": "WebGL GLSL ES 1.0 (OpenGL ES GLSL ES 1.0 Chromium)",
            "maxTextureSize": 8192
        },
        "canvasHash": hashlib.md5(str(uuid.uuid4()).encode()).hexdigest()[:8],
        "audioHash": "pending",
        "touch": {
            "ontouchstart": True,
            "maxTouchPoints": 5
        },
        "page": {
            "title": f"{CAMPAIGN_NAME} - INRFlash",
            "characterSet": "UTF-8",
            "contentType": "text/html",
            "readyState": "loading",
            "url": f"https://offers.inrflash.com/camp.php?ref=XM4R&camp={CAMPAIGN_NAME}",
            "referrer": ""
        },
        "perf": {
            "navigationStart": int(time.time() * 1000),
            "domLoading": int(time.time() * 1000) + 3000,
            "loadEventEnd": 0
        },
        "automation": {
            "webdriver": False,
            "hasChrome": False,
            "hasPhantom": False,
            "hasSelenium": False,
            "hasNightmare": False,
            "hasPuppeteer": False
        },
        "window": {
            "iframe": False,
            "focused": True,
            "visibility": "visible"
        },
        "localIps": ["10.1.10.1", socks_ip],
        "collectedAt": time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime()),
        "battery": {
            "charging": random.choice([True, False]),
            "level": round(random.uniform(0.2, 0.9), 2),
            "chargingTime": None,
            "dischargingTime": None
        }
    }
    return fp_data

def generate_fb_data():
    now = int(time.time() * 1000)
    key_delay = random.randint(2000, 6000)
    fb_data = {
        "loadedAt": now,
        "keystrokes": random.randint(1, 3),
        "keyDurations": [random.randint(5, 15)],
        "firstKeyAt": now + key_delay,
        "lastKeyAt": now + key_delay + random.randint(100, 500),
        "mouseMoves": random.randint(1, 5),
        "clicks": random.randint(1, 3),
        "touchStarts": random.randint(1, 3),
        "scrolls": random.randint(0, 2),
        "focuses": random.randint(1, 2),
        "blurs": random.randint(0, 2),
        "visibilityChanges": 0,
        "pasted": False,
        "autofilled": random.choice([True, False]),
        "submittedAt": now + key_delay + random.randint(500, 1500),
        "fillToSubmitMs": random.randint(300, 800),
        "totalOnPageMs": random.randint(4000, 6000)
    }
    return fb_data

# ================= REDIRECT CAPTURE =================
def generate_publisher(wallet, proxy=None, socks_ip=None):
    ref = WALLETS[wallet]
    camp = CAMPAIGN_NAME
    url = f"https://offers.inrflash.com/camp.php?ref={ref}&camp={camp}"

    print(f"{Fore.YELLOW}[CONNECT] Requesting Campaign Portal: {url}", flush=True)

    headers = {
        "sec-ch-ua": '"Chromium";v="154", "Android WebView";v="154", "Not A(Brand";v="99"',
        "sec-ch-ua-mobile": "?1",
        "sec-ch-ua-platform": '"Android"',
        "Upgrade-Insecure-Requests": "1",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": UA_STRING,
        "Origin": "https://offers.inrflash.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "X-Requested-With": "mark.via.gq",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": url,
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-IN,en-US;q=0.9,en;q=0.8",
        "Priority": "u=0, i"
    }

    fp_data = generate_fingerprint_data(socks_ip=socks_ip)
    fb_data = generate_fb_data()

    post_data = {
        "_fp": json.dumps(fp_data, separators=(',', ':')),
        "_fb": json.dumps(fb_data, separators=(',', ':')),
        "wallet_number": wallet
    }

    try:
        with httpx.Client(timeout=15.0, proxy=proxy, follow_redirects=False) as client:
            r = client.post(url, headers=headers, data=post_data)
            print(f"{get_color_by_status(r.status_code)}[SERVER] Received Status Code: {r.status_code}", flush=True)

            if r.status_code == 302:
                location = r.headers.get("Location")
                print(f"{Fore.GREEN}Redirect captured → {location}", flush=True)
                return location
            elif r.status_code == 200:
                if "location" in r.text.lower():
                    print(f"{Fore.YELLOW}[!] Found location in body", flush=True)
    except Exception as e:
        print(f"{Fore.RED}Publisher error: {type(e).__name__}: {e}", flush=True)
        send_telegram_msg(f"⚠️ *Publisher Error:* `{type(e).__name__}`")
    return None

def get_color_by_status(code):
    if code == 200: return Fore.GREEN
    if code in (301, 302): return Fore.CYAN
    return Fore.RED

# ================= CLICKID EXTRACTOR =================
def extract_click_id(url):
    if not url:
        return None
    decoded_url = url.replace("%24", "$")
    parsed = urlparse(decoded_url)
    params = parse_qs(parsed.query)

    if "cl" in params:
        return params["cl"][0]

    for key in params:
        if key.lower() == "cl":
            return params[key][0]

    return None

def get_clickid(start_url, proxy=None):
    headers = {"User-Agent": UA_STRING}
    visited = set()
    try:
        with httpx.Client(timeout=15.0, proxy=proxy, follow_redirects=False) as client:
            current_url = start_url
            for hop in range(15):
                if current_url in visited:
                    break
                visited.add(current_url)

                print(f"{Fore.CYAN}[HOP {hop+1}] Checking: {current_url[:100]}...", flush=True)

                cid = extract_click_id(current_url)
                if cid:
                    print(f"{Fore.GREEN}[FOUND] ClickID: {cid}...", flush=True)
                    return cid

                r = client.get(current_url, headers=headers)
                print(f"{Fore.YELLOW}  Status: {r.status_code}", flush=True)

                if r.status_code in (301, 302, 303, 307, 308):
                    loc = r.headers.get("Location")
                    if loc:
                        current_url = urljoin(current_url, loc)
                        cid = extract_click_id(current_url)
                        if cid:
                            print(f"{Fore.GREEN}[FOUND] ClickID from redirect: {cid}", flush=True)
                            return cid
                        continue

                import re
                meta_match = re.search(r']+http-equiv=["\']refresh["\'][^>]+content=["\'][^"]*url=([^"\']+)', r.text, re.I)
                if meta_match:
                    current_url = urljoin(current_url, meta_match.group(1))
                    cid = extract_click_id(current_url)
                    if cid:
                        print(f"{Fore.GREEN}[FOUND] ClickID from meta refresh: {cid}", flush=True)
                        return cid
                    continue

                js_match = re.search(r'window\.location\.(?:replace|href)\s*=\s*["\']([^"\']+)["\']', r.text, re.I)
                if js_match:
                    current_url = urljoin(current_url, js_match.group(1))
                    cid = extract_click_id(current_url)
                    if cid:
                        print(f"{Fore.GREEN}[FOUND] ClickID from JS redirect: {cid}", flush=True)
                        return cid
                    continue

                applink_match = re.search(r'(https://cl-6degreedigital\.adosiz\.net/[^\s"\']+)', r.text)
                if applink_match:
                    cid = extract_click_id(applink_match.group(1))
                    if cid:
                        print(f"{Fore.GREEN}[FOUND] ClickID from app.link: {cid}", flush=True)
                        return cid

                break
    except Exception as e:
        print(f"{Fore.RED}Redirect Hop Error encountered: {type(e).__name__}: {e}", flush=True)
    return None

# ================= POSTBACK =================
def retry_fire_pb(click_id, event_id, goal_label, proxy=None):
    url = f"{PB_BASE}&click_id={click_id}"
    print(f"{Fore.BLUE}[POSTBACK] Firing {goal_label} (event_id={event_id})", flush=True)
    print(f"{Fore.BLUE}[POSTBACK] URL: {url[:100]}...", flush=True)

    for attempt in range(3):
        try:
            with httpx.Client(timeout=20.0, proxy=proxy) as client:
                headers = {"User-Agent": UA_STRING}
                response = client.get(url, headers=headers)
                print(f"{Fore.MAGENTA}[PB] Status Code: {response.status_code}", flush=True)

                if response.status_code == 200:
                    print(f"{Fore.GREEN}✅ {goal_label} (event_id={event_id}) Success", flush=True)
                    msg = f"✅ *Postback Success!*\n\n🎯 *Event:* `{goal_label}`\n🆔 *ClickID:* `{click_id}`\n📡 *Status:* `200 OK`"
                    send_telegram_msg(msg)
                    return True
                else:
                    print(f"{Fore.YELLOW}⚠️ {goal_label} Status: {response.status_code}", flush=True)
        except Exception as e:
            print(f"{Fore.RED}Postback Attempt {attempt+1} Warning: {type(e).__name__}", flush=True)
        time.sleep(4)
    
    send_telegram_msg(f"❌ *Postback Failed!*\n🎯 *Event:* `{goal_label}`\n🆔 *ClickID:* `{click_id}`")
    return False

# ================= MAIN LOOP =================
wallet_index = 0
print(f"{Fore.GREEN}[READY] Entering persistent runtime loop engine...\n", flush=True)

while True:
    wallet = list(WALLETS.keys())[wallet_index]
    wallet_index = (wallet_index + 1) % len(WALLETS)

    print(f"\n{Fore.MAGENTA}=== STARTING SESSION: Wallet {wallet} ===", flush=True)

    chosen_socks = random.choice(SOCKS5_PROXIES) if SOCKS5_PROXIES else None
    print(f"{Fore.BLUE}[PROXY] Connecting to Selected SOCKS5 Node...", flush=True)
    live_ip, proxy_healthy = get_current_socks_ip(chosen_socks)

    if proxy_healthy:
        print(f"{Fore.BLUE}[PROXY] Active SOCKS5 IP Address -> {Fore.WHITE}{live_ip}", flush=True)
        active_proxy = chosen_socks
    else:
        print(f"{Fore.RED}[⚠️] Selected SOCKS5 Node Failed: {live_ip}", flush=True)
        print(f"{Fore.YELLOW}[⚠️] Switching loop routing context to Direct Clean Network IP...", flush=True)
        active_proxy = None
        live_ip = FIXED_IP

    start_url = generate_publisher(wallet, proxy=active_proxy, socks_ip=live_ip)
    if not start_url:
        print(f"{Fore.RED}[-] Step failed. Re-executing wallet loop...", flush=True)
        continue

    active_id = get_clickid(start_url, proxy=active_proxy)
    if not active_id:
        print(f"{Fore.RED}[-] Extraction failed. Re-executing wallet loop...", flush=True)
        continue

    print(f"{Fore.GREEN}[SUCCESS] ClickID: {active_id[:60]}...", flush=True)

    for event_id in range(1):
        wait = random.randint(60, 90) if event_id == 0 else random.randint(5, 10)
        realtime_countdown(wait, f"Delaying for event_id={event_id}")

        print(f"{Fore.CYAN}[ACTION] Firing event_id={event_id} now!", flush=True)
        retry_fire_pb(active_id, event_id, f"EVENT_{event_id}", proxy=active_proxy)

    session_delay = random.randint(40, 80)
    realtime_countdown(session_delay, "Global Session Cooldown Matrix", Fore.MAGENTA)
