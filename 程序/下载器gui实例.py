
# encoding:utf-8
import os
from tkinter import *
from tkinter import filedialog
import urllib.request


class FileDownload:
    def __init__(self, master):
        self.filename=StringVar()
        self.filename.set('选择要打开的文件信息')
        self.src_dir=''
        self.urls=[]
        # tkinter刚开始不熟悉，布局麻烦，这里使用的网格布局，row，column 的index，定位cell
        open_btn=Button(master, text="打开文件",width=15,height=3,borderwidth=2,
                                  command=self.openfile)
        download_btn=Button(master, text="开始下载",width=15,height=3,borderwidth=2,
                                  command=self.download)
        open_btn.grid(row=0,column=0,ipadx=5,ipady=3,padx=10,pady=3)
        download_btn.grid(row=1,column=0,ipadx=5,ipady=3,padx=10,pady=3)
        self.file_label=Label(master,textvariable=self.filename,wraplength=250,fg='green',bg='white',)
        self.file_label.grid(row=0,column=1,rowspan=2,ipadx=200,ipady=15,padx=10,pady=2)#,padx=20,pady=10,
        self.text=Text(master,width=100,height=50,bg='grey',fg='blue')
        self.text.grid(row=2,columnspan=2,ipadx=10,ipady=10)

    def openfile(self):
        # 系统默认打开用户的桌面文件
        default_dir=os.path.join(os.path.expanduser("~"), 'Desktop')
        fname = filedialog.askopenfilename(title='选择打开的文件', filetypes=[('txt文本','*.txt'), ('All Files', '*')],
                                    initialdir=(os.path.expanduser(default_dir)))
        print('打开的文件',fname)
        self.src_dir=fname[0:fname.rindex('/')]
        self.filename.set(fname)
        self.urls=self.read_urls(fname)

    # 读取urls
    def read_urls(self,fname):
        urls=[]
        with open(fname) as f:
            urls=f.readlines()
        urls=[url.replace('\n','') for url in urls]
        for i in urls:
            print(i)
        return urls

    def print_schedule(self,a,b,c):
        '''
        打印进度条信息
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
        '''
        per = 100.0 * a * b / c
        if per > 100 :
            per = 100
        print('下载进度%.1f%%' % per)

    def download(self):
        i=1
        urls_nums=len(self.urls)
        for url in self.urls:
            print('正在下载:%s'%url)
            # 在界面上显示下载的日志信息
            self.text.insert(END,'正在下载%d/%d:%s\n'%(i,urls_nums,url))
            self.text.see(END)
            self.text.update()# 这个很关键，更新页面text信息
            filename = url.split('/')[-1]
            # 文件明太长，或者含有'=,%,&'这些非法字符windows无法识别，会报错，
            # 这里简单的截取了url的后20个字符作为名字
            if len(filename)>20:
                filename=filename[-20:]
            local = os.path.join(self.src_dir,filename)
            urllib.request.urlretrieve(url,local,self.print_schedule)
            i+=1
        self.text.insert(END,'下载结束')
        self.text.see(END)
        self.text.update()


if __name__=='__main__':
    tker = Tk()
    tker.title("自动文件下载器")
    tker.columnconfigure(0, weight=3)
    tker.columnconfigure(1, weight=7)
    tker.rowconfigure(0, weight=1)
    tker.rowconfigure(1, weight=1)
    tker.rowconfigure(2, weight=8)
    tker.geometry('640x480') # 设置主窗口的初始大小640x480
    app = FileDownload(tker)
    tker.mainloop()