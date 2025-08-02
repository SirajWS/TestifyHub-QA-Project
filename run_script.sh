#!/bin/bash

# Taxi Automation Script Runner
echo "🚕 Starting Taxi Automation Script"
echo "=================================="

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "❌ Virtual environment not found. Please run:"
    echo "python3 -m venv venv"
    echo "source venv/bin/activate"
    echo "pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Check if required packages are installed
echo "📦 Checking dependencies..."
python -c "import selenium, webdriver_manager" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Required packages not found. Installing..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies!"
        exit 1
    fi
fi

# Check if Chrome is available
if ! command -v google-chrome &> /dev/null; then
    echo "❌ Google Chrome not found. Please install Google Chrome first."
    echo "Run: sudo apt install -y google-chrome-stable"
    exit 1
fi

echo "✅ All dependencies are ready!"
echo ""
echo "⚠️  IMPORTANT: Make sure to update your credentials in config.py"
echo "   - Email: Update the 'EMAIL' variable"
echo "   - Password: Update the 'PASSWORD' variable"
echo "   - Addresses: Update 'DEPARTURE_ADDRESS' and 'ARRIVAL_ADDRESS'"
echo ""
echo "🚀 Starting the automation script..."
echo ""

# Run the script
python taxi_automation.py

echo ""
echo "🎉 Script execution finished!"