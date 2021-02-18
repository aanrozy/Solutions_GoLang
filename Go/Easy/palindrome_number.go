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
