from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import time
import os
import sys
import subprocess
from pathlib import Path

# Import configuration
try:
    from config import *
except ImportError:
    print("❌ Configuration file not found. Using default values.")
    print("   Please create config.py or update values in this script.")
    # Fallback configuration
    EMAIL = "siraj.workstation@gmail.com"
    PASSWORD = "password"
    DEPARTURE_ADDRESS = "Hammam Sousse"
    ARRIVAL_ADDRESS = "Sousse Centre Ville"
    CHROME_PROFILE_PATH = "/tmp/SeleniumProfile"
    HEADLESS_MODE = False
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 20
    LOGIN_TIMEOUT = 15
    ENABLE_DEBUG_LOGS = True
    SCREENSHOT_ON_ERROR = False
    TARGET_URL = "https://mobile.thunder.webify.pro/#/client"

# ==== CHROME SETUP ====
options = Options()
# Create profile directory if it doesn't exist
os.makedirs(CHROME_PROFILE_PATH, exist_ok=True)

options.add_argument(f"--user-data-dir={CHROME_PROFILE_PATH}")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--no-sandbox")  # Required for Linux in many environments
options.add_argument("--disable-dev-shm-usage")  # Required for Linux in many environments
options.add_argument("--disable-gpu")  # Good for headless environments
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

# Enable headless mode if configured
if HEADLESS_MODE:
    options.add_argument("--headless")

def initialize_webdriver():
    """Initialize Chrome WebDriver with fallback options"""
    chrome_options = [
        None,  # Let webdriver-manager handle it
        '/usr/bin/chromedriver',  # Common system location
        '/usr/local/bin/chromedriver',  # Alternative system location
        str(Path.home() / '.local' / 'bin' / 'chromedriver'),  # User installation
    ]
    
    for chrome_path in chrome_options:
        try:
            if chrome_path is None:
                # Try webdriver-manager first
                service = Service(ChromeDriverManager().install())
            else:
                # Try specific path
                if not os.path.exists(chrome_path):
                    continue
                service = Service(chrome_path)
            
            driver = webdriver.Chrome(service=service, options=options)
            # Execute script to prevent detection
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            return driver
            
        except Exception as e:
            if ENABLE_DEBUG_LOGS:
                print(f"⚠️ Failed with ChromeDriver path {chrome_path}: {e}")
            continue
    
    # If all fails, try to install via apt
    print("📦 Attempting to install ChromeDriver via package manager...")
    try:
        subprocess.run(['sudo', 'apt', 'install', '-y', 'chromium-chromedriver'], 
                      check=True, capture_output=True)
        driver = webdriver.Chrome(service=Service('/usr/bin/chromedriver'), options=options)
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        if ENABLE_DEBUG_LOGS:
            print(f"❌ Package manager installation failed: {e}")
    
    raise Exception("Could not initialize ChromeDriver. Please install manually.")

try:
    driver = initialize_webdriver()
    wait = WebDriverWait(driver, PAGE_LOAD_TIMEOUT)
    print("🚀 Chrome WebDriver initialized successfully.")
except Exception as e:
    print(f"❌ Failed to initialize WebDriver: {e}")
    print("💡 Try running: sudo apt install chromium-chromedriver")
    sys.exit(1)

def safe_click(xpath, description, timeout=None):
    """Safely click an element with error handling"""
    if timeout is None:
        timeout = DEFAULT_TIMEOUT
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small delay after scrolling
        element.click()
        if ENABLE_DEBUG_LOGS:
            print(f"✅ {description} clicked successfully.")
        return True
    except TimeoutException:
        if ENABLE_DEBUG_LOGS:
            print(f"⏰ Timeout waiting for {description} to be clickable")
        return False
    except Exception as e:
        if ENABLE_DEBUG_LOGS:
            print(f"❌ Failed to click {description}: {e}")
        return False

def safe_input(xpath, value, description, timeout=None):
    """Safely input text into an element"""
    if timeout is None:
        timeout = DEFAULT_TIMEOUT
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)  # Small delay after scrolling
        element.clear()
        element.send_keys(value)
        if ENABLE_DEBUG_LOGS:
            print(f"✅ {description} entered successfully.")
        return True
    except TimeoutException:
        if ENABLE_DEBUG_LOGS:
            print(f"⏰ Timeout waiting for {description} input field")
        return False
    except Exception as e:
        if ENABLE_DEBUG_LOGS:
            print(f"❌ Failed to enter {description}: {e}")
        return False

def wait_for_page_load(timeout=None):
    """Wait for page to fully load"""
    if timeout is None:
        timeout = PAGE_LOAD_TIMEOUT
    try:
        WebDriverWait(driver, timeout).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        time.sleep(2)  # Additional wait for any dynamic content
        return True
    except TimeoutException:
        if ENABLE_DEBUG_LOGS:
            print("⏰ Page load timeout")
        return False

# 1️⃣ Open the page: /client
try:
    print("🌐 Opening the taxi booking website...")
    driver.get(TARGET_URL)
    wait_for_page_load()
    print("🌐 Page loaded successfully.")

    # Wait until "Compte" is clickable - try multiple selectors
    compte_selectors = [
        '//span[contains(text(), "Compte")]',
        '//button[contains(text(), "Compte")]',
        '//*[contains(text(), "Compte")]',
        '//a[contains(text(), "Compte")]'
    ]
    
    compte_clicked = False
    for selector in compte_selectors:
        if safe_click(selector, "Compte button", 5):
            compte_clicked = True
            break
    
    if not compte_clicked:
        raise Exception("Could not find or click Compte button")
        
except Exception as e:
    print(f"❌ Error opening page / Compte: {e}")
    driver.quit()
    sys.exit(1)

# 2️⃣ Perform login
try:
    print("🔐 Starting login process...")
    
    # Wait for login form to appear
    time.sleep(3)
    
    if not safe_input('//input[@formcontrolname="email"]', EMAIL, "Email", LOGIN_TIMEOUT):
        # Try alternative selector
        if not safe_input('//input[@type="email"]', EMAIL, "Email (alternative)", DEFAULT_TIMEOUT):
            raise Exception("Could not find email input field")
    
    if not safe_input('//input[@formcontrolname="password"]', PASSWORD, "Password", DEFAULT_TIMEOUT):
        # Try alternative selector
        if not safe_input('//input[@type="password"]', PASSWORD, "Password (alternative)", DEFAULT_TIMEOUT):
            raise Exception("Could not find password input field")
    
    # Try multiple selectors for login button
    login_selectors = [
        '//button[contains(text(), "Connexion")]',
        '//button[contains(text(), "Login")]',
        '//button[contains(text(), "Se connecter")]',
        '//input[@type="submit"]',
        '//button[@type="submit"]'
    ]
    
    login_clicked = False
    for selector in login_selectors:
        if safe_click(selector, "Login button", 5):
            login_clicked = True
            break
    
    if not login_clicked:
        raise Exception("Could not find or click login button")
    
    # Wait for login to process
    time.sleep(5)
    print("✅ Login process completed.")
    
except Exception as e:
    print(f"❌ Login error: {e}")
    driver.quit()
    sys.exit(1)

# 3️⃣ Navigate to Accueil & refresh
try:
    print("🏠 Navigating to home page...")
    
    # Try multiple selectors for Accueil
    accueil_selectors = [
        '//span[contains(text(), "Accueil")]',
        '//button[contains(text(), "Accueil")]',
        '//*[contains(text(), "Accueil")]',
        '//a[contains(text(), "Accueil")]',
        '//span[contains(text(), "Home")]',
        '//*[contains(text(), "Home")]'
    ]
    
    accueil_clicked = False
    for selector in accueil_selectors:
        if safe_click(selector, "Accueil button", 5):
            accueil_clicked = True
            break
    
    if not accueil_clicked:
        print("⚠️ Could not find Accueil button, proceeding anyway...")
    
    time.sleep(3)
    driver.refresh()
    print("🔁 Page refreshed.")
    wait_for_page_load(15)
    
except Exception as e:
    print(f"❌ Error with Accueil or refresh: {e}")
    # Don't exit here, try to continue

# 4️⃣ Enter addresses & order taxi
try:
    print("📍 Entering address information...")
    
    # Start address - try multiple selectors
    start_selectors = [
        '//input[@placeholder="Adresse de départ"]',
        '//input[contains(@placeholder, "départ")]',
        '//input[contains(@placeholder, "From")]',
        '//input[contains(@placeholder, "departure")]'
    ]
    
    start_entered = False
    for selector in start_selectors:
        if safe_input(selector, DEPARTURE_ADDRESS, "Start address", DEFAULT_TIMEOUT):
            start_entered = True
            break
    
    if not start_entered:
        raise Exception("Could not find or fill start address field")
    
    # Destination address - try multiple selectors
    dest_selectors = [
        '//input[@placeholder="Adresse d\'arrivée"]',
        "//input[@placeholder=\"Adresse d'arrivée\"]",
        '//input[contains(@placeholder, "arrivée")]',
        '//input[contains(@placeholder, "To")]',
        '//input[contains(@placeholder, "destination")]'
    ]
    
    dest_entered = False
    for selector in dest_selectors:
        if safe_input(selector, ARRIVAL_ADDRESS, "Destination address", DEFAULT_TIMEOUT):
            dest_entered = True
            break
    
    if not dest_entered:
        raise Exception("Could not find or fill destination address field")

    time.sleep(3)

    # Commander button - try multiple selectors
    commander_selectors = [
        '//button[contains(text(), "Commander")]',
        '//button[contains(text(), "Order")]',
        '//button[contains(text(), "Book")]',
        '//button[contains(text(), "Réserver")]',
        '//input[@value="Commander"]',
        '//*[contains(text(), "Commander")]'
    ]
    
    commander_clicked = False
    for selector in commander_selectors:
        if safe_click(selector, "Commander button", DEFAULT_TIMEOUT):
            commander_clicked = True
            break
    
    if not commander_clicked:
        raise Exception("Could not find or click Commander button")
    
    print("🚕 Taxi successfully requested!")
    time.sleep(5)  # Wait to see confirmation
    
except Exception as e:
    print(f"❌ Error with address input or ordering: {e}")

# === End ===
print("🎉 Script execution completed.")
print("🛑 Press Enter to close the browser...")
try:
    input()
except KeyboardInterrupt:
    print("\n🛑 Script interrupted by user.")
finally:
    driver.quit()
    print("👋 Browser closed successfully.")