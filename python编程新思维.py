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

1.2  python常用标准库解析
"""