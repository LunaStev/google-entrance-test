bool isPalindrome(int x) {
    int t = x;
    long r = 0;

    while (x > 0) {
        int d = x % 10;
        r = r * 10 + d;
        x = x / 10;
    }

    if (t == r) {
        return true;
    } else {
        return false;
    }
}
