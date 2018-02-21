from selenium import webdriver


class RunEdgeTests:

    def __init__(self, url="http://www.letskodeit.com"):
        self.url = url

    def test(self):
        driver = webdriver.Edge()
        driver.get(self.url)


if __name__ == '__main__':
    edge = RunEdgeTests()
    edge.test()
