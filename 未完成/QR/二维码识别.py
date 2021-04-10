from PIL import ImageGrab
from PIL import Image
import os
from pyzbar import pyzbar
import webbrowser
results: any


def grab():
    """
    截屏并解析二维码，
    注意截屏时二维码不被遮挡。
    """
    global results
    img = ImageGrab.grab()  # 截屏
    print('正在解码...')
    results = pyzbar.decode(image=img, symbols=[pyzbar.ZBarSymbol.QRCODE])  # 解码
    if len(results):  # 打印解析结果
        print('QR信息：')
        print(results)
        print('-'*10)
        for result in results:
            print('二维码地址：\n'+result.data.decode("utf-8"))
    else:
        print("Can not recognize.\n请确保二维码不被遮挡")
        if input('按回车再次识别，输入其他退出') == '':
            grab()
        else:
            exit()


def decode_qr_code(code_img_path):
    """
    指定文件图片解析，注意文件路径及名称完整
    :param code_img_path: 需要解析的图片路径
    :return: 返回解析结果
    """
    if not os.path.exists(code_img_path):
        raise FileExistsError(code_img_path)

    # Here, set only recognize QR Code and ignore other type of code
    return pyzbar.decode(Image.open(code_img_path), symbols=[pyzbar.ZBarSymbol.QRCODE])


def get_results(qr_path):
    """
    指定文件识别时使用，注意文件路径及名称完整
    :param qr_path: 需要解析的图片路径
    """
    global results
    print("正在解码...")
    results = decode_qr_code(qr_path)  # 解析结果
    if len(results):  # 打印解析结果
        print('QR信息：')
        print(results)
        print('-' * 10)
        for result in results:
            print('二维码地址：\n'+result.data.decode("utf-8"))
    else:
        print("Can not recognize.")


def open_url():
    """
    打开解析出的网址
    """
    if input('按回车打开网址，输入其他则退出') == '':
        for result in results:
            webbrowser.open(url=result.data.decode('utf-8'))
    else:
        exit()


# 选择模式
choice = input('输入1截屏识别二维码，注意二维码要在屏幕不被遮挡\n输入2识别指定文件二维码，\n输入其他退出：')
if choice == str(1):
    grab()
    open_url()
elif choice == str(2):
    path = input('请输入待识别文件(注意要完整路径加后缀)：\n')
    get_results(path)
    open_url()
else:
    exit()
