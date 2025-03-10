function solution(k, roomNumbers) {
    const room = new Map();
    const answer = [];

    function find(n) {
        if (!room.has(n)) return n;
        let next = find(room.get(n));
        room.set(n, next);
        return next;
    }

    for (let num of roomNumbers) {
        let emptyRoom = find(num);
        answer.push(emptyRoom);
        room.set(emptyRoom, find(emptyRoom + 1));
    }

    return answer;
}