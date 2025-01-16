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


