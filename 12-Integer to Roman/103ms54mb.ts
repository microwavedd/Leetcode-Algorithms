function intToRoman(n: number): string {
    let r = '';

    while (true)
    {
        if (n - 1000 > -1) {
            r += 'M';
            n -= 1000;
        } else if (n - 900 > -1) {
            r += "CM";
            n -= 900;
        } else if (n - 500 > -1) {
            r += 'D';
            n -= 500;
        } else if (n - 400 > -1) {
            r += "CD";
            n -= 400;
        } else if (n - 100 > -1) {
            r += 'C';
            n -= 100;
        } else if (n - 90 > -1) {
            r += "XC";
            n -= 90;
        } else if (n - 50 > -1) {
            r += 'L';
            n -= 50;
        } else if (n - 40 > -1) {
            r += "XL";
            n -= 40;
        } else if (n - 10 > -1) {
            r += 'X';
            n -= 10;
        } else if (n - 9 > -1) {
            r += "IX";
            n -= 9;
        } else if (n - 5 > -1) {
            r += 'V';
            n -= 5;
        } else if (n - 4 > -1) {
            r += "IV";
            n -= 4;
        } else if (n - 1 > -1) {
            r += 'I';
            n -= 1;
        } else {
            break
        }
    }
    return r
};