// 섭취 횟수가 가장 낮은 음식의 횟수 => a_1
// a_1 * 음식 종류 <= k: a_1 * 음식 종류를 먹고 돌아온다. k -= a_1 * (음식 종류)
/// a_1 * 음식 종류 > k: 음식을 다 먹지 못한다. k %= (음식 종류)하고 종료. 
// 두번째로 가장 낮은 음식의 횟수 => a_2
// (a_2 - a_1) * (음식 종류 - 1) <= k: k -= (a_2 - a_1) * (음식 종류)
/// a_1 * 음식 종류 > k: 음식을 다 먹지 못한다. k %= (음식 종류)하고 종료.
// a_n까지 반복하고도 k > 0일 경우: 음식을 다 먹고도 방송이 울리지 못한다. 더 섭취해야할 음식이 없어 -1을 만환한다.
// a_n까지 반복하고 k === 0일 경우: 더 섭취해야 할 음식이 없어 -1을 반환한다.

// 각 라운드에서 먹는 음식의 종류를 특정할 수 있다. 따라서 라운드별로 진행해보기.
// 이전의 음식 개수: previous
// difference = current - previous (현재 먹는 음식의 종류가 한정됌)
// if difference * left food count <= k => previous = current, left food count -= 1, k -= difference * left food count
// else return k % left food count


function solution(foodTimes, k) {
    const sortedFoodEntries = foodTimes.map((foodTime, index) => [ index + 1, foodTime ]).sort(([ index1, foodTime1, ], [ index2, foodTime2 ]) => foodTime1 - foodTime2);
    
    for (let round = 0, previous = 0, leftTime = k; round < sortedFoodEntries.length; round++) {
        const [ _, current ] = sortedFoodEntries[round];
        const difference = (current - previous);
        const leftFoodCount = sortedFoodEntries.length - round;
        const requiredTime = difference * leftFoodCount;
        if (requiredTime <= leftTime) {
            leftTime -= requiredTime;
            previous = current;
        } else {
            const leftFoodEntries = sortedFoodEntries.slice(round).sort(([ index1 ], [ index2 ]) => index1 - index2);
            const offset = leftTime % leftFoodCount;
            const [ targetIndex ] = leftFoodEntries[offset];
            return targetIndex;   
        }
    }
    return -1;
    
}