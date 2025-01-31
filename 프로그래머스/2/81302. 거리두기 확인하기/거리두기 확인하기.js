function isPlaceDistant(place) {
    
    const occupiedSeats = [];
    for (let i = 0; i < place.length; i++) {
        for (let j = 0; j < place[0].length; j++) {
            if (place[i][j] === 'P') {
                occupiedSeats.push([ i, j ]);
            }
        }
    }
    
    for (let i = 0; i < occupiedSeats.length; i++) {
        for (let j = i + 1; j < occupiedSeats.length; j++) {
            const [ x1, y1 ] = occupiedSeats[i];
            const [ x2, y2 ] = occupiedSeats[j];
            const distance = Math.abs(x1 - x2) + Math.abs(y1 - y2);
            if (distance > 2) {
                continue;
            } else if (distance === 1) {
                return false;
            } else if (Math.abs(x1 - x2) === 2 && y1 === y2) {
                const x3 = Math.min(x1, x2) + 1;
                if (place[x3][y1] !== 'X') {
                    return false;
                }
            } else if (Math.abs(y1 - y2) === 2 && x1 === x2) {
                const y3 = Math.min(y1, y2) + 1;
                if (place[x1][y3] !== 'X') {
                    return false;
                }
            } else if (Math.abs(x1 - x2) === 1 && Math.abs(y1 - y2) === 1) {
                const x3 = Math.min(x1, x2);
                const y3 = Math.min(y1, y2);
                if (!(place[x3][y3] === 'X' && place[x3 + 1][y3 + 1] === 'X' || place[x3 + 1][y3] === 'X' && place[x3][y3 + 1])) {
                    return false;
                }    
            }
        }
    }
    return true;
}


function solution(places) {
    return places.map((place) => isPlaceDistant(place) ? 1 : 0);
}