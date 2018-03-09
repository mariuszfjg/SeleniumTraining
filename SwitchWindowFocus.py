from selenium import webdriver
import time


class SwitchWindowFocus:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'

    def exercise(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(self.url)

        main_window_handle = driver.current_window_handle

        open_new_window = driver.find_element_by_id('openwindow')
        open_new_window.click()
        time.sleep(2)

        #Switch to newly opened window
        all_handles = driver.window_handles

        for handle in all_handles:
            if handle not in main_window_handle:
                driver.switch_to.window(handle)
                search_box = driver.find_element_by_id('search-courses')
                search_box.send_keys('python')
                time.sleep(2)
                driver.close()
                break

        driver.switch_to.window(main_window_handle)

        driver.find_element_by_id('name').send_keys('abrakadabra')


        time.sleep(2)
        driver.quit()

def main():
    switch_window_focus = SwitchWindowFocus()
    switch_window_focus.exercise()


if __name__ == '__main__':
    main()
