# import matplotlib.pyplot as plt

# #导入数据:
# scores = [88, 76, 59, 92, 45, 67, 81, 100, 55, 73]

# #初始化数据
# excellent = 0
# good = 0
# medium = 0
# pass_num = 0
# fail = 0

# for score in scores:
#     if score >=90:
#         grade="优秀"
#         excellent+=1
#     elif score>=80:
#         grade="良好"
#         good+=1
#     elif score>=70:
#         grade="中等"
#         medium+=1
#     elif score>=60:
#         grade="及格"
#         pass_num+=1
#     else:
#         grade="不及格"
#         fail+=1
#     print(f"学生成绩:{score},等级:{grade}")
# print("\n")
# print(f"优秀人数:{excellent}")
# print(f"良好人数：{good}")
# print(f"中等人数：{medium}")
# print(f"及格人数：{pass_num}")
# print(f"不及格人数：{fail}")

# # 绘制柱状图
# # 设置中文，防止中文乱码
# plt.rcParams["font.sans-serif"] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False

# grade_names = ["优秀", "良好", "中等", "及格", "不及格"]
# people_counts = [excellent, good, medium, pass_num, fail]

# plt.bar(grade_names, people_counts)
# plt.title("学生成绩各分数段人数柱状图")
# plt.ylabel("人数")
# plt.show()




# #构建校园网IP地址列表
# campus_ips = [
#     "1号教学楼-192.168.1.1", "1号教学楼-192.168.1.2", "1号教学楼-192.168.1.3",  # 1号教学楼（索引0-2）
#     "2号宿舍楼-192.168.2.1", "2号宿舍楼-192.168.2.2", "2号宿舍楼-192.168.2.3",  # 2号宿舍楼（索引3-5）
#     "行政楼-192.168.3.1", "行政楼-192.168.3.2"  # 行政楼（索引6-7）
# ]
# print("原始列表：", campus_ips)

# # 列表增删操作
# # 添加访客区IP
# campus_ips.append("访客区-192.168.4.1")
# # 删除 "2号宿舍楼-192.168.2.3"
# campus_ips.remove("2号宿舍楼-192.168.2.3")
# print("增删后列表：", campus_ips)

# #IP列表切片操作 
# build1 = campus_ips[0:3]   # 1号教学楼 0,1,2
# build2 = campus_ips[3:5]   #2号教学楼
# admin = campus_ips[5:7]    # 行政楼
# visitor = campus_ips[7:]   # 访客区
# print("1号教学楼IP：", build1)
# print("2号宿舍楼IP：", build2)
# print("行政楼IP：", admin)
# print("访客区IP：", visitor)

# #列表遍历与统计 
# count_total = len(campus_ips)
# count_1 = 0
# count_2 = 0
# count_admin = 0
# count_visitor = 0

# for ip_info in campus_ips:
#     if "1号教学楼" in ip_info:
#         count_1 +=1
#     elif "2号宿舍楼" in ip_info:
#         count_2 +=1
#     elif "行政楼" in ip_info:
#         count_admin +=1
#     elif "访客区" in ip_info:
#         count_visitor +=1

# print(f"\n总IP数量：{count_total}")
# print(f"1号教学楼IP数量：{count_1}")
# print(f"2号宿舍楼IP数量：{count_2}")
# print(f"行政楼IP数量：{count_admin}")
# print(f"访客区IP数量：{count_visitor}")

# #饼状图可视化
# import matplotlib.pyplot as plt

# labels = ["1号教学楼","2号宿舍楼","行政楼","访客区"]
# nums = [count_1, count_2, count_admin, count_visitor]
# plt.pie(nums,labels=labels,autopct="%.1f%%")
# plt.title("各楼栋IP数量占比")
# plt.show()


# orders = [
#     {'id': 'A001', 'user': '张三', 'amount': 199, 'status': '已支付', 'city': '北京'},
#     {'id': 'A002', 'user': '李四', 'amount': 89, 'status': '已取消', 'city': '上海'},
#     {'id': 'A003', 'user': '王五', 'amount': 599, 'status': '已支付', 'city': '广州'},
#     {'id': 'A004', 'user': '张三', 'amount': 1299, 'status': '已支付', 'city': '北京'},
#     {'id': 'A005', 'user': '赵六', 'amount': 45, 'status': '待支付', 'city': '深圳'},
#     {'id': 'A006', 'user': '李四', 'amount': 320, 'status': '已支付', 'city': '上海'},
#     {'id': 'A007', 'user': '王五', 'amount': 78, 'status': '已取消', 'city': '广州'},
#     {'id': 'A008', 'user': '赵六', 'amount': 899, 'status': '已支付', 'city': '深圳'},
# ]

# # (1) 筛选有效订单，提取所有“已支付”的订单金额
# paid_amounts = [o['amount'] for o in orders if o['status'] == '已支付']
# print("(1)已支付订单金额：", paid_amounts)

# # (2) 将所有订单金额换算
# amount_fen = [o['amount'] * 100 for o in orders]
# print("(2)全部订单金额（单位：分）：", amount_fen)

# # (3) 提取所有订单的用户名列表
# user_list = [o['user'] for o in orders]
# print("(3)所有用户名单：", user_list)

# # (4) 多条件筛选
# big_paid_ids = [o['id'] for o in orders if o['status'] == '已支付' and o['amount']>500]
# print("(4)已支付且金额>500的订单ID：", big_paid_ids)

# # (5) if-else条件表达式
# order_tag = ["大额" if o['amount'] >=500 else "普通" for o in orders]
# print("(5)订单标签列表：", order_tag)
