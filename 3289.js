var getSneakyNumbers = function(nums) {
    const digits = {};
    const sneaky = []
    for (var i of nums) {
        if (i in digits) {
            digits[i] ++;
        } else {
            digits[i] = 1;
        }
    }
    for (var i of nums) {
        if (digits[i] === 2 && !sneaky.includes(i)) {
            sneaky.push(i);
        }
    }
    return sneaky
};

console.log(getSneakyNumbers([1, 0, 0, 1]));
