def solution(citations):
    citations = sorted(citations, reverse = True)

    for i in range(0, len(citations)):
        if citations[i] <= i:
            return i
        
    if max(citations) > len(citations):
        return len(citations)
    return 0