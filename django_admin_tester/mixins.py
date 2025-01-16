from typing import Type, List, Optional
from django.db import models
from .browsers import BrowserFactory

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


