
def solution(n, people):
    people_with_id = [(index, weight, height)
                      for index, (weight, height) in enumerate(people)]
    rank_table = {}
    for person1 in people_with_id:
        rank = 1
        person1_id, person1_weight, person1_height = person1
        for person2 in people_with_id:
            person2_id, person2_weight, person2_height = person2
            if person1_id != person2_id and person1_weight < person2_weight and person1_height < person2_height:
                rank += 1
        rank_table[person1_id] = rank

    return [rank_table[i] for i in range(n)]


if __name__ == "__main__":
    n = int(input())
    people = [[int(string) for string in input().split()] for i in range(n)]
    answer = solution(n, people)
    for index, num in enumerate(answer):
        if index == len(answer) - 1:
            print(f"{num}", end="\n")
        else:
            print(f"{num}", end=" ")


# (x1, y1), (x2, y2)
# x1 > x2, y1 > y2일 때
# 덩치가 더 크다
# 덩치가 더 큰 사람의 수가 k명 있을 때 등수가 k + 1
# 각 사람별로 덩치가 더 큰 사람의 수를 계산
# 시간복잡도 n * n => O(n ** 2)
# 공간복잡도: O(n)
