#!/usr/bin/env python3
"""
ChromeDriver Setup Script
Alternative to webdriver-manager for environments where it doesn't work properly.
"""

import os
import requests
import zipfile
import tempfile
import shutil
import subprocess
import json
from pathlib import Path

def get_chrome_version():
    """Get the installed Chrome version"""
    try:
        result = subprocess.run(['google-chrome', '--version'], 
                              capture_output=True, text=True, check=True)
        version = result.stdout.strip().split()[-1]
        # Extract major version
        major_version = version.split('.')[0]
        return major_version
    except Exception as e:
        print(f"❌ Could not determine Chrome version: {e}")
        return None

def download_chromedriver(version):
    """Download ChromeDriver for the specified Chrome version"""
    # ChromeDriver download URL for Chrome 114+
    base_url = "https://storage.googleapis.com/chrome-for-testing-public"
    
    try:
        # Get available versions
        versions_url = f"{base_url}/LATEST_RELEASE_{version}"
        response = requests.get(versions_url)
        
        if response.status_code != 200:
            print(f"⚠️ Using fallback version detection...")
            # Try the JSON API
            json_url = f"{base_url}/last-known-good-versions.json"
            json_response = requests.get(json_url)
            if json_response.status_code == 200:
                data = json_response.json()
                driver_version = data['channels']['Stable']['version']
            else:
                raise Exception("Could not determine ChromeDriver version")
        else:
            driver_version = response.text.strip()
        
        # Download ChromeDriver
        platform = "linux64"
        download_url = f"{base_url}/{driver_version}/{platform}/chromedriver-{platform}.zip"
        
        print(f"📥 Downloading ChromeDriver {driver_version}...")
        print(f"   URL: {download_url}")
        
        response = requests.get(download_url, stream=True)
        response.raise_for_status()
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
            for chunk in response.iter_content(chunk_size=8192):
                tmp_file.write(chunk)
            zip_path = tmp_file.name
        
        return zip_path, driver_version
        
    except Exception as e:
        print(f"❌ Failed to download ChromeDriver: {e}")
        return None, None

def install_chromedriver(zip_path, version):
    """Extract and install ChromeDriver"""
    try:
        # Create chromedriver directory
        chromedriver_dir = Path.home() / '.local' / 'bin'
        chromedriver_dir.mkdir(parents=True, exist_ok=True)
        
        # Extract ChromeDriver
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Find the chromedriver executable in the zip
            for file_info in zip_ref.filelist:
                if file_info.filename.endswith('chromedriver') and not file_info.is_dir():
                    # Extract to temporary location first
                    with tempfile.TemporaryDirectory() as temp_dir:
                        zip_ref.extract(file_info, temp_dir)
                        extracted_path = Path(temp_dir) / file_info.filename
                        
                        # Move to final location
                        final_path = chromedriver_dir / 'chromedriver'
                        shutil.move(str(extracted_path), str(final_path))
                        
                        # Make executable
                        os.chmod(final_path, 0o755)
                        
                        print(f"✅ ChromeDriver {version} installed to {final_path}")
                        return str(final_path)
        
        raise Exception("ChromeDriver executable not found in zip file")
        
    except Exception as e:
        print(f"❌ Failed to install ChromeDriver: {e}")
        return None
    finally:
        # Clean up zip file
        if os.path.exists(zip_path):
            os.unlink(zip_path)

def main():
    print("🔧 Setting up ChromeDriver...")
    
    # Get Chrome version
    chrome_version = get_chrome_version()
    if not chrome_version:
        print("❌ Please install Google Chrome first")
        return False
    
    print(f"🌐 Chrome version detected: {chrome_version}")
    
    # Download ChromeDriver
    zip_path, driver_version = download_chromedriver(chrome_version)
    if not zip_path:
        return False
    
    # Install ChromeDriver
    chromedriver_path = install_chromedriver(zip_path, driver_version)
    if not chromedriver_path:
        return False
    
    # Verify installation
    try:
        result = subprocess.run([chromedriver_path, '--version'], 
                              capture_output=True, text=True, check=True)
        print(f"✅ ChromeDriver verification: {result.stdout.strip()}")
        
        # Add to PATH instructions
        bin_dir = Path(chromedriver_path).parent
        print(f"\n📝 To use ChromeDriver from anywhere, add this to your ~/.bashrc:")
        print(f"   export PATH=\"{bin_dir}:$PATH\"")
        
        return True
        
    except Exception as e:
        print(f"❌ ChromeDriver verification failed: {e}")
        return False

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)