'use strict'
var arr = ["hii", "tyy", "by"];
var newarr = arr.filter(func);
console.log(newarr);
function func(a)
{
    console.log(`${a}`)
    if (a.search(/y/i) != -1)
        return (a);
}
console.log(process.versions);