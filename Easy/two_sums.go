func reverse(x int) int {
    y := 0
  	for x < 0 || x > 0 {
        z := x % 10
        y *= 10
        y += z
        x /= 10
  	}
    if y >= -2147483648 && y <= 2147483647{
        return y
    } else {
        return 0
    }
}
