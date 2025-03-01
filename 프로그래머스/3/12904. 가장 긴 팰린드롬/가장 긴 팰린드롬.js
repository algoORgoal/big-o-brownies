


function solution(s)
{
    return manacher(s);
}

function manacher(s) {
    const t = `#${s.split('').join('#')}#`;
    const { center, radius, computed } = [ ...t ].reduce(({ center, radius, computed }, element, index, array) => {
        if (index === 0) {
            computed.set(index, 0);
            return {
                center,
                radius,
                computed,
            };
        }
        const mirror = 2 * center - index;
        let [ left, right ] = [ center - radius, center + radius ];
        
        let [ currentRadius, currentLeft, currentRight ] = [ 0, index, index ];
        
        if (index <= right) {
            currentRadius = Math.min(computed.get(mirror), mirror - left);
            [ currentLeft, currentRight ] = [ index - currentRadius, index + currentRadius ];
        }
        
        while (currentLeft - 1 >= 0 && currentRight + 1 < array.length && array[currentLeft - 1] === array[currentRight + 1]) {
            currentRadius += 1;
            [ currentLeft, currentRight ] = [ index - currentRadius, index + currentRadius ]
        }
        
        computed.set(index, currentRadius);
        
        if (currentRight > right) {
            return {
                center: index,
                radius: currentRadius,
                computed,
            }   
        }
        
        return {
            center,
            radius,
            computed,
        };
            
    }, {
        center: 0,
        radius: 0,
        computed: new Map(),
    });
    
    const { index, radius: maxRadius } = [ ...computed ].reduce((accumulator, [ index, radius ]) => {
        if (accumulator.radius < radius) {
            return {
                radius,
                index,
            };
        }
        return accumulator;
    }, {
        index: 0,
        radius: computed.get(0),
    });
    
    return [...t.slice(index - maxRadius, index + maxRadius + 1)].filter((character) => character !== '#').length;
}