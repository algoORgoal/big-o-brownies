// 스택에 쌓이는 top의 재료가 "빵, 야채, 고기, 빵"일 때 pop이키고 1 증가
// 1 빵, 2 야채, 3 고기
// 1 2 3 1

class Solution {
    fun solution(ingredients: IntArray): Int {
        val stack = ArrayDeque<Int>()
        val count = ingredients.fold(0) { count, ingredient ->
            when {
                stack.size < 3 -> {
                    stack.addLast(ingredient)
                    count
                }
                else -> {
                    val top = stack.slice(stack.size - 3..stack.size - 1) + ingredient
                    val isHamburger = top[0] == 1 && top[1] == 2 && top[2] == 3 && top[3] == 1
                    when (isHamburger) {
                        true -> {
                            stack.removeLast()
                            stack.removeLast()
                            stack.removeLast()
                            count + 1
                        }
                        else -> {
                            stack.addLast(ingredient)
                            count
                        }
                    }
                    
                }
            }
        }
        return count
    }
}