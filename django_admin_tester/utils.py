import os
import time
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from .settings import admin_tester_settings

def take_screenshot(driver: WebDriver, name: Optional[str] = None) -> str:
    """Take a screenshot and save it to the configured directory."""
    if not admin_tester_settings.SCREENSHOT_ON_FAILURE:
        return
    
    screenshot_dir = admin_tester_settings.SCREENSHOT_DIR or 'screenshots'
    os.makedirs(screenshot_dir, exist_ok=True)
    
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name or 'screenshot'}_{timestamp}.png"
    filepath = os.path.join(screenshot_dir, filename)
    
    driver.save_screenshot(filepath)
    return filepath


