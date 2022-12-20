import extract
import tkinter

class Window():
    main = tkinter.Tk()
    def __init__(self):
        self.extract = extract.Extract()
        self.main.geometry('350x200+' + str(int(0.5 * self.main.winfo_screenwidth())) +
                      '+' + str(int(0.5 * self.main.winfo_screenheight())))
        self.main.title('随机抽取器v3.0')
        start = tkinter.Button(self.main, text='抽一个', command=lambda : self.show_res(), font=('Arial', 13))
        start.place(x=140, y=100, anchor='w')
        welcome = tkinter.Label(self.main, text='欢迎使用随机抽取器v3.0', font=('Arial', 16))
        welcome.place(x=50, y=40, anchor='w')
        close = tkinter.Button(self.main, text='退出', command=lambda : self.main.destroy(), font=('Arial', 10))
        close.place(x=260, y=160, anchor='w')
        self.varOne = tkinter.BooleanVar()
        cbutOne = tkinter.Checkbutton(self.main, text="允许重复", variable=self.varOne)
        cbutOne.place(x=10, y=160, anchor='w')
        self.main.mainloop()

    def show_res(self):
        self.extract.ifAgain = self.varOne.get()
        show = tkinter.Tk()
        show.geometry('300x100+' + str(int(0.5 * show.winfo_screenwidth())) +
                      '+' + str(int(0.5 * show.winfo_screenheight())))
        show.title('抽取结果')
        # account = tkinter.Label(show, text = '第' + str(num) + '位中奖的同学是:', font = ('Arial', 10))
        # account.place(x = 70, y = 15, anchor = 'center')
        res_lab = tkinter.Label(show, text = self.extract.giveOne(), font = ('Arial', 20), fg = 'red')
        res_lab.place(x = 150, y = 40, anchor = 'center')
        def open_new(show):
            show.destroy()
            self.show_res()
        next_button = tkinter.Button(show, text = '再抽一个', command = lambda : open_new(show))
        next_button.place(x = 200, y = 77, anchor = 'w')
        # end_button = tkinter.Button(show, text = '不来了', command = lambda : self.main.destroy())
        # end_button.place(x = 40, y = 77, anchor = 'w')
        show.mainloop()

a = Window()