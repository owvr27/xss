from modules.xss.scanner import scan_xss

if args.xss:
    results = scan_xss(args.url)
    for r in results:
        print(f"[XSS] {r['context']} → {r['url']}")
