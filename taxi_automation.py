from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# ==== CONFIGURATION ====
email = "siraj.workstation@gmail.com"
password = "password"
# Updated for Linux path
chrome_profile_path = "/tmp/SeleniumProfile"

adresse_depart = "Hammam Sousse"
adresse_arrivee = "Sousse Centre Ville"

# ==== CHROME SETUP ====
options = Options()
# Create profile directory if it doesn't exist
os.makedirs(chrome_profile_path, exist_ok=True)

options.add_argument(f"--user-data-dir={chrome_profile_path}")
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--allow-insecure-localhost")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--no-sandbox")  # Required for Linux in many environments
options.add_argument("--disable-dev-shm-usage")  # Required for Linux in many environments
options.add_argument("--disable-gpu")  # Good for headless environments

# For headless mode (uncomment if needed)
# options.add_argument("--headless")

try:
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    wait = WebDriverWait(driver, 15)
    print("🚀 Chrome WebDriver initialized successfully.")
except Exception as e:
    print(f"❌ Failed to initialize WebDriver: {e}")
    exit(1)

def safe_click(xpath, description):
    """Safely click an element with error handling"""
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        element.click()
        print(f"✅ {description} clicked successfully.")
        return True
    except Exception as e:
        print(f"❌ Failed to click {description}: {e}")
        return False

def safe_input(xpath, value, description):
    """Safely input text into an element"""
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        element.clear()
        element.send_keys(value)
        print(f"✅ {description} entered successfully.")
        return True
    except Exception as e:
        print(f"❌ Failed to enter {description}: {e}")
        return False

# 1️⃣ Open the page: /client
try:
    driver.get("https://mobile.thunder.webify.pro/#/client")
    print("🌐 Page loaded.")

    # Wait until "Compte" is clickable
    if not safe_click('//span[contains(text(), "Compte")]', "Compte button"):
        raise Exception("Could not click Compte button")
        
except Exception as e:
    print(f"❌ Error opening page / Compte: {e}")
    driver.quit()
    exit(1)

# 2️⃣ Perform login
try:
    if not safe_input('//input[@formcontrolname="email"]', email, "Email"):
        raise Exception("Could not enter email")
    
    if not safe_input('//input[@formcontrolname="password"]', password, "Password"):
        raise Exception("Could not enter password")
    
    if not safe_click('//button[contains(text(), "Connexion")]', "Login button"):
        raise Exception("Could not click login button")
    
    # Wait a bit for login to process
    time.sleep(3)
    print("✅ Login completed.")
    
except Exception as e:
    print(f"❌ Login error: {e}")
    driver.quit()
    exit(1)

# 3️⃣ Navigate to Accueil & refresh
try:
    if not safe_click('//span[contains(text(), "Accueil")]', "Accueil button"):
        raise Exception("Could not click Accueil button")
    
    time.sleep(2)
    driver.refresh()
    print("🔁 Page refreshed.")
    time.sleep(5)
    
except Exception as e:
    print(f"❌ Error with Accueil or refresh: {e}")

# 4️⃣ Enter addresses & order taxi
try:
    # Start address
    if not safe_input('//input[@placeholder="Adresse de départ"]', adresse_depart, "Start address"):
        raise Exception("Could not enter start address")
    
    # Destination address
    if not safe_input('//input[@placeholder="Adresse d\'arrivée"]', adresse_arrivee, "Destination address"):
        raise Exception("Could not enter destination address")
    
    time.sleep(2)

    # Commander button
    if not safe_click('//button[contains(text(), "Commander")]', "Commander button"):
        raise Exception("Could not click Commander button")
    
    print("🚕 Taxi successfully requested.")
    
except Exception as e:
    print(f"❌ Error with address input or ordering: {e}")

# === End ===
print("🎉 Script execution completed.")
print("🛑 Press Enter to close the browser...")
input()
driver.quit()