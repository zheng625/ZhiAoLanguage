
print("学号：202578040429 姓名：郑敖")

num = int(input("请输入一个四位自然数："))
qian = num // 1000        
bai = (num // 100) % 10   
shi = (num // 10) % 10    
ge = num % 10
print(f"数字{num}的千位：{qian}，百位：{bai}，十位：{shi}，个位：{ge}")
