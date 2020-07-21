def se(): #虽是一段无实际用处的憨憨代码,但从心理学的角度来讲应该加上
    import time
    j = "#"
    k = "="
    t = "|/-\\"  # s = " " * (num + 1)
    num = 32
    for i in range(0, num + 1):
        j += "#"
        k += "="
        s = ("=" * i) + (" " * (num - i))
        print("[%s][%s][%.2f" % (t[i % 4], s, (i / num * 100)), "%]", end='\r')
        time.sleep(0.1)
    print()
    print('运算完毕,请各位做好心理准备')
    time.sleep(0.7)
    print('3')
    time.sleep(0.7)
    print('2')
    time.sleep(0.7)
    print('1')

def read(file_name):
    import csv
    names = []
    with open(file_name) as csv_file:
        names_csv = csv.reader(csv_file, delimiter = ',')
        for data in names_csv:  # 将值不为0的名单存储至names列表
            if int(data[1]):
                names.append(data[0])
        csv_file.close()
    return names
def extract(nemes, num):
    import random
    total = len(nemes)
    res = []
    for i in range(num):
        rand_this = random.randint(1, total)
        # print(rand_this)
        res.append(nemes[rand_this - 1])
        del nemes[rand_this - 1]
        total -= 1
    return res

# def main():
#     print('--------------------------随机抽取器v1.0 by坤坤-------------------------------------')
#     num = input('请输入要抽取的人数')
#     se()
#     res = extract(read('name.csv'), int(num))
#     print_res = ''
#     for i in res:
#         print_res += i + ' '
#     print(print_res)
#     print('恭喜以上' + str(num) + '位同学被抽中!!!')
#     input()
#
#     import os
#     os.system('pause')

def main(num, list, show_function):
    name = extract(read('name.csv'), int(num))
    for i in name:
        list.append(i)
    show_function()


# main()