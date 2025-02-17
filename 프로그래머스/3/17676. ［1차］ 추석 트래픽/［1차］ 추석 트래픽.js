// for each end time, count the number of requests being processed.
// Proof: Let's say we start measuring the number of request at time t.
// Since there is always k in our loop that contains all the requests being processed form time t,
// we can make sure to find the answer.

const getTimestamp = (dateStr, timeStr) => {
    const ISOString = `${dateStr}T${timeStr}Z`;
    return new Date(ISOString).getTime();
}

const getMilliSec = (secStr) => {
    return Number(secStr.slice(0, secStr.length - 1)) * 1_000;
}

function solution(lines) {
    const timelines = lines.map((line) => {
        const [ dateStr, timeStr, intervalStr, ] = line.split(' ');
        const timestamp = getTimestamp(dateStr, timeStr);
        const interval = getMilliSec(intervalStr);
        return [ timestamp - interval + 1, timestamp ];
        
    }).sort(( [ starttime1, endtime1, ], [ starttime2, endtime2 ]) => endtime1 - endtime2);
    
    const processedRequestsInIntervals= timelines.map(([ _, endtime]) => {
        const [ targetStarttime, targetEndtime ] = [ endtime, endtime + 1000 - 1 ];
        const timelinesInInterval = timelines.filter(([ starttime, endtime, ]) => !(targetStarttime > endtime || targetEndtime < starttime));
        return timelinesInInterval.length;
    });
    return Math.max(...processedRequestsInIntervals);
    
}
