# Advanced Web Scraper with Playwright & Scrapy

A powerful web scraping framework built with **Scrapy** and **Playwright** for handling JavaScript-heavy websites, infinite scroll, lazy-loaded content, and anti-bot detection.

## Features

- 🚀 **Playwright Integration** - Render JavaScript-heavy pages
- 🔄 **Infinite Scroll Support** - Auto-scroll to load dynamic content
- 🛡️ **Anti-Bot Detection** - Stealth headers, user-agent rotation
- 🌐 **Proxy Rotation** - Built-in proxy support for distributed requests
- 📊 **Multi-format Output** - Export to JSON and CSV automatically
- ⚙️ **Configurable Settings** - Easy customization via `settings.py`

## Requirements

- Python 3.8+
- Playwright browsers (Chromium)

## Installation

```bash
# Create and activate virtual environment (recommended)
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Install Playwright browser (Chromium)
playwright install chromium
```

## Project Structure

```
├── run.py              # Entry point to run the spider
├── spider.py           # Main spider logic (customize selectors here)
├── settings.py         # Scrapy configuration (proxies, delays, etc.)
├── middlewares.py      # Stealth & proxy middleware
├── pipelines.py        # Data export pipeline (JSON/CSV)
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## Quick Start

### 1. Configure Your Target

Edit `spider.py` to set your target URLs and CSS selectors:

```python
# spider.py
start_urls = ["https://your-target-site.com"]

# In parse() method, update selectors:
items = response.css("div.product")  # Change to match your target
yield {
    "title": item.css("h2::text").get(default="").strip(),
    "price": item.css("span.price::text").get(default="").strip(),
    # Add more fields as needed
}
```

### 2. Configure Settings (Optional)

Edit `settings.py` to customize:

- **Proxy list**: Add residential proxies in `ROTATING_PROXY_LIST`
- **Download delay**: Adjust `DOWNLOAD_DELAY` to avoid rate limiting
- **Concurrency**: Set `CONCURRENT_REQUESTS` based on your needs
- **Browser options**: Configure headless mode and browser arguments

### 3. Run the Spider

```bash
python run.py
```

### 4. Check Output

Scraped data will be saved to:
- `output.json` - JSON format
- `output.csv` - CSV format

## Configuration Options

### Anti-Bot Settings (`settings.py`)

| Setting | Default | Description |
|---------|---------|-------------|
| `CONCURRENT_REQUESTS` | 4 | Max concurrent requests |
| `DOWNLOAD_DELAY` | 2 | Delay between requests (seconds) |
| `RANDOMIZE_DOWNLOAD_DELAY` | True | Randomize delay to avoid detection |
| `COOKIES_ENABLED` | True | Enable cookie handling |
| `ROBOTSTXT_OBEY` | False | Ignore robots.txt (use responsibly) |
| `RETRY_TIMES` | 3 | Number of retries on failure |

### Proxy Configuration

Add your proxies in `settings.py`:

```python
ROTATING_PROXY_LIST = [
    "http://user:pass@proxy1:port",
    "http://user:pass@proxy2:port",
]
```

### Custom Selectors

Update these in `spider.py`:

```python
# Item selector
items = response.css("div.item")

# Field selectors
"title": item.css("h2::text").get()
"price": item.css("span.price::text").get()
"url": item.css("a::attr(href)").get()

# Pagination selector
next_page = response.css("a.next::attr(href)").get()
```

## Troubleshooting

### Common Issues

**1. Empty output**
- Verify your CSS selectors match the target site
- Check if the site requires login or has CAPTCHA
- Increase `wait_for_timeout` in spider methods

**2. Request failures / timeouts**
- Add valid proxies to `ROTATING_PROXY_LIST`
- Increase `PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT`
- Reduce `CONCURRENT_REQUESTS`

**3. Bot detection**
- Ensure `StealthMiddleware` is enabled
- Use residential proxies
- Increase `DOWNLOAD_DELAY`

### Debug Mode

Enable debug logging in `run.py`:

```python
custom = {
    "LOG_LEVEL": "DEBUG",  # Change from INFO to DEBUG
}
```

## Best Practices

1. **Respect robots.txt** - Set `ROBOTSTXT_OBEY = True` for ethical scraping
2. **Rate limiting** - Use appropriate delays to avoid overwhelming servers
3. **User-Agent rotation** - Already enabled via `fake-useragent`
4. **Error handling** - Check logs for failed requests
5. **Test incrementally** - Start with a few pages before scaling

## License

MIT License - Feel free to use and modify for your projects.

## Disclaimer

Use this tool responsibly and ethically. Always comply with:
- Website terms of service
- Applicable laws and regulations
- Rate limits and server capacity
- Data privacy requirements
