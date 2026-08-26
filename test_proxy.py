import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

# List of proxies from your Webshare dashboard
proxy_list = [
    ("31.59.20.176", 6754),
    ("45.38.107.97", 6014),
    ("198.105.121.200", 6462),
    ("64.137.96.74", 6641),
    ("198.23.243.226", 6361),
    ("38.154.185.97", 6370),
    ("84.247.60.125", 6095),
    ("142.111.67.146", 5611),
    ("191.96.254.138", 6185),
    ("31.58.9.4", 6077),
]

USERNAME = "rfjfhzjr"
PASSWORD = "0fazklyp5yh8"

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

working_proxies = []
print("Testing proxies, please wait...")

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(test_proxy, ip, port): (ip, port) for ip, port in proxy_list}
    for future in as_completed(futures):
        ip, port, result_ip, delay = future.result()
        if result_ip:
            working_proxies.append((ip, port, result_ip, delay))
            print(f"[OK] {ip}:{port} -> Output IP: {result_ip} (Response Time: {delay:.2f}s)")
        else:
            print(f"[FAIL] {ip}:{port} is not working.")

# Sort by speed (fastest first)
best_proxies = sorted(working_proxies, key=lambda x: x[3])

print("\n" + "="*50)
print("TOP 3 FASTEST WORKING PROXIES:")
for ip, port, result_ip, delay in best_proxies[:3]:
    print(f"   {ip}:{port} | IP: {result_ip} | Speed: {delay:.2f}s")