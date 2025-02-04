const isIndexInRange = (array, index) => index < array.length;

function findExtremumIndex(array, indexes, isMinimumLevel) {
    return indexes.reduce((accumulator, index) => {
        if (isIndexInRange(array, index) && ((isMinimumLevel && (array[index] < array[accumulator])) || (!isMinimumLevel && (array[index] > array[accumulator])))){
            return index;
        }
        return accumulator;
    });
}

const getLevel = (index) => Math.floor(Math.log2(index + 1));

const getIsMinimumLevel = (index) => getLevel(index) % 2 === 0;

const getParentIndex = (index) => Math.floor((index - 1) / 2);
const getChildrenIndex = (index) => [ 2 * index + 1, 2 * index + 2 ];

const compareIndexes = (heap, index1, index2, direction) => direction ? heap[index1] < heap[index2] : heap[index2] > heap[index1];

const swap = (heap, index1, index2) => [ heap[index1], heap[index2] ] = [ heap[index2], heap[index1] ];

const getGrandparentIndex = (index) => {
  if (index < 3) return null;
  return getParentIndex(getParentIndex(index));
};



// function bubbleUp(heap, index) {
//     if (index === 0) {
//         return;
//     }
    
//     const isMinimumLevel = getIsMinimumLevel(index);
//     const parentIndex = getParentIndex(index);
//     if (index === heap.length - 1 && ((isMinimumLevel && heap[index] > heap[parentIndex]) || (!isMinimumLevel && heap[index] < heap[parentIndex]))) { 
//         swap(heap, index, parentIndex);
//         index = parentIndex;
//         bubbleUp(heap, index);
//         return;
//     }
    
//     if (index <= 2) {
//        return;
//     }
    
//     const grandparentIndex = Math.floor(((Math.floor((index - 1) / 2)) - 1) / 2);
//     if ((isMinimumLevel && heap[index] < heap[grandparentIndex]) || (!isMinimumLevel && heap[index] > heap[grandparentIndex])) {
//         swap(heap, index, grandparentIndex);
//         bubbleUp(heap, grandparentIndex);
//     }
// }

function bubbleUp(heap, index) {
  if (index === 0) return;

  const parentIndex = getParentIndex(index);
  // Determine whether the new element is on a min or max level.
  if (getIsMinimumLevel(index)) {
    // For a node on a min-level, if it is greater than its parent, it belongs on the max side.
    if (heap[index] > heap[parentIndex]) {
      swap(heap, index, parentIndex);
      bubbleUpMax(heap, parentIndex);
    } else {
      bubbleUpMin(heap, index);
    }
  } else {
    // For a node on a max-level, if it is less than its parent, it belongs on the min side.
    if (heap[index] < heap[parentIndex]) {
      swap(heap, index, parentIndex);
      bubbleUpMin(heap, parentIndex);
    } else {
      bubbleUpMax(heap, index);
    }
  }
}

// Bubble up on min levels (compare with grandparent only)
function bubbleUpMin(heap, index) {
  const grandparentIndex = getGrandparentIndex(index);
  if (grandparentIndex !== null && heap[index] < heap[grandparentIndex]) {
    swap(heap, index, grandparentIndex);
    bubbleUpMin(heap, grandparentIndex);
  }
}

// Bubble up on max levels (compare with grandparent only)
function bubbleUpMax(heap, index) {
  const grandparentIndex = getGrandparentIndex(index);
  if (grandparentIndex !== null && heap[index] > heap[grandparentIndex]) {
    swap(heap, index, grandparentIndex);
    bubbleUpMax(heap, grandparentIndex);
  }
}

function bubbleDown(heap, index) { 
    let isMinimumLevel = getIsMinimumLevel(index);
    const childrenIndex = getChildrenIndex(index);
    const grandchildrenIndex = childrenIndex.flatMap(getChildrenIndex);
    
    const extremumIndex = findExtremumIndex(heap, [ index, ...childrenIndex, ...grandchildrenIndex ], isMinimumLevel);
    if (index === extremumIndex) {
        return;
    }
    
    swap(heap, index, extremumIndex);
    if (childrenIndex.some((childIndex) => childIndex === extremumIndex)) {
        return;
    }
    
    index = extremumIndex;
    const parentIndex = getParentIndex(index);
    
    if ((isMinimumLevel && (heap[index] > heap[parentIndex])) || (!isMinimumLevel && (heap[index] < heap[parentIndex]))) {
        [ heap[index], heap[parentIndex] ] = [ heap[parentIndex], heap[index] ];
        index = parentIndex;
        // bubbleDown(heap, index);
    } 
    bubbleDown(heap, index);
    
    
}

function insertHeap(heap, element) {
    heap.push(element);
    bubbleUp(heap, heap.length - 1);
}

function deleteHeap(heap, isMinimum) {
    if (heap.length === 0) {
        return null;
    }
    if (heap.length === 1) {
        return heap.pop();
    }
    
    const extremumIndex = findExtremumIndex(heap, [ 0, 1, 2 ], isMinimum);
    swap(heap, extremumIndex, heap.length - 1);
    const node = heap.pop();
    
    if (heap.length >= 2) {
        bubbleDown(heap, extremumIndex);
    }
    
    return node;
}

function solution(operations) {    
    const heap = [];
    
    operations.forEach((operation) => {
        const [ operationType, number] = operation.split(' ').map((element) => isNaN(element) ? element : Number(element));
        if (operationType === 'I') {
            insertHeap(heap, number);
        }
        else if (operationType === 'D' && number === -1) {
            deleteHeap(heap, true)
        }
        else if (operationType === 'D' && number === 1) {
            deleteHeap(heap, false);
        }
    })
    
    if (heap.length === 0) {
        return [ 0, 0 ];
    }
    return [ Math.max(...heap), Math.min(...heap) ]; 
    
    
}