// log를 event로 분류: 사용자 시청 시작, 사용자 시청 종료 => 정렬
// sliding window: 주어진 range를 지나가면서 얼마나 많은 log를 커버하는지 확인한다.
// window start: start event가 등장하면 시청자 수 감소, end event가 등장하면 시청자 수 증가
// window end: start event가 시청자 수 증가, event event가 등장하면 시청자 수 감소

const getTimestamp = (timeStr) => {
    const [ hour, min, sec ] = timeStr.split(':').map((str) => Number(str));
    const timestamp = hour * 3600 + min * 60 + sec;
    return timestamp;
}

const getTimeStr = (timestamp) => {
    const units = [ Math.floor(timestamp / 3600), Math.floor((timestamp % 3600) / 60), timestamp % 60 ];
    return units.map((unit) => String(unit).padStart(2, '0')).join(':');
}

function solution(playtimeStr, adtimeStr, logs) {
    const [ starttime, endtime ] = [ 0, getTimestamp(playtimeStr) ];
    const events = logs.flatMap((log) => {
        const [ starttime, endtime ] = log.split('-').map((timeStr) => getTimestamp(timeStr));
        return [[ "start", starttime, ], [ "end", endtime, ]]
    }).sort(([ type1, time1, ], [ type2, time2 ]) => time1 - time2);
    
    
    const adtime = getTimestamp(adtimeStr);
    let acc = 0;
    let viewerCount = 0;
    let nextEventIndex = 0;
    let previousEventIndex = 0;
    let mostPopularTime = 0;
    let mostPopularAcc = 0;
    
    for (let i = 0; i <= endtime; i++) {
        let nextEvent = events[nextEventIndex];
        
        acc += viewerCount;
        
        while (nextEventIndex < events.length && i === nextEvent[1]) {
            viewerCount = nextEvent[0] === "start" ? viewerCount + 1 : viewerCount - 1;
            nextEventIndex += 1;
            nextEvent = events[nextEventIndex];
        }
        
        if (i >= adtime) {
            if (mostPopularAcc < acc) {
                mostPopularAcc = acc;
                mostPopularTime = i - adtime;
            }
            
            
            let previousEvent = events[previousEventIndex];
            while (previousEventIndex < events.length && i - adtime === previousEvent[1]) {
                viewerCount = previousEvent[0] === "end" ? viewerCount + 1 : viewerCount - 1;
                previousEventIndex += 1;
                previousEvent = events[previousEventIndex];
            }
        }
    }
    
    return getTimeStr(mostPopularTime);
}