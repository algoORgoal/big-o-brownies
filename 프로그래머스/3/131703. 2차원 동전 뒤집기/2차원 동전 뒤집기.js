// 어떤 경우에 목표 상태를 만들 수 있고, 어떤 경우에 목표 상태를 만들 수 없을까?
// 행과 열을 뒤집는 순서는 상관 없다.
// post order traverse: 가능한 모든 경우 탐색하고 되돌려놓기
// space complexity: O(nm * 2^20)

const json = (value) => JSON.stringify(value);

function solution(beginning, target) {
    const current = beginning;
    
    let columnFlipCount = 0;
    let rowFlipCount = 0;
    for (let i = 0; i < target.length; i++) {
        let differenceCount = 0;
        for (let j = 0; j < target[i].length; j++) {
            if (i === 0 && current[i][j] !== target[i][j]) {
                for (let k = 0; k < target.length; k++) current[k][j] ^= 1;
                columnFlipCount += 1;
                continue;
            }
            
            if (current[i][j] !== target[i][j]) differenceCount += 1;
        }
        
        if (differenceCount !== 0 && differenceCount !== target[i].length) {
            return -1;
        } else if (differenceCount === target[i].length) rowFlipCount += 1;
    }
    
    return Math.min(columnFlipCount + rowFlipCount, 1 + (target[0].length - columnFlipCount) + (target.length - 1 - rowFlipCount));
    
}

