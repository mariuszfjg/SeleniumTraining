from selenium import webdriver
import selenium.common.exceptions as sce
from selenium.webdriver.support.select import Select


class WorkingWithHiddenElements:

    def __init__(self):
        self.url_letskodeit = 'https://letskodeit.teachable.com/p/practice'
        self.url_expedia = 'https://www.expedia.com'

    def exercise_letskodeit_hidden_element(self):
        driver = webdriver.Chrome()
        driver.get(self.url_letskodeit)
        driver.implicitly_wait(3)

        text_box_element = driver.find_element_by_id('displayed-text')

        hide_button = driver.find_element_by_id('hide-textbox')
        show_button = driver.find_element_by_id('show-textbox')

        print("click hide button")
        hide_button.click()

        text_box_element_status = text_box_element.is_displayed()
        print('Text box is displayed? : ' + str(text_box_element_status))

        print("click show button")
        show_button.click()

        text_box_element_status = text_box_element.is_displayed()
        print('Text box is displayed? : ' + str(text_box_element_status))

        driver.quit()

    def exercise_expedia_hidden_element(self):
        driver = webdriver.Chrome()
        driver.get(self.url_expedia)
        driver.implicitly_wait(3)

        dropdown_children_amount = driver.find_element_by_id("package-1-children-hp-package")
        selector_dropdown_children_amount = Select(dropdown_children_amount)
        print("Selecting 0 children")
        selector_dropdown_children_amount.select_by_visible_text('0')

        self.is_selector_age_children_displayed(driver)

        selector_dropdown_children_amount.select_by_visible_text('1')

        self.is_selector_age_children_displayed(driver)

        driver.quit()

    def is_selector_age_children_displayed(self, driver):
        try:
            children_age_element = driver.find_element_by_id("package-1-age-select-1-hp-package")
            children_age_element_status = children_age_element.is_displayed()
            print("Status of element 'children-age-selector' is: " + str(children_age_element_status))
        except sce.NoSuchElementException:
            print("DropDown Element for choosing Children age is not available")


def main():
    working_with_hidden_element = WorkingWithHiddenElements()
    working_with_hidden_element.exercise_letskodeit_hidden_element()
    working_with_hidden_element.exercise_expedia_hidden_element()

if __name__ == "__main__":
    main()
