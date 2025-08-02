# Taxi Automation Script

This Selenium-based automation script automates the process of booking a taxi through the Thunder mobile web application.

## Features

- Automated login to the taxi booking platform
- Address input for departure and arrival locations
- Taxi booking automation
- Cross-platform compatibility (Linux optimized)
- Error handling and logging

## Prerequisites

1. **Python 3.7+** installed on your system
2. **Google Chrome browser** installed
3. **Internet connection** for downloading ChromeDriver

## Installation

1. Install the required Python packages:
```bash
pip install -r requirements.txt
```

2. Make sure Google Chrome is installed on your system:
```bash
# On Ubuntu/Debian
sudo apt update
sudo apt install google-chrome-stable

# On CentOS/RHEL/Fedora
sudo dnf install google-chrome-stable
```

## Configuration

Before running the script, update the configuration variables in `taxi_automation.py`:

```python
# ==== CONFIGURATION ====
email = "your-email@example.com"        # Your account email
password = "your-password"               # Your account password
adresse_depart = "Your departure address"
adresse_arrivee = "Your destination address"
```

## Usage

Run the automation script:

```bash
python taxi_automation.py
```

### Script Flow

1. **Page Loading**: Opens the Thunder mobile web app
2. **Authentication**: Clicks on "Compte" and logs in with provided credentials
3. **Navigation**: Goes to "Accueil" (Home) and refreshes the page
4. **Booking**: Enters departure and arrival addresses, then requests a taxi
5. **Completion**: Waits for user input before closing the browser

## Features Added for Linux

- **Linux-compatible paths**: Uses `/tmp/SeleniumProfile` instead of Windows paths
- **Additional Chrome options**: Added `--no-sandbox` and `--disable-dev-shm-usage` for Linux compatibility
- **Directory creation**: Automatically creates the profile directory if it doesn't exist
- **Better error handling**: Improved error messages and graceful exits

## Headless Mode

To run the script without opening a browser window (headless mode), uncomment this line in the script:

```python
options.add_argument("--headless")
```

## Security Notes

⚠️ **Important**: This script contains hardcoded credentials. For production use:

1. Use environment variables for sensitive data:
```python
import os
email = os.getenv('TAXI_EMAIL')
password = os.getenv('TAXI_PASSWORD')
```

2. Consider using encrypted credential storage
3. Never commit real credentials to version control

## Troubleshooting

### Common Issues

1. **Chrome not found**: Make sure Google Chrome is installed and in your PATH
2. **Permission denied**: Ensure the script has write permissions to `/tmp/`
3. **Element not found**: The website might have changed - check XPath selectors
4. **Network issues**: Verify internet connection and website availability

### Debug Mode

For debugging, you can:
- Remove the `--headless` option to see browser actions
- Add longer `time.sleep()` delays between actions
- Use browser developer tools to inspect element selectors

## License

This script is for educational and personal use only. Please ensure compliance with the target website's terms of service.
