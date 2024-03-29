/*
Given an array of integers , Find the Nth smallest element in this array of integers.

Notes
Array/list size is at least 3 .

Array/list's numbers could be a mixture of positives , negatives and zeros .

Repetition in array/list's numbers could occur , so don't Remove Duplications .

nthSmallest({3,1,2} ,2) ==> return (2) 
nthSmallest({15,20,7,10,4,3} ,3) ==> return (7) 
nthSmallest({15,20,7,10,4,3} ,3) ==> return (7) 
nthSmallest({177,225,243,-169,-12,-5,2,92} ,5) ==> return (92)

from https://www.codewars.com/kata/5a512f6a80eba857280000fc/javascript
*/

function nthSmallest(array, n) {
    const sortedArray = array.sort((a, b) => a - b)
    return sortedArray[n - 1]
}

console.log(nthSmallest([3,1,2], 2)) // 2
console.log(nthSmallest([15,20,7,10,4,3], 3)) // 7
console.log(nthSmallest([2,169,13,-5,0,-1], 4)) // 2
console.log(nthSmallest([2,1,3,3,1,2], 3)) // 2
