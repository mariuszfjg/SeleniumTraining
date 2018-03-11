from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class HoverMouseAction:
    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'
        self.driver = self.initialize_driver()

    def initialize_driver(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.maximize_window()

        return driver

    def scroll_element_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                              element)
        self.driver.execute_script("window.scrollBy(0, -200);")

    def exercise(self):
        self.driver.get(self.url)
        hover_element = self.driver.find_element_by_id('mousehover')

        self.scroll_element_into_view(hover_element)
        time.sleep(5)
        self.click_element_on_hover_dropdown("Top", hover_element)

        self.scroll_element_into_view(hover_element)
        time.sleep(5)
        self.click_element_on_hover_dropdown("Reload", hover_element)

        self.driver.quit()

    def click_element_on_hover_dropdown(self, element_text, hover_element):
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(hover_element).perform()
            time.sleep(3)
            item_to_click_xpath = '//div[@class="mouse-hover-content"]' \
                                  '//a[text()="' + element_text + '"]'
            self.driver.find_element_by_xpath(item_to_click_xpath).click()
            time.sleep(3)
        except:
            print("Click on " + element_text + " failed")

def main():
    hover_mouse_action = HoverMouseAction()
    hover_mouse_action.exercise()


if __name__ == '__main__':
    main()
