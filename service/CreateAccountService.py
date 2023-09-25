import time

from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

import ImapMail
from model import DTO
from service import Utils

NOPECHA_KEY = 'I-YB20YNPT9DUE'


def start(driver: WebDriver, register_options: DTO.Register_Options):
    Utils.go_to_url(driver, f"https://nopecha.com/setup#{NOPECHA_KEY}")
    time.sleep(3)
    Utils.go_to_url(driver, 'https://github.com/')
    time.sleep(2)
    Utils.wait_util(driver, By.XPATH, '/html/body/div[1]/div[1]/header/div/div[2]/div/div/a', 2).click()
    time.sleep(2)
    print('SINGUP ...')
    Utils.wait_util(driver, By.ID, 'email', 3).send_keys(register_options.username_mail)
    time.sleep(2)
    Utils.wait_util(driver, By.ID, 'email', 3).send_keys(Keys.ENTER)
    time.sleep(1)
    Utils.wait_util(driver, By.ID, 'password', 3).send_keys(register_options.pass_github)
    time.sleep(2)
    Utils.wait_util(driver, By.ID, 'password', 3).send_keys(Keys.ENTER)


    Utils.wait_util(driver, By.ID, 'login', 3).send_keys(register_options.username_github)
    time.sleep(2)
    Utils.wait_util(driver, By.ID, 'login', 3).send_keys(Keys.ENTER)

    Utils.wait_util(driver, By.ID, 'opt_in', 3).send_keys('n')
    time.sleep(2)
    Utils.wait_util(driver, By.ID, 'opt_in', 3).send_keys(Keys.ENTER)


    time.sleep(1)
    Utils.wait_util_clickable(driver, By.ID, 'signup_button', 30).click()
    time.sleep(3)
    code = ImapMail.get_code_from_mail(register_options.username_mail, register_options.pass_mail, r'(\d{8})')
    print('code : ' + code)
    Utils.wait_util(driver, By.XPATH, '/html/body/div[1]/div[5]/main/div[2]/div[1]/div[1]/div/launch-code/form/fieldset/div/input[1]', 30).send_keys(code)
    time.sleep(1)