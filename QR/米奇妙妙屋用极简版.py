from PIL import ImageGrab
from pyzbar import pyzbar
import webbrowser

input('回车启动')
img = ImageGrab.grab()
results = pyzbar.decode(image=img, symbols=[pyzbar.ZBarSymbol.QRCODE])
if len(results):
    for result in results:
        webbrowser.open(url=result.data.decode('utf-8'))
else:
    input('未扫描到二维码，回车退出')
