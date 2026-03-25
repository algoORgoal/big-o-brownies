

def solution(channels):
    kbs1_index = 1
    kbs2_index = 1

    commands = []

    if channels[0] != "KBS1":
        for index, channel in enumerate(channels):
            if channel == "KBS1":
                kbs1_index = index
                break
            commands.append("1")

        for index in range(kbs1_index, 0, -1):
            channels[index -
                     1], channels[index] = channels[index], channels[index - 1]
            commands.append("4")

    if channels[1] != "KBS2":
        for index, channel in enumerate(channels):
            if channel == "KBS2":
                kbs2_index = index
                break
            commands.append("1")

        for index in range(kbs2_index, 1, -1):
            channels[index -
                     1], channels[index] = channels[index], channels[index - 1]
            commands.append("4")

    return "".join(commands)

# 1 / 2 3 4 3 2 1
# 1 / 2 3 4 3 2


if __name__ == "__main__":
    n = int(input())
    channels = [input() for i in range(n)]
    answer = solution(channels)
    print(answer)


# menu = channel list
# arrow = marking current channel

# initial state: the arrow marks the first channel

# 1. arrow += 1
# 2. arrow -= 1
# 3. arrow += 1, swap i and i + 1
# 4. arrow -= 1, swap i and i - 1
# invalid commands are ignored
# KBS1 on the first place in the list
# KBS2 on the second place in the list

# the sequence length <= 500

# channels: 100
# 1. KBS1 찾기 ( <= 100)
# 2. 옮기기 ( <= 100 )
# 3. KBS2 찾기 ( <= 100)
# 4. 옮기기 ( <= 100)
