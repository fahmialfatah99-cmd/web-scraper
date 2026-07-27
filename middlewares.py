import random
from fake_useragent import UserAgent
from scrapy import signals


class StealthMiddleware:
    """Inject stealth headers & bypass basic bot detection."""

    def __init__(self):
        self.ua = UserAgent()

    def process_request(self, request, spider):
        # Set User-Agent yang valid - gunakan browser modern
        request.headers["User-Agent"] = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        )
        request.headers["Accept-Language"] = "en-US,en;q=0.9,id;q=0.8"
        request.headers["Accept"] = (
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"
        )
        request.headers["sec-ch-ua"] = (
            '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"'
        )
        request.headers["sec-ch-ua-mobile"] = "?0"
        request.headers["sec-ch-ua-platform"] = '"Windows"'
        request.headers["sec-fetch-dest"] = "document"
        request.headers["sec-fetch-mode"] = "navigate"
        request.headers["sec-fetch-user"] = "?1"
        request.headers["sec-fetch-site"] = "none"
        request.headers["upgrade-insecure-requests"] = "1"
        
        # Hapus header yang mencurigakan
        request.headers.pop("Scrapy", None)
        request.headers.pop("scrapy", None)
        
        # Set referer jika belum ada
        if "Referer" not in request.headers:
            request.headers["Referer"] = "https://www.google.com/"


class ProxyMiddleware:
    """Rotate proxy per request."""

    def __init__(self, proxies):
        self.proxies = proxies

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist("ROTATING_PROXY_LIST"))

    def process_request(self, request, spider):
        if self.proxies:
            proxy = random.choice(self.proxies)
            request.meta["proxy"] = proxy
            spider.logger.debug(f"Using proxy: {proxy}")
