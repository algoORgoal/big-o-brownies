class Solution {
    fun solution(todo_list: Array<String>, finished: BooleanArray): Array<String> {
        val entries = todo_list.zip(finished)
        return entries.filter {
            [ task, isFinished ] ->
            if (isFinished) false
            else true
        }.map {
            [ task ] -> task
        }
    }
}