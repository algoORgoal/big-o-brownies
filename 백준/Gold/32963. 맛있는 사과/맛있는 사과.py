import bisect

# brute force: 각 query마다 모든 사과 탐색 -> O(nq)
# 맛 크기 오름차순으로 정렬할 경우
# 맛 크기 순으로 정렬한 것 중에서 사이즈가 가장 큰 것의 개수를 다시 찾아야 함

# [1, 3], [2, 3], [3, 2], [4, 2], [5, 1]
# p = 1 => 사이즈 가장 큰 것의 개수: 3 / 3
# p = 2 => 사이즈 가장 큰 것의 개수: 3
# 오름차순으로 정렬 후, 끝에서부터 가장 큰 요소와 가장 큰 요소의 빈도수를 계산
# 시간복잡도: O(nlogn) + O(qlogn) + O(q)

def main(n: int, q: int, t: list[int], s: list[int], queries: list[int]):
    apples = [ list(tuple) for tuple in zip(t, s) ]
    apples.sort(key=lambda x: x[0])
    
    maxValueMemo = dict()
    for index in range(len(apples) - 1, -1, -1):
        if index == len(apples) - 1:
            maxValueMemo[index] = [apples[index][1], 1]
        else:
            if maxValueMemo[index + 1][0] > apples[index][1]:
                maxValueMemo[index] = list(maxValueMemo[index + 1])
            elif maxValueMemo[index + 1][0] == apples[index][1]:
                maxValueMemo[index] = list(maxValueMemo[index + 1])
                maxValueMemo[index][1] += 1
            else:
                maxValueMemo[index] = [apples[index][1], 1]
    
    appleTastes = [apple[0] for apple in apples]
    for query in queries:
        index = bisect.bisect_left(appleTastes, query)
        if index > len(apples) - 1:
            print(0)
        else:
            frequency = maxValueMemo[index][1]
            print(frequency)
        
if __name__ == "__main__":
    n, q = [ int(string) for string in input().split(' ') ]
    t = [ int(string) for string in input().split(' ') ]
    s = [ int(string) for string in input().split(' ') ]
    queries = [ int(input()) for i in range(0, q) ]
    main(n, q, t, s, queries)