import traceback

import psycopg2 as psycopg2
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from model import DTO
from service import GologinService, CreateAccountService

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTBkMDZiOTMyOTJmN2FiZWI4OWM0OGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTExNDI2Yzg4MzQzOTljZmFjNTIzMWIifQ.-ZxBVqSEk3Ne9-etxa77MXaUZLCGa3MxCrPv72HiCMU'
conn = psycopg2.connect(
    host="ec2-52-5-167-89.compute-1.amazonaws.com",
    database="d28mi0g1842i6e",
    user="dhlsgxhixjwmnn",
    password="69db8ea38414fdff967b063290c751a0e411574f8ba06f62da1329fbe4fcd507"
)

# Open a cursor to perform database operations
cur = conn.cursor()

if __name__ == '__main__':
    register_ops: DTO.Register_Options = DTO.Register_Options('mafusiwezorw', 'Anhmanhbu8',
                                                              'mafusiwezorw@outlook.com', 'KDbzLeXO62',
                                                              'Mafusiwezorw', 'Roy')
    gl = GologinService.create_empty(register_ops.username_github, token)

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    cs = Service(executable_path=r'/Users/daoducmanh/PycharmProjects/gologinpython/chromedriver')

    driver = webdriver.WebDriver(service=cs, options=chrome_options)
    try:
        CreateAccountService.start(driver, register_ops)
    except Exception as ex:
        print(ex)
        traceback.print_exc()
