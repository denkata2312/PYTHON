import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://www.mobile.bg/obiava-11707835305972543-dodge-challenger-srt-hellcat-6-2-hemi-nalichen'
url = pyqrcode.create(address)
url.png('hellcat.png', scale=8)