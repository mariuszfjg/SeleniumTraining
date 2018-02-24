from selenium import webdriver


class AutoCompleteExercise:
    def __init__(self):
        self.url = 'https://www.southwest.com'
        self.search_bar = None
        self.auto_complete_menu = None
        self.auto_complete_menu_entries = None

    def test(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(self.url)

        auto_complete_menu_id = 'js-menu-wrapper'
        search_bar_id = 'air-city-departure'

        self.search_bar = driver.find_element_by_id(search_bar_id)
        self.put_string_into_search_bar("New")

        self.auto_complete_menu = driver.find_element_by_id(auto_complete_menu_id)
        self.auto_complete_menu_entries = self.auto_complete_menu.find_elements_by_xpath('.//li')

        self.print_proposed_entries_from_auto_complete_menu()

        driver.quit()

    def print_proposed_entries_from_auto_complete_menu(self):
        for entry in self.auto_complete_menu_entries:
            entry_position = str(self.auto_complete_menu_entries.index(entry) + 1)
            entry_text, entry_visibility = self.if_entry_not_visible_move_down_the_auto_complete_menu(entry)

            print("Proposed Entry no. " + entry_position +
                  "\tis " + entry_text +
                  "\t\tand visibility is set to " + entry_visibility)

    def if_entry_not_visible_move_down_the_auto_complete_menu(self, entry):
        if not entry.is_displayed():
            self.move_down_the_auto_complete_menu()
        return entry.text, str(entry.is_displayed())

    def move_down_the_auto_complete_menu(self):
        self.auto_complete_menu.find_element_by_xpath('.//following-sibling::div[not(contains(@class, "swa-g-disabled"))]').click()

    def put_string_into_search_bar(self, string):
        self.search_bar.click()
        self.search_bar.clear()
        self.search_bar.send_keys(string)


def main():
    auto_complete_exercise = AutoCompleteExercise()
    auto_complete_exercise.test()


if __name__ == '__main__':
    main()
