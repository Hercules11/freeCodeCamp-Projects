function convertToRoman(num) {
    let result = "";
    let k_place = parseInt(num / 1000);
    let h_place = parseInt(num /100) % 10;
    let ten_place = parseInt(num /10) % 10;
    let low_place = num % 10;
    result += 'M'.repeat(k_place);
    if (h_place <= 3) {
        result += 'C'.repeat(h_place);
    } else if (h_place === 4){
        result += 'CD';
    } else if (h_place <= 8) {
        result += ('D' + 'C'.repeat(h_place - 5));
    } else if (h_place === 9) {
        result += 'CM';
    }

    if (ten_place <= 3) {
        result += 'X'.repeat(ten_place);
    } else if (ten_place === 4){
        result += 'XL';
    } else if (ten_place <= 8) {
        result += ('L' + 'X'.repeat(ten_place - 5));
    } else if (ten_place === 9) {
        result += 'XC';
    }

    if (low_place <= 3) {
        result += 'I'.repeat(low_place);
    } else if (low_place === 4){
        result += 'IV';
    } else if (low_place <= 8) {
        result += ('V' + 'I'.repeat(low_place - 5));
    } else if (low_place === 9) {
        result += 'IX';
    }
    return result;
}