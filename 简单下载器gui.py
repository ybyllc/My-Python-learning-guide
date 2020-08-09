from tkinter import *
import tkinter.messagebox as messagebox
import urllib.request
import os

# In[1]:
# In[2]:
class MyApp(Frame):

    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self,text="下载地址")
        self.helloLabel.pack()
        self.xzdz = Entry(self, show=None, font=('Arial', 14))  # 显示成明文形式
        self.xzdz.pack()
        self.quitButton = Button(self,text="开始下载")#,command=self.downloadstrat
        self.quitButton.pack()

    def downloadstrat(self):
        messagebox.showinfo("答案","下屁")

myapp = MyApp()
myapp.master.title('下载器')
myapp.mainloop()

# In[3]:
url = str(xzdz)  # 下载地址

filename = url[url.rindex('/') + 1:]  # 截取文件名
print('filename = ' + filename)

downloaded = '0'


def download_listener(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    new_downloaded = '%.1f' % per
    global downloaded
    if new_downloaded != downloaded:
        downloaded = new_downloaded
        print('download %s%%  %s/%s' % (downloaded, a * b, c))


path = 'D:\\download\\'  # 下载目录
if not os.path.exists(path):
    os.mkdir(path)

response = urllib.request.urlretrieve(url, path + filename, download_listener)