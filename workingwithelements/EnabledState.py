from selenium import webdriver
import selenium.common.exceptions as sce


class EnabledState:

    def __init__(self):
        self.url = 'http://www.google.com'

    def is_enabled(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(3)

        e1 = driver.find_element_by_id("gs_htif0")
        print str(e1.id) + " is enabled? " + str(e1.is_enabled())

        e2 = driver.find_element_by_id("gs_taif0")
        print str(e2.id) + " is enabled? " + str(e2.is_enabled())

        e3 = driver.find_element_by_id("lst-ib")
        print str(e3.id) + " is enabled? " + str(e3.is_enabled())

        e3.clear()
        e3.send_keys("Letskodeit")
        e3.submit()

        driver.quit()

def main():
    enabled_state_object = EnabledState()
    enabled_state_object.is_enabled()


if __name__ == "__main__":
    main()
