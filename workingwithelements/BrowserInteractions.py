from selenium import webdriver
import selenium.common.exceptions as sce


class BrowserInteractions:

    def __init__(self):
        self.url_lets_kode_it_teachable_practice = 'https://letskodeit.teachable.com/pages/practice'
        self.url_lets_kode_it_teachable = 'https://letskodeit.teachable.com/'

    def test1(self):
        driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(self.url_lets_kode_it_teachable_practice)
        title_of_the_page = driver.title

        print("Title of the page is '" + title_of_the_page + "'")
        driver.refresh()
        driver.get('http://www.facebook.com')

        driver.back()

        driver.forward()

        source_of_the_page = driver.page_source
        print(source_of_the_page)

        driver.quit()

    def test2(self):
        driver = webdriver.Firefox()

        driver.maximize_window()
        driver.get(self.url_lets_kode_it_teachable)

        login_page_element_xpath = '//div[@id="navbar"]//a[contains(text(), "Login")]'
        login_page_element = driver.find_element_by_xpath(login_page_element_xpath)
        login_page_element.click()

        driver.implicitly_wait(3)

        login_page_url = driver.current_url

        if login_page_url != self.url_lets_kode_it_teachable:
            print("Page is changed, button was clicked")

        email_input_element_xpath = '//input[@id="user_email"]'
        password_input_element_xpath = '//input[@id="user_password"]'
        invalid_credentials_alert_xpath = '//div[contains(text(), "Invalid email or password")]'

        try:
            driver.find_element_by_xpath(invalid_credentials_alert_xpath)
            print("Wrong credentials alert found before entering any credentials... something is wrong")
        except sce.NoSuchElementException:
            print("No Alert found. Good to go!")
            pass

        email_input_element = driver.find_element_by_xpath(email_input_element_xpath)
        password_input_element = driver.find_element_by_xpath(password_input_element_xpath)

        email_input_element.send_keys("mariusz.figiel1@live.com")
        password_input_element.send_keys("some_password")

        login_button_xpath = '//form[@id="new_user"]//input[@value="Log In"]'
        login_button = driver.find_element_by_xpath(login_button_xpath)

        login_button.click()

        try:
            driver.find_element_by_xpath(invalid_credentials_alert_xpath)
            print("Wrong credentials alert found. It's good")
        except sce.NoSuchElementException:
            print("No Alert found. ... something went wrong")
            pass

        driver.quit()


def main():
    browser_interactions = BrowserInteractions()

    browser_interactions.test2()


if __name__ == '__main__':
    main()
