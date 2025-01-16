from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from .settings import admin_tester_settings
from .exceptions import AdminTesterBrowserError

class BrowserFactory:
    """Factory for creating WebDriver instances."""
    
    @staticmethod
    def create_browser(browser_type: Optional[str] = None, **kwargs) -> webdriver.Remote:
        """Create a new WebDriver instance based on settings."""
        browser_type = browser_type or admin_tester_settings.BROWSER
        
        creators = {
            'chrome': BrowserFactory._create_chrome,
            'firefox': BrowserFactory._create_firefox,
        }
        
        creator = creators.get(browser_type.lower())
        if not creator:
            raise AdminTesterBrowserError(f"Unsupported browser type: {browser_type}")
        
        return creator(**kwargs)
    
    @staticmethod
    def _create_chrome(**kwargs) -> webdriver.Chrome:
        """Create a Chrome WebDriver instance."""
        options = ChromeOptions()
        
        if admin_tester_settings.HEADLESS:
            options.add_argument('--headless')
        
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        window_size = admin_tester_settings.WINDOW_SIZE
        options.add_argument(f'--window-size={window_size[0]},{window_size[1]}')
        
        # Add custom Chrome options from kwargs
        for arg in kwargs.get('chrome_options', []):
            options.add_argument(arg)
        
        try:
            return webdriver.Chrome(
                ChromeDriverManager().install(),
                options=options
            )
        except Exception as e:
            raise AdminTesterBrowserError(f"Failed to create Chrome WebDriver: {str(e)}")

    @staticmethod
    def _create_firefox(**kwargs) -> webdriver.Firefox:
        """Create a Firefox WebDriver instance."""
        options = FirefoxOptions()
        
        if admin_tester_settings.HEADLESS:
            options.add_argument('--headless')
        
        try:
            return webdriver.Firefox(
                executable_path=GeckoDriverManager().install(),
                options=options
            )
        except Exception as e:
            raise AdminTesterBrowserError(f"Failed to create Firefox WebDriver: {str(e)}")


