package main

import "fmt"

func reverseOnlyLetters(s string) string {
	runes := []rune(s)
	i := 0
	j := len(runes) - 1

	for i < j {
		if !unicode.IsLetter(runes[i]) {
			i++
			continue
		}
		if !unicode.IsLetter(runes[j]) {
			j--
			continue
		}
		runes[i], runes[j] = runes[j], runes[i]
		i++
		j--
	}
	return string(runes)

}

func main() {
	fmt.Println("vim-go")
}
