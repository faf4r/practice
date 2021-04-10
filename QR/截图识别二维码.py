from PIL import ImageGrab
from pyzbar import pyzbar
import webbrowser
results: any


def grab():
    """
    截屏并解析二维码，
    并打印二维码信息和解析出的网站。
    ！！！
    注意二维码不要被挡住
    """
    global results
    print('正在截屏...')
    img = ImageGrab.grab()  # 截屏
    print('正在解码...')
    results = pyzbar.decode(image=img, symbols=[pyzbar.ZBarSymbol.QRCODE])  # 解码
    if len(results):
        print('QR信息：')
        print(results)
        print('-'*10)
        for result in results:
            print('二维码地址：\n'+result.data.decode('utf-8'))
    else:
        print("Can not recognize.\n请确保二维码不被遮挡")
        if input('按回车再次识别，输入其他退出') == '':
            grab()
        else:
            exit()


def leave():
    """
    不打开网站时使用，便于用户复制网址。
    """
    if input('按回车退出') == '':
        exit()
    else:
        exit()


def choose():
    """
    选择模式：自动转到网页或者只解析。
    ！只解析可查看二维码完整信息。
    """
    choice = input('!!!注意二维码不要被遮挡!!!\n按回车打开网址，输入其他将不打开网址')
    if choice == '':
        grab()
        for result in results:
            webbrowser.open(url=result.data.decode('utf-8'))  # 打开网址
    else:
        grab()
        leave()


if __name__ == '__main__':
    choose()
