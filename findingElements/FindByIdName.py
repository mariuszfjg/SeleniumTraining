from selenium import webdriver

class FindByIdName:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/pages/practice'

    def test(self):
        driver = webdriver.Firefox()
        driver.get(self.url)

        element_by_id = driver.find_element_by_id('name')

        if element_by_id is not None:
            print("Found element by id")

        element_by_name = driver.find_element_by_name('show-hide')

        if element_by_name is not None:
            print("Found element by name")

        driver.quit()

if __name__ == "__main__":
    ff = FindByIdName()
    ff.test()