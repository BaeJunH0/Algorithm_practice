def solution(routes):
    answer = 0
    
    # 진입점을 기준으로 정렬
    sorted_routes = sorted(routes, key = lambda x : x[0])

    last = sorted_routes[0]
    
    # 앞의 차가 나가기 전에 진입이 이루어지는가?
    for i in range(1, len(sorted_routes)):
        # 겹치는 경우
        if last[1] >= sorted_routes[i][0]:
            last = [sorted_routes[i][0], min(last[1], sorted_routes[i][1])]
        # 겹치지 않는 경우
        else:
            last = sorted_routes[i]
            answer += 1
            
    answer += 1
    return answer