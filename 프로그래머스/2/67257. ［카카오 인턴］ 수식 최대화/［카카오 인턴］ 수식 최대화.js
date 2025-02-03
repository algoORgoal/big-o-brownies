function solution(expression) {
    const precedenceTables = generatePrecedenceTables(['+','-','*']);
    const postfixes = precedenceTables.map((precedenceTable) => convertToPostfix(expression, precedenceTable));

    return Math.max(...postfixes.map(evaluatePostfix).map(Math.abs));
}

function convertToPostfix(infix, precedenceTable) {
    const tokens = infix.split(/([-*+])/);
    let { stack, output } = tokens.reduce((accumulator, token) => {
        if (isNaN(token)) {
            while (true) {
                if (!accumulator.stack.length) {
                    break;
                }
                const top = accumulator.stack[accumulator.stack.length - 1];
                if (precedenceTable[top] < precedenceTable[token]) {
                    break;
                }
                accumulator.output.push(accumulator.stack.pop());
            }
            
            accumulator.stack.push(token);
            return accumulator;
        }
        accumulator.output.push(token);
        return accumulator;
    }, {
        stack: [],
        output: [],
    });
    
    while (stack.length) {
        output.push(stack.pop());
    }
    
    return output;
}

function evaluatePostfix(tokens) {
    return tokens.reduce((accumulator, token) => {
        if (isNaN(token)) {
            const number2 = accumulator.pop();
            const number1 = accumulator.pop();
            if (token === '+') {
                accumulator.push(number1 + number2);
            } else if (token === '-') {
                accumulator.push(number1 - number2);
            } else if (token === '*') {
                accumulator.push(number1 * number2);
            }
            return accumulator;
        }
        accumulator.push(Number(token));
        return accumulator;
    }, [])[0];
}

function generatePrecedenceTables(operators, precedence = 0) {
    if (!operators.length) {
        return [{}];
    }
    
    return operators.reduce((accumulator, operator) => {
        const nextPrecedenceTables = generatePrecedenceTables(operators.filter((targetOperator) => targetOperator !== operator), precedence + 1);
        const precendenceTables = nextPrecedenceTables.map((precedenceTable) => ({
            [operator]: precedence,
            ...precedenceTable,
        }));
        
        accumulator.push(...precendenceTables);
        return accumulator;
    }, []);
    
}