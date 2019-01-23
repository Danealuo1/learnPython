# 上下文管理器： 一个可以在程序中加载独立上下文的对象
# 上下文管理器使用with显式创建
# 进入和退出分别对应_enter_()和_exit_()方法

# 文件操作打开及管理
# 1.with结束后，文件被自动关闭
# 2.with可以包含多个表达式及as
# with open("python123.txt", "r") as f:
#     for line in f:
#         print(line)

# with open("python123.txt", "r") as fi, \
#         open("to_f.txt", "w") as fo:
#     for line in fi:
#         fo.write(line)

# 自定义with兼容对象
# 重载__enter__()方法
# 重载__exit__()方法


# class DemoClass:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print("进入上下文管理器")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("退出上下文管理器")
#
#     def run(self):
#         print("DemoClass的某个实例对象在运行")
#
# with DemoClass("123") as f:
#     f.run()

# as引用是__enter__()返回值
# 在定义类中self表达的是对象本身

# 迭代器类型
# class Demolterator:
#     def __init__(self, container):
#         self.container = container
#         self.salt = len(self.container)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.salt -= 1
#         if self.salt >= 0:
#             return self.container[self.salt]
#         else:
#             raise StopIteration
#
# di = Demolterator([1,2,3,4,5,6,7,8])
#
# for i in di:
#     print(i, end='')

# def getValue():
#     import random
#     ls = list(range(10))
#     print(ls, end='')
#     return ls[random.randint(0, 9)]
#
# for i in range(10):
#     print(getValue())

# def bar(foo):
#     def wrapper(a):
#         print("{:*^20}".format('BEGIN'))
#         foo(a)
#         print("{:*^20}".format('END'))
#
#     return wrapper
#
# @bar
# def printA(a):
#     print("这是变量{}".format(a))
#
# printA("python123")

"""
装饰器函数必须返回一个函数对象引用
否则，无法利用语法糖
因此，需要在内部定义一个函数
最好都用wrapper这个名字

装饰器使用场景
1）对原函数功能的补充：测量时间、增加打印等
2）对原函数功能的调整：利用原函数运行结果，再次运算产生新的结果
3）对原函数功能的重写：只是借助原来的名字，谨慎修改旧函数

"""

# format基本用法
# 不带编号，即{}
# 带数字编号，可调换顺序，即{1}、{2}
# 带关键字，即{a}

# name = "xiao"
# age = "18"
# gender = "girl"
# print("姓名： %s, 性别： %s， 年龄：%s" % (name,gender, age))
# print("姓名：{}， 性别：{}， 年龄：{}".format(name,gender,age))
# print("姓名：{0}，性别：{1}，年龄：{2}，性别：{1}".format(name, gender, age))

# format进阶用法
# <（默认）左对齐 >右对齐   ^ 中间对齐

