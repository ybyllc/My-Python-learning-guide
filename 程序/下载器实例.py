# coding: utf-8
import urllib.request
import os

url = 'https://nchc.dl.sourceforge.net/Setup.exe'  # 下载地址

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