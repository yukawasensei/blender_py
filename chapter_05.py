# 列表

list1 = [1, 10, 8, 2, 5, 4, 4, 0, 5]

# 增加

list2 = []
a = "元素1"
list2.append(a)


for i in  list1:
    new = str(i)
    list2.append(new)

list3 = list2+list1

# print(list3)

# 删除

list2.pop()
# print(list2)

# while"4" in list2:
#     list2.remove("4")

while True:
    if "4" in list2:
        list2.remove("4")
    else:
        break

# print(list2)

# 查找
print(list2)
b = list2[4]
print(b)
list2.pop(0)
del list2[0]
print(list2)

# 修改

list2[1] = "新的元素"
print(list2)

list2[1] =list1
print(list2)

s = "新的元素"

# for i in range(len(s)):
#     print(s[i],end=" ")

s1 = s[0:2]
print(s1)