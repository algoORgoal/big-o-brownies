// for every word, look at the word right behind itself
// check from which index the word becomes diffrent
// if there's no part they become(the first part of the current string is the same as the previous one), set it previous.length + 1

function solution(words) {
    const sortedWords = words.sort();
    
    const autocompleters = sortedWords.reduce((accumulator, word, index, array) => {
        if (index === 0) {
            accumulator.push(1);
            return accumulator;
        }
        const previousWord = array[index - 1];
        
        const different = [ ...previousWord ].findIndex((_, index) => previousWord[index] !== word[index]);
        if (different === -1) {
            accumulator[index - 1] = Math.max(accumulator[index - 1], previousWord.length);
            accumulator.push(previousWord.length + 1);
            return accumulator;
        }
        accumulator[index - 1] = Math.max(accumulator[index - 1], different + 1);
        accumulator.push(different + 1);
        return accumulator;
    }, []);
    
    return autocompleters.reduce((accumulator, required) => accumulator + required ,0);
}

// qo wa war warr warri warro
// 1  2  3   4    4