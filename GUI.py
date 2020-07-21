import extract
import tkinter as tk

class Window():
    main = tk.Tk()
    extracted_name = []

    def __init__(self, global_size_base):
        self.__global_size_base = global_size_base
        # self.extracted_name = extract.extract(extract.read('name.csv'), int(num))
        self.main.geometry('350x200+' + str(int(0.5 * self.main.winfo_screenwidth())) +
                      '+' + str(int(0.5 * self.main.winfo_screenheight())))
        self.main.title('随机抽取器v2.3 by坤坤')
        start = tk.Button(self.main, text='开始使用', command=lambda : self.input_num(), font=('Arial', 13))
        start.place(x=60, y=100, anchor='w')
        about = tk.Button(self.main, text='关于作者', command=self.about, font=('Arial', 13))
        about.place(x=190, y=100, anchor='w')
        welcome = tk.Label(self.main, text='欢迎使用随机抽取器v2.3', font=('Arial', 16))
        welcome.place(x=50, y=40, anchor='w')
        close = tk.Button(self.main, text='退出', command=lambda : self.main.destroy(), font=('Arial', 10))
        close.place(x=260, y=160, anchor='w')
        self.main.mainloop()

    def size(self):
        global global_size_base
        # 自动根据基数生成字体与窗口大小的字符串

    def show_res(self): # 传入被抽中的名单列表和总人数
        num = len(self.extracted_name)
        show = tk.Tk()
        show.geometry('300x100+' + str(int(0.5 * show.winfo_screenwidth())) +
                      '+' + str(int(0.5 * show.winfo_screenheight())))
        show.title('抽取结果')
        account = tk.Label(show, text = '第' + str(num) + '位中奖的同学是:', font = ('Arial', 10))
        account.place(x = 70, y = 15, anchor = 'center')
        res_lab = tk.Label(show, text = self.extracted_name[0], font = ('Arial', 20), fg = 'red')
        res_lab.place(x = 150, y = 50, anchor = 'center')
        def open_new(show):
            show.destroy()
            if num == 1:
                return
            del self.extracted_name[0]
            self.show_res()
        next_button = tk.Button(show, text = '下一位', command = lambda : open_new(show))
        next_button.place(x = 220, y = 77, anchor = 'w')
        show.mainloop()

    def input_num(self):
        input_window = tk.Tk()
        input_window.geometry('170x100+' + str(int(0.5 * input_window.winfo_screenwidth())) +
                      '+' + str(int(0.5 * input_window.winfo_screenheight())))
        input_window.title('输入')
        input_entry = tk.Entry(input_window, width = 15, font = ('Arial', 10))
        input_entry.place(x = 30, y = 25, anchor = 'w')
        start = tk.Button(input_window, text = '开始',
                          command = lambda : extract.main(input_entry.get(), self.extracted_name, self.show_res))
        start.place(x = 70, y = 65, anchor = 'w')

    def about(self):
        about = tk.Tk()
        about.title('关于')
        about.geometry('170x100+' + str(int(0.5 * about.winfo_screenwidth())) +
                      '+' + str(int(0.5 * about.winfo_screenheight())))
        introduce = tk.Label(about, text = '那必然是你们最帅的', font = ('Arial', 10))
        introduce.place(x = 25, y = 25, anchor = 'w')
        name = tk.Label(about, text='坤坤', font=('Arial', 20))
        name.place(x=50, y=60, anchor='w')


a = Window(100)
# print(a.extracted_name)
# a.show_res('hhh', 2)

'''
主页面放置欢迎语句和三个按钮,分别是开始使用,关于作者和退出,按下开始使用后弹出新窗口,
输入窗口放置一个输入框和一个确定按钮,按下确定按钮后关闭输入窗口
不断弹出show_res窗口,每弹出一个都关闭上一个,最后弹出一个总名单窗口
'''