import ssl, urllib.request, sys
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
try:
    with urllib.request.urlopen("https://localhost:443", context=ctx, timeout=30) as r:
        print("OK", r.status)
except Exception as e:
    print("FAIL", e)
    sys.exit(1)
