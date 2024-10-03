from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SbisPage(BasePage):
    CONTACTS_BUTTON = (By.LINK_TEXT, "Контакты")
    TENSOR_BANNER = (By.XPATH, "//img[contains(@alt, 'Тензор')]")

    def go_to_contacts(self):
        self.click(self.CONTACTS_BUTTON)

    def click_tensor_banner(self):
        self.click(self.TENSOR_BANNER)
