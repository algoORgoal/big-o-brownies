function solution(string) {
    const strings = [ ...string ].map((character, index) => {
        return string.slice(index) + string.slice(0, index);
    })
    const validStringCount = strings.filter(isStringValid).length;
    return validStringCount;
    
}

function isStringValid(string) {
    let trimmedString = '';
    
    for (let i = 0; i < string.length;) {
        if (string[i] === '[' && string[i + 1] === ']' || string[i] === '(' && string[i + 1] === ')' || string[i] === '{' && string[i + 1] === '}' ) {
            i += 2;
            continue;
        }
        trimmedString += string[i];
        i += 1;
    }
    
    if (!trimmedString) {
        return true;
    }
    if (trimmedString === string || trimmedString.length === 1) {
        return false;
    }
    return isStringValid(trimmedString);
}