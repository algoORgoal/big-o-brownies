const NUM_TO_DAY_MAP = {
    0: 'SUN',
    1: 'MON',
    2: 'TUE',
    3: 'WED',
    4: 'THU',
    5: 'FRI',
    6: 'SAT',
};

function solution(a, b) {
    const date = new Date(2016, a - 1, b);
    const dayNum = date.getDay();
    const day = NUM_TO_DAY_MAP[dayNum];
    return day;
}