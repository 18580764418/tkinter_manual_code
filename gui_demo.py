# tkinter实现菜单功能
import os
from tkinter import *
from PIL import Image, ImageTk


class Window(Frame):

    def __init__(self, master=None, num=20):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
        self.num = num
        self.file_list = []
        self.entry_list = list(range(self.num))
        self.img_list = list(range(self.num))
        self.images_name = list(range(self.num))
        self.text = StringVar()
        self.img_path = "{}/origin_img/files/".format(os.path.abspath('.'))
        self.rename_img_path = "{}/origin_img/new_files/".format(os.path.abspath('.'))
        self.bnt = None
        self.count = 0

    def init_window(self):
        self.master.title("第一个窗体")

        self.pack(fill=BOTH, expand=1)

        # 实例化一个Menu对象，这个在主窗体添加一个菜单
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # 创建File菜单，下面有Save和Exit两个子菜单
        file = Menu(menu)
        file.add_command(label='Save')
        file.add_command(label='Exit', command=self.client_exit)
        menu.add_cascade(label='File', menu=file)

        # 创建Edit菜单，下面有一个Undo菜单
        edit = Menu(menu)
        edit.add_command(label='Undo')
        edit.add_command(label='Show  Image', command=self.show_img)
        menu.add_cascade(label='Edit', menu=edit)

    def client_exit(self):
        exit()

    def show_img(self, num):
        for i in range(num):
            load = Image.open(self.img_path + self.file_list[num * self.count + i])
            self.images_name[i] = self.file_list[num * self.count + i]
            render = ImageTk.PhotoImage(load)

            img = Label(self, image=render)
            img.image = render
            img.grid(row=i)
            entry_label = Entry(self)
            entry_label.grid(row=i, column=1)
            self.img_list[i] = img
            self.entry_list[i] = entry_label

            self.bnt.grid(row=num, column=1, sticky=W, padx=5, pady=5)

    def show_btn(self):
        self.file_list = os.listdir(self.img_path)
        self.bnt = Button(self, text='Run', command=self.rename_img)
        self.bnt.grid(row=0, column=1, sticky=W, padx=5, pady=5)

    def rename_img(self):
        if self.count != 0:
            for i in range(self.num):
                str_code = self.entry_list[i].get()
                os.rename(self.img_path + self.images_name[i],
                          self.rename_img_path + str_code + "_" + self.images_name[i])
        self.show_img(self.num)
        self.count += 1
        self.update()


root = Tk()
root.geometry("400x800")
app = Window(root, 20)
app.show_btn()
root.mainloop()
