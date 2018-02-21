from selenium import webdriver


class RunFFTests:

    def __init__(self, url='http://www.letskodeit.com'):
        self.url = url

    def test(self):
        driver = webdriver.Firefox()
        driver.get(self.url)


if __name__ == '__main__':
    ff = RunFFTests()
    ff.test()
