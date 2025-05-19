impl Solution {
    pub fn is_palindrome(mut x: i32) -> bool {
        let t: i32 = x;
        let mut r: i32 = 0;

        while x > 0 {
            let mut d: i32 = x % 10;
            r = r * 10 + d;
            x = x / 10;
        }

        if t == r {
            true
        } else {
            false
        }
    }
}
