import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
from .payloads import PAYLOADS
from .context import detect_context

HEADERS = {"User-Agent": "LΞX-XSS"}

def inject(url, params, payload):
    q = {p: payload for p in params}
    parsed = urlparse(url)
    return urlunparse(parsed._replace(query=urlencode(q, doseq=True)))

def scan_xss(url):
    parsed = urlparse(url)
    params = parse_qs(parsed.query)
    if not params:
        return []

    findings = []

    for ctx, payloads in PAYLOADS.items():
        for payload in payloads:
            test_url = inject(url, params, payload)
            r = requests.get(test_url, headers=HEADERS, timeout=10)

            detected = detect_context(r.text, payload)
            if detected:
                findings.append({
                    "url": test_url,
                    "context": detected
                })

    return findings
