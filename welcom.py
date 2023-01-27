import tkinter as tk
import draw_picture
import tkinter.messagebox
from init import resurce_path
from threading import Thread

def r():
    try:
        draw_picture.draw(inputimage.get(),eval(inputposition.get()),inputedition.get())
    except:
        tkinter.messagebox.showerror("发生错误喵","输入有误或RP太差，生成数据包失败")
helpopen=False
def help():
    global helpopen
    if helpopen: return 0
    helpopen=True
    help=tk.Toplevel()
    help.title("How to use")
    help.geometry('870x500')
    help.resizable(False,False)
    help.iconbitmap(resurce_path(r'resourses\logo.ico'))
    helpimage=tk.PhotoImage(file=resurce_path(r'resourses\help.gif'))
    helptext=tk.Text(help,width=125,height=50)
    helptext.place(x=0,y=0)
    helptext.image_create('end',image=helpimage)
    def close():
        global helpopen
        helpopen=False
        help.destroy()
    help.protocol('WM_DELETE_WINDOW',close)
    while True:
        help.update()
def makehelp():
    thread=Thread(target=help,daemon=True)
    thread.start()

'''GUI 窗口界面'''
root=tk.Tk()
root.geometry("400x200")
root.title("Minecraft 二次元福音")
root.iconbitmap(resurce_path(fr'resourses\logo.ico'))
root.resizable(False,False)
imagelable=tk.Label(root,text="输入图片名称:",bg='lightgray')
imagelable.place(x=10,y=13)
inputimage=tk.Entry(root,width=40,bg='lightgray')
inputimage.place(x=107,y=15)
positionlable=tk.Label(root,text="输入图片左上角的坐标:",bg='lightgray')
positionlable.place(x=10,y=53)
inputposition=tk.Entry(root,width=33,bg='lightgray')
inputposition.place(x=157,y=55)
mcedition=tk.Label(root,text="请输入使用的MC版本:",bg='lightgray')
mcedition.place(x=10,y=95)
inputedition=tk.Entry(root,width=34,bg='lightgray')
inputedition.place(x=150,y=97)
ready=tk.Button(root,width=10,height=1,bg='lightgray',text='生成数据包',command=r)
ready.place(x=168,y=160)
h=tk.Button(root,width=5,height=1,text='help',command=makehelp)
h.place(x=345,y=160)
root.mainloop()
# (-75,1,-160)