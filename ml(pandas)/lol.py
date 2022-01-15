import pyqrcode
from pyz

qr = pyqrcode.create("hello")
qr.png('abc.png', scale=8)