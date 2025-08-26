from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_dashboard_up():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--ignore-certificate-errors")
    d = webdriver.Chrome(options=opts)
    try:
        d.get("https://localhost:443")
        assert d.title is not None
    finally:
        d.quit()
