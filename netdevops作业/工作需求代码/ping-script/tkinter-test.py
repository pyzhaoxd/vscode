# -*- encoding: utf-8 -*-
'''
@File    :   简单文本编辑器.py
@Time    :   2020/04/05 11:35:39
@Author  :   Konggu
@Desc    :   None
'''
import os
import tkinter as tk
import tkinter.messagebox
from functools import partial as pto
from tkinter import filedialog, dialog

path = r'C:\Users\64530\Desktop\记事本汇总\\'
file_text = ''
window = tk.Tk()
window.title('文件编辑器')    # 窗口标题
window.geometry('500x300')    # 窗口尺寸
t1 = tk.Text(window, width=50, height=10, bg='palegreen', font=(12))
t1.pack()

# 打开文件
def open_file():
    file_path = filedialog.askopenfilename(title=u'选择文件', initialdir=(os.path.expanduser(path)))   # 文件选择框（选择文件）
    with open(file=file_path, mode='r+', encoding='utf-8') as f:
        file_text = f.read()      # 读文件
    t1.insert('insert', file_text)

# 保存文件
def save():
    file_path = path + '文件.txt'       # 指定一个路径
    file_text = t1.get('1.0', tk.END)
    if file_path is not None:
        with open(file=file_path, mode='w', encoding='utf-8') as f:       # 保存到指定路径
            f.write(file_text)
        t1.delete('1.0', tk.END)
        print("保存成功")
        tkinter.messagebox.showinfo(title='提示',message='保存成功！')

# 退出
def quit():
    res = tk.messagebox.askokcancel(title = '等一下！',message='保存一手吗？')      # 弹出框，可选(确定/取消)
    print(res)
    if res:
        save()
        window.quit()
    else:
        pass

def main():
    bt1 = tk.Button(window, text='打开文件', width=15, height=2, command=open_file)
    bt1.pack()
    bt2 = tk.Button(window, text='退出', width=15, height=2, command=quit)
    bt2.pack()
    window.mainloop()


if __name__ == "__main__":
    main()