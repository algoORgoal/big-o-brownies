// 자물쇠: 홈과 돌기 부분(들어간부분, 나온부분)
// 열쇠: 홈과 돌기 부분(들어간 부분, 나온 부분)
// 자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 영향 X
// 자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 함
// 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안 됌
// 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.
// 서로 겹치는 영역에서, 열쇠의 돌기 부분 === 자물쇠의 홈 부분, 열쇠의 홈 부분 === 자물쇠의 돌기 부분
// 모든 상태를 탐색할 경우
// 가능한 이동 경로: 1. 상, 하, 좌, 우로 좌물쇠 이동, 반시계/시계방향 회전
// 시간복잡도: 가로 배치 * 세로 배치 * 4회전 * 맞는지 확인 연산 =  O(2M * 2N * 4 * MN) = O(16M^2N^2) = O(M^2N^2) <= 160,000
// 공간복잡도: O(16MN) = O(MN)
// 상태: 방향(1,2,3,4), 자물쇠에서 겹치는 부분(rowRange: [start, end ], columnRange: [ start, end ])
// 만약 모든 상태마다 key를 만들 때 공간복잡도: 4 * 2M * 2N * MN = 16M^2N^2 = 16 * 400 * 400 = 2,560,000
// dfs를 하면서 key를 재사용할 때 공간복잡도: 4 * 2M * 2N = 16MN = 64,000
// 현재 상태로부터 다음 상태로 굳이 전이시킬 필요가 없기 때문에 dfs/bfs가 아닌 반복문으로 가능한다.
// key를 배치하고, lock에 해당하는 곳에 xor해서 전부 1이 나오는지 확인
// O((m+n)^2*(m^2+n^2))
// m <= 20, n <= 20
// 4방향 * (rotateKey 연산 + keymatrix 채워넣는 연산 + key matrix 확인하는 연산)
// 시간복잡도: 4 * (m^2 + (n+m)^ * (n + m)) = O((n+m)^3)
// 공간복잡도: O((n+m)^2)

const rotateKey = (key) => {
    const rotatedKey = Array.from({ length: key.length }, () => Array.from({ length: key[0].length }, () => 0));
    for (let i = 0; i < key.length; i++) {
        for (let j = 0; j < key[i].length; j++) {
            rotatedKey[j][key.length - 1 - i] = key[i][j];
        }
    }
    
    return rotatedKey;
}


function solution(key, lock) {
    
    for (let i = 0; i < 4; i++) {
        if (i >= 1) key = rotateKey(key);
        if (checkCanOpen(key, lock)) return true;
    }
    return false;
    

}

function checkCanOpen(key, lock) {
    const [ keyRowCount, keyColumnCount ] = [ key.length, key[0].length ];
    const [ lockRowCount, lockColumnCount ] = [ lock.length, lock[0].length ];
    
    const matrix = Array.from({ length: 2 * keyRowCount + lockRowCount }, () => Array.from({ length: 2 * keyColumnCount + lockColumnCount }, () => 0));
    
    for (let i = 0; i < lockRowCount; i++) {
        for (let j = 0; j < lockColumnCount; j++) {
            matrix[keyRowCount + i][keyColumnCount + j] = lock[i][j];
        }
    }
    
    const keyMatrix = Array.from({ length: 2 * keyRowCount + lockRowCount }, () => Array.from({ length: 2 * keyColumnCount + lockColumnCount }, () => 0));
    
    for (let i = 0; i < matrix.length - keyRowCount; i++) {
        for (let j = 0; j < matrix[i].length - keyColumnCount; j++) {
            for (let k = 0; k < keyRowCount; k++) {
                for (let l = 0; l < keyColumnCount; l++) {
                    keyMatrix[i + k][j + l] = key[k][l];
                }
            }
            let canOpen = true;
            for (let k = 0; k < lockRowCount && canOpen === true; k++) {
                for (let l = 0; l < lockColumnCount && canOpen === true; l++) {
                    if ((matrix[keyRowCount + k][keyColumnCount + l] ^ keyMatrix[keyRowCount + k][keyColumnCount + l]) !== 1) canOpen = false;
                }
            }
            if (canOpen) return true;
            
            for (let k = 0; k < keyRowCount; k++) {
                for (let l = 0; l < keyColumnCount; l++) {
                    keyMatrix[i + k][j + l] = 0;
                }
            }
        }
    }
    return false;
}