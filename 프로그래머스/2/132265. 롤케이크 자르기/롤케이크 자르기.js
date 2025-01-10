function solution(toppingList) {
    const toppingCountTable = toppingList.reduce((accumulator, topping, index) => {
        accumulator.toppingTypes.add(topping);
        accumulator[index] = accumulator.toppingTypes.size;
        return accumulator;
    }, {
        toppingTypes: new Set(),
    });
    
    const reversedToppingList = toppingList.reverse();
    const reversedToppingCountTable = reversedToppingList.reduce((accumulator, topping, index) => {
        accumulator.toppingTypes.add(topping);
        accumulator[index] = accumulator.toppingTypes.size;
        return accumulator;
    }, {
        toppingTypes: new Set(),
    });
    
    const fairDistributionCount = Object.keys(toppingList).reduce((accumulator, _, index, array) => {
        if (index === array.length - 1) {
            return accumulator;
        }
        const toppingListLength = toppingList.length;
        const toppingListLastIndex = toppingListLength - 1;
        if (toppingCountTable[index] === reversedToppingCountTable[toppingListLastIndex - index - 1]) {
            return accumulator + 1;
        }
        return accumulator;
    }, 0);
    return fairDistributionCount;
}