# 字面量的写法
# print(100 )# 整数
# print(3.14)# 浮点数
# print(True)# 布尔值
# print(False)# 布尔值
# print("学Python后悔三年,不学后悔一辈子")# 字符串
# print("-----------------")# 字符串  
# print(None)# 空值

# print(True+1)
# print(False-1)


# 变量
num=125
print(num)

num=num+0.4
print(num)


num="I am SpiderMan!"
print(num)

num=True
print(num)

# 案例:视频播放量
base=20.7
nincr=50
print("第一个月播放量:",base+nincr)
print("第二个月播放量:",base+nincr*2)

# 优化:
base,nincr=20.7,50
print("第一个月播放量:",base+nincr)
print("第二个月播放量:",base+nincr*2)


# 案例:实现交换两个变量的值
a=10
b=20
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)

# type()函数判断数据类型
print(type("学Python后悔三年,不学后悔一辈子"))
print(type(100 ))
print(type(3.14))
print(type(False))
print(type(None))


# isinstance()函数判断数据类型
x=100
print("x:",x)
print(isinstance(x,float))
print(isinstance(x,int))