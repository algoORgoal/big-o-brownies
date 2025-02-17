// each request has [ start time, end time ]. Find the maximum number of requests that overwraps in any 1 second window
// (+1) event at request's start time
// (-1) event at request's end time + 1000?
// Why end time + 1000?
// requeest is counted in a window if request request start time <= window start time < request end time + 1000
// so at request end time + 1000, we stop counting for the request.

class Queue {
    constructor() {
        this.front = [];
        this.back = [];
    }
    
    get size() {
        return this.front.length + this.back.length;
    }
    
    get isEmpty() {
        return this.size === 0;
    }
    
    enqueue(element) {
        this.back.push(element);
    }
    
    move() {
        
        while (this.back.length) {
            this.front.push(this.back.pop());
        }
    }
    
    dequeue() {
        if (this.isEmpty) return null;
        if (this.front.length) return this.front.pop();
        this.move();
        return this.front.pop();
    }
    
    get peek() {
        if (this.isEmpty) return null;
        if (this.front.length) return this.front[this.front.length - 1];
        this.move();
        return this.front[this.front.length - 1];
    }
}

const getTimestamp = (dateStr, timeStr) => {
    const ISOString = `${dateStr}T${timeStr}Z`;
    return new Date(ISOString).getTime();
}

const getMilliSec = (secStr) => {
    return Number(secStr.slice(0, secStr.length - 1)) * 1_000;
}

function solution(lines) {
    
    
    const events = lines.flatMap((line => {
        const [ dateStr, timeStr, intervalStr, ] = line.split(' ');
        const endTime = getTimestamp(dateStr, timeStr);
        const duration = getMilliSec(intervalStr);
        const startTime = endTime - duration + 1;
        
        return [[ startTime, 1 ], [ endTime + 1000, -1]];
    }))
    
    events.sort(([ t1, e1 ], [ t2, e2 ]) => t1 - t2 || e1 - e2);
    
    let maxRequests = 0;
    let currentRequests = 0;
    
    for (const [ time, event ] of events) {
        currentRequests += event;
        maxRequests = Math.max(maxRequests, currentRequests);
    }
    return maxRequests;
    
}
