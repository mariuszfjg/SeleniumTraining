from selenium import webdriver
import time

class JavaScriptPopup:
    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'

    def exercise(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.maximize_window()
        driver.implicitly_wait(3)
        
        driver.find_element_by_id('name').send_keys('Mariusz')
        self.exercise_alert_popup(driver)
        self.exercise_confirm_popup(driver)

        driver.quit()

    def exercise_alert_popup(self, driver):
        driver.find_element_by_id('alertbtn').click()
        time.sleep(2)
        self.exercise_with_popup(driver, 'alert')

    def exercise_confirm_popup(self, driver):
        self.exercise_confirm_popup_accept_scenario(driver)
        self.exercise_confirm_popup_cancel_scenario(driver)

    def exercise_confirm_popup_accept_scenario(self, driver):
        driver.find_element_by_id('confirmbtn').click()
        time.sleep(2)
        self.exercise_with_popup(driver,
                                 'confirm')

    def exercise_confirm_popup_cancel_scenario(self, driver):
        driver.find_element_by_id('confirmbtn').click()
        time.sleep(2)
        self.exercise_with_popup(driver,
                                 'confirm',
                                 to_accept=False)

    def exercise_with_popup(self, driver, popup_type, to_accept=True):
        if popup_type=='confirm' and to_accept==False:
            popup = driver.switch_to.alert
            popup.dismiss()
            time.sleep(2)
        else:
            popup = driver.switch_to.alert
            popup.accept()
            time.sleep(2)


def main():
    java_script_popup = JavaScriptPopup()
    java_script_popup.exercise()


if __name__ == '__main__':
    main()
