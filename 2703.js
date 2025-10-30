var argumentsLength = function(...args) {
    let tot = 0
    for(var i in args){
        tot ++
    }
    return tot
};