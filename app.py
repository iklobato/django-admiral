from django.contrib.auth import get_user_model
from django.test import LiveServerTestCase
from django.urls import reverse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time


class AdminPageTest(LiveServerTestCase):
    model_class = None
    test_filters = []

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        if not cls.model_class:
            raise ValueError("model_class attribute must be set")
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.selenium = webdriver.Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def setUp(self):
        User = get_user_model()
        self.admin_user = User.objects.create_superuser(
            username='admin', email='admin@example.com', password='admin123'
        )
        self.failed_actions = []

    def login_admin(self):
        self.selenium.get(f"{self.live_server_url}/admin/")
        username_input = self.selenium.find_element(By.NAME, "username")
        password_input = self.selenium.find_element(By.NAME, "password")
        username_input.send_keys("admin")
        password_input.send_keys("admin123")
        self.selenium.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def test_admin_page(self):
        self.login_admin()

        app_label = self.model_class._meta.app_label
        model_name = self.model_class._meta.model_name
        url = reverse(f'admin:{app_label}_{model_name}_changelist')
        self.selenium.get(f"{self.live_server_url}{url}")

        self.test_specified_filters()
        self.test_search()
        self.test_add_form()
        self.test_list_actions()
        self.test_sorting()

        if self.failed_actions:
            self.fail("\n".join(self.failed_actions))

    def test_specified_filters(self):
        wait = WebDriverWait(self.selenium, 10)
        try:
            filters = self.selenium.find_elements(By.CLASS_NAME, "admin-filter")
            for filter_elem in filters:
                filter_name = filter_elem.text.split('\n')[0]

                if not self.test_filters or filter_name in self.test_filters:
                    options = filter_elem.find_elements(By.TAG_NAME, 'a')
                    for option in options:
                        try:
                            wait.until(
                                EC.element_to_be_clickable(
                                    (By.ID, option.get_attribute('id'))
                                )
                            )
                            option.click()
                            time.sleep(0.5)
                            error_note = self.selenium.find_elements(
                                By.CLASS_NAME, "errornote"
                            )
                            if error_note:
                                self.failed_actions.append(
                                    f"Filter error: {filter_name} - {option.text}"
                                )
                        except Exception as e:
                            self.failed_actions.append(
                                f"Failed to click filter: {filter_name} - {option.text} - {str(e)}"
                            )
        except Exception as e:
            self.failed_actions.append(f"Filter test failed: {str(e)}")

    def test_search(self):
        try:
            search_input = self.selenium.find_element(By.ID, "searchbar")
            if search_input:
                search_input.send_keys("test")
                search_input.submit()
                time.sleep(0.5)
        except Exception as e:
            self.failed_actions.append(f"Search test failed: {str(e)}")

    def test_add_form(self):
        try:
            add_button = self.selenium.find_element(By.CLASS_NAME, "addlink")
            if add_button:
                add_button.click()
                time.sleep(0.5)
                error_notes = self.selenium.find_elements(By.CLASS_NAME, "errornote")
                if error_notes:
                    self.failed_actions.append("Add form error")
                self.selenium.back()
        except Exception as e:
            self.failed_actions.append(f"Add form test failed: {str(e)}")

    def test_list_actions(self):
        try:
            from selenium.webdriver.support.select import Select

            action_select = Select(self.selenium.find_element(By.NAME, "action"))
            options = action_select.options[1:]
            for option in options:
                action_select.select_by_value(option.get_attribute("value"))
        except Exception as e:
            self.failed_actions.append(f"List actions test failed: {str(e)}")

    def test_sorting(self):
        try:
            sortable_headers = self.selenium.find_elements(
                By.CSS_SELECTOR, "th.sortable"
            )
            for header in sortable_headers:
                header.click()
                time.sleep(0.5)
                error_notes = self.selenium.find_elements(By.CLASS_NAME, "errornote")
                if error_notes:
                    self.failed_actions.append(f"Sorting error: {header.text}")
        except Exception as e:
            self.failed_actions.append(f"Sorting test failed: {str(e)}")
