#!/usr/bin/env python
# coding=utf-8
# author=hades
# @Time    : 2018/4/26 14:31
# @File    : open_image.py
# @Software: PyCharm


from Tkinter import *
import os
from PIL import Image
from PIL import ImageGrab
import ctypes
import random

img_file_nmae  = []
def listfiels(path):
    path = path.replace("\\", "/")
    mlist = os.listdir(path)

    for m in mlist:
        mpath = os.path.join(path, m)
        if os.path.isfile(mpath):
            pt = os.path.abspath(mpath)
            if pt[-3:] == 'jpg':
                img_file_nmae.append(pt)
        else:
            pt = os.path.abspath(mpath)
            if pt[-3:]  == 'jpg':
                img_file_nmae.append(pt)
            listfiels(pt)

    return img_file_nmae





def screen_shot():
    try:
        dll = ctypes.cdll.LoadLibrary('PrScrn.dll')
    except Exception:
        print("Dll load error!")
        return 0
    else:
        try:
            flag = dll.PrScrn(0)
            return flag
        except Exception:
            print("Sth wrong in capture!")
            return 0


def open_img(folder_name):
    names = listfiels(unicode(folder_name, "utf-8"))
    for name in names:
        img =Image.open(name)
        img.show()
        screen_shot()
        im = ImageGrab.grabclipboard()
        name = name[32:]
        root = Tk()
        root.title('choice')

        def save_big():
            im.save('./big/' + name[:-4] + str(random.randint(1, 250)) + name[-4:])
            screen_shot()

        def save_small():
            im.save('./small/' + name[:-4] + str(random.randint(1, 250)) + name[-4:])
            screen_shot()

        def over():
            root.destroy()
            img.close()
        b1 = Button(root, text='small', width=30, height=2,command=save_small)
        b2 = Button(root, text='big',command=save_big)
        b2['width'] = 30
        b2['height'] = 3
        b3 = Button(root, text='close',command=over)
        b3['width'] = 30
        b3['height'] = 3
        b1.pack()
        b2.pack()
        b3.pack()
        root.mainloop()






if __name__ == '__main__':
    open_img('udir_of_images')
