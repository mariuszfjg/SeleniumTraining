from selenium import webdriver


class RunChromeTests:

    def __init__(self, url="http://www.letskodeit.com"):
        self.url = url

    def test(self):
        driver = webdriver.Chrome()
        driver.get(self.url)


if __name__ == '__main__':
    chrome = RunChromeTests()
    chrome.test()
