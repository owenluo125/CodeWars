// https://www.codewars.com/kata/52f3149496de55aded000410/c

int sum_digits(int n) {
    int sum = 0;
    if (n < 0) {
        n *= -1;
    }
    while (n > 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
