// 현재 왼손의 위치
// 현재 오른손의 위치
// 지금까지 눌린 숫자

class Solution {
    fun computeDistance(middle: Int, other: Int): Int {
        return when (middle) {
            2 -> when (other) {
                2 -> 0
                1, 5, 3 -> 1
                4, 8, 6 -> 2
                7, 0, 9 -> 3
                else -> 4
            }
            5 -> when (other) {
                5 -> 0
                4, 2, 8, 6 -> 1
                1, 3, 7, 0, 9 -> 2
                else -> 3
            }
            8 -> when (other) {
                8 -> 0
                5, 0, 7, 9 -> 1
                4, 2, 6 -> 2
                1, 3 -> 3                
                else -> 2
            }
            else -> when (other) {
                0 -> 0
                8 -> 1
                5, 7, 9 -> 2
                2, 4, 6 -> 3
                1, 3 -> 4
                else -> 1
            }
        }
    } 
    
    fun solution(numbers: IntArray, hand: String): String {
        var leftPosition: Int = -1
        var rightPosition: Int = -1
        return numbers.fold("") { acc, number ->            
            acc + when (number) {
                1, 4, 7 -> {
                    leftPosition = number
                    "L"
                }
                2, 5, 8, 0 -> when {
                    computeDistance(number, leftPosition) > computeDistance(number, rightPosition) -> {
                        rightPosition = number
                        "R"
                    }
                    computeDistance(number, leftPosition) < computeDistance(number, rightPosition) -> {
                        leftPosition = number
                        "L"
                    }
                    else -> when (hand) {
                        "left" -> {
                            leftPosition = number
                            "L"
                        }
                        else -> {
                            rightPosition = number
                            "R"
                        }
                    }
                }
                else -> {
                    rightPosition = number
                    "R"
                }
            }
        }
    }
}