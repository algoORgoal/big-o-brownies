def solution(sizes):
    for i in range(0, len(sizes)):
        width, height = sizes[i]
        if width < height:
            sizes[i] = [height, width]
    return max(size[0] for size in sizes) * max(size[1] for size in sizes)
    
    

# 완전탐색: 2 * 2 * 2 *... 
# O(2 ** n) (1 <= n <= 10_000)

# 최소로 만드는 방법:
# 모든 도형의 가로를 길게, 세로를 짧게
# max_a, max_b
# 이 때 a[i], b[i]를 스위칭한다고 해보자.
# a[i] > b[i] 이므로 max_b가 더 커질 수 있다.



