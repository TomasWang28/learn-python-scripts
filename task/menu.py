# 设计并实现一款菜单
# 	要求：
# 		操作方便，可由用户选择是否退出。

import time
menu='''
----欢迎来我的餐厅来点餐----
菜单如下：
    1.烤鸭
    2.烤红薯
    3.烤土豆
请选择你要点的菜单：'''
rights=['1','2','3','烤鸭','烤红薯','烤土豆']

select = input(menu)
if select in rights:
    start = time.time()
    while True:
        zuocai=input("正在给你做菜,请稍等,按Q/q退出！")
        if zuocai.lower() == 'q':
            break
end = time.time()
fintime=end-start
if fintime < 2.5:
    print("您的%s 是5成熟，请慢用！" % select)
elif fintime >= 2.5 and fintime <4:
    print("您的%s 是7成熟，请慢用！" % select)
elif fintime >= 4 and fintime <5:
    print("您的%s 是9成熟，请慢用！" % select)
else:
    print("您的%s烤糊了，请慢用！(嘻嘻)" % select)

print('总共用时%.2f秒！'%fintime)
#菜单脚本写的比较欢乐，客人选择他要点的菜并统计时间判断食物的成熟度，哈哈