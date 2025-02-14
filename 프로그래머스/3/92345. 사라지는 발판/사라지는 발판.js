// 가질 수 있는 상태의 postorder traverse를 돌린다.
// node에 저장해야할 상태는 다음과 같다.
// a의 위치, b의 위치, 발판이 존재하는 보드 위치(비트마스크로 최소화), 이번에 움직여야할 사람, 움직인 횟수

const checkValidLoc = (board, [ x, y ]) => x >= 0 && x < board.length && y >= 0 && y < board[0].length;

const getAroundLocs = ([ x, y ]) => [[ x - 1, y ], [ x + 1, y ], [ x, y - 1], [ x, y + 1]];

const getValidAroundLocs = (board, loc) => getAroundLocs(loc).filter((loc) => checkValidLoc(board, loc));

const getBitPos = (board, [ x, y ]) => x * board[0].length + y;

const checkFootrest = (board, [ x, y ]) => board[x][y];

const Json = (value) => JSON.stringify(value);

function solution(board, aloc, bloc) {
    
    
    const rootState = {
        aloc,
        bloc,
        mask: 0,
        turn: 'a'
    };
    const rootKey = Json(rootState);
    
    const root = {
        ...rootState,
        visited: false,
    }
    
    const stack = [ root ];
    
    const visitedStates = new Set(rootKey);
    const computedStates = new Map();
    
    
    while (stack.length) {
        const { aloc, bloc, mask, turn, visited, stepCount, } = stack.pop();
        const state = { aloc, bloc, mask, turn };
        const key = Json(state);
        const loc = turn === "a" ? aloc: bloc;
        const moves = getValidAroundLocs(board, loc).filter((aroundLoc) => {
            const bitPos = getBitPos(board, aroundLoc);
            return ((1 << bitPos) & mask) === 0 && checkFootrest(board, aroundLoc);
        })
        
        if (!visited) {
            stack.push({ 
                ...state,
                visited: true,
            });
            
            moves.forEach((move) => {
                let nextAloc, nextBloc, nextTurn;
                if (turn === 'a') {
                    nextAloc = move;
                    nextBloc = bloc;
                    nextTurn = 'b';
                } else {
                    nextAloc = aloc;
                    nextBloc = move;
                    nextTurn = 'a';
                }
                const nextMask = (1 << getBitPos(board, loc)) | mask;
                
                const nextState = {
                    aloc: nextAloc,
                    bloc: nextBloc,
                    mask: nextMask,
                    turn: nextTurn,
                }
                const nextKey = Json(nextState);
                
                const nextNode = {
                    ...nextState,
                    visited: false,
                }
                
                if (!visitedStates.has(nextKey)){
                    stack.push(nextNode);
                    visitedStates.add(nextKey);
                }

            });
            
        }else {
            if (((1 << getBitPos(board, loc)) & mask) !== 0) {
                computedStates.set(key, {
                    winner: turn === 'a' ? 'b' : 'a',
                    stepCount: 0,
                });
                continue;
            }
            
            if (moves.length === 0) {
                computedStates.set(key, {
                    winner: turn === 'a' ? 'b' : 'a',
                    stepCount: 0,
                });
                continue;
            }
            
            const outcomes = moves.map((move) => {
                let nextAloc, nextBloc, nextTurn;
                if (turn === 'a') {
                    nextAloc = move;
                    nextBloc = bloc;
                    nextTurn = 'b';
                } else {
                    nextAloc = aloc;
                    nextBloc = move;
                    nextTurn = 'a';
                }
                
                const nextMask = (1 << getBitPos(board, loc)) | mask;
                const nextKey = Json({
                    aloc: nextAloc,
                    bloc: nextBloc,
                    mask: nextMask,
                    turn: nextTurn,
                });
            
                return computedStates.get(nextKey); 
            });
            
            const winningOutcomes = outcomes.filter(({ winner }) => winner === turn);
            if (winningOutcomes.length) {
                const best = Math.min(...winningOutcomes.map(({ stepCount }) => stepCount));
                computedStates.set(key, { winner: turn, stepCount: best + 1 });
            } else {
                const worst = Math.max(...outcomes.map(({ stepCount }) => stepCount));
                computedStates.set(key, { winner: turn === 'a' ? 'b' : 'a', stepCount: worst + 1 });
            }
        }
        
    }
    
    const { stepCount } = computedStates.get(rootKey);
    return stepCount;
}
