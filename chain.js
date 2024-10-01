// promise_chain.js
function asyncTask(message, delay) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (message === 'Error') {
                reject('Error occurred');
            } else {
                resolve(`Completed: ${message}`);
            }
        }, delay);
    });
}

// Usage
asyncTask('Task 1', 1000)
    .then(result => {
        console.log(result);
        return asyncTask('Task 2', 2000);
    })
    .then(result => {
        console.log(result);
        return asyncTask('Error', 1000);
    })
    .catch(error => {
        console.error(error);
    });
