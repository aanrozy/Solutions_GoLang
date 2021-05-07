/*
Given an integer x, return true if x is palindrome integer. An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
Input: x = 121
Output: true
Input: x = -121
Output: false
*/
func isPalindrome(x int) bool {
    x2 := x
    y := 0
  	for x > 0 {
        z := x % 10
        y *= 10
        y += z
        x /= 10
  	}
    if y >= 0 && y <= 2147483647{
        if y == x2{
            return true
        } else {
            return false
        }
    } else {
        return false
    }
}
