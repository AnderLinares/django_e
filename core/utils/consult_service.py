import io

import pytesseract
import requests
from PIL import Image
from bs4 import BeautifulSoup


class SunatService(object):
    # need: pytesseract, BeautifulSoup, sudotesseract - ocr

    def __init__(self):
        super().__init__()
        self.sunat_url = 'http://www.sunat.gob.pe/cl-ti-itmrconsruc/'

    def ruc_info_from_dni(self, dni):
        session = requests.Session()
        session.get(self.sunat_url + 'jcrS03Alias')
        session.get(self.sunat_url + 'FrameCriterioBusquedaCelular.jsp')
        captcha = session.get(self.sunat_url + 'captcha?accion=image')
        captcha = pytesseract.image_to_string(Image.open(io.BytesIO(captcha.content)))
        print(captcha)
        formdata = {
            'accion': 'consPorTipdoc',
            'razSoc': '',
            'nroRuc': '',
            'nrodoc': dni,
            'contexto': 'ti - it',
            'search1': '',
            'codigo': captcha,
            'tQuery': 'on',
            'tipdoc': '1',
            'search2': dni,
            'coddpto': '',
            'codprov': '',
            'coddist': '',
            'search3': '',
        }

        result = session.post(self.sunat_url + 'jcrS03Alias', data=formdata)
        result = BeautifulSoup(result.content, 'html.parser')
        result = [td.text.strip() for td in
                  result.find('table', attrs={'cellpadding': 2}).find_all('td')]
        result = list(zip(*[iter(result)] * 4))
        return [dict(ruc=item[0], name=item[1],
                     location=item[2], status=item[3])
                for item in result
                ]

sunat = SunatService()
json_ruc = sunat.ruc_info_from_dni(dni='45851641')

