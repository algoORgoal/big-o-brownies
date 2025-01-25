function isValidInBase(numberStr, base) {
    return [...numberStr].every((digit) => Number(digit) < base);   
}

function safeParseInt(numberStr, base) {
    return isValidInBase(numberStr, base) ? parseInt(numberStr, base) : NaN;
}


function findMaximalDigit(expressions) {
    const numbers = expressions.flatMap((tokens) => tokens.split(' ').flatMap((token) => [...token].map((char) => isNaN(Number(char)) ? -Infinity : Number(char))));
    return Math.max(...numbers);                                                                                      
}

function evaludateExpression(tokens, base) {
    const [ num1, operator, num2, , result ] = tokens.map((token, index) => index % 2 === 0 ? safeParseInt(token, base) : token);
    
    if (isNaN(num1) || isNaN(num2) || isNaN(result)) {
        return false;
    }
    
    return ((operator === '+' && num1 + num2 === result) || (operator === '-' && num1 - num2 === result));
}

function solution(expressions) {
    const tokenizedExpressions = expressions.map((expression) => expression.split(' '));
    const maximalDigit = findMaximalDigit(expressions);
          
    const bases = Array.from({ length: 9 - maximalDigit }, (_, index) => maximalDigit + 1 + index);
    
    const validBases = bases.filter(base => tokenizedExpressions.every((tokenizedExpression) => tokenizedExpression[tokenizedExpression.length - 1] === 'X' || evaludateExpression(tokenizedExpression, base)));
    
    return tokenizedExpressions.filter((tokens) => tokens[tokens.length - 1] === 'X')
        .map((tokens) => {
            const results = validBases.map((base) => {
                const num1 = safeParseInt(tokens[0], base);
                const operator = tokens[1];
                const num2 = safeParseInt(tokens[2], base);
                
                return (operator === '+' ? num1 + num2 : num1 - num2).toString(base);
            });
            
            const finalResult = results.every((result) => result === results[0]) ? results[0] : '?'
            return [ ...tokens.slice(0, -1), finalResult ].join(' ');
        });

}