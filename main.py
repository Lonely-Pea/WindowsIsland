import tkinter as tk
import time
import os
import threading
import psutil#计算内存
#窗口
class Win(tk.Tk):
    def __init__(self):
        super().__init__()
        self.overrideredirect(True)#设置窗口没有边框
        self.geometry("%dx%d+%d+%d" % (200,50,(self.winfo_screenwidth()-200)/2,50))#设置窗口大小
        self.attributes("-alpha",0.5)#设置窗口半透明
        self.attributes("-topmost",True)#设置窗口始终位于顶部
#界面
class Desktop(tk.Frame):
    def __init__(self,master):
        super().__init__()
        self.master=master
        self.pack(fill=tk.BOTH,expand=True)#放置框架
        self.config(background="black")#设置框架黑色
        #变量
        self.more=0#是否展开,初始为没有
        #显示时间
        self.time_now=time.strftime("%Y-%m-%d\n%H:%M:%S",time.localtime())#获取当前时间
        self.time_label=tk.Label(self,text=self.time_now,background="black",foreground="white")#显示时间的标签
        self.time_label.place(x=0,y=0,width=150,height=50)
        self.master.after(1000,self.get_time)#1秒后重新获取时间
        #时间标签可以拖动
        self.time_label.bind("<Button-1>",self.get_point)
        self.time_label.bind("<B1-Motion>",self.move)
        #还原按钮
        self.reduce_button=Button(master=self,text="还\n原",command=self.reduce)
        self.reduce_button.place(x=150,y=0,width=25,height=50)
        #退出按钮
        self.quit_button=Button(master=self,text="X",command=self.quit_)
        self.quit_button.place(x=175,y=0,width=25,height=25)
        #展开按钮
        self.more_button=Button(master=self,text="↓",command=self.more_)
        self.more_button.place(x=175,y=25,width=25,height=25)
        #展开框架
        self.more_frame=tk.Frame(self,bg="black")
        self.more_frame.place(x=0,y=50,width=200,height=100)
        #展开框架下的内容
        self.cmd_button=Button(master=self.more_frame,text="Cmd",command=self.start_cmd)#cmd快捷按钮
        self.cmd_button.place(x=0,y=0,width=50,height=50)
        self.powershell_button=Button(master=self.more_frame,text="Power\nShell",command=self.start_powershell)#PowerShell快捷按钮
        self.powershell_button.place(x=50,y=0,width=50,height=50)
        self.calculator_button=Button(master=self.more_frame,text="计算器",command=self.start_calculator)#计算器快捷按钮
        self.calculator_button.place(x=100,y=0,width=50,height=50)
        self.drawing_button=Button(master=self.more_frame,text="画图",command=self.start_drawing)#画图快捷按钮
        self.drawing_button.place(x=150,y=0,width=50,height=50)
        self.memory_button=Button(master=self.more_frame,text="内存\n管理",command=self.start_memory)#内存管理
        self.memory_button.place(x=0,y=50,width=50,height=50)
        self.screenshot_button=Button(master=self.more_frame,text="截图",command=self.start_screenshot)#截图快捷按钮
        self.screenshot_button.place(x=50,y=50,width=50,height=50)
        self.taskmgr_button=Button(master=self.more_frame,text="任务\n管理器",command=self.start_taskmgr)#任务管理器快捷按钮
        self.taskmgr_button.place(x=100,y=50,width=50,height=50)
        self.explorer_button=Button(master=self.more_frame,text="文件\n管理",command=self.start_explorer)#文件资源管理器快捷按钮
        self.explorer_button.place(x=150,y=50,width=50,height=50)
    def get_time(self):#获取时间
        self.time_now=time.strftime("%Y-%m-%d\n%H:%M:%S",time.localtime())#重新获取时间
        self.time_label.config(text=self.time_now)#更改显示的时间文字
        self.master.after(1000,self.get_time)#一秒后再次执行此函数
    def move(self,event):#移动事件
        new_x=(event.x-self.x)+self.master.winfo_x()
        new_y=(event.y-self.y)+self.master.winfo_y()
        if self.more==0:
            self.master.geometry("%dx%d+%d+%d"%(200,50,new_x,new_y))
        else:
            self.master.geometry("%dx%d+%d+%d"%(200,150,new_x,new_y))
    def reduce(self,event=None):#还原
        self.master.geometry("%dx%d+%d+%d"%(200,50,(self.winfo_screenwidth()-200)/2,50))
        try:
            frame_memory.destroy()
        except Exception as e:
            pass
        self.more_button.config(text="↓")
        self.more=0
    def get_point(self,event):#获取当前位置
        self.x=event.x
        self.y=event.y
    def quit_(self,event=None):#退出程序
        self.master.destroy()
    def more_(self,event=None):#展开
        if self.more==0:#没有展开
            self.more=1
            self.more_button.config(text="↑")
            self.master.geometry("%dx%d"%(200,150))
        else:#展开了
            self.more=0 
            self.more_button.config(text="↓")
            self.master.geometry("%dx%d"%(200,50))
    def start_cmd(self,event=None):#打开cmd
        def start():
            os.system("cmd.exe")
        thread_cmd=threading.Thread(target=start)
        thread_cmd.start()
    def start_powershell(self,event=None):#打开powershell
        def start():
            os.system("Powershell.exe")
        thread_powershell=threading.Thread(target=start)
        thread_powershell.start()
    def start_calculator(self,event=None):#打开计算器
        def start():
            os.system("calc.exe")
        thread_calculator=threading.Thread(target=start)
        thread_calculator.start()
    def start_drawing(self,event=None):#打开画图
        def start():
            os.system("mspaint.exe")
        thread_drawing=threading.Thread(target=start)
        thread_drawing.start()
    def start_memory(self,event=None):#打开内存管理界面
        global frame_memory
        def get_memory():#获取内存
            try:
                total=float(mem.total)/1024/1024/1024
                used=float(mem.used)/1024/1024/1024
                free=float(mem.free)/1024/1024/1024
                total_label.config(text="总计内存:%.2fG"%total)
                used_label.config(text="已用内存:%.2fG"%used)
                free_label.config(text="空闲内存:%.2fG"%free)
                self.master.update()
                time.sleep(0.1)
                get_memory()
            except Exception:
                pass
        def quit_memory(event=None):#退出
            frame_memory.destroy()
        #创建内存管理界面框架
        frame_memory=tk.Frame(self.more_frame,bg="black")
        frame_memory.place(x=0,y=0,width=200,height=100)
        #实例化内存读取
        mem=psutil.virtual_memory()
        #界面
        total_label=tk.Label(frame_memory,text="总计内存:获取中",background="black",foreground="white")
        total_label.place(x=0,y=0,width=175,height=100/3)
        used_label=tk.Label(frame_memory,text="已用内存:获取中",background="black",foreground="white")
        used_label.place(x=0,y=100/3,width=175,height=100/3)
        free_label=tk.Label(frame_memory,text="空闲内存:获取中",background="black",foreground="white")
        free_label.place(x=0,y=100/3*2,width=175,height=100/3)
        back_button=Button(master=frame_memory,text="X",command=quit_memory)
        back_button.place(x=175,y=0,width=25,height=20)
        #获取内存
        thread_get_memory=threading.Thread(target=get_memory)
        thread_get_memory.start()
    def start_screenshot(self,event=None):#打开截图工具
        def start():
            os.system("snippingtool.exe")
        thread_screenshot=threading.Thread(target=start)
        thread_screenshot.start()
    def start_taskmgr(self,event=None):#打开任务管理器
        def start():
            os.system("taskmgr.exe")
        thread_taskmgr=threading.Thread(target=start)
        thread_taskmgr.start()
    def start_explorer(self,event=None):#打开文件管理器
        def start():
            os.system("explorer.exe")
        thread_explorer=threading.Thread(target=start)
        thread_explorer.start()
#按钮
class Button(tk.Label):
    def __init__(self,master,text,command):
        super().__init__(master)
        self.master=master
        self.config(text=text)
        self.config(cursor="hand2")
        self.config(background="black")
        self.config(foreground="white")
        self.bind("<Button-1>",command)
        self.bind("<Enter>",self.enter)
        self.bind("<Leave>",self.leave)
    def enter(self,event=None):
        self.config(background="grey")
    def leave(self,event=None):
        self.config(background="black")
if __name__=="__main__":
    win=Win()
    desktop=Desktop(master=win)
    win.mainloop()
