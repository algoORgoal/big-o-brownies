def solution(nums):
    pokemons = set()
    for num in nums:
        if num not in pokemons:
            pokemons.add(num)
    
    return min(len(nums) // 2, len(pokemons))

# 현재 선택한 포켓몬 종류 중에
#  없으면 담고
#  있으면 스킵
#  만약 nums/2만큼 담았으면 그만 담기