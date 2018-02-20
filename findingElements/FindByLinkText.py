from selenium import webdriver
import selenium.common.exceptions as sce


class FindByLinkText:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'
        # self.url = 'https://www.google.com'

    def test(self):
        driver = webdriver.Firefox()
        driver.get(self.url)

        try:
            element_by_link_text = driver.find_element_by_link_text('Login')

            if element_by_link_text is not None:
                print("Test passes by link text")
        except sce.NoSuchElementException:
            print("No element found by link text")
        finally:
            pass

        try:
            element_by_partial_link_text = driver.find_element_by_partial_link_text('Practi')
            if element_by_partial_link_text is not None:
                print("Test passes by partial link text")
        except sce.NoSuchElementException:
            print("No element found by partial link text Selector")
        finally:
            pass

        driver.quit()


if __name__ == "__main__":
    ff = FindByLinkText()
    ff.test()