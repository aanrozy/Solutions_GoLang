fmt.Println("square")
for i := 0; i < 5; i++ {
	for j := 0; j < 5; j++ {
		fmt.Print("* ")
	}
	fmt.Println("")
}

fmt.Println("triangle")
for i := 0; i < 5; i++ {
	for j := 0; j < i; j++ {
		fmt.Print("* ")
	}
	fmt.Println("")
}

fmt.Println("reverse triangle")
for i := 5; i > 0; i-- {
	for j := 0; j < i; j++ {
		fmt.Print("* ")
	}
	fmt.Println("")
}