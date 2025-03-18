def solution(food_times, k):
    # 모든 음식을 먹는 데 걸리는 총 시간이 k 이하라면 더 이상 먹을 음식이 없으므로 -1을 반환
    if sum(food_times) <= k:
        return -1

    # (음식 소요시간, 음식 번호) 튜플 리스트 생성 (음식 번호는 1부터 시작)
    food_list = [(time, idx + 1) for idx, time in enumerate(food_times)]
    # 소요시간 기준으로 오름차순 정렬
    food_list.sort(key=lambda x: x[0])
    
    previous_time = 0  # 이미 처리한(소모한) 음식 시간의 누적합
    n = len(food_times)  # 남은 음식 개수

    # 정렬된 음식 리스트 순회
    for i, (time, food_idx) in enumerate(food_list):
        # 현재 음식까지 남은 시간이 얼마나 더 필요한지
        diff = time - previous_time
        if diff != 0:
            # 남은 음식 전체에 diff 만큼 빼려면 필요한 총 시간
            spend = diff * n
            if spend <= k:
                k -= spend
                previous_time = time  # 누적된 시간을 갱신
            else:
                # 여기서 k초 내에 전체 라운드를 돌 수 없으므로, 남은 음식 중 k초 후 먹을 음식을 결정
                k %= n
                # 남은 음식을 원래 번호 기준으로 정렬
                remaining_foods = sorted(food_list[i:], key=lambda x: x[1])
                return remaining_foods[k][1]
        n -= 1

    return -1