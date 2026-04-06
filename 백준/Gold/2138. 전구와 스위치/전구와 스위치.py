

def solution(n, source, target):
    # 처음 시작을 스위칭하는 경우
    new1 = [source[i] for i in range(len(source))]
    new1[0] ^= 1
    new1[1] ^= 1

    count1 = 1

    for i in range(1, len(new1) - 1):
        if new1[i - 1] != target[i - 1]:
            new1[i - 1] ^= 1
            new1[i] ^= 1
            new1[i + 1] ^= 1
            count1 += 1

    if new1[len(new1) - 2] != target[len(target) - 2]:
        new1[len(new1) - 2] ^= 1
        new1[len(new1) - 1] ^= 1
        count1 += 1

    # 처음 시작을 스위칭하지 않는 경우
    new2 = [source[i] for i in range(len(source))]

    count2 = 0

    for i in range(1, len(new2) - 1):
        if new2[i - 1] != target[i - 1]:
            new2[i - 1] ^= 1
            new2[i] ^= 1
            new2[i + 1] ^= 1
            count2 += 1

    if new2[len(new2) - 2] != target[len(target) - 2]:
        new2[len(new2) - 2] ^= 1
        new2[len(new2) - 1] ^= 1
        count2 += 1

    if new1 != target and new2 != target:
        return -1
    if new1 != target:
        return count2
    if new2 != target:
        return count1
    return min(count1, count2)


if __name__ == "__main__":
    n = int(input())
    source = [int(char) for char in input()]
    target = [int(char) for char in input()]
    answer = solution(n, source, target)
    print(answer)
