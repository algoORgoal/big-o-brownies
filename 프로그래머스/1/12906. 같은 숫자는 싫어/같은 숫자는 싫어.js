function solution(arr)
{
    return arr.reduce((acc, element) => {
        if (acc.length === 0) acc.push(element);
        else if (acc[acc.length - 1] !== element) acc.push(element);
        return acc;
    }, []);

}