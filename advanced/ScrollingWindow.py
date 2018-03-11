from selenium import webdriver
import time


class ScrollingWindow:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        driver.implicitly_wait(3)

        # Scroll Down
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(1)

        # Scroll Up
        driver.execute_script("window.scrollBy(0, -500);")
        time.sleep(1)

        # Scroll element into vie
        element = driver.find_element_by_id('mousehover')
        driver.execute_script("arguments[0].scrollIntoView(true);",
                              element)
        time.sleep(1)
        driver.execute_script("window.scrollBy(0, -100)")
        time.sleep(1)

        # Native Way to scroll element into view
        driver.execute_script("window.scrollBy(0, -1000);")
        time.sleep(1)
        location = element.location_once_scrolled_into_view
        print("Location of an element: " + str(location))
        time.sleep(1)

        driver.quit()


def main():
    scrolling_window = ScrollingWindow()
    scrolling_window.test()


if __name__ == '__main__':
    main()

