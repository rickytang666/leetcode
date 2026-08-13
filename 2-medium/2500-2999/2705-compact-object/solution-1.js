/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if (!obj) return null;
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if (typeof(obj) !== "object") return obj;

    const ans = {};
    for (const key in obj) {
        let val = compactObject(obj[key])
        if (val) ans[key] = val;
    }

    return ans;
};