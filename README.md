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

Before running the script, update the configuration in `config.py`:

```python
# Login Credentials
EMAIL = "your-email@example.com"         # Your actual email
PASSWORD = "your-password"               # Your actual password

# Trip Details
DEPARTURE_ADDRESS = "Your departure address"
ARRIVAL_ADDRESS = "Your destination address"

# Browser Settings
HEADLESS_MODE = False                    # Set to True for background execution
```

## Usage

### Quick Start

The easiest way to run the script:

```bash
./run_script.sh
```

### Manual Execution

Alternatively, activate the virtual environment and run the script manually:

```bash
source venv/bin/activate
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
- **Configuration file**: Separate `config.py` for easy credential and setting management
- **Multiple selector support**: Tries multiple XPath selectors for better compatibility
- **Auto-detection prevention**: Includes measures to avoid bot detection

## Headless Mode

To run the script without opening a browser window (headless mode), set this in `config.py`:

```python
HEADLESS_MODE = True
```

## Security Notes

⚠️ **Important**: Keep your credentials secure:

1. **Never commit real credentials** to version control
2. **Use environment variables** for sensitive data:
```bash
export TAXI_EMAIL="your-email@example.com"
export TAXI_PASSWORD="your-password"
```

3. **Update config.py** with environment variables:
```python
import os
EMAIL = os.getenv('TAXI_EMAIL', 'default-email@example.com')
PASSWORD = os.getenv('TAXI_PASSWORD', 'default-password')
```

4. Consider using encrypted credential storage for production use

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
