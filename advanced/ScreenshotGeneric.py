from selenium import webdriver
import time


class ScreenshotGeneric:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com'
        self.destination_catalog_for_screenshots = 'C:\\Users\\mariu\\Desktop\\SeleniumScreenshots\\'

    def exercise(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(self.url)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys('abc@gmail.com')
        driver.find_element_by_id('user_password').send_keys('abc')
        driver.find_element_by_name('commit').click()

        filename = 'test.png'

        self.take_screenshot(driver)

    def create_full_path_for_screenshot(self, filename):
        '''
        Creates full path for save_screenshot method
        :param filename:
        :return full_screenshot_path:
        '''
        full_screenshot_path = self.destination_catalog_for_screenshots + filename
        return full_screenshot_path

    def take_screenshot(self, driver):
        '''
        Takes screenshot of current web page
        :param driver:
        :return:
        '''
        filename = str(round(time.time()*1000)) + '.png'
        try:
            driver.save_screenshot(self.create_full_path_for_screenshot(filename))
            print("Screenshot has been saved in " + self.destination_catalog_for_screenshots +
                  '\nunder name ' + filename)
        except Exception as e:
            print('Issue: ' + str(e))


def main():
    screenshot = ScreenshotGeneric()
    screenshot.exercise()


if __name__ == '__main__':
    main()
