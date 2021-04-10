import os
from PIL import Image
'''
请确保该文件与图片文件夹在同一目录内
'''

def show(dir_name):
    directory_name = dir_name
    for filename in os.listdir(r"./"+directory_name):
            img=Image.open(directory_name + "/" + filename)
            img.show()

if __name__ == '__main__':
    show('唯美img')
