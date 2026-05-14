


    

def solution(required_order, skill_trees):
    total = 0
    for skill_tree in skill_trees:
        order = ''.join([ skill for skill in skill_tree if skill in required_order ])
        if required_order.startswith(order):
            total += 1
    
    return total

# 가능한 스킬트리 개수를 출력
# 선행 스킬 순서: skill
# 유저가 만든 스킬 순서들: skill_trees
# 출력: 유저가 만든 스킬 순서들 중 선행 스킬 순서를 만족하는 것들의 개수

# 스킬: 알파벳 대문자
# skill, skill_trees 모두 스킬이 중복해서 주어지지 않는다.
# for skill_tree in skill_trees:
#   order = ''.join([ char for char in skill_tree if char in skill ])
#   if skill.startswith(order):
#     return True
#   else:
#     return False

# 시간복잡도:
# O(len(skill) * len(skill_tree[i]) * len(skill_trees))
# len(skill) <= 26, len(skill_tree[i]) <= 26, len(skill_trees) <= 20
# 26 * 26 * 20 => doable