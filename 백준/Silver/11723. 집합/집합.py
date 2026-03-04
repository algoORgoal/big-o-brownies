import sys
input = sys.stdin.readline
write = sys.stdout.write


num_set = set()
FULL_SET = set(range(1, 21))


def solution(command):
    if len(command) == 1:
        command_type = command[0]
        run(num_set, command_type)
    else:
        command_type, num = command
        run(num_set, command_type, num)


def run(num_set, command, num=-1):
    if command == "add":
        add(num_set, num)
        return
    if command == "remove":
        remove(num_set, num)
        return
    if command == "check":
        check(num_set, num)
        return
    if command == "toggle":
        toggle(num_set, num)
        return
    if command == "all":
        all(num_set)
        return
    if command == "empty":
        empty(num_set)
        return


def add(num_set, num):
    num_set.add(num)


def remove(num_set, num):
    if num in num_set:
        num_set.remove(num)


def check(num_set, num):
    if num in num_set:
        write("1\n")
    else:
        write("0\n")


def toggle(num_set, num):
    if num in num_set:
        num_set.remove(num)
    else:
        num_set.add(num)


def all(num_set):
    num_set.clear()
    num_set.update(FULL_SET)


def empty(num_set):
    num_set.clear()


if __name__ == "__main__":
    m = int(input())
    for i in range(0, m):
        line = input().split()
        if len(line) == 1:
            solution(line)
        else:
            solution([line[0], int(line[1])])


# 시간복잡도: O(m)
# 공간복잡도: O(m)
