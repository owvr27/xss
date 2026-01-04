 LΞX Security Framework

Made by Omar Abdelsalam


# LΞX Security Framework

**LΞX** is a modular **security testing framework** built for **bug bounty hunters**, **penetration testers**, and **security engineers**.

It focuses on **high-signal reconnaissance** and **intelligent XSS detection**, avoiding noisy scanning and false positives.

LΞX is designed with **real-world methodology**, not payload spraying.

---

## 🔥 Core Philosophy

Most security tools fail because they:
- Blindly spray payloads
- Ignore execution context
- Produce false positives
- Miss DOM-based vulnerabilities

**LΞX is different.**

It prioritizes:
- Context awareness
- Verification over guessing
- Manual control where required
- Ethical and authorized testing

---

## 🧠 Architecture Overview

lex-framework/
├── lex.py # Main CLI entry
├── modules/
│ ├── recon/ # Passive recon modules
│ └── xss/
│ ├── scanner.py # Core XSS logic
│ ├── payloads.py # Context-aware payloads
│ ├── context.py # Injection context detection
│ └── verifier.py # Reflection & execution checks
└── extensions/
└── lex-xss-extension/ # Browser-based DOM XSS tester


---

## ✨ Features

### 🔍 Recon Module
- Subdomain enumeration using **subfinder + amass**
- Live host detection with **httpx**
- Clean, deduplicated output
- Passive-first, low-noise methodology

### 🧪 XSS Module
- Reflected XSS detection
- Context-aware injection (HTML / Attribute / JS)
- DOM XSS sink awareness
- Reflection confirmation before reporting
- Designed to reduce false positives

### 🌐 Browser Extension (LΞX XSS Tester)
- Manual, user-initiated DOM XSS testing
- Injects payload **only into the active page**
- Alerts **only on successful execution**
- No background scanning
- Chrome Web Store–safe design

---

## 🖥 Modes

### CLI Mode
Professional, scriptable, tool-style interface.

```bash
./lex.py -u "https://target.com/?q=test" --xss

Example output:

[XSS] html → https://target.com/?q=<svg/onload=alert(1)>

GUI Mode

Visual workflow for recon and testing.

python3 lex_gui.py

    ASCII banner on startup

    Button-based execution

    Organized result output

Browser Extension Mode

Manual DOM XSS testing inside the browser.

    Open the target page

    Click LΞX XSS Tester

    Press Test XSS

    Alert fires only if vulnerability exists

🎯 Supported XSS Types

    Reflected XSS

    Attribute-based XSS

    JavaScript context XSS

    DOM-based XSS (manual verification)

    Event-handler injection

    Stored XSS detection is intentionally limited to avoid unsafe automation.

📁 Output Structure

results/
 └── target.com/
     ├── live_subdomains.txt
     ├── xss_findings.txt
     └── logs/

🛠 Requirements
Core

    Python 3.8+

    requests

Recon Tools

    subfinder

    amass

    httpx

Browser Extension

    Chromium-based browser (Chrome, Edge, Brave)

⚠️ Legal & Ethical Notice

This framework is intended only for authorized security testing.

    Do NOT scan systems you do not own

    Do NOT test without permission

    The browser extension requires manual user interaction

    No automated exploitation is performed

The author is not responsible for misuse.
👤 Author

Omar Abdelsalam

Security Researcher & Tool Developer
🚀 Roadmap

    Playwright-based execution verification

    Payload mutation engine

    Stored XSS tracking queue

    URL & JS crawler integration

    Config-based scanning profiles

    Docker support

    Windows executable release

⭐ Acknowledgment

If you find LΞX useful, consider starring the repository and contributing.

LΞX is built to reflect how real security testing is done — carefully, intelligently, and ethically.


---

