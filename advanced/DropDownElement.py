from selenium import webdriver
import time
from selenium.webdriver.support.select import Select


class DropDownElementExercise:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'

    def exercise_test(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(3)

        element = driver.find_element_by_id('carselect')
        select_element = Select(element)

        select_element.select_by_value('benz')
        time.sleep(2)

        select_element.select_by_index('2')
        time.sleep(2)

        select_element.select_by_visible_text('BMW')
        time.sleep(2)

        select_element.select_by_index(2)
        time.sleep(2)


def main():
    dropdown_element = DropDownElementExercise()
    dropdown_element.exercise_test()


if __name__ == "__main__":
    main()
