// 1. 가장 낮은 소요 시간 순서대로 정렬하기
// 2. 라운드 별로, 가장 낮은 소요시간인 것부터 0으로 만들기
//   - 라운드별 소요 시간 = (음식의 종류) * (현재 제거하려는 음식 소요 시간)
//    if 라운드별 소요 시간 < (현재 장애까지 남은 시간) => 각 음식의 소요 시간 - (현재 제거하려는 음식 소요시간), (현재 장애까지 남은 시간) -= (라운드별 소요 시간)
//    if (라운드별 소요 시간 === (현재 장애까지 남은 시간) => 
//    if (라운드별 소요 시간 > (현재 장애까지 남은 시간) =>

function solution(foodTimes, k) {
    const sortedFoodTimeEntries = foodTimes.map((foodTime, index) => [ index + 1, foodTime ]).sort(([ index1, foodTime1 ], [ index2, foodTime2 ]) => foodTime1 - foodTime2);
    
    for (let round = 0, leftTime = k, previousFoodTime = 0; round < foodTimes.length; round++) {
        const [ currentIndex, currentFoodTime ] = sortedFoodTimeEntries[round];
        const diff = currentFoodTime - previousFoodTime;
        if (diff !== 0) {
            const turnaroundTime = diff * (sortedFoodTimeEntries.length - round);
            if (turnaroundTime <= leftTime) {
                previousFoodTime = currentFoodTime;
                leftTime -= turnaroundTime;
            } else {
                const sortedRemainingFoodTimeEntries = sortedFoodTimeEntries.slice(round);
                
                return sortedRemainingFoodTimeEntries.sort(([ index1, foodTime1, ], [ index2, foodTime2 ]) => index1 - index2)[leftTime % sortedRemainingFoodTimeEntries.length][0];
            }
        }
    }
    
    return -1;
}