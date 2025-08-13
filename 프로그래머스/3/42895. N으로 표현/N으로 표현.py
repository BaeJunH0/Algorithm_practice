def solution(N, number):
    """
    숫자 N과 사칙연산만으로 number를 표현하는 최소 횟수를 찾는 함수

    Args:
        N (int): 사용할 숫자
        number (int): 목표 숫자

    Returns:
        int: N 사용 횟수의 최솟값. 8보다 크면 -1 반환.
    """
    
    # N이 number와 같다면 1번 사용한 것
    if N == number:
        return 1

    # N 사용 횟수별로 만들 수 있는 숫자들을 저장할 리스트 (최대 8번)
    # s[i]는 N을 i+1번 사용해서 만들 수 있는 숫자들의 집합을 저장
    s = [set() for _ in range(8)]

    # N을 i+1번 사용해서 만들 수 있는 초기 숫자들 (N, NN, NNN, ...)
    for i in range(8):
        # i+1번 반복해서 만든 숫자를 집합에 추가
        s[i].add(int(str(N) * (i + 1)))

    # N 사용 횟수를 2부터 8까지 반복
    for i in range(1, 8):
        # s[i]를 채우기 위해, s[j]와 s[i-j-1]의 숫자들을 조합
        for j in range(i):
            # s[j]의 모든 숫자와 s[i-j-1]의 모든 숫자에 대해 사칙연산 수행
            for op1 in s[j]:
                for op2 in s[i - j - 1]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    # 나누기 연산은 0으로 나누는 경우를 제외하고 수행
                    if op2 != 0:
                        s[i].add(op1 // op2)

        # 현재 i+1번 사용해서 만든 숫자 집합에 number가 있는지 확인
        if number in s[i]:
            # number를 찾았다면, 사용 횟수 (i+1)를 반환
            return i + 1

    # 8번을 초과하는 경우에는 -1 반환
    return -1

