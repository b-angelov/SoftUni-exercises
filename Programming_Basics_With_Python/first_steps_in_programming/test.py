import pyqrcode
import png
from pyqrcode import QRCode

link = "http://www.drugiaobzor.com/"
url = pyqrcode.create(link)
url.png("pypqr_code.png",scale=82)