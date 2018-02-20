from selenium import webdriver
import selenium.common.exceptions as sce


class FindByXPathCSSSelector:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'
        # self.url = 'https://www.google.com'

    def test(self):
        driver = webdriver.Firefox()
        driver.get(self.url)

        try:
            element_by_xpath = driver.find_element_by_xpath("//input[@id='name']")

            if element_by_xpath is not None:
                print("Test passes by xpath")
        except sce.NoSuchElementException:
            print("No element found by xpath")
        finally:
            pass

        try:
            element_by_css = driver.find_element_by_css_selector("#displayed-text")

            if element_by_css is not None:
                print("Test passes by css")
        except sce.NoSuchElementException:
            print("No element found by CSS Selector")
        finally:
            pass

        driver.quit()


if __name__ == "__main__":
    ff = FindByXPathCSSSelector()
    ff.test()