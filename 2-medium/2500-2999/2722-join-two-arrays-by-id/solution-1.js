/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function(arr1, arr2) {
    const ans = {};
    arr1.forEach((item) => {
        ans[item.id] = item;
    });
    arr2.forEach((item) => {
        if (ans[item.id]) {
            Object.keys(item).forEach((key) => {
                ans[item.id][key] = item[key];
            });
        } else {
            ans[item.id] = item;
        }
    })

    return Object.values(ans);
};