def solution(cacheSize, cities):
    answer = 0
    cache = []
    
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        i = i.upper()
        # cache miss
        if i not in cache:
            answer += 5
            if len(cache) == cacheSize:
                cache = cache[1:]
            cache.append(i)
        # cache hit
        else:
            answer += 1
            index = cache.index(i)
            cache = cache[:index] + cache[index+1:]
            cache.append(i)
    return answer