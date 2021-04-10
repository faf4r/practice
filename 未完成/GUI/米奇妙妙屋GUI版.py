from PIL import ImageGrab
from pyzbar import pyzbar
import tkinter as tk
import webbrowser

results: any


def grab():
    img = ImageGrab.grab()
    global results
    results = pyzbar.decode(image=img, symbols=[pyzbar.ZBarSymbol.QRCODE])
    urls = []
    if len(results):
        for result in results:
            urls.append(result.data.decode('utf-8'))
        label['text'] = urls
        button0.pack()
    else:
        label['text'] = '未扫描到二维码'


def open_url():
    for result in results:
        webbrowser.open(url=result.data.decode('utf-8'))


win = tk.Tk()
win.title('米奇妙妙屋GUI版')

button = tk.Button(win, text='截屏二维码', command=grab)
label = tk.Label(win, text='结果')
button0 = tk.Button(win, text='打开网站', command=open_url)

button.pack()
label.pack()
win.mainloop()
