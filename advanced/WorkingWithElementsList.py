from selenium import webdriver
import time


class WorkingWithElementsList:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'

    def exercise_test(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(3)

        radio_button_list_xpath = "//input[@type='radio' and @name='cars']"
        radio_buttons_list = driver.find_elements_by_xpath(radio_button_list_xpath)

        size_of_radio_button_list = len(radio_buttons_list)
        print("Number of radio elements: " + str(size_of_radio_button_list))

        for radio_button in radio_buttons_list:
            is_radio_button_selected = radio_button.is_selected()

            if not is_radio_button_selected:
                radio_button.click()
                time.sleep(2)


def main():
    working_with_elements_list = WorkingWithElementsList()
    working_with_elements_list.exercise_test()


if __name__ == "__main__":
    main()
