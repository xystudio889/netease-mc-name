import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from random import choice
from pyperclip import copy
from ttkbootstrap.dialogs import Messagebox
from threading import Timer
from pathlib import Path
from os.path import join

folder=Path(__file__).parent.resolve()

def generate_random_name():
    name = choice(adjective_list) + choice(noun_list) + choice(verb_list)
    random_name.set(name)

def share():
    copy('https://github.com/xystudio889')
    Messagebox.show_info(title='分享', message='源码链接复制成功！')

def copy_text():
    copy(random_name.get())
    random_nameEntry.select_range(0, END)
    t = Timer(0.2, lambda: random_nameEntry.select_clear())
    t.start()

root = ttk.Window(title="网易随机名称生成器")#, themename='popfortlight')
root.geometry('660x460+400+120')
root.minsize(500, 400)
#root.iconbitmap('icon.ico')

random_name = ttk.StringVar()
random_name.set('')

with open(join(folder,'assets', 'adj.txt'), encoding='u8') as f:
    adjective_list = f.read().splitlines()
with open(join(folder,'assets', 'n.txt'), encoding='u8') as f:
    noun_list = f.read().splitlines()
with open(join(folder,'assets', 'v.txt'), encoding='u8') as f:
    verb_list = f.read().splitlines()

nameFrame = ttk.Frame()
random_nameEntry = ttk.Entry(
    nameFrame, 
    width=26, 
    bootstyle='primary', 
    state='readonly', 
    font=('微软雅黑', 16), 
    justify=CENTER, 
    textvariable=random_name
)

copyBtn = ttk.Button(nameFrame, text='复制', bootstyle='primary-outline', width=7, command=copy_text)

generateBtn = ttk.Button(text='生成随机昵称', bootstyle='warning', width=15, command=generate_random_name)
shareBtn = ttk.Button(text='共享这个应用', bootstyle='secondary', width=15, command=share)

infoLabel = ttk.Label(text='Version 1.0.0', bootstyle='secondary', justify='center', font=('微软雅黑 Light', 12))

#放置控件
random_nameEntry.pack(side=LEFT, padx=10)
copyBtn.pack(side=RIGHT, ipady=7)
nameFrame.pack(pady=20)

generateBtn.pack(ipady=10, pady=10)
shareBtn.pack(ipady=10)

infoLabel.pack(side=BOTTOM)

root.mainloop()
