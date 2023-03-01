# print("Hello world")
import tkinter as tk

from PIL import Image, ImageTk

import requests

import re

import webbrowser

root = tk.Tk()

root.geometry("800x800+200+200")

root.title("在线观看电影")

def show():
    num = num_int_var.get()
    word = input_va.get()
    if num == 1:
        link = 'https://www.wannengjiexi.com/jiexi1/?url='+word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
    elif num == 2:
        link = 'https://www.wannengjiexi.com/jiexi2/?url=' + word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)
    else:
        link = 'https://www.wannengjiexi.com/jiexi3/?url=' + word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" src="(.*?)"', html_data)[0]
        webbrowser.open(video_url)

global photo

image = Image.open("/Users/summer/Downloads/littlebear.jpeg")

photo = ImageTk.PhotoImage(image)

# img = tk.PhotoImage(file='img  littlebear.jpeg')

tk.Label(root, image=photo).pack(fill='both')

choose_frame = tk.LabelFrame(root)

choose_frame.pack(pady=10, fill='both')

tk.Label(choose_frame, text="选择接口:", font=("黑体", 20)).pack(side=tk.LEFT)

num_int_var = tk.IntVar()

num_int_var.set(1)

input_va = tk.StringVar()

tk.Radiobutton(choose_frame, text='①号通用VIP引擎系统【稳定可用】', font=("黑体", 10), variable=num_int_var, value=1).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text='②号通用VIP引擎系统【稳定可用】', font=("黑体", 10), variable=num_int_var, value=2).pack(side=tk.LEFT, padx=5)
tk.Radiobutton(choose_frame, text='③号通用VIP引擎系统【稳定可用】', font=("黑体", 10), variable=num_int_var, value=3).pack(side=tk.LEFT)

input_frame = tk.LabelFrame(root)
input_frame.pack(pady=10, fill='both')

tk.Label(input_frame, text="播放地址:", font=("黑体", 20)).pack(side=tk.LEFT)
tk.Entry(input_frame, width=100, relief='flat', textvariable=input_va).pack(side=tk.LEFT, fill='both')
tk.Button(root, text='点击在线解析播放', font=("黑体", 15), relief='flat', bg='green', command=show).pack(fill='both')
root.mainloop()


