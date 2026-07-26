# ========== Python 入门示例 ==========
# 新手友好的基础语法，欢迎学习 Python 🎉

# 1. 变量与数据类型
name = "小明"
age = 18
height = 1.75
is_student = True

print(f"我叫{name}，今年{age}岁，身高{height}米，是否学生：{is_student}")

# 2. 列表（List）和循环
hobbies = ["编程", "音乐", "篮球", "阅读"]
print(f"\n我的爱好有 {len(hobbies)} 个：")
for hobby in hobbies:
    print(f"  - {hobby}")

# 3. 字典（Dict）的使用
student = {
    "name": "小红",
    "scores": {"语文": 92, "数学": 88, "英语": 95}
}
print(f"\n{student['name']} 的成绩单：")
for subject, score in student["scores"].items():
    print(f"  {subject}: {score} 分")

# 4. 条件判断
score = 85
if score >= 90:
    grade = "优秀"
elif score >= 80:
    grade = "良好"
elif score >= 60:
    grade = "及格"
else:
    grade = "不及格"
print(f"\n分数 {score} 分，等级：{grade}")

# 5. 函数定义
def calculate_bmi(weight, height):
    """计算 BMI 指数"""
    bmi = weight / (height ** 2)
    return bmi

# 调用函数
my_bmi = calculate_bmi(70, 1.75)
print(f"\nBMI 指数：{my_bmi:.1f}")

if my_bmi < 18.5:
    print("体重偏轻")
elif my_bmi < 24:
    print("体重正常")
else:
    print("体重偏重")

# 6. 列表推导式（简洁地创建列表）
squares = [x ** 2 for x in range(1, 11)]
print(f"\n1 到 10 的平方：{squares}")

# 7. 异常处理
try:
    num = int("42")
    print(f"\n字符串转数字成功：{num}")
except ValueError as e:
    print(f"\n转换失败：{e}")

# 8. 文件读写（写入并读取）
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("这是 Python 写入的文件内容！")

with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(f"\n从文件读取的内容：{content}")

print("\n✅ Python 基础示例运行完毕！")
