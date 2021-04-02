orginal_list = [2, 3, 4, 5, 1, 3, 4]
# 方法一
new_list = []
for i in orginal_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)

# 方法二 字典去重
new_list1 = list(dict.fromkeys(orginal_list))
print(new_list1)

# 方法三 集合去重
new_list2 = list(set(orginal_list))
# new_list2.sort(key=orginal_list.index)
print(new_list2)
