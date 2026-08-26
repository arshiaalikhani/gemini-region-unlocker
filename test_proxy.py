import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# ====================================================
#  USER CONFIGURATION - EDIT THESE VALUES
# ====================================================

# 1. Enter your Webshare username and password
USERNAME = "your_username_here"   # <-- ENTER YOUR USERNAME
PASSWORD = "your_password_here"   # <-- ENTER YOUR PASSWORD

# 2. Add your proxy IP:port pairs in the list below
#    Format: ("IP_ADDRESS", PORT_NUMBER)
#    Example: ("198.105.121.200", 6462)
proxy_list = [
    # ("ENTER_IP_HERE", ENTER_PORT_HERE),   # <-- ADD YOUR PROXIES HERE
]

# ====================================================

def test_proxy(ip, port):
    proxy_url = f"http://{USERNAME}:{PASSWORD}@{ip}:{port}"
    proxies = {
        "http": proxy_url,
        "https": proxy_url,
    }
    try:
        start = time.time()
        response = requests.get("https://api.ipify.org", proxies=proxies, timeout=10)
        elapsed = time.time() - start
        if response.status_code == 200:
            return (ip, port, response.text.strip(), elapsed)
    except Exception:
        pass
    return (ip, port, None, None)

# ====================================================
#  DO NOT EDIT BELOW THIS LINE
# ====================================================

if USERNAME == "your_username_here" or PASSWORD == "your_password_here":
    print("❌ ERROR: Please set your Webshare username and password in the script.")
    exit(1)

if not proxy_list:
    print("❌ ERROR: proxy_list is empty. Please add your proxies.")
    print("   Format: (\"IP_ADDRESS\", PORT_NUMBER)")
    print("   Example: (\"198.105.121.200\", 6462)")
    exit(1)

working_proxies = []
print("🔍 Testing proxies, please wait...\n")

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(test_proxy, ip, port): (ip, port) for ip, port in proxy_list}
    for future in as_completed(futures):
        ip, port, result_ip, delay = future.result()
        if result_ip:
            working_proxies.append((ip, port, result_ip, delay))
            print(f"✅ [OK] {ip}:{port} -> Output IP: {result_ip} (Response Time: {delay:.2f}s)")
        else:
            print(f"❌ [FAIL] {ip}:{port} is not working.")

best_proxies = sorted(working_proxies, key=lambda x: x[3])

print("\n" + "="*50)
print("🏆 TOP 3 FASTEST WORKING PROXIES:")
for i, (ip, port, result_ip, delay) in enumerate(best_proxies[:3], 1):
    print(f"   #{i} {ip}:{port} | IP: {result_ip} | Speed: {delay:.2f}s")
