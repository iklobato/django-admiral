# Django Admiral

Django Admiral is a powerful testing framework for Django Admin interfaces that helps you automatically test filters, search functionality, and other admin panel features using Selenium WebDriver.

## Features

- Automated testing of Django Admin filters
- Search functionality testing
- Add form validation
- List action testing
- Column sorting verification
- Headless browser testing support
- Easy to integrate with existing Django projects
- Customizable filter testing

## Installation

```bash
pip install django-admiral
```

## Requirements

- Python 3.6+
- Django 3.0+
- Selenium WebDriver
- Chrome/Chromium browser

## Quick Start

1. First, install the required dependencies:

```bash
pip install selenium webdriver_manager
```

2. Create a test file for your model (e.g., `tests.py`):

```python
from django_admiral import AdminPageTest
from .models import UserProfile

class TestUserProfile(AdminPageTest):
    model_class = UserProfile
    test_filters = ('status', 'created_date')  # Optional: specify filters to test
```

3. Run your tests:

```bash
python manage.py test
```

## Usage Examples

### Basic Usage

```python
from django_admiral import AdminPageTest
from .models import UserProfile

class TestUserProfile(AdminPageTest):
    model_class = UserProfile
```

### Testing Specific Filters

```python
class TestUserProfile(AdminPageTest):
    model_class = UserProfile
    test_filters = ('count_filter', 'TransactionsCustomFilter')
```

### Custom Setup

```python
class TestUserProfile(AdminPageTest):
    model_class = UserProfile
    test_filters = ('status', 'date_joined')

    def setUp(self):
        super().setUp()
        # Add your custom setup here
        self.user_profile = UserProfile.objects.create(
            name="Test User",
            status="active"
        )
```

## What Gets Tested

When you run the tests, Django Admiral automatically checks:

1. **Filters**
   - Clicks each filter option
   - Verifies no errors occur
   - Tests specified filters or all filters if none specified

2. **Search**
   - Tests the search functionality
   - Verifies search results load properly

3. **Add Form**
   - Attempts to access the add form
   - Verifies form loads correctly

4. **List Actions**
   - Tests all available list actions
   - Verifies action dropdowns work correctly

5. **Sorting**
   - Tests column sorting
   - Verifies sort operations complete successfully

## Configuration

### Headless Testing

By default, tests run in headless mode. You can modify this in your test class:

```python
@classmethod
def setUpClass(cls):
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # Remove this line to see the browser
    cls.selenium = webdriver.Chrome(options=chrome_options)
```

### Custom Wait Times

```python
class TestUserProfile(AdminPageTest):
    model_class = UserProfile
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium.implicitly_wait(20)  # Customize wait time
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## Acknowledgments

- Django Admin interface
- Selenium WebDriver
- Python Testing Framework

# Django Admiral Development Roadmap

| Category | Feature | Priority | Status | Description |
|----------|---------|----------|--------|-------------|
| **Core Testing** | Permission Testing | High | 🚀 Planned | Test user roles, access restrictions, and custom permissions |
| | Form Validation | High | 🚀 Planned | Validate required fields, custom validators, error messages |
| | Bulk Actions | Medium | 💡 Proposed | Test bulk operations, confirmations, and permissions |
| | Advanced Filters | High | 🚀 Planned | Test filter combinations, ranges, and dependencies |
| | Custom Actions | Medium | 💡 Proposed | Support for testing custom admin actions |
|----------|---------|----------|--------|-------------|
| **Performance** | Response Metrics | Medium | 💡 Proposed | Track load times, response times, and performance metrics |
| | Load Testing | Low | 🤔 Considering | Test admin performance under heavy load |
| | Pagination Testing | Medium | 💡 Proposed | Test with large datasets and different page sizes |
| | Memory Usage | Low | 🤔 Considering | Monitor and optimize memory consumption |
|----------|---------|----------|--------|-------------|
| **UI/UX** | Responsive Testing | High | 🚀 Planned | Test mobile, tablet, and desktop views |
| | Accessibility | High | 🚀 Planned | ARIA labels, keyboard navigation, screen readers |
| | Visual Testing | Medium | 💡 Proposed | Screenshot comparison and visual regression |
| | Layout Validation | Medium | 💡 Proposed | Verify UI elements positioning and styling |
|----------|---------|----------|--------|-------------|
| **Integration** | Multi-Browser | High | 🚀 Planned | Support Firefox, Safari, and other browsers |
| | CI/CD Pipeline | High | 🚀 Planned | Easy integration with common CI/CD platforms |
| | Docker Support | Medium | 💡 Proposed | Containerized testing environment |
| | Database Support | Medium | 💡 Proposed | Test with different database backends |
|----------|---------|----------|--------|-------------|
| **Advanced Features** | Auto Test Generation | High | 🚀 Planned | Generate tests based on model structure |
| | Factory Integration | Medium | 💡 Proposed | Integration with factory_boy for test data |
| | Smart Scenarios | Low | 🤔 Considering | AI-powered test scenario generation |
| | Data Validation | High | 🚀 Planned | Complex data validation patterns |
|----------|---------|----------|--------|-------------|
| **Reporting** | Test Reports | High | 🚀 Planned | Detailed HTML/PDF test reports |
| | Coverage Analysis | Medium | 💡 Proposed | Track test coverage metrics |
| | Failure Analysis | High | 🚀 Planned | Detailed failure analysis with screenshots |
| | Metrics Dashboard | Low | 🤔 Considering | Web dashboard for test metrics |
|----------|---------|----------|--------|-------------|
| **Developer Tools** | CLI Tool | Medium | 💡 Proposed | Command-line interface for test management |
| | Debug Mode | High | 🚀 Planned | Enhanced logging and debugging capabilities |
| | Configuration GUI | Low | 🤔 Considering | Visual test configuration interface |
| | Plugin System | Medium | 💡 Proposed | Extensible architecture for plugins |
|----------|---------|----------|--------|-------------|
| **Security** | CSRF Testing | High | 🚀 Planned | Test token validation and security measures |
| | XSS Prevention | High | 🚀 Planned | Test input sanitization and encoding |
| | Auth Testing | High | 🚀 Planned | Comprehensive authentication testing |
| | Session Security | Medium | 💡 Proposed | Test session handling and security |
|----------|---------|----------|--------|-------------|
| **Reliability** | Error Handling | High | 🚀 Planned | Test various failure scenarios |
| | State Management | Medium | 💡 Proposed | Test state preservation and navigation |
| | Recovery Testing | Medium | 💡 Proposed | Test system recovery procedures |
| | Concurrency | Low | 🤔 Considering | Test concurrent user actions |
|----------|---------|----------|--------|-------------|
| **Documentation** | Interactive Docs | High | 🚀 Planned | Interactive examples and tutorials |
| | Video Tutorials | Low | 🤔 Considering | Video-based learning resources |
| | Best Practices | High | 🚀 Planned | Comprehensive best practices guide |
| | API Reference | High | 🚀 Planned | Detailed API documentation |

**Status Legend:**
- 🚀 Planned: High priority, actively being worked on
- 💡 Proposed: Medium priority, in planning phase
- 🤔 Considering: Low priority, under consideration

**Priority Levels:**
- High: Critical for core functionality
- Medium: Important but not critical
- Low: Nice to have features
## Change Log

### 1.0.0
- Initial release
- Basic filter testing
- Admin panel navigation
- Headless browser support
