BOT_NAME = "advanced_scraper"

SPIDER_MODULES = ["."]
NEWSPIDER_MODULE = "."

# === PLAYWRIGHT ===
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    "args": [
        "--disable-blink-features=AutomationControlled",
        "--no-sandbox",
    ],
}
PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30000

# === PROXY ROTATION ===
ROTATING_PROXY_LIST = [
    "http://user:pass@proxy1:port",
    "http://user:pass@proxy2:port",
    # Tambahkan proxy residential di sini
]

# === ANTI-BLOCKING ===
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 3
RANDOMIZE_DOWNLOAD_DELAY = True
COOKIES_ENABLED = True
ROBOTSTXT_OBEY = False
RETRY_TIMES = 5
RETRY_HTTP_CODES = [403, 429, 500, 502, 503, 504]

# Disable default headers that might reveal bot
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
}

DOWNLOADER_MIDDLEWARES = {
    "scrapy.downloadermiddlewares.useragent.UserAgentMiddleware": None,
    "middlewares.StealthMiddleware": 540,
    "middlewares.ProxyMiddleware": 550,
}

ITEM_PIPELINES = {
    "pipelines.DataPipeline": 300,
}
