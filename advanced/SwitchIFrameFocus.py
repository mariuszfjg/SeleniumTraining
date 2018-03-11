from selenium import webdriver
import time


class SwitchIFrame:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'

    def exercise(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(self.url)

        driver.execute_script('window.scrollBy(0, 1000);')

        driver.switch_to.frame('courses-iframe')

        time.sleep(3)

        search_box = driver.find_element_by_id('search-courses')
        search_box.send_keys('python')

        time.sleep(3)

        driver.switch_to.default_content()

        driver.execute_script('window.scrollBy(0, -1000);')
        time.sleep(3)
        driver.find_element_by_id('name').send_keys('Test success')


def main():
    switch_iframe_focus = SwitchIFrame()
    switch_iframe_focus.exercise()


if __name__ == '__main__':
    main()
