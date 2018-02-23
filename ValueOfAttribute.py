from selenium import webdriver
import time


class ValueOfAttribute:

    def __init__(self):
        self.url = 'https://letskodeit.teachable.com/p/practice'
        self.element = None
        self.values_of_attributes_dict = None

    def exercise_test(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        driver.implicitly_wait(3)

        self.element = driver.find_element_by_id("name")
        self.values_of_attributes_dict = {'class': None,
                                          'id': None,
                                          'name': None,
                                          'placeholder': None,
                                          'type': None
                                          }

        self.get_attributes_value()
        self.print_attributes_values()

    def get_attributes_value(self):
        for attribute_name in self.values_of_attributes_dict.keys():
            self.values_of_attributes_dict[attribute_name] = self.element.get_attribute(attribute_name)

    def print_attributes_values(self):
        for attribute_name in self.values_of_attributes_dict.keys():
            print("The Value of the attribute " + attribute_name +
                  " is: " + self.values_of_attributes_dict[attribute_name]
                  )


def main():
    value_of_attribute = ValueOfAttribute()
    value_of_attribute.exercise_test()


if __name__ == "__main__":
    main()
