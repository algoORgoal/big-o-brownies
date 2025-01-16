function solution(queue1, queue2) {
    const slidingWindow = [ ...queue1, ...queue2 ];
    let [ left, right ] = [ 0, queue1.length ];
    const target = slidingWindow.reduce((accumulator, element) => accumulator + element) / 2;
    
    let currentSum = queue1.reduce((accumulator, element) => accumulator + element);
    let moveCount = 0;
    
    console.log(target);
    while (moveCount <= 2 * slidingWindow.length) {
        if (currentSum === target) {
            return moveCount;
        } else if (currentSum < target) {
            currentSum += slidingWindow[right];
            moveCount += 1;
            right = (right + 1) % slidingWindow.length;
        } else {
            currentSum -= slidingWindow[left];
            moveCount += 1;
            left = (left + 1)  % slidingWindow.length;
        }
    }
    return -1;
}