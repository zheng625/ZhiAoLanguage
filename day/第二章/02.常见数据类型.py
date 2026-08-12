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

#定义字符串的三种方式
#1.单引号
s1='学习Python后悔三年,不学后悔一辈子' 
#2.双引号
s2="学习Python后悔三年,不学后悔一辈子"
#3.三引号
s3="""
morning 
afternoon
evening
"""
print("s1:",s1)
print("s2:",s2)
print("s3:",s3) 

print(type(s1))
print(type(s2))
print(type(s3)) 


#转义字符
#常用转义字符
# \'=单引号
s1='It\'s a good day!'
print('s1:',s1)
# \"=双引号
s2="he said:\"how are you?\""
print("s2:",s2)
# \n=换行
s3="你好\nPython新世界"
# \t=制表符
s4="\t尊敬的各位领导老师\n\t大家好"
print("s4:",s4)





#字符串的拼接
mes1="床前明月光," "疑是地上光.\n" "      举头望明月," "低头思故乡。"
print("mes1:",mes1)