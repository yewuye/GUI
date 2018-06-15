from PIL import Image as Img  # 处理图片
from tkinter import *  # UI设计需要
from tkinter.filedialog import *  # 打开对话框


info = {
    'path': []
}


# UI设计
def make_app():
    app = Tk()
    Label(app, text='图片压缩工具').pack()
    Listbox(app, name='lbox', bg='white').pack(fill=BOTH, expand=True)
    # 后续需要操作的时候，给一个name
    Button(app, text='打开', command=get_img).pack()
    Button(app, text='压缩', command=compress).pack()
    app.geometry('300x400')
    return app


def get_img():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])


def compress():
    for f_path in info['path']:
        output = '/home/qianran/Pictures/'
        name = f_path.split('/')[-1]
        if info['path']:
            image = Img.open(f_path)
            image.save(output + 'c_' + name, quality=60)
            # print('i\'m here.')
        else:
            print('there are no pictures to compress!')


app = make_app()
app.mainloop()
