# 密码生成器
# 	要求：
# 		使用相关模块生成不少于8位密码的脚本


import string,random

def dec(func):
    def internal():
        print('...开始创建密码...')
        func()
        print('...密码生成完毕...')
    return internal
#用装饰器来修饰makepass函数
@dec
def makepass():
    #主要执行就是这么一行其他为修饰作用，用string模块和choices结合
    print("".join(random.choices(string.ascii_letters + string.digits, k=16)))

if __name__ == "__main__":
    makepass()





