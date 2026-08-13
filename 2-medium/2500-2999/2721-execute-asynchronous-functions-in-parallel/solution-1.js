/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    if (functions.length === 0) return Promise.resolve([]);
    const results = new Array(functions.length).fill(null);
    let completed = 0;
    return new Promise((resolve, reject) => {
        functions.forEach((fn, i) => {
            fn()
                .then(res => {
                    results[i] = res;
                    completed++;
                    if (completed === functions.length) {
                        resolve(results);
                    }
                })
                .catch(err => {
                    reject(err);
                });
        })
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */