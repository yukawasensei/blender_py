# if判断

samples = input("请输入你的渲染采样")
# samples = int(samples)

# print(samples,type(samples))

# if samples == 64:
#     print(f"你的采样数值是{samples}")
# else:
#     print("你的渲染采样不是64")

# if type(samples) == type("字符串"):
#     print("你的数据类型是字符串")
# else:
#     pass

# 逻辑运算符
# if samples !="64":
#     print("不等于64")
# else:
#     print("等于64")

# if samples !="64":
#     print("不等于64")
#     if int(samples) > 64:
#         print("大于64")
#     elif int(samples) < 64:
#         print("小于64")
# else:
#     print("等于64")

if samples !="64":
    print("不等于64")
elif int(samples) > 64:
    print("大于64")
elif int(samples) < 64:
    print("小于64")
else:
    print("等于64")