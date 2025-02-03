function solution(triangle) {
    const maximumPaths = Array.from({ length: triangle.length }, (_, i) => Array.from({ length: triangle[i].length }, () => -Infinity));
    for (let i = triangle.length - 1; i >= 0; i--){
        for (let j = 0; j < triangle[i].length; j++) {
            if (i === triangle.length - 1) {
                maximumPaths[i][j] = triangle[i][j];
                continue;
            }
            maximumPaths[i][j] = Math.max(maximumPaths[i + 1][j], maximumPaths[i + 1][j + 1]) + triangle[i][j];
        }
    }
    return maximumPaths[0][0];
}