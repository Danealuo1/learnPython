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