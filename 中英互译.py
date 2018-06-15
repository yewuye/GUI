from tkinter import *
from tkinter import messagebox
import requests


def translate():
    content = entry1.get()

    if content == '':
        messagebox.showinfo('提示', '请输入要翻译的内容!')
    else:
        url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        data = {
            'action': 'FY_BY_REALTIME',
            'client': 'fanyideskweb',
            'doctype': 'json',
            'from': 'AUTO',
            'i': content,
            'keyfrom': 'fanyi.web',
            # 'salt': '1528944949581',
            # 'sign': '9902db0d716e3f16066fffd9065d0c12',
            'smartresult': 'dict',
            'to': 'AUTO',
            'typoResult': 'false',
            'version': '2.1',
        }
        try:
            response = requests.post(url, data).json()
            response = response['translateResult'][0][0]['tgt']
            res.set(response)
        except Exception:
            messagebox.showinfo('提示', '请连接您的网络!')

app = Tk()
app.geometry('400x100+500+300')
res = StringVar()

label1 = Label(app, text='请输出要翻译的内容', font='微软雅黑')
label1.grid(row=0, column=0)
label2 = Label(app, text='翻译之后的结果', font='微软雅黑')
label2.grid(row=1, column=0)
entry1 = Entry(app)
entry1.grid(row=0, column=1)
entry2 = Entry(app, textvariable=res)  # textvariable=res
entry2.grid(row=1, column=1)
button1 = Button(app, text='翻译', font='微软雅黑', command=translate)
button1.grid(row=2, column=0, sticky=W)

button2 = Button(app, text='退出', font='微软雅黑', command=app.quit)
button2.grid(row=2, column=1, sticky=E)

app.mainloop()
