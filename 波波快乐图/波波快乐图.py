import os
from PIL import Image
'''
请确保该文件与图片文件夹在同一目录内
'''

dir_name = '唯美img'
directory_name = dir_name
for filename in os.listdir(r"./"+directory_name):
        img=Image.open(directory_name + "/" + filename)
        img.show()



