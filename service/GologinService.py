import json

import requests
from gologin import GoLogin

API_BASE_URL = 'https://api.gologin.com'


def create_profile(name: str, token: str) -> GoLogin:
    """

    :rtype: object
    """
    gl = GoLogin({
        "token": token,
    })

    profile_id = getProfileIdByName(token, name)

    if profile_id is None:
        profile_id = gl.create({
            "name": name,

            "navigator": {
                "language": 'en-US',
                "userAgent": 'random',  # Your userAgent (if you don't want to change, leave it at 'random')
                "resolution": 'random',  # Your resolution (if you want a random resolution - set it to 'random')
                "platform": 'mac',
            },
            'proxyEnabled': False,  # Specify 'false' if not using proxy
            'proxy': {
                'mode': 'none',
                'autoProxyRegion': 'us'
            },
            "webRTC": {
                "mode": "alerted",
                "enabled": True,
            },
            "geolocation": {
                "mode": "allow",
                "enabled": True,
                "customize": True,
                "fillBasedOnIp": False,
                "latitude": 24.76176411847304,
                "longitude": 90.39498007665587,
                "accuracy": 10
            },
            "extensions": {
                "enabled": False,
                "preloadCustom": False,
                "names": []
            },
            "chromeExtensions": [
                "dknlfmjaanfblgfdfebhijalfmhmjjjo"
            ]
        })
        print("create success: id: " + profile_id)
    else:
        print("profile existed id: " + profile_id)

    return GoLogin({
        "token": token,
        "profile_id": profile_id,
        "credentials_enable_service": False,
    })


def create_empty(name: str, token: str) -> GoLogin:
    """

    :rtype: object
    """
    gl = GoLogin({
        "token": token,
    })

    profile_id = getProfileIdByName(token, name)

    if profile_id is None:
        profile_id = gl.create({
            "name": name,
            'proxyEnabled': False,  # Specify 'false' if not using proxy
            'proxy': {
                'mode': 'none',
                'autoProxyRegion': 'us'
            },
            "chromeExtensions": [
                "dknlfmjaanfblgfdfebhijalfmhmjjjo"
            ]
        })
        print("create success: id: " + profile_id)
    else:
        print("profile existed id: " + profile_id)

    return GoLogin({
        "token": token,
        "profile_id": profile_id,
        "credentials_enable_service": False,
    })


def getProfileIdByName(token: str, name: str):
    url = API_BASE_URL + "/browser/v2"

    payload = {}
    headers = {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
    }

    response = json.loads(requests.request("GET", url, headers=headers, data=payload).content.decode('utf-8'))
    print(response)
    profiles = response.get('profiles')
    for profile in profiles:
        if profile.get('name') == name:
            return profile.get('id')
    return None


if __name__ == '__main__':
    create_profile('daomanhhh3',
                   'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NTBkMDZiOTMyOTJmN2FiZWI4OWM0OGEiLCJ0eXBlIjoiZGV2Iiwiand0aWQiOiI2NTExNDI2Yzg4MzQzOTljZmFjNTIzMWIifQ.-ZxBVqSEk3Ne9-etxa77MXaUZLCGa3MxCrPv72HiCMU')
    print('ok')
