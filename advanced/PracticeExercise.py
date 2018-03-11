from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class PracticeExercise:

    def __init__(self):
        self.url = 'https://www.airbnb.pl/'
        self.search_bar = None
        self.date_picker = None
        self.guest_picker = None

    def exercise(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(5)

        self.get_search_bar_element(driver)
        self.search_location("Turyn", driver)

        self.pick_date_actions(driver)
        self.pick_guests_actions(driver)

        time.sleep(5)
        driver.quit()

    def get_search_bar_element(self, driver):
        search_bar_id = "GeocompleteController-via-SearchBarV2-SearchBarV2"
        search_bar_elements_list = driver.find_elements_by_id(search_bar_id)
        self.get_visible_search_bar_element(search_bar_elements_list)

    def get_visible_search_bar_element(self, search_bar_elements):
        for search_bar_element in search_bar_elements:
            if search_bar_element.is_displayed():
                self.search_bar = search_bar_element
                break

    def search_location(self, location, driver):
        hover_action = ActionChains(driver).move_to_element(self.search_bar)
        hover_action.perform()
        self.search_bar.click()
        self.search_bar.clear()
        self.search_bar.send_keys(location)
        self.search_bar.submit()

    def pick_date_actions(self, driver):
        self.click_on_date_picker(driver)
        self.select_dates_range(driver)
        self.confirm_date_selection(driver)

    @staticmethod
    def confirm_date_selection(driver):
        confirm_button_xpath = "//div[@id='menuItemComponent-date_picker']//span[contains(@data-action, 'save')]"
        confirm_button = driver.find_element_by_xpath(confirm_button_xpath)
        confirm_button.click()

    def click_on_date_picker(self, driver):
        date_picker_xpath = "//button[@aria-controls='menuItemComponent-date_picker']"
        self.date_picker = driver.find_element_by_xpath(date_picker_xpath)
        self.date_picker.click()

    def select_dates_range(self, driver):
        list_of_date_elements = self.generate_list_of_date_elements(driver)
        for i in range(len(list_of_date_elements)):
            if i == 0 or i == len(list_of_date_elements) - 1:
                list_of_date_elements[i].click()
            else:
                hover_action = ActionChains(driver).move_to_element(list_of_date_elements[i])
                hover_action.perform()

    @staticmethod
    def generate_list_of_date_elements(driver):
        list_of_date_elements = []
        for day_number in range(23, 28):
            date_element_xpath = "//div[@id='menuItemComponent-date_picker']//td[contains(text(),{0}) and contains(@aria-label, 'lutego')]"\
                                    .format(day_number)
            list_of_date_elements.append(driver.find_element_by_xpath(date_element_xpath))
        return list_of_date_elements

    def pick_guests_actions(self, driver):
        self.click_on_guest_picker(driver)
        self.increment_number_of_guests(driver)
        self.confirm_guest_choice(driver)

    @staticmethod
    def click_on_guest_picker(driver):
        guest_picker_xpath = '//button[contains(@aria-controls,"menuItemComponent-guest_picker")]'
        guest_picker = driver.find_element_by_xpath(guest_picker_xpath)
        guest_picker.click()

    @staticmethod
    def increment_number_of_guests(driver, number_of_guests=1):
        change_adult_guest_amount_button_xpath = '//div[@id="menuItemComponent-guest_picker"]' \
                                                 '//button[@aria-controls="StepIncrementerRow-value-GuestCountFilter-via-GuestCountPanel' \
                                                 '-adults"] '
        change_adult_guest_amount_buttons = driver.find_elements_by_xpath(change_adult_guest_amount_button_xpath)
        increment_adult_guest_amount_button = change_adult_guest_amount_buttons[1]
        for guest in range(number_of_guests):
            increment_adult_guest_amount_button.click()

    @staticmethod
    def confirm_guest_choice(driver):
        confirm_guest_choice_button_xpath = '//div[@id="menuItemComponent-guest_picker"]//span[@data-action="save"]'
        confirm_guest_choice_button = driver.find_element_by_xpath(confirm_guest_choice_button_xpath)
        confirm_guest_choice_button.click()


def main():
    practice_exercise = PracticeExercise()
    practice_exercise.exercise()


if __name__ == "__main__":
    main()
