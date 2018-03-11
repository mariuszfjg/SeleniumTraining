from selenium import webdriver


class WindowSize:

    def __init__(self):
        self.url = 'https://www.google.com'

    def test(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(self.url)
        driver.implicitly_wait(3)

        height = driver.execute_script("return window.innerHeight;")
        width = driver.execute_script("return window.innerWidth;")

        print("Window has size (H/W) : {0}px/{1}px".format(str(height),
                                                       str(width)
                                                       ))

        driver.quit()


def main():
    windows_size = WindowSize()
    windows_size.test()


if __name__ == '__main__':
    main()

