def solution(nums):
    dic = {}
    for i in nums:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    want = len(nums) // 2
    length = len(list(dic.keys()))
    return length if length <= want else want