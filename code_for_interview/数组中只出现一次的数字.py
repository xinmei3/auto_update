# 列表中只有两种元素，
# 一种为出现次数是两次的，一种为出现次数是1次的。
# 输出只出现一次的数字
array = [4, 1, 2, 1, 3, 4]


# 返回[a,b] 其中ab是出现一次的两个数字


# 方法一
def Find_Nums_Appear_Once(array):
    # write code here
    ans = []
    for elem in array:
        # print(array.count(elem))
        if elem in ans:
            ans.remove(elem)
        else:
            ans.append(elem)
    return ans


print("方法一")
print(Find_Nums_Appear_Once(array))


# 方法二 只对只有一个数字时有效
def find_nums_appear_once(Array):
    array = list(Array)
    res = 0
    for i in array:
        res ^= i
    return res


print(find_nums_appear_once(array))
