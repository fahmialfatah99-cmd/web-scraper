"""
Jalankan: python run.py
UI Interaktif untuk konfigurasi scraper Jobstreet
"""
import os
import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spider import AdvancedSpider


def clear_screen():
    """Bersihkan layar terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """Tampilkan header aplikasi."""
    print("=" * 60)
    print("       JOBSTREET SCRAPER - INTERACTIVE CONFIGURATION")
    print("=" * 60)
    print()


def print_menu(current_config):
    """Tampilkan menu konfigurasi."""
    print("\n--- KONFIGURASI SAAT INI ---")
    for key, value in current_config.items():
        display_value = str(value)
        if len(display_value) > 50:
            display_value = display_value[:47] + "..."
        print(f"  {key}: {display_value}")
    print()
    
    print("--- MENU ---")
    print("  1. Ubah URL Target")
    print("  2. Ubah Mode Headless (True/False)")
    print("  3. Ubah Log Level (INFO/DEBUG/WARNING/ERROR)")
    print("  4. Ubah Download Delay (detik)")
    print("  5. Ubah Concurrent Requests")
    print("  6. Ubah Retry Times")
    print("  7. Atur Proxy (comma-separated)")
    print("  8. Set User Agent Custom")
    print("  9. Reset ke Default")
    print("  0. MULAI SCRAPING")
    print("  q. Keluar")
    print()


def get_input(prompt, default=""):
    """Mendapatkan input dari user dengan nilai default."""
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ").strip()


def get_yes_no(prompt, default=True):
    """Mendapatkan input Yes/No dari user."""
    default_str = "Y/n" if default else "y/N"
    while True:
        user_input = input(f"{prompt} [{default_str}]: ").strip().lower()
        if not user_input:
            return default
        if user_input in ['y', 'yes', 'ya', 'true', '1']:
            return True
        if user_input in ['n', 'no', 'tidak', 'false', '0']:
            return False
        print("Input tidak valid. Masukkan Y atau N.")


def main():
    """Fungsi utama untuk menjalankan UI interaktif."""
    # Konfigurasi default
    config = {
        "TARGET_URL": "https://www.jobstreet.co.id/id/job-search/",
        "HEADLESS": True,
        "LOG_LEVEL": "INFO",
        "DOWNLOAD_DELAY": 3,
        "CONCURRENT_REQUESTS": 1,
        "RETRY_TIMES": 5,
        "PROXIES": [],
        "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    }
    
    running = True
    
    while running:
        clear_screen()
        print_header()
        print_menu(config)
        
        choice = input("Pilih opsi [0-9/q]: ").strip().lower()
        
        if choice == 'q':
            print("\n❌ Program dihentikan. Selamat tinggal!")
            sys.exit(0)
        
        elif choice == '1':
            new_url = get_input("Masukkan URL target baru", config["TARGET_URL"])
            config["TARGET_URL"] = new_url
            print(f"✅ URL diubah menjadi: {new_url}")
        
        elif choice == '2':
            new_headless = get_yes_no("Gunakan mode headless?", config["HEADLESS"])
            config["HEADLESS"] = new_headless
            print(f"✅ Headless diubah menjadi: {new_headless}")
        
        elif choice == '3':
            print("Pilihan Log Level: INFO, DEBUG, WARNING, ERROR")
            new_level = get_input("Masukkan Log Level", config["LOG_LEVEL"]).upper()
            if new_level in ['INFO', 'DEBUG', 'WARNING', 'ERROR']:
                config["LOG_LEVEL"] = new_level
                print(f"✅ Log Level diubah menjadi: {new_level}")
            else:
                print("❌ Log Level tidak valid!")
        
        elif choice == '4':
            try:
                new_delay = float(get_input("Masukkan Download Delay (detik)", str(config["DOWNLOAD_DELAY"])))
                if new_delay >= 0:
                    config["DOWNLOAD_DELAY"] = new_delay
                    print(f"✅ Download Delay diubah menjadi: {new_delay} detik")
                else:
                    print("❌ Delay tidak boleh negatif!")
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        elif choice == '5':
            try:
                new_concurrent = int(get_input("Masukkan Concurrent Requests", str(config["CONCURRENT_REQUESTS"])))
                if new_concurrent >= 1:
                    config["CONCURRENT_REQUESTS"] = new_concurrent
                    print(f"✅ Concurrent Requests diubah menjadi: {new_concurrent}")
                else:
                    print("❌ Concurrent Requests minimal 1!")
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        elif choice == '6':
            try:
                new_retry = int(get_input("Masukkan Retry Times", str(config["RETRY_TIMES"])))
                if new_retry >= 0:
                    config["RETRY_TIMES"] = new_retry
                    print(f"✅ Retry Times diubah menjadi: {new_retry}")
                else:
                    print("❌ Retry Times tidak boleh negatif!")
            except ValueError:
                print("❌ Input harus berupa angka!")
        
        elif choice == '7':
            print("Masukkan daftar proxy dipisahkan koma (contoh: http://user:pass@proxy:port,http://...")
            print("Kosongkan jika tidak menggunakan proxy")
            proxy_input = get_input("Proxy list", ",".join(config["PROXIES"]) if config["PROXIES"] else "")
            if proxy_input.strip():
                config["PROXIES"] = [p.strip() for p in proxy_input.split(",") if p.strip()]
                print(f"✅ Proxy diatur: {len(config['PROXIES'])} proxy(s)")
            else:
                config["PROXIES"] = []
                print("✅ Proxy dihapus (tidak menggunakan proxy)")
        
        elif choice == '8':
            new_ua = get_input("Masukkan User Agent custom", config["USER_AGENT"])
            config["USER_AGENT"] = new_ua
            print(f"✅ User Agent diubah")
        
        elif choice == '9':
            config = {
                "TARGET_URL": "https://www.jobstreet.co.id/id/job-search/",
                "HEADLESS": True,
                "LOG_LEVEL": "INFO",
                "DOWNLOAD_DELAY": 3,
                "CONCURRENT_REQUESTS": 1,
                "RETRY_TIMES": 5,
                "PROXIES": [],
                "USER_AGENT": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
            }
            print("✅ Konfigurasi direset ke default!")
        
        elif choice == '0':
            print("\n" + "=" * 60)
            print("                  KONFIRMASI MULAI")
            print("=" * 60)
            print("\nKonfigurasi yang akan digunakan:")
            for key, value in config.items():
                display_value = str(value)
                if len(display_value) > 50:
                    display_value = display_value[:47] + "..."
                print(f"  {key}: {display_value}")
            print()
            
            confirm = get_yes_no("Apakah Anda yakin ingin memulai scraping?", True)
            
            if confirm:
                print("\n🚀 Memulai scraping...")
                print("-" * 60)
                
                try:
                    # Update spider start_urls
                    AdvancedSpider.start_urls = [config["TARGET_URL"]]
                    
                    # Update custom_settings di spider
                    AdvancedSpider.custom_settings = {
                        "PLAYWRIGHT_LAUNCH_OPTIONS": {
                            "headless": config["HEADLESS"],
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
                            "user_agent": config["USER_AGENT"],
                            "locale": "id-ID",
                            "timezone_id": "Asia/Jakarta",
                            "viewport": {"width": 1920, "height": 1080},
                            "device_scale_factor": 1,
                            "has_touch": False,
                            "is_mobile": False,
                        },
                    }
                    
                    # Setup settings
                    custom_settings = {
                        "PLAYWRIGHT_LAUNCH_OPTIONS": {
                            "headless": config["HEADLESS"],
                            "args": [
                                "--disable-blink-features=AutomationControlled",
                                "--no-sandbox",
                            ],
                        },
                        "LOG_LEVEL": config["LOG_LEVEL"],
                        "DOWNLOAD_DELAY": config["DOWNLOAD_DELAY"],
                        "CONCURRENT_REQUESTS": config["CONCURRENT_REQUESTS"],
                        "RETRY_TIMES": config["RETRY_TIMES"],
                        "ROTATING_PROXY_LIST": config["PROXIES"],
                        "DEFAULT_REQUEST_HEADERS": {
                            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
                            "Accept-Language": "en-US,en;q=0.9,id;q=0.8",
                            "User-Agent": config["USER_AGENT"],
                        },
                    }
                    
                    settings = get_project_settings()
                    settings.update(custom_settings)
                    
                    process = CrawlerProcess(settings)
                    process.crawl(AdvancedSpider)
                    process.start()
                    
                    print("\n" + "=" * 60)
                    print("✅ SCRAPING SELESAI!")
                    print("=" * 60)
                    print("\nHasil disimpan di:")
                    print("  - output.json")
                    print("  - output.csv")
                    print()
                    
                    running = False
                    
                except KeyboardInterrupt:
                    print("\n\n⚠️  Scraping dihentikan oleh user.")
                    sys.exit(0)
                except Exception as e:
                    print(f"\n❌ TERJADI ERROR: {e}")
                    print("\nDetail error:")
                    import traceback
                    traceback.print_exc()
                    sys.exit(1)
            else:
                print("❌ Scraping dibatalkan.")
        
        else:
            print("❌ Opsi tidak valid! Silakan pilih 0-9 atau q.")
        
        # Pause sebentar agar user bisa membaca output
        if choice != '0':
            input("\nTekan ENTER untuk melanjutkan...")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Program dihentikan oleh user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ FATAL ERROR: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
