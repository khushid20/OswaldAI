#
# from selenium import webdriver
# import time  # Import time module
#
# class infow():
#     def __init__(self):
#         self.driver = webdriver.Chrome()
#
#     def get_info(self, query):
#         self.query = query
#         self.driver.get(url="https://www.wikipedia.org")
#         search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
#         #search.click()
#         # search.send_keys(query)
#         # enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
#         # enter.click()
#
# assist = infow()
# assist.get_info("hello")
#
#
#
#
# # Add a wait before exiting
# '''time.sleep(1000)  # Wait for 10 seconds before exiting'''
#
from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Import time module

class infow():
    def __init__(self):
        self.driver = webdriver.Chrome()  # Initialize Chrome WebDriver

    def get_info(self, query):
        self.query = query
        self.driver.get("https://www.wikipedia.org")
        search_input = self.driver.find_element(By.ID, "searchInput")  # Use By.ID to locate element
        search_input.click()
        search_input.send_keys(query)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/fieldset/button')
        search_button.click()

        # Add a delay to keep the browser open for a few seconds
        time.sleep(1000) # Wait for 1000 seconds



