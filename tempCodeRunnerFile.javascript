"use strict"

let x = "abc";
const s = new Set([...x]);

console.log(s);
const words = ["ad","bd","aaab","baa","badab"];

for(let word of words) {
    for (let char of word) {
        console.log(char);
    }
}
