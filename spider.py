import scrapy
from scrapy_playwright.page import PageMethod


class AdvancedSpider(scrapy.Spider):
    name = "advanced"

    # === TARGET URLS - Jobstreet Indonesia ===
    start_urls = ["https://www.jobstreet.co.id/id/job-search/"]
    
    custom_settings = {
        "PLAYWRIGHT_LAUNCH_OPTIONS": {
            "headless": True,
            "args": [
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-web-security",
                "--ignore-certificate-errors",
                "--disable-gpu",
            ],
        },
        "PLAYWRIGHT_CONTEXT_ARGS": {
            "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            "locale": "id-ID",
            "timezone_id": "Asia/Jakarta",
            "viewport": {"width": 1920, "height": 1080},
            "device_scale_factor": 1,
            "has_touch": False,
            "is_mobile": False,
        },
    }
    
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        # Tunggu hingga halaman fully loaded
                        PageMethod("wait_for_load_state", "networkidle", timeout=60000),
                        # Tunggu elemen job card muncul
                        PageMethod("wait_for_selector", "[data-automation='jobTitle']", timeout=30000),
                        # Scroll perlahan untuk trigger lazy load
                        PageMethod("evaluate", "window.scrollTo(0, 500)"),
                        PageMethod("wait_for_timeout", 3000),
                        PageMethod("evaluate", "window.scrollTo(0, 1500)"),
                        PageMethod("wait_for_timeout", 3000),
                        PageMethod("evaluate", "window.scrollTo(0, document.body.scrollHeight)"),
                        PageMethod("wait_for_timeout", 5000),
                    ],
                },
                errback=self.errback_close_page,
            )

    async def parse(self, response):
        page = response.meta.get("playwright_page")
        
        # Ambil content setelah JavaScript selesai render
        if page:
            # Tunggu sebentar untuk memastikan semua konten ter-load
            await page.wait_for_timeout(2000)
            html = await page.content()
            response = scrapy.http.TextResponse(
                url=response.url,
                body=html.encode('utf-8'),
                encoding='utf-8'
            )
            await page.close()

        # === SELECTOR UNTUK JOBSTREET ===
        # Jobstreet menggunakan data-automation attribute untuk job cards
        items = response.css("[data-automation='jobTitle']")

        for item in items:
            # Cari parent container dari job card
            job_card = item.xpath('./ancestor::*[contains(@class, "job-card")][1]')
            
            if job_card:
                title_elem = job_card.css("[data-automation='jobTitle'] ::text").get()
                company_elem = job_card.css("[data-automation='jobCompany'] ::text").get()
                location_elem = job_card.css("[data-automation='jobLocation'] ::text").get()
                salary_elem = job_card.css("[data-automation='jobSalary'] ::text").get()
                link_elem = job_card.css("a[href*='/job/']::attr(href)").get()
                
                yield {
                    "title": title_elem.strip() if title_elem else "",
                    "company": company_elem.strip() if company_elem else "",
                    "location": location_elem.strip() if location_elem else "",
                    "salary": salary_elem.strip() if salary_elem else "",
                    "url": response.urljoin(link_elem) if link_elem else "",
                    "scraped_at": response.url,
                }

        # === PAGINATION - Cari tombol next page ===
        next_page = response.css("a[aria-label='Next Page']::attr(href)").get()
        if not next_page:
            # Alternatif selector untuk pagination
            next_page = response.css("li.pagination-item--active + li a::attr(href)").get()
        
        if next_page and not next_page.startswith('#'):
            self.logger.info(f"Found next page: {next_page}")
            yield scrapy.Request(
                url=response.urljoin(next_page),
                callback=self.parse,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_load_state", "networkidle", timeout=60000),
                        PageMethod("wait_for_selector", "[data-automation='jobTitle']", timeout=30000),
                    ],
                },
                errback=self.errback_close_page,
            )
        else:
            self.logger.info("No more pages found")

    async def errback_close_page(self, failure):
        page = failure.request.meta.get("playwright_page")
        if page:
            try:
                await page.close()
            except:
                pass
        self.logger.error(f"Request failed: {failure.value}")
