# 1.1 再看python计算生态3
"""
第三方库主站 https://pypi.org/
pypi: python package index

判断第三方库可用性的一些方法
1）查看开发历史，近半年与更新记录
2）访问项目主页，文档齐全
3）评星较高
"""

# 1.2 python常用标准库解析
"""
time库：
1）提供获取系统时间并格式化输出的功能
2）提供系统级精确计时功能，用于程序性能分析

基本定义和概念：
1）计时起点： 1970年1月1日0时0分0秒，可以用time.gmtime(0)获取

time库的时间表示方法：
浮点数时间：一般从计时起点开始计算。可以看作是一种时间戳。
struct_time时间：便于程序员使用的内部结构
字符串时间： 便于用户查看的时间


"""

# import time
# t = time.gmtime()
# print(t)

"""
time库函数的分类（14个）
时间获取：time（）   gmtime（）  ctime（）   asctime（）  
localtime（）
mktime（）

时间格式化：
strftime（）  strptime（）

程序计时：
clock（）  monotonic（）  perf_counter（）
process_time（）   sleep（）

辅助函数：
get_clock_info()

struct_time: python中用于保存时间对象、带有属性标签的数据类型

1.2  python常用标准库解析

"""
# import time
# print(time.gmtime())


# 函数1  time()函数，返回一个从计时起点开始的表示时间的浮点数,返回的是一个时间戳
# import time
# print(time.time())
# # 函数2  gmtime()函数，返回一个struct_time表示的时间
# print(time.gmtime())
# # 函数3 localtime() 返回一个struct_time表示的本地时间
# print(time.localtime())
# # 函数4  mktime() 将一个struct_time的本地时间t转变为一个浮点数时间
# print(time.mktime(time.gmtime()))
# # 函数5 asctime() 返回一个字符串表示的时间，如果提供参数t，则把t变成字符串时间
# print(time.asctime())
# # 函数6  ctime() 返回一个字符串表示的时间
# print(time.ctime())

"""
小结：
1）产生浮点数时间： time（）、 mktime（）
2）产生struct_time时间： gmtime() localtime()
3）产生字符串时间： ctime（）、 asctime（）

"""

# import time
# # t = time.gmtime()
# # print(t)
# # 时间格式化 strftime(tpl,t)  tpl是格式化模板字符串，定义输出结果
# # t是struct_time变量    将struct_time时间变成格式化时间
# # print(time.strftime("%Y-%m-%d %H:%M:%S",t))
#
# # strptime(str, tpl)   str是字符串形式时间，tpl是格式化模板字符串
#
# ts = '2018-01-27 12:55:20'
# print(time.strptime(ts, '%Y-%m-%d %H:%M:%S'))

# import time
# print(time.perf_counter())   # 返回一个精确计时时间，包含全部时间，单位为秒
# print(time.process_time())    # 返回一个进程计时时间，不包含sleep()时间，单位为秒
#
# time.sleep(5.5)   # 将线程挂起s秒，s可以是浮点数
# print(time.get_clock_info('perf_counter'))    # 返回计时时钟的属性值
# # time.get_clock_into(name)  name是时钟的字符串名字

"""
time库函数的分类（14个）
时间获取：time()  gmtime() ctime() asctime() localtime() mktime()
时间格式化：strftime() strptime()
程序计时：clock() monotonic() perf_counter() process_time() sleep()
辅助函数：get_clock_info()
"""

"""
random库函数的分类
基本随机函数： seed() random() getstate() setstate()
扩展随机函数：  randint() getrandbits() randrange() choice() shuffle() sample()

"""

# seed函数  初始化给定的随机数种子，默认为当前系统时间
import random
# random.seed(10)
# random函数 生成一个【0.0,1.0）之间的随机小数
# print(random.random())

# getstate() 返回随机数生成器内部状态，元组类型
# t = random.getstate()
# print(t)
# print(type(t))

# setstate（state） 设置随机数生成器内部状态，该状态从getstate（）函数获取

# randint(a,b) 生成一个[a,b]之间的整数
# print(random.randint(10,13))  # 注意：边界值可取

# randrange(m,n,k) 生成一个[m,n)之间的以k为步长的随机整数
# print(random.randrange(10,30,5))

# getrandbits(k)   生成一个k比特长的随机整数
# print(random.getrandbits(16))

# choice(seq)  从序列seq中随机选择一个元素
# print(random.choice([1,4,9,22,8]))

# shuffle(seq)   将序列seq中元素随机排序，原序列被修改
# ls = [1,2,3,4,5]
# random.shuffle(ls)
# print(ls)     # ls被修改

# sample(pop, k)  从序列或集合pop中随机选择k个元素，原序列或集合不变
# ls = [1,2,3,4,5,6,7,8,9]
# print(random.sample(ls, 3))

"""
re库：处理正则表达式的标准库
正则表达式由字符和操作符构成

1.2 python常用标准库解析4 re库 要再看一下 没看懂

.     表示任何单个字符
[]    字符集，对单个字符给出取值范围
[^ ]  非字符集，对单个字符给出排除范围
*     前一个字符0次或无限次扩展
+     前一个字符1次或无限次扩展
？    前一个字符0次或1次扩展
|     左右表达式任意一个
{m}   扩展前一个字符m次
{m,n} 扩展前一个字符m至n次（含n）
^     匹配字符串开头
$     匹配字符串结尾
()    分组标记，内部只能使用|操作符
\d    数字，等价于[0,9]
\w    单词字符，等价于[A-Za-z0-9]

 re库的主要函数（7个）
 基础函数： compile()
 功能函数： search() match() findall() split()  finditer() sub()
 

"""

# import re
# # re.search(pattern, string, flags=0)
# match = re.search(r'[1-9]\d{5}', 'BIT 100081')
# if match:
#     # match.group() 返回match的一个或多个子组
#     # 如果只有唯一的参数， .groupa(0) 获取匹配后的字符串
#     print(match.group(0))

"""
功能函数1：  search（）
re.search(pattern,string,flags=0)
在一个字符串中搜索匹配正则表达式的第一个位置，返回macth对象
pattern: 正则表达式的字符串或原生字符串表示
string:待匹配字符串
flags:正则表达式使用时的控制标记

功能函数2： match()
re.match(pattern,string,flags=0)
在一个字符串的 开始位置 起匹配正则表达式，返回match对象

功能函数3： findall()
re.findall(pattern,string,flags=0)
搜索字符串，以列表类型返回全部能匹配的子串

功能函数4： split()
re.split(pattern,string,maxsplit=0,flags=0)
将一个字符串按照正则表达式匹配结果进行分割，返回列表类型
maxsplit: 最大分割数，剩余部分作为最后一个元素输出

功能函数5： finditer()
re.finditer(pattern,string,flags=0)
搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象

功能函数6： sub()
re.sub(pattern, repl, string, count=0, flags=0)
在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
repl: 替换匹配字符串的字符串
string：待匹配字符串
count： 匹配的最大替换数
flags： 正则表达式使用时的控制标记


 
"""
# import re
# ls = re.findall(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)

# import re
# ls = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084')
# print(ls)
# lo = re.split(r'[1-9]\d{5}', 'BIT100081 TSU100084', maxsplit=1)
# print(lo)

# 1.2 python常用标准库解析（上）4

# import re
# for m in re.finditer(r'[1-9]\d{5}', 'BIT100081 TSU100084'):
#     if m:
#         print(m.group(0))       # 每个结果m是一个match的对象

# import re
# r_sub = re.sub(r'[1-9]\d{5}', ':zipcode', 'BIT100081 TSU100084')
# print(r_sub)

# re库的使用方法
# 方法一，函数式用法：一次性操作
# import re
# rst = re.search(r'[1-9]\d{5}', 'BIT 100081')
# print(rst)

# 方法二，面向对象用法： 编译后的多次操作
# import re
# pat = re.compile('r[1-9]\d{5}')     # 一次编译
# rst = pat.search('BIT 100081')      # 编译后的多次使用
# print(rst)

"""
re.compile()函数的使用
regex = re.compile(pattern, flags=0)
将正则表达式的字符串形式编译成正则表达式对象
直接用：
regex.search()
regex.match()
regex.findall()
regex.split()
regex.finditer()
regex.sub()
调用其他方法即可

"""

"""
match对象：
match对象是一次匹配的结果，包括匹配的各种信息
match是一个对象，也就是一个类

match对象的属性如下：
.string：待匹配的文本
.re : 匹配时使用的pattern对象（正则表达式）
.pos: 正则表达式搜索文本的开始位置
.endpos: 正则表达式搜索文本的结束位置
.group(0): 获得匹配后的字符串
.start(): 匹配字符串在原始字符串的开始位置
.end(): 匹配字符串在原始字符串的结束位置
.span():  返回 (.start(), .end())


小结：
re库的主要函数（7个）：
基础函数： compile（）
功能函数： search（）、match（）、findall（）、split（）、
finditer（）、sub（）
compile()的用法、match对象

"""

# 蒙特卡罗猜测： 计算机匹配正则表达式
# 输入： 一个正则表达式，由程序员给出
# 程序：  随机产生字符串，匹配正则表达式
# 计时： 统计时间及猜测次数

"""
需求的真实应用
1）正则表达式代表病毒片段
2）任何文件都可以表示为十六进制字符的组合形式
3）匹配：病毒引擎的扫描过程

"""

"""
练习题1：
蒙特卡洛猜测： 计算机匹配正则表达式
正则表达式： r'[1-2][^2-8][D-F]0+[A-f]'
随机字符串： 32个字符长度，字母表示0-9，A-Z，十六进制字符
输出： 匹配次数、匹配字符串、程序关键部分所用时间（5位小数）

"""
# import time, random, re
#
# def genStr():
#     global sigma
#     s = ""
#     # 循环32次，生成32位字符长度的随机字符
#     for i in range(32):
#         s += sigma[random.randint(0, 15)]
#     return s
#
# sigma = "0123456789ABCDEF"
# # 匹配次数
# count = 0
# regex = re.compile(r'[1-2][^2-8][D-F]0+[A-f]')
# # 程序关键部分所用的时间
# start_time = time.perf_counter()
# match = regex.search(genStr())
# while not match:
#     count += 1
#     match = regex.search(genStr())
#
# print("程序匹配： 猜测{}次， {}->{}".format(count, match.string, match.group(0)))
# # match.string  待匹配的文本  match.group(0) 匹配后的字符串
# end_time = time.perf_counter()
# # 程序用时
# print("程序用时：{}秒".format(end_time-start_time))


# 1.4 python常用标准库解析中

# os库的使用
# os库提供通用的、基本的操作系统交互功能
# os库提供了几百个与文件系统、操作系统功能相关的函数
# 常用路径操作、进程管理、环境参数等几类
"""
路径操作： os.path子库，处理文件路径及信息
进程管理： 启动系统中其他程序
环境参数： 获得系统软硬件信息等环境参数
"""

"""
os.path子库以path为入口，用于操作和处理文件路径
import os.path
或 import os.path as op
"""

"""
函数1  os.path.abspath(path) 
返回path在当前系统中的绝对路径
"""
# import os.path
# print(os.path.abspath('python123.txt'))

"""
函数2  os.path.normpath(path) 
归一化path的表示形式，统一用\\分隔路径
"""

# import os.path
# print(os.path.normpath("E://learnPython//learnPython//python123.txt"))

"""
函数3 os.path.relpath(path)
返回当前程序与文件之间的相对路径（relative path）
"""

# import os.path
# print(os.path.relpath('E:\learnPython\learnPython\python123.txt'))

"""
函数4 os.path.dirname(path)
返回path中的目录名称
"""

# import os.path
# print(os.path.dirname('E:\learnPython\learnPython\python123.txt'))

"""
函数5 os.path.basename(path)
返回path中最后的文件名称
"""

# import os.path
# # print(os.path.basename('E:\learnPython\learnPython\python123.txt'))

"""
函数6 os.path.join(path, *path)
组合path与paths， 返回一个路径字符串

"""
#
# import os.path
# print(os.path.join("E:/", "learnPython/learnPython/python123.txt"))

"""
函数7  os.path.exists(path)
判断path对应文件或目录是否存在，返回True或False

"""

# import os.path
# print(os.path.exists('E:/learnPython/learnPython/python1234.txt'))

"""
函数8 os.path.isfile(path)
判断path所对应是否为已存在的文件，返回True或False

"""

# import os.path
# print(os.path.isfile('E:/learnPython/learnPython/python123.txt'))

"""
函数9 os.path.isdir(path)
判断path所对用是否为已存在的目录，返回True或False

"""

