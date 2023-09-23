import email as email_parse
import os
import poplib
import re
import time
import traceback

import autoit
import photoshop.api as ps
from photoshop.api import ExportType
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from photoshop import Session


class Register_Options:
    def __init__(self, username_github: str, pass_github: str, username_mail: str, pass_mail: str):
        self.username_github = username_github
        self.pass_github = pass_github
        self.username_mail = username_mail
        self.pass_mail = pass_mail


def register_github_student_pack(driver: WebDriver, register_options: Register_Options):
    go_to_url(driver, "https://education.github.com/discount_requests/application")
    singIn(driver, register_options)
    # Scroll down to the bottom of the page.
    actions = ActionChains(driver)
    actions.move_to_element(driver.find_element(By.TAG_NAME, 'body'))
    actions.scroll_by_amount(0, 1200)
    actions.perform()
    if not driver.current_url.__contains__('additional_information'):
        wait_util(
            driver, By.XPATH,
            '/html/body/div/main/div/div/div[1]/div/div[4]/div/form/div[1]/fieldset/div/div[1]/div/label/div'
            , 5).click()
        time.sleep(1)

        wait_util(
            driver, By.XPATH, "/html/body/div/main/div/div/div[1]/div/div[4]/div/form/div[1]/div[5]/div/auto-complete/input"
            , 5).send_keys("Ananda Mohan College")

        time.sleep(2)

        wait_util(
            driver, By.XPATH, "/html/body/div/main/div/div/div[1]/div/div[4]/div/form/div[2]/textarea"
            , 5).send_keys("for learn")

        driver.find_element(By.XPATH, '/html/body/div/main/div/div/div[1]/div/div[4]/div/form/div[4]/input').click()

        time.sleep(3)

    # Find the element that represents the file upload field.
    upload_buttion = driver.find_element(By.XPATH,
                                         "/html/body/div/main/div/div/div[1]/div[2]/form/div[1]/div[2]/div[4]/button")
    upload_buttion.click()

    time.sleep(3)
    image = getImage(register_options.username_github)

    autoit.control_send("[CLASS:#32770]", "Edit1", image)
    autoit.control_click("[CLASS:#32770]", "Button1")
    time.sleep(3)
    dropdown = Select(driver.find_element(By.ID, 'discount_request_attachment_proof_type'))
    dropdown.select_by_value("2. Dated official/unofficial transcript - Fair")
    time.sleep(10)
    wait_util(
        driver, By.XPATH, "/html/body/div/main/div/div/div[1]/div[2]/form/div[7]/input"
        , 10).click()
    wait_util(
        driver, By.XPATH, "/html/body/div/div[1]/div/h1"
        , 10)
    submit_success = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/h1").text
    if submit_success.__contains__('Thanks for submitting'):
        print("submit success")


def go_to_url(driver: WebDriver, url: str):
    driver.get(url)


def wait_util(driver: WebDriver, by: str, element: str, time_wait: int) -> any:
    return WebDriverWait(driver, time_wait).until(
        visibility_of_element_located((by, element)))


def get_code_from_mail(email_username: str, email_password: str) -> str:
    try:
        email = email_username
        password = email_password
        pop3_server = "outlook.office365.com"
        server = poplib.POP3_SSL(pop3_server, 995)

        # ssl加密后使用
        # server = poplib.POP3_SSL('pop.163.com', '995')
        print(server.set_debuglevel(1))  # 打印与服务器交互信息
        print(server.getwelcome())  # pop有欢迎信息
        server.user(email)
        server.pass_(password)
        print('Messages: %s. Size: %s' % server.stat())
        print(email + ": successful")
        num_messages = len(server.list()[1])
        result: str = ''
        for i in range(num_messages):
            # get the message at index i
            message_lines = server.retr(i + 1)[1]
            # join the message lines into a single string
            message_text = b'\n'.join(message_lines)
            # print draw
            raw_text: str = message_text.decode('utf-8')
            # parse the message text into an email object
            message = email_parse.message_from_bytes(message_text)
            # print the subject and sender of the message
            sub: str = message["subject"];
            sender: str = message["from"];
            print(f'Subject: {sub}')
            print(f'From: {sender}')
            if sender.__contains__('noreply@github.com'):
                # and sub.__contains__('Please verify your device'):
                # Create a regular expression pattern to match the text pattern.
                pattern = r'Verification code: (\d{6})'

                # Use the re.search() function to search for the pattern in the email.
                match = re.search(pattern, raw_text)

                # If the pattern is found, extract the 6 digits after it.
                if match:
                    print(raw_text)
                    result = match.group(1)
                # result = re.findall("[0-9]{6}", content)[0]
        return result
    except Exception as ex:
        print(ex)
        traceback.print_exc()
        return ''


def singIn(driver: WebDriver, register_options):
    wait_util(driver, By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/input[2]", 5).send_keys(
        register_options.username_github)
    time.sleep(1)
    wait_util(driver, By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/form/div/input[1]", 5).send_keys(
        register_options.pass_github + Keys.ENTER)
    time.sleep(3)
    if driver.page_source.__contains__('We just sent your authentication code via email'):
        try:
            code = get_code_from_mail(register_options.username_mail, register_options.pass_mail)
            if code == '':
                raise ValueError('Khong get dc code tu mail ' + register_options.username_mail)
            wait_util(
                driver, By.XPATH, "/html/body/div[1]/div[3]/main/div/div[3]/div[2]/div[2]/form/input[2]", 2).send_keys(
                code)
        except Exception as ex:
            ex.with_traceback()
def getImage(name : str) -> str:
    jpg = rf'C:\Users\daoma\PycharmProjects\gologinpython\{name}.jpg'
    if os.path.exists(jpg):
        return jpg
    app = ps.Application()
    doc = app.activeDocument
    fullname_first = doc.artLayers["fullname_first"]
    fullname_first.textItem.contents = name+' Roy'

    fullname_body = doc.artLayers["fullname_body"]
    fullname_body.textItem.contents = name+' Roy'

    first_name = doc.artLayers["first_name"]
    first_name.textItem.contents = name

    first_name = doc.artLayers["last_name"]
    first_name.textItem.contents = 'Roy'
    target_width = 3120
    target_height = 4038
    doc.resizeImage(target_width, target_height)

    # # save to jpg
    # doc.saveAs(jpg, options, asCopy=True)
    options = ps.JPEGSaveOptions(quality=5)
    # Export the image as JPEG
    # doc.exportDocument(jpg, jpeg_options, as_copy=True, file_system=FileSystemType.LOCAL)
    doc.saveAs(jpg, options, asCopy=True)
    return jpg


# if __name__ == '__main__':
    # app = ps.Application()
    # doc = app.activeDocument
    # fullname_first = doc.artLayers["fullname_first"]
    # fullname_first.textItem.contents = 'Daomanh Roy'
    #
    # fullname_body = doc.artLayers["fullname_body"]
    # fullname_body.textItem.contents = 'Daomanh Roy'
    #
    # first_name = doc.artLayers["first_name"]
    # first_name.textItem.contents = 'Daomanh'
    #
    # first_name = doc.artLayers["last_name"]
    # first_name.textItem.contents = 'Roy'
    # target_width = 3120
    # target_height = 4038
    # doc.resizeImage(target_width, target_height)
    #
    # # # save to jpg
    # jpg = r'C:\Users\daoma\PycharmProjects\gologinpython\text.jpg'
    # # doc.saveAs(jpg, options, asCopy=True)
    # options = ps.JPEGSaveOptions(quality=5)
    # # Export the image as JPEG
    # # doc.exportDocument(jpg, jpeg_options, as_copy=True, file_system=FileSystemType.LOCAL)
    # doc.saveAs(jpg, options, asCopy=True)
    # doc.exportDocument(jpg, exportAs=ps.ExportType.SaveForWeb, options=jpeg_options)
    # app.doJavaScript(f'alert("save to jpg: {jpg}")')