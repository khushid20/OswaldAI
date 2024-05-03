from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # Import time module


class music():
    def __init__(self):
        self.driver = webdriver.Chrome() # Initialize Chrome WebDriver

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element(By.XPATH, '//*[@id="video-title"]')  # Use By.XPATH to locate element
        video.click()
        time.sleep(1000)  # Wait for 1000 seconds

# assist = music()
# assist.play('Believer')


