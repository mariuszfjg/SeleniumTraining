from selenium import webdriver
import time


class CalendarSelection:

    def __init__(self):
        self.url = "http://www.expedia.com"

    def test1(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        driver.implicitly_wait(3)

        driver.find_element_by_id('tab-flight-tab-hp').click()

        departing_field = driver.find_element_by_id('flight-departing-hp-flight')

        departing_field.click()

        date_to_select_xpath = "//button" \
                               "[@class='datepicker-cal-date']" \
                               "[@data-year='2018']" \
                               "[@data-month='1']" \
                               "[contains(text(), '25')]"
        date_to_select = driver.find_element_by_xpath(date_to_select_xpath)
        date_to_select.click()

        time.sleep(3)
        driver.quit()


def main():
    calendar_selection = CalendarSelection()
    calendar_selection.test1()


if __name__ == '__main__':
    main()
