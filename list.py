list = [1, 2, 3, 4, 5, 6, 7 ]

# print(list[0])
# print(list[1:3])

# print(list[1])
# list[1] = 66
# print(list[1])

# del list[0]
# print(list)

# print(list[:3])
# print(list[3:])

# print(len(list))
# print(max(list))
# print(min(list))

# list.append(8)
# print(list)
# print(list.count(3))

# list2 = ['a','b','c']
# list.extend(list2)
# print(list)

# print(list.index(3))
# list.insert(2,'a')
# print(list)

# list.pop(2)
# print(list)
# list.remove(3)
# print(list)

# list.sort(reverse=True)
# print(list)

# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond,reverse=True)
# 输出类别
print ('排序列表：', random)