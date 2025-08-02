# Taxi Automation Configuration File
# =================================
# 
# Update these values with your actual credentials and preferences
# Never commit real credentials to version control!

# Login Credentials
EMAIL = "siraj.workstation@gmail.com"  # Replace with your actual email
PASSWORD = "password"                   # Replace with your actual password

# Trip Details
DEPARTURE_ADDRESS = "Hammam Sousse"
ARRIVAL_ADDRESS = "Sousse Centre Ville"

# Browser Settings
CHROME_PROFILE_PATH = "/tmp/SeleniumProfile"
HEADLESS_MODE = False  # Set to True to run browser in background (no window)

# Timeout Settings (in seconds)
DEFAULT_TIMEOUT = 10
PAGE_LOAD_TIMEOUT = 20
LOGIN_TIMEOUT = 15

# Debug Settings
ENABLE_DEBUG_LOGS = True
SCREENSHOT_ON_ERROR = False  # Set to True to save screenshots when errors occur

# Website URL
TARGET_URL = "https://mobile.thunder.webify.pro/#/client"