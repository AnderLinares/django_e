import requests
from bs4 import BeautifulSoup
import pytesseract
import io
from PIL import Image
url = "https://www.sunarp.gob.pe/ConsultaVehicular/"

session = requests.Session()
formdata = {
    "__EVENTTARGET": "",
    "__EVENTARGUMENT": "",
    "captch_cv_ClientState": {},
    "_CurrentGuid_captch_cv": "",
    "__VIEWSTATE": "/wEPDwULLTExNzU2MjY4NDcPZBYCAgMPZBYEAgMPFgIeB1Zpc2libGVoFgICAQ8PFgQeBFRleHRlHwBoZGQCBQ8WAh8AZxYCAgEPZBYCAgEPZBYKAgEPDxYCHwFlZGQCBw8PFgIfAQUqTm8gc2UgZW5jb250cmFyb24gZGF0b3MgcGFyYSBsYSBQbGFjYSBOby4uZGQCCQ8WAh4Fc3R5bGUFHnZpc2liaWxpdHk6aGlkZGVuO2RpcGxheTpub25lO2QCCw9kFhhmD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIBD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAICD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIDD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIED2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIFD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIGD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIHD2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIID2QWBGYPZBYCAgEPDxYCHwFlZGQCAQ9kFgICAQ8PFgIfAWVkZAIJD2QWAmYPZBYCAgEPDxYCHwFlZGQCCg9kFgRmD2QWAgIBDw8WAh8BZWRkAgEPZBYCAgEPDxYCHwFlZGQCCw9kFgRmD2QWAgIBDw8WAh8BZWRkAgEPZBYCAgEPDxYCHwFlZGQCDQ8PFgIfAWVkZBgBBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WAgUJY2FwdGNoX2N2BQljYXB0Y2hfY3YPPVQhyuBuf/iFbyFvIEJemyBheRTmF6ehS8MIY1Y5PA==",
    "__VIEWSTATEGENERATOR": "",
    "__EVENTVALIDATION": "/wEdAAQDMsQ3Zjx5Ji/YXMx2SgLPZ9s5VvBihdTWFzePQULU9SmvrUibYCHeLKKRGtnR5yeZf5MUp2golT/J9ICuDcwjcvM48o+AcQvUVDzcKchUmMs4vLUHMGllOT2upAOhQW4=",
    "txtNoPlac": "ABI453",
    "btn_buscar": "Buscar",
    "txtCaptcha": "ci6syl9e"
}
result = session.post(url, data=formdata)
result = BeautifulSoup(result.content, 'html.parser')
table = result.find("img", id="captch_cv")
print(table)
url_captcha = "https://www.sunarp.gob.pe" + table['src']
request_url = session.get(url_captcha)
captcha = pytesseract.image_to_string(Image.open(io.BytesIO(request_url.content)))
print(captcha)