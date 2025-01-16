# setup.py
from setuptools import setup, find_packages

setup(
    name='django-admin-tester',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A Django app for automated testing of admin interfaces',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/django-admin-tester',
    author='Your Name',
    author_email='your.email@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 3.2',
        'Framework :: Django :: 4.0',
        'Framework :: Django :: 4.1',
        'Framework :: Django :: 4.2',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django>=3.2',
        'selenium>=4.0.0',
        'webdriver_manager>=3.8.0',
    ],
    extras_require={
        'test': [
            'pytest>=7.0.0',
            'pytest-django>=4.5.0',
            'pytest-selenium>=4.0.0',
        ],
    }
)

# django_admin_tester/__init__.py
from django.apps import AppConfig

class DjangoAdminTesterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_admin_tester'
    verbose_name = 'Django Admin Tester'
    
    def ready(self):
        from . import signals

# django_admin_tester/apps.py
from django.apps import AppConfig
from django.conf import settings

class DjangoAdminTesterConfig(AppConfig):
    name = 'django_admin_tester'
    verbose_name = 'Django Admin Tester'

    def ready(self):
        # Import signal handlers
        from . import signals
        
        # Register default settings
        self.register_default_settings()
    
    def register_default_settings(self):
        """Register default settings for the app."""
        defaults = {
            'ADMIN_TESTER_WAIT_TIMEOUT': 10,
            'ADMIN_TESTER_IMPLICIT_WAIT': 10,
            'ADMIN_TESTER_BROWSER': 'chrome',
            'ADMIN_TESTER_HEADLESS': True,
            'ADMIN_TESTER_WINDOW_SIZE': (1920, 1080),
            'ADMIN_TESTER_SCREENSHOT_ON_FAILURE': True,
            'ADMIN_TESTER_SCREENSHOT_DIR': None,
            'ADMIN_TESTER_DEFAULT_ADMIN_USERNAME': 'admin',
            'ADMIN_TESTER_DEFAULT_ADMIN_EMAIL': 'admin@example.com',
            'ADMIN_TESTER_DEFAULT_ADMIN_PASSWORD': 'admin123',
            'ADMIN_TESTER_CUSTOM_WAIT_CONDITIONS': {},
        }
        
        for key, default_value in defaults.items():
            if not hasattr(settings, key):
                setattr(settings, key, default_value)

# django_admin_tester/settings.py
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

class AdminTesterSettings:
    """Settings handler for Django Admin Tester."""
    
    @property
    def WAIT_TIMEOUT(self):
        return getattr(settings, 'ADMIN_TESTER_WAIT_TIMEOUT', 10)
    
    @property
    def IMPLICIT_WAIT(self):
        return getattr(settings, 'ADMIN_TESTER_IMPLICIT_WAIT', 10)
    
    @property
    def BROWSER(self):
        return getattr(settings, 'ADMIN_TESTER_BROWSER', 'chrome')
    
    @property
    def HEADLESS(self):
        return getattr(settings, 'ADMIN_TESTER_HEADLESS', True)
    
    @property
    def WINDOW_SIZE(self):
        return getattr(settings, 'ADMIN_TESTER_WINDOW_SIZE', (1920, 1080))
    
    @property
    def SCREENSHOT_ON_FAILURE(self):
        return getattr(settings, 'ADMIN_TESTER_SCREENSHOT_ON_FAILURE', True)
    
    @property
    def SCREENSHOT_DIR(self):
        return getattr(settings, 'ADMIN_TESTER_SCREENSHOT_DIR', None)
    
    @property
    def DEFAULT_ADMIN_USERNAME(self):
        return getattr(settings, 'ADMIN_TESTER_DEFAULT_ADMIN_USERNAME', 'admin')
    
    @property
    def DEFAULT_ADMIN_EMAIL(self):
        return getattr(settings, 'ADMIN_TESTER_DEFAULT_ADMIN_EMAIL', 'admin@example.com')
    
    @property
    def DEFAULT_ADMIN_PASSWORD(self):
        return getattr(settings, 'ADMIN_TESTER_DEFAULT_ADMIN_PASSWORD', 'admin123')
    
    @property
    def CUSTOM_WAIT_CONDITIONS(self):
        return getattr(settings, 'ADMIN_TESTER_CUSTOM_WAIT_CONDITIONS', {})

admin_tester_settings = AdminTesterSettings()

# django_admin_tester/exceptions.py
class AdminTesterError(Exception):
    """Base exception for admin testing errors."""
    pass

class AdminTesterConfigError(AdminTesterError):
    """Raised when there's a configuration error."""
    pass

class AdminTesterBrowserError(AdminTesterError):
    """Raised when there's a browser-related error."""
    pass

class AdminTesterTimeoutError(AdminTesterError):
    """Raised when a wait timeout occurs."""
    pass

# django_admin_tester/browsers.py
from typing import Dict, Any, Optional
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

# django_admin_tester/utils.py
import os
import time
from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver
from .settings import admin_tester_settings
from .exceptions import AdminTesterError

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

# django_admin_tester/mixins.py
from typing import Type, List, Optional
from django.db import models
from django.test import TestCase
from selenium.webdriver.remote.webdriver import WebDriver
from .settings import admin_tester_settings
from .browsers import BrowserFactory
from .test_cases import AdminPageTest

class AdminTestMixin:
    """Mixin to add admin testing capabilities to any test case."""
    
    model_class: Optional[Type[models.Model]] = None
    test_filters: List[str] = []
    browser_type: Optional[str] = None
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = BrowserFactory.create_browser(cls.browser_type)
    
    @classmethod
    def tearDownClass(cls):
        if hasattr(cls, 'selenium'):
            cls.selenium.quit()
        super().tearDownClass()

# django_admin_tester/decorators.py
from functools import wraps
from typing import Callable, Any
from .exceptions import AdminTesterError
from .utils import take_screenshot

def screenshot_on_failure(func: Callable) -> Callable:
    """Decorator to take a screenshot when a test fails."""
    @wraps(func)
    def wrapper(self, *args, **kwargs) -> Any:
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            if hasattr(self, 'selenium'):
                screenshot_path = take_screenshot(
                    self.selenium,
                    f"{self.__class__.__name__}_{func.__name__}"
                )
                raise AdminTesterError(
                    f"{str(e)}\nScreenshot saved to: {screenshot_path}"
                ) from e
            raise
    return wrapper

# django_admin_tester/test_cases.py
[Previous implementation of AdminPageTest with the following changes:]
1. Import from local modules
2. Use settings from admin_tester_settings
3. Use BrowserFactory for WebDriver creation
4. Add screenshot_on_failure decorator to test methods
5. Add custom wait conditions support
6. Add more robust error handling
7. Add support for different browsers

# README.md
# Django Admin Tester

A Django app for automated testing of admin interfaces using Selenium.

## Installation

```bash
pip install django-admin-tester
```

## Configuration

Add 'django_admin_tester' to your INSTALLED_APPS setting:

```python
INSTALLED_APPS = [
    ...
    'django_admin_tester',
]
```

## Settings

Configure the app in your Django settings:

```python
# Admin Tester settings
ADMIN_TESTER_WAIT_TIMEOUT = 10
ADMIN_TESTER_IMPLICIT_WAIT = 10
ADMIN_TESTER_BROWSER = 'chrome'  # or 'firefox'
ADMIN_TESTER_HEADLESS = True
ADMIN_TESTER_WINDOW_SIZE = (1920, 1080)
ADMIN_TESTER_SCREENSHOT_ON_FAILURE = True
ADMIN_TESTER_SCREENSHOT_DIR = 'test_screenshots'
```

## Usage

Create your test case:

```python
from django_admin_tester import AdminPageTest
from myapp.models import MyModel

class MyModelAdminTest(AdminPageTest):
    model_class = MyModel
    test_filters = ['status', 'category']
```

# .gitignore
*.pyc
__pycache__
*.pyo
*.pyd
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
*.egg-info/
.installed.cfg
*.egg
