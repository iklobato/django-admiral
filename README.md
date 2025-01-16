# Django Admiral 🚢

Django Admiral is a robust testing framework designed to automate comprehensive testing of Django Admin interfaces. Built with Selenium WebDriver, it provides an extensive suite of tools for testing filters, search functionality, form validations, and other admin panel features.

## ✨ Features

### Core Testing Capabilities
- 🔍 Automated testing of all admin filters with custom filter support
- 🔎 Comprehensive search functionality testing
- 📝 Form validation and submission testing
- 📋 Bulk action verification
- 🔄 Column sorting and ordering tests
- 📊 List view pagination testing

### Advanced Features
- 📸 Automatic screenshot capture on test failures
- 🌐 Multiple browser support (Chrome, Firefox)
- 🎯 Custom wait conditions for dynamic content
- ⚙️ Flexible configuration through Django settings
- 🔧 Extensible test cases with mixins
- 📦 Modular design for easy customization

### Developer Experience
- 🚀 Simple integration with existing Django projects
- 📝 Detailed error reporting with screenshots
- 🔄 Seamless CI/CD integration
- 🎨 Clean, Pythonic API

## 🛠 Installation

```bash
pip install django-admiral
```

## 📋 Requirements

- Python 3.8+
- Django 3.2+
- Selenium 4.0+
- Chrome/Firefox browser

## 📁 Project Structure

```
django-admiral/
├── django_admiral/
│   ├── __init__.py
│   ├── apps.py
│   ├── browsers.py
│   ├── decorators.py
│   ├── exceptions.py
│   ├── mixins.py
│   ├── settings.py
│   ├── test_cases.py
│   └── utils.py
├── tests/
│   ├── __init__.py
│   └── test_admin.py
├── LICENSE
├── MANIFEST.in
├── README.md
├── setup.cfg
└── setup.py
```

## 🚀 Quick Start

1. Add 'django_admiral' to your INSTALLED_APPS:

```python
INSTALLED_APPS = [
    ...
    'django_admiral',
]
```

2. Configure settings in your Django settings file:

```python
# Django Admiral settings
ADMIN_TESTER_BROWSER = 'chrome'  # or 'firefox'
ADMIN_TESTER_HEADLESS = True
ADMIN_TESTER_SCREENSHOT_ON_FAILURE = True
ADMIN_TESTER_SCREENSHOT_DIR = 'test_screenshots'
```

3. Create your test case:

```python
from django_admiral import AdminPageTest
from myapp.models import Product

class ProductAdminTest(AdminPageTest):
    model_class = Product
    test_filters = ['category', 'status']
```

## 💡 Usage Examples

### Basic Admin Testing

```python
from django_admiral import AdminPageTest
from myapp.models import Product

class ProductAdminTest(AdminPageTest):
    model_class = Product
```

### Advanced Configuration

```python
from django_admiral import AdminPageTest, AdminTesterSettings
from myapp.models import Order

class OrderAdminTest(AdminPageTest):
    model_class = Order
    test_filters = ['status', 'payment_method']
    browser_type = 'firefox'
    
    @classmethod
    def setUpClass(cls):
        cls.custom_settings = AdminTesterSettings(
            wait_timeout=15,
            screenshot_on_failure=True,
            window_size=(1920, 1080)
        )
        super().setUpClass()
```

### Custom Wait Conditions

```python
from django_admiral import AdminPageTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class CustomAdminTest(AdminPageTest):
    model_class = MyModel
    
    def setUp(self):
        super().setUp()
        self.custom_wait_conditions = {
            'table_loaded': (EC.presence_of_element_located, 
                           (By.CLASS_NAME, 'results')),
            'filters_ready': (EC.element_to_be_clickable, 
                            (By.CLASS_NAME, 'admin-filter'))
        }
```

## ⚙️ Configuration Options

### Available Settings

```python
ADMIN_TESTER_SETTINGS = {
    'WAIT_TIMEOUT': 10,
    'IMPLICIT_WAIT': 10,
    'BROWSER': 'chrome',
    'HEADLESS': True,
    'WINDOW_SIZE': (1920, 1080),
    'SCREENSHOT_ON_FAILURE': True,
    'SCREENSHOT_DIR': 'test_screenshots',
    'DEFAULT_ADMIN_USERNAME': 'admin',
    'DEFAULT_ADMIN_EMAIL': 'admin@example.com',
    'DEFAULT_ADMIN_PASSWORD': 'admin123',
    'CUSTOM_WAIT_CONDITIONS': {},
}
```

### Browser Support

Currently supported browsers:
- Chrome/Chromium (default)
- Firefox

## 🧪 Test Coverage

Django Admiral automatically tests:

1. **Filter Operations**
   - Filter presence and clickability
   - Filter option selections
   - Multiple filter combinations
   - Filter reset functionality

2. **Search Functionality**
   - Search input presence
   - Search result loading
   - Empty search handling
   - Search with special characters

3. **Form Operations**
   - Add form accessibility
   - Form field validation
   - Form submission
   - Error message handling

4. **List Actions**
   - Action dropdown presence
   - Action selection
   - Bulk action execution
   - Action confirmation dialogs

5. **Sorting and Pagination**
   - Column sort operations
   - Multiple column sorting
   - Page navigation
   - Items per page selection

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🗓 Roadmap

### Upcoming Features
- 🚀 Support for async operations testing
- 🚀 Custom admin action testing helpers
- 💡 API endpoint testing integration
- 💡 Advanced reporting capabilities
- 🤔 Performance testing tools
- 🤔 Security testing features

## 📊 Version History

### 1.0.0 (2024-01-16)
- Initial release with core feature set
- Multiple browser support
- Screenshot capabilities
- Custom wait conditions
- Comprehensive documentation

### 1.1.0 (Coming Soon)
- Advanced reporting features
- Custom action testing
- Performance improvements
- Additional browser support
