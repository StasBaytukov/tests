from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TensorPage(BasePage):
    PEOPLE_POWER_BLOCK = (By.XPATH, "//h2[contains(text(), 'Сила в людях')]")
    MORE_LINK = (By.XPATH, "//a[contains(text(), 'Подробнее')]")
    ABOUT_PAGE_TITLE = (By.XPATH, "//h1[text()='О компании']")
    WORKING_SECTION_IMAGES = (By.CSS_SELECTOR, ".timeline__img")

    def is_people_power_visible(self):
        return self.is_element_visible(self.PEOPLE_POWER_BLOCK)

    def click_more(self):
        self.click(self.MORE_LINK)

    def is_about_page_visible(self):
        return self.is_element_visible(self.ABOUT_PAGE_TITLE)

    def get_image_sizes(self):
        images = self.find_elements(self.WORKING_SECTION_IMAGES)
        return [(img.size["height"], img.size["width"]) for img in images]
