from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Optional
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

def open_netflix() -> Optional[str]:
    
    chrome_options = Options()

    # Run Chrome in headless mode
    # chrome_options.add_argument("--headless")
    # Set various browser preferences and arguments for headless mode
    chrome_options.add_argument(
        "--window-size=1366,768 --no-sandbox --disable-dev-shm-usage --disable-gpu --disable-notifications")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        "(KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
    chrome_options.add_experimental_option("prefs", {
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "useAutomationExtension": False,
        "profile.default_content_setting_values.notifications": 2 
    })
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options)
    driver.get('https://www.netflix.com/watch/81739231?trackId=200257858')
    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="appMountPoint"]/div/div[2]/div/div[2]/a'))).click()
    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div[1]/div/div[1]/input'))).send_keys(
            'gurusai21102000@gmail.com')
    time.sleep(5)
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/div[2]/div/div/input'))).send_keys(
            '#Chilukuri21')
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div/form/button').click()
    time.sleep(5)

    driver.get('https://www.netflix.com/watch/81739231?trackId=200257858')
    
    time.sleep(3)
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-uia="player-skip-intro"]'))).click()
    
    time.sleep(3)
    WebDriverWait(driver, 1500).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-uia="next-episode-seamless-button"]'))).click()
    time.sleep(3)
    # next_episode = '//*[@id="appMountPoint"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/button[2]'
    # print(check_exists_by_xpath(driver,next_episode))
    # while(True):
    #     if(check_exists_by_xpath(driver,next_episode)):
    #         WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
    #         (By.XPATH, next_episode))).click()
    #         break
            
    
    time.sleep(150)


def check_exists_by_xpath(webdriver,xpath):
    try:
        webdriver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True
   
open_netflix()
# /div/div[2]/button

# <button class="button-primary watch-video--skip-content-button medium hasLabel default-ltr-cache-1mjzmhv" data-uia="player-skip-intro" type="button"><span class="default-ltr-cache-bf8b0m">Skip Intro</span></button>