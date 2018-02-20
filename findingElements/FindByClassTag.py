from selenium import webdriver
import selenium.common.exceptions as sce


class FindByClassTag:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'
        # self.url = 'https://www.google.com'

    def test(self):
        driver = webdriver.Firefox()
        driver.get(self.url)

        try:
            elementByClassName= driver.find_element_by_class_name('inputs')
            elementByClassName.send_keys('testing the element')

            if elementByClassName is not None:
                print("Test passes by class name")
        except sce.NoSuchElementException:
            print("No element found by class name")
        finally:
            pass

        try:
            elementByTagName = driver.find_element_by_tag_name('a')
            elementByTagName.send_keys('Type something for fun ;)')

            if elementByTagName is not None:
                print("Test passes by tag name")
        except sce.NoSuchElementException:
            print("No element found by tag name Selector")
        finally:
            pass

        # driver.quit()


if __name__ == "__main__":
    ff = FindByClassTag()
    ff.test()