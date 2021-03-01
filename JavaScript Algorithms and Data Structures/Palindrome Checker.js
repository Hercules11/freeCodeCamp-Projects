function palindrome(str) {
    let newStr = str.match(/\w+/g).join("").replace('_', '').toLowerCase();
    // console.log(newStr);
    let str_two = newStr.split('').reverse().join('');
    // 判断回文数，反转字符串， 比较是否相等;
    return str_two === newStr;
}


palindrome("eye2_A3*3#A2");