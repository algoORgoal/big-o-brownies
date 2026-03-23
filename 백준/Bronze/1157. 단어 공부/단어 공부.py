from math import inf


def solution(string):
    table = {}
    for char in string:
        upper_char = char.upper()
        if upper_char not in table:
            table[upper_char] = 0
        table[upper_char] += 1

    most_frequent_chars = []
    freq_count = -inf

    for upper_char in table:
        if freq_count < table[upper_char]:
            freq_count = table[upper_char]
            most_frequent_chars = [upper_char]
        elif freq_count == table[upper_char]:
            most_frequent_chars.append(upper_char)

    if len(most_frequent_chars) > 1:
        return "?"
    else:
        return most_frequent_chars[0]


if __name__ == "__main__":
    string = input()
    answer = solution(string)
    print(answer)


# 소문자 => 대문자 변환
# 대문자 개수 해쉬맵으로 증가시키기
# 가장 빈도 많은 문자열 리스트 구하기
# 리스트 길이 1이면 해당 문자, 아니면 ? 반환
