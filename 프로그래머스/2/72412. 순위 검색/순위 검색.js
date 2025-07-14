const CATEGORIES = {
    languages: [ "java", "python", "cpp" ],
    positions: [ "backend", "frontend" ],
    experienceLevels: [ "junior", "senior" ],
    favioriteFoods: [ "chicken", "pizza" ],
};


const fillQuery = (completeQueries, oldQuery, index) => {
    if (index === oldQuery.length) return completeQueries;
    if (oldQuery[index] === '-') {
        const categoryEntries = Object.entries(CATEGORIES);
        const [ _, categoryList] = categoryEntries[index]
        
        const newQueries = completeQueries.flatMap((completeQuery) => {
            return categoryList.map((option) => completeQuery.concat(option));
        });
        
        
        return fillQuery(newQueries, oldQuery, index + 1);
    }
    
    const newQueries = completeQueries.map((completeQuery) => completeQuery.concat(oldQuery[index]));
    return fillQuery(newQueries, oldQuery, index + 1);
}

function solution(info, queries) {
    const scoreboard = new Map();
    info.forEach((personString) => {
        const parts = personString.split(" ");
        const score = Number(parts.pop());
        const fields = parts; // [lang, pos, exp, food]

      // mask 0~15: 0b0000 ~ 0b1111
        for (let mask = 0; mask < 16; mask++) {
            const keyParts = [];
            for (let i = 0; i < 4; i++) {
                // 비트 i 가 켜져 있으면 원본, 꺼져 있으면 '-'
                keyParts.push((mask & (1 << i)) ? fields[i] : '-');
            }
            const key = keyParts.join(" ");
            if (!scoreboard.has(key)) scoreboard.set(key, []);
            scoreboard.get(key).push(score);
        }
    });
    
    scoreboard.forEach((value, key, map) => map.get(key).sort((a, b) => a - b));
    
    return queries.map((query) => {
        const [ language, and1, position, and2, experienceLevel, and3, favoriteFood, scoreString ] = query.split(" ");
        
        const key = [ language, position, experienceLevel, favoriteFood ].join(" ");
            const target = Number(scoreString);
            const list = scoreboard.get(key);

            if (!list || list.length === 0 || list[list.length - 1] < target) return 0;
            
            let start = 0;
            let end = list.length - 1;
            while (start < end) {
                const middle = Math.floor((start + end) / 2);
                if (target <= list[middle]) {
                    end = middle;
                } else { // list[middle] < target
                    start = middle + 1;
                }
            }
            const lowerbound = start;
            return list.length - lowerbound;
            
    });
}


// 트리 사용시: 100,000 * 24 * 4(분류 찾는데 사용) * log2 2000(탐색) => 약 10억번 연산으로 시간초과 충분히 가능
// 따라서, 그냥 매핑태이블을 사용해서 분류 찾는데 사용되는 시간을 줄여야 한다 => 100,000 * log 2000