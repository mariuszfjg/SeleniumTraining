from selenium import webdriver


class Screenshot:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com'


    def exercise(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(3)
        driver.get(self.url)

        driver.find_element_by_link_text("Login").click()
        driver.find_element_by_id("user_email").send_keys('abc@gmail.com')
        driver.find_element_by_id('user_password').send_keys('abc')
        driver.find_element_by_name('commit').click()

        destination_path_for_screenshot = 'C:\\Users\\mariu\\Desktop\\test.png'

        try:
            driver.save_screenshot(destination_path_for_screenshot)
            print("Screenshot has been saved in " + destination_path_for_screenshot)
        except Exception as e:
            print('Issue: ' + str(e))


def main():
    screenshot = Screenshot()
    screenshot.exercise()


if __name__ == '__main__':
    main()
