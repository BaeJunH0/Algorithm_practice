def solution(nums):
    dic = {}
    for i in nums:
        if i not in dic.keys():
            dic[i] = 1
        else:
            dic[i] += 1
    
    if len(dic.keys()) < len(nums) // 2:
        return len(dic.keys())
    else:
        return len(nums) // 2