
from app import AdminPageTest
from core.yourapp.admin import FIELDS
from core.yourapp.models import AllFieldTypes


class ProductAdminTest(AdminPageTest):
    model_class = AllFieldTypes
    test_filters = FIELDS

