# 🌐 Gemini Access Guide

### Accessing Google Gemini from Region-Restricted Locations

> A practical, step-by-step guide for accessing **Google Gemini** when your country or region is not available through the normal service configuration.

---

## 📌 Overview

If Google Gemini displays a **country/region restriction error**, this guide walks you through a complete setup using a residential-grade proxy and local Chrome configuration.

The process covers:

- 🌍 Obtaining a residential-grade proxy
- ⚡ Testing proxies for speed and stability
- 🖥️ Configuring a proxy in Windows
- 🔐 Handling proxy authentication
- 🌐 Adjusting Chrome's local region configuration
- 🔄 Preventing Chrome Sync from overwriting the configuration
- ✅ Verifying your public IP
- 🚀 Accessing Gemini
- 🧹 Restoring your normal network configuration

---

## 🧭 Table of Contents

- [Requirements](#-requirements)
- [1--get-a-residential-grade-proxy](#1--get-a-residential-grade-proxy)
- [2--find-the-fastest-proxy](#2--find-the-fastest-proxy)
- [3--configure-the-proxy-in-windows](#3--configure-the-proxy-in-windows)
- [4--authenticate-the-proxy](#4--authenticate-the-proxy)
- [5--modify-chromes-local-state](#5--modify-chromes-local-state)
- [6--disable-chrome-sync](#6--disable-chrome-sync)
- [7--verify-the-proxy](#7--verify-the-proxy)
- [8--access-gemini](#8--access-gemini)
- [9--disable-the-proxy](#9--disable-the-proxy)
- [⚠️ Important Notes](#️-important-notes)
- [🛠️ Troubleshooting](#️-troubleshooting)

---

## 🧰 Requirements

Before starting, make sure you have:

- Windows
- Google Chrome
- A residential-grade proxy
- Proxy username and password
- Python installed
- Internet access

---

# 1 — Get a Residential-Grade Proxy

A residential-grade proxy is required for this setup.

One option mentioned in this guide is **Webshare**.

Visit:

**[https://www.webshare.io/](https://www.webshare.io/)**

Create an account and obtain the available free proxies.

According to the original guide, a new account provides:

- **10 free proxies**
- **1 GB total bandwidth**
- **1-month validity**

### ⚠️ Important

The **1 GB bandwidth is shared across all 10 proxies**.

It is **not 1 GB per proxy**.

---

# 2 — Find the Fastest Proxy

Once you have your proxy list, test them to find the fastest and most stable connection.

The original project uses a Python script for this purpose.

Save the script as:

```text
test_proxy.py
```

Open **Command Prompt**, navigate to the directory containing the script, and run:

```bash
python test_proxy.py
```

The script should return the **top 3 proxies**.

Use the first result as your primary candidate.

Record:

```text
Proxy IP
Proxy Port
Username
Password
```

You'll need these values during the Windows configuration step.

---

# 3 — Configure the Proxy in Windows

Open:

```text
Control Panel
    ↓
Network and Internet
    ↓
Internet Options
    ↓
Connections
    ↓
LAN settings
```

Under **Proxy server**:

1. Enable **Use a proxy server for your LAN**
2. Enter the proxy IP address
3. Enter the proxy port
4. Leave **Bypass proxy for local addresses** unchecked
5. Click **OK**

Example:

```text
Address: 198.105.121.200
Port:    6462
```

> The IP address and port above are examples. Use the credentials provided by your proxy provider.

---

# 4 — Authenticate the Proxy

Open Google Chrome after configuring the proxy.

A **Windows Security** authentication dialog should appear.

Enter the credentials provided by your proxy provider.

```text
Username: <your-proxy-username>
Password: <your-proxy-password>
```

Enable:

```text
Remember my credentials
```

Then click **OK**.

### 🔐 Why is this necessary?

The proxy may appear correctly configured in Windows but still fail to work until its authentication credentials have been supplied.

---

# 5 — Modify Chrome's Local State

> ⚠️ **Important:** Close Chrome completely before editing this file.

Open **Task Manager** and make sure there are no remaining:

```text
chrome.exe
```

processes.

### Open the Local State file

Press:

```text
Win + R
```

Then enter:

```text
%localappdata%\Google\Chrome\User Data\Local State
```

Open the file using Notepad or another text editor.

---

## 🔧 Update Region Configuration

Locate the following settings.

### `is_glic_eligible`

Make sure it is:

```json
"is_glic_eligible": true
```

If the value is:

```json
"is_glic_eligible": false
```

change it to:

```json
"is_glic_eligible": true
```

If the setting does not exist, the original guide recommends adding it near the beginning of the JSON object.

---

### `variations_country`

If you find:

```json
"variations_country": "ir"
```

change the country code to:

```json
"variations_country": "us"
```

If the value is stored as an array, for example:

```json
"variations_country": ["109.0.5414.120", "ir"]
```

preserve the version number and change only the country code:

```json
"variations_country": ["109.0.5414.120", "us"]
```

---

### `variations_permanent_consistency_country`

Apply the same logic here.

If the country is:

```text
ir
```

change it to:

```text
us
```

If the value contains a version number, preserve the version and change only the country code.

---

### 💾 Save

Save the file:

```text
Ctrl + S
```

Then close the editor.

---

# 6 — Disable Chrome Sync

Chrome Sync can potentially restore previously synchronized configuration.

Open Chrome and navigate to:

```text
chrome://settings/syncSetup
```

Disable **Sync**.

This prevents synchronized settings from overwriting the local configuration while testing.

---

# 7 — Verify the Proxy

Before trying Gemini, verify that your traffic is actually going through the proxy.

Open:

```text
https://api.ipify.org
```

The page should display your current public IP address.

### ✅ Working

If the displayed IP matches your configured proxy IP:

```text
Proxy IP
    ↓
api.ipify.org
    ↓
Same IP
```

your proxy is active.

### ❌ Not working

If the page still displays your original public IP, the proxy has not been applied correctly.

Try:

1. Re-authenticating the proxy
2. Checking the Windows proxy configuration
3. Selecting another proxy
4. Running the proxy test script again

---

# 8 — Access Gemini

Once the proxy connection has been verified, open:

```text
https://gemini.google.com/app
```

At this point, the region-related error described in the original guide should no longer appear.

---

# 9 — Disable the Proxy

After you're finished, disable the proxy to return to your normal network connection and avoid unnecessarily consuming proxy bandwidth.

Navigate to:

```text
Control Panel
    ↓
Network and Internet
    ↓
Internet Options
    ↓
Connections
    ↓
LAN settings
```

Disable:

```text
Use a proxy server for your LAN
```

Click:

```text
OK
```

Then restart Chrome.

---

# ⚠️ Important Notes

## 📡 Bandwidth

The free proxy allocation described in this guide provides:

```text
10 proxies
1 GB total bandwidth
1 month validity
```

Remember that the **1 GB is shared across all proxies**.

### Recommended usage

Use the proxy primarily for essential tasks.

Avoid:

- 🎥 Video streaming
- 📦 Large downloads
- 🖼️ Media-heavy websites
- ⬇️ Bandwidth-intensive activity

These can consume the available bandwidth very quickly.

---

## ⚡ Proxy Stability

Free proxies are not guaranteed to remain stable.

A proxy may:

- Become slow
- Stop responding
- Become unavailable
- Provide inconsistent performance

If the selected proxy stops working, test another proxy from your available list.

---

# 🛠️ Troubleshooting

## Gemini still shows a region error

If the proxy is working but Gemini continues displaying a region restriction:

### 1. Clear Google site data

Open:

```text
chrome://settings/siteData
```

Clear relevant Google cookies and site data.

---

### 2. Try Incognito Mode

Open an Incognito window:

```text
Ctrl + Shift + N
```

Then test Gemini again.

This helps eliminate cached browser state as a potential cause.

---

### 3. Check Chrome Sync

Make sure Sync is still disabled:

```text
chrome://settings/syncSetup
```

---

### 4. Verify the public IP again

Open:

```text
https://api.ipify.org
```

Make sure the displayed IP corresponds to the configured proxy.

---

# 🔄 Quick Setup Summary

```text
Get Proxy
    │
    ▼
Test Proxies
    │
    ▼
Select Fastest Proxy
    │
    ▼
Configure Windows Proxy
    │
    ▼
Authenticate
    │
    ▼
Modify Chrome Local State
    │
    ▼
Disable Chrome Sync
    │
    ▼
Verify Public IP
    │
    ▼
Open Gemini
    │
    ▼
Disable Proxy When Finished
```

---

## 📝 Disclaimer

This guide documents a technical configuration for dealing with region-related access issues.

Availability of Google services, proxy services, and regional access can change over time. Always comply with the applicable **terms of service, laws, and policies** in your location and for the services you use.

---

## ⭐ If This Guide Helped

If you found this guide useful, consider:

- ⭐ Starring the repository
- 🐛 Reporting issues
- 💡 Suggesting improvements
- 🔧 Contributing fixes or improvements

---

\<div align="center">

### 🌐 Access • Configure • Verify

**Built as a practical technical guide for region-restricted environments.**

\</div>
