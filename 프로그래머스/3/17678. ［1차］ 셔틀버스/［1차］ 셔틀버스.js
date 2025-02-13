const calculateTimestamp = (timeStr) => {
    const [ hourStr, minStr ] = timeStr.split(':');
    return Number(hourStr) * 60  + Number(minStr);
}

const calculateTimeStr = (timestamp) => {
    const [ hour, min ] = [ Math.floor(timestamp / 60), timestamp % 60 ];
    const hourStr = hour.toString().padStart(2, "0");
    const minStr = min.toString().padStart(2, "0");
    return `${hourStr}:${minStr}`;
}


function solution(n, t, m, timetable) {
    const initialTimestamp = calculateTimestamp("09:00");
        
    const shuttleBusTimestamps = [ ...Array(n).keys() ].map((index) => {
        const relapsedTime = index * t;
        return initialTimestamp + relapsedTime;
    });
        
    
    const crewTimestamps = timetable.map(calculateTimestamp);
    const stack = [ ...crewTimestamps ].sort((a, b) => a - b).reverse();

    const lastShuttleBusCrewTimestamps = shuttleBusTimestamps.reduce((accumulator, shuttleBusTimestamp, index) => {
        if (stack.length === 0) return [];
        accumulator = [];
        for (let i = 0; i < m && stack[stack.length - 1] <= shuttleBusTimestamp; i++) {
            accumulator.push(stack.pop());
        }
        return accumulator;
    }, 0);
    
    if (lastShuttleBusCrewTimestamps === 0) {
        const lastShuttleBusTimestamp = shuttleBusTimestamps.pop();
        return calculateTimeStr(lastShuttleBusTimestamp);
    }
    
    if (lastShuttleBusCrewTimestamps.length < m) {
        const lastShuttleBusTimestamp = shuttleBusTimestamps.pop();
        return calculateTimeStr(lastShuttleBusTimestamp);
    }
    
    const lastTimestampInLastBus = lastShuttleBusCrewTimestamps.pop();
    return calculateTimeStr(lastTimestampInLastBus - 1);
}

