// constructing graph
// traverse tree post-order 
// For each unvisited node, store [ revenue, fee ]
// To get fee, 10% from each child's revenue and sales and store it as sales


// 문제의 절산 방식이 제대로 정의되지 않았다.
// 합산 절사인 경우: 자신의 판매량 수수료가 0.9이고, subtree에서 거둬들인 수수료가 0.9인 경우 => 합산하여 1.8에서 깎은 1원을 수수료로 내야 한다.
// 개별 절사인 경우: 자신의 판며량 수수료가 0.9이고, subtree에서 거둬들인 수수료가 0.9인 경우 => 개별 절사하여 아무 수수료도 내지 않는다.
function solution(enrolls, referrals, sellers, amounts) {
    
    const graph = referrals.reduce((accumulator, referral, index) => {
        const enroll = enrolls[index];
        if (!accumulator[referral]) {
            accumulator[referral] = [];
        }
        accumulator[referral].push(enroll);
        return accumulator;
    }, {});
    
    const revenueTable = sellers.reduce((accumulator, seller, index) => {
        if (!accumulator[seller]) {
            accumulator[seller] = [];
        }
        const amount = amounts[index];
        accumulator[seller].push(amount * 100);
        return accumulator;
    }, {});
    
    const computedEarnings = new Map();
    
    const root = {
        node: '-',
        visited: false,
    }
    
    const stack = [ root ];
    while (stack.length) {
        const { node, visited } = stack.pop();
        
        if (!visited) {
            stack.push({
                node,
                visited: true,
            });
            if (!graph[node]) continue;
            graph[node].forEach((child) => {
                stack.push({
                    node: child,
                    visited: false,
                });
            });
            continue;
        }
        
        if (!graph[node]) {
            computedEarnings.set(node, revenueTable[node] || []);
            continue;
        };
        
        const earnings = graph[node].flatMap((child) => {
            const earnings = computedEarnings.get(child);
            
            const adjustedEarnings = earnings.map((fee) => fee - Math.floor(fee * 0.1));
            const chargedEarnings = earnings.map((fee) => Math.floor(fee * 0.1)).filter((earning) => earning !== 0);
            
            computedEarnings.set(child, adjustedEarnings);
            
            return chargedEarnings;
        }, 0);
        computedEarnings.set(node, revenueTable[node] ? [ ...revenueTable[node], ...earnings ] : earnings);
    }
    
    const earning = enrolls.map((enroll) => {
        const earnings = computedEarnings.get(enroll);
        return earnings.reduce((accumulator, earning) => accumulator + earning, 0);
    });
    return earning;
}
