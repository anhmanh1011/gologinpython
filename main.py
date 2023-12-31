import traceback
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chromium.service import ChromiumService

import service.RegisterService as register
from service import GologinService
from webdriver_manager.chrome import ChromeDriverManager

#
# gl = GoLogin({
#     "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTBlNWEwZWUxOTZhMTEyMWVkZDY5NDEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTBlNWI1ZTM2MmEzNGNkZjFmNzhhNDAifQ.W5BDEO-yVBrtxVvqi78rf8GWQ4_Z-Yt4xAu7l0Fydyg",
#     "profile_id": '650eb8fc1e82d8240c6d9c36',
#     "credentials_enable_service": False,
#
# })
#
# # profile_id = gl.create({
# #     "name": 'profile_mac',
# #     "os": 'mac',
# #     "navigator": {
# #         "language": 'en-US',
# #         "userAgent": 'random',  # Your userAgent (if you don't want to change, leave it at 'random')
# #         "resolution": 'random',  # Your resolution (if you want a random resolution - set it to 'random')
# #         "platform": 'mac',
# #     },
# #     'proxyEnabled': False,  # Specify 'false' if not using proxy
# #     'proxy': {
# #         'mode': 'none',
# #         'autoProxyRegion': 'us'
# #         # 'host': '',
# #         # 'port': '',
# #         # 'username': '',
# #         # 'password': '',
# #     },
# #     "webRTC": {
# #         "mode": "alerted",
# #         "enabled": True,
# #     },
# # });
#
# # gl.update({
# #     "id": profile_id,
# #     "name": 'profile_mac2',
# #     'proxy': {
# #         'mode': 'none',
# #         'autoProxyRegion': 'us'
# #         # 'host': '',
# #         # 'port': '',
# #         # 'username': '',
# #         # 'password': '',
# #     },
# #     "geolocation": {
# #         "mode": "prompt",
# #         "enabled": True,
# #         "customize": True,
# #         "fillBasedOnIp": False,
# #         "latitude": 24.76176411847304,
# #         "longitude": 90.39498007665587,
# #         "accuracy": 10
# #     }
# # })


token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTBlNWEwZWUxOTZhMTEyMWVkZDY5NDEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTBlNWI1ZTM2MmEzNGNkZjFmNzhhNDAifQ.W5BDEO-yVBrtxVvqi78rf8GWQ4_Z-Yt4xAu7l0Fydyg'
if __name__ == '__main__':

    register_ops: register.Register_Options = register.Register_Options('weelerteetsy', 'Anhmanhbu8',
                                                                        'weelerteetsy@hotmail.com', 'I8MJ8A29',
                                                                        'Weelerteetsy', 'Roy')

    gl = GologinService.create_profile(register_ops.username_github, token)

    debugger_address = gl.start()
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", debugger_address)
    # cs = Service(executable_path=r'/Users/daoducmanh/PycharmProjects/gologinpython/chromedriver')
    # driver = webdriver.Chrome(service=cs, options=chrome_options)
    driver = webdriver.Chrome(ChromeDriverManager().install())

    try:
        register.register_github_student_pack(driver, register_ops)
    except Exception as ex:
        print(ex)
        traceback.print_exc()
# finally:
# driver.quit()
# gl.stop()
