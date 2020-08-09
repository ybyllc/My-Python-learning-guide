# coding: utf-8
# 编码是utf-8

# 导入窗口模块
from tkinter import *
import tkinter.messagebox as messagebox

# In[1]:
# 第一段代码
class MyApp(Frame):
#窗口名称叫myapp

    def __init__(self,master=None):
        #初始化
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        #窗口
        self.helloLabel = Label(self,text="世界上最帅的人是谁？")
        self.helloLabel.pack()
        self.quitButton = Button(self,text="谁呢？",command=self.who)
        self.quitButton.pack()
        self.quitButton2 = Button(self,text="是我自己",command=self.who2)
        self.quitButton2.pack()

    def who(self):
        #第一个提示框who
        messagebox.showinfo("答案","当然是一杯原谅绿茶啦")

    def who2(self):
        #第二个提示框who2
        messagebox.showinfo("答案","没错！就是你自己！")


myapp = MyApp()
myapp.master.title('hello')
myapp.mainloop()
