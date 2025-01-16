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
                    self.selenium, f"{self.__class__.__name__}_{func.__name__}"
                )
                raise AdminTesterError(
                    f"{str(e)}\nScreenshot saved to: {screenshot_path}"
                ) from e
            raise

    return wrapper
