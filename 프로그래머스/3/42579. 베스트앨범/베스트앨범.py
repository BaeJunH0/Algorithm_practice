def solution(genres, plays):
    answer = []
    
    # 1. 장르 순서 정하기
    genre_plays = {}
    for i in range(len(genres)):
        if genres[i] not in genre_plays:
            genre_plays[genres[i]] = plays[i]
        else:
            genre_plays[genres[i]] += plays[i]
    
    sorted_genre_plays = sorted(genre_plays.items(), key = lambda x : x[1], reverse = True)
    
    sorted_genres = [x[0] for x in sorted_genre_plays]
    
    # 2. 조회 수에 따른 순서 정하기
    for i in sorted_genres:
        temp = []
        for j in range(len(genres)):
            if genres[j] == i:
                temp.append(j)
        temp.sort(key = lambda x : plays[x], reverse = True)
        answer += temp[:2]
    
    return answer