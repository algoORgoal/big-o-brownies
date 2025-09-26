function solution(wallpaper) {
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;
    for (let i = 0; i < wallpaper.length; i++) {
        for (let j = 0; j < wallpaper[0].length; j++) {
            if (wallpaper[i][j] === '#') {
                minX = Math.min(minX, i);
                minY = Math.min(minY, j);
                maxX = Math.max(maxX, i + 1);
                maxY = Math.max(maxY, j + 1);
            }
        }
    }
    return [ minX, minY, maxX, maxY ];
}

// 모든 cell을 포함하는 조건
// 최소값 x, 최소값 y 포함
// 최대값 x, 최대값 y 포함
// x: row, y: col
// 시간복잡도 O(nm)