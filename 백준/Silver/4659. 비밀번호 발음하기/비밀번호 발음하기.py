
def solution(password):
    # at least one vowel: a, e, i, o, u
    if any([vowel in password for vowel in ['a', 'e', 'i', 'o', 'u']]) == False:
        return False

    # cannot contain three consecutive vowels or three consecutive consonants
    for i in range(len(password) - 2):
        chunk = password[i:i + 3]
        if all([is_vowel(char) for char in chunk]) or all([is_consonant(char) for char in chunk]):
            return False

    # cannot contain two consecutive occurrences of the same letter except 'ee' or 'oo'
    for i in range(len(password) - 1):
        chunk = password[i:i + 2]
        if chunk[0] == chunk[1] and chunk not in ['ee', 'oo']:
            return False

    return True


def is_consonant(char):
    return not is_vowel(char)


def is_vowel(char):
    return char in ['a', 'e', 'i', 'o', 'u']


if __name__ == "__main__":
    while True:
        password = input()
        if password == "end":
            break
        answer = solution(password)
        if answer == True:
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")


# 1. at least one vowel: a, e, i, o, u
# 2. cannot contain three consecutive vowels or three consecutive consonants
# 3. cannot contain two consecutive occurrences of the same letter except 'ee' or 'oo'
