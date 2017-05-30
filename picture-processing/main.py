#coding=utf-8

print("Hello World!\n")
from PIL import Image
im = Image.open("172438.png")
print(im.format, im.size, im.mode) #查看图片属性

