from selenium import webdriver
import selenium.common.exceptions as sce
import time

class RadioAndCheckbox:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'
        self.radio_buttons = {'bmw' : None,
                          'benz': None,
                          'honda': None,
                          }
        self.checkboxes = {'bmw' : None,
                          'benz': None,
                          'honda': None,
                          }

    def exercise(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(10)
        self.find_all_elements(driver)
        self.select_all_elements_one_by_one()

    def find_all_elements(self, driver):
        self.find_radio_buttons(driver)
        self.find_checkboxes(driver)

    def find_radio_buttons(self, driver):
        for key in self.radio_buttons.keys():
            element_id = "{0}radio".format(key)
            self.radio_buttons[key] = self.find_element_by_id_handling_NoSuchElementException(element_id, driver)

    def find_checkboxes(self, driver):
        for key in self.checkboxes.keys():
            element_id = "{0}check".format(key)
            self.checkboxes[key] = self.find_element_by_id_handling_NoSuchElementException(element_id, driver)

    @staticmethod
    def find_element_by_id_handling_NoSuchElementException(element_id, driver):
        try:
            element = driver.find_element_by_id(element_id)
            print("Found element " + element_id)
            return element
        except sce.NoSuchElementException:
            print("Could not find element with id " + element_id)

    def select_all_elements_one_by_one(self):
        self.select_all_radio_buttons_one_by_one()
        self.select_all_checkboxes_one_by_one()

    def select_all_radio_buttons_one_by_one(self):
        for radio_button_key, radio_button_element in self.radio_buttons.iteritems():
            if radio_button_element is not None:
                print('Clicking Radio Button ' + radio_button_key)
                time.sleep(2)
                radio_button_element.click()
                self.message_for_radio_button()

    def select_all_checkboxes_one_by_one(self):
        for checkbox_key, checkbox_element in self.checkboxes.iteritems():
            if checkbox_element is not None:
                print('Clicking Checkbox ' + checkbox_key)
                time.sleep(2)
                checkbox_element.click()
                self.message_for_checkboxes()

    def message_for_radio_button(self):
        for radio_button in self.radio_buttons.keys():
            state_of_radio_button = self.radio_buttons[radio_button].is_selected()
            print("Is " + radio_button + " selected? --> " + str(state_of_radio_button))

    def message_for_checkboxes(self):
        for checkbox in self.checkboxes.keys():
            state_of_checkbox = self.checkboxes[checkbox].is_selected()
            print("Is " + checkbox + " selected? --> " + str(state_of_checkbox))


def main():
    radio_and_checkbox = RadioAndCheckbox()
    radio_and_checkbox.exercise()


if __name__ == '__main__':
    main()
