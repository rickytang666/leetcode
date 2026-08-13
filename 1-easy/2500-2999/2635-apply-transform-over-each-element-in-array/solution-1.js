/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let ans = [];
    for (const [i, num] of arr.entries()) {
        ans.push(fn(num, i));
    }
    return ans;
};