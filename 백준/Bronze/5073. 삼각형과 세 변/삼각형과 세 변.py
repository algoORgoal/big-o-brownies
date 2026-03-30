def solution(a, b, c):
    if a + b <= c or b + c <= a or c + a <= b:
        return 3
    if a == b == c:
        return 0
    if a == b or b == c or c == a:
        return 1
    else:
        return 2


if __name__ == "__main__":
    while True:
        a, b, c = [int(string) for string in input().split()]
        if a == b == c == 0:
            break
        answer = solution(a, b, c)
        if answer == 0:
            print("Equilateral")
        elif answer == 1:
            print("Isosceles")
        elif answer == 2:
            print("Scalene")
        else:
            print("Invalid")
